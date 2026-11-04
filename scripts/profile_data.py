#!/usr/bin/env python3
"""Read only the anonymous, public GitHub calendar. Fail closed on schema drift."""
import argparse
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import urllib.request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
ACCOUNT = "S3rri-dev"
SOURCE = f"https://github.com/users/{ACCOUNT}/contributions"


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.labels = {}
        self.target = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "td" and "data-date" in attrs:
            day = date.fromisoformat(attrs["data-date"])
            level = int(attrs["data-level"])
            key = attrs["id"]
            if day in self.cells or not 0 <= level <= 4:
                raise ValueError("Invalid or duplicate calendar day")
            self.cells[day] = (key, level)
        if tag == "tool-tip" and "for" in attrs:
            self.target = attrs["for"]
            self.labels[self.target] = ""

    def handle_data(self, data):
        if self.target is not None:
            self.labels[self.target] += data

    def handle_endtag(self, tag):
        if tag == "tool-tip":
            self.target = None


def parse_calendar(html, today):
    parser = CalendarParser()
    parser.feed(html)
    start = today - timedelta(days=364)
    days = []
    for offset in range(365):
        day = start + timedelta(days=offset)
        if day not in parser.cells:
            raise ValueError(f"Incomplete public calendar: missing {day}")
        key, level = parser.cells[day]
        label = parser.labels.get(key, "").strip()
        match = re.fullmatch(r"(No|[\d,]+) contributions? on .+\.", label)
        if not match:
            raise ValueError(f"Unrecognised public calendar label on {day}: {label!r}")
        count = 0 if match[1] == "No" else int(match[1].replace(",", ""))
        if (count == 0) != (level == 0):
            raise ValueError(f"Inconsistent level/count on {day}")
        days.append({"date": day.isoformat(), "count": count, "level": level})
    return days


def validate(snapshot):
    if snapshot.get("account") != ACCOUNT or snapshot.get("source") != SOURCE:
        raise ValueError("Unexpected public data source")
    end = date.fromisoformat(snapshot["through"])
    days = snapshot["days"]
    if len(days) != 365:
        raise ValueError("Expected exactly 365 calendar days")
    for index, day in enumerate(days):
        if day["date"] != (end - timedelta(days=364-index)).isoformat():
            raise ValueError("Unordered, duplicate or missing day")
        if type(day["count"]) is not int or day["count"] < 0:
            raise ValueError("Invalid contribution count")
        if type(day["level"]) is not int or not 0 <= day["level"] <= 4:
            raise ValueError("Invalid contribution level")
        if (day["count"] == 0) != (day["level"] == 0):
            raise ValueError("Inconsistent contribution level")
    if snapshot["total"] != sum(day["count"] for day in days):
        raise ValueError("Incorrect total")
    if snapshot["active_days"] != sum(day["count"] > 0 for day in days):
        raise ValueError("Incorrect active day count")
    stamp = datetime.fromisoformat(snapshot["fetched_at"])
    if stamp.tzinfo is None or stamp.astimezone(ZoneInfo("Europe/Madrid")).date() != end:
        raise ValueError("Inconsistent snapshot timestamp")
    return snapshot


def fetch():
    now = datetime.now(timezone.utc)
    today = now.astimezone(ZoneInfo("Europe/Madrid")).date()
    request = urllib.request.Request(SOURCE, headers={
        "User-Agent": "S3rri-public-profile/1.0", "Accept-Language": "en"})
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read(2_000_001)
    if len(html) > 2_000_000:
        raise ValueError("Public calendar exceeds size limit")
    days = parse_calendar(html.decode("utf-8"), today)
    return validate({
        "account": ACCOUNT, "source": SOURCE,
        "visibility": "anonymous-public-calendar", "through": today.isoformat(),
        "fetched_at": now.isoformat(timespec="seconds"),
        "total": sum(day["count"] for day in days),
        "active_days": sum(day["count"] > 0 for day in days), "days": days})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate saved data without network")
    args = parser.parse_args()
    target = ROOT / "data/activity.json"
    if args.check:
        snapshot = validate(json.loads(target.read_text()))
    else:
        snapshot = fetch()  # No writes until the complete response has passed validation.
        target.parent.mkdir(exist_ok=True)
        temporary = target.with_suffix(".tmp")
        temporary.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
        temporary.replace(target)
    print(f"Public calendar through {snapshot['through']}: {snapshot['total']} contributions, "
          f"{snapshot['active_days']} active days; 365 dates verified.")
