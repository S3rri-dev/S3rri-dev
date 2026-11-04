"""Calendar integrity checks: gaps and schema drift must never become fake zeros."""
import copy
from datetime import date, timedelta
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from profile_data import parse_calendar, validate


class PublicCalendarTests(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 11, 4)
        self.parts = []
        for offset in range(365):
            day = self.today - timedelta(days=364-offset)
            count, level = (1234, 4) if offset == 364 else (0, 0)
            label = "1,234 contributions on November 4th." if count else "No contributions on a day."
            self.parts.append(f'<td id="d{offset}" data-date="{day}" data-level="{level}"></td>'
                              f'<tool-tip for="d{offset}">{label}</tool-tip>')

    def test_counts_and_future_exclusion(self):
        future = '<td id="future" data-date="2026-11-05" data-level="4"></td>'
        days = parse_calendar("".join(reversed(self.parts)) + future, self.today)
        self.assertEqual(len(days), 365)
        self.assertEqual(days[-1]["count"], 1234)
        self.assertEqual(days[0]["date"], "2025-11-05")
        self.assertEqual(sum(day["count"] for day in days), 1234)

    def test_missing_day_rejected(self):
        with self.assertRaisesRegex(ValueError, "Incomplete"):
            parse_calendar("".join(self.parts[1:]), self.today)

    def test_unknown_tooltip_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unrecognised"):
            parse_calendar("".join(self.parts).replace("No contributions on", "Nothing on", 1), self.today)

    def test_duplicate_day_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            parse_calendar("".join(self.parts) + self.parts[0], self.today)

    def test_false_intensity_rejected(self):
        with self.assertRaisesRegex(ValueError, "Inconsistent"):
            parse_calendar("".join(self.parts).replace('data-level="0"', 'data-level="4"', 1), self.today)

    def test_saved_snapshot_totals_and_dates(self):
        path = Path(__file__).resolve().parents[1] / "data/activity.json"
        snapshot = json.loads(path.read_text())
        validate(snapshot)
        for corrupt in ("total", "days"):
            changed = copy.deepcopy(snapshot)
            if corrupt == "total":
                changed["total"] += 1
            else:
                changed["days"][1]["date"] = changed["days"][0]["date"]
            with self.assertRaises(ValueError):
                validate(changed)


if __name__ == "__main__":
    unittest.main()
