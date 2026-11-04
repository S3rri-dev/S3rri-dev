#!/usr/bin/env python3
"""Original, self-contained profile cards. Python standard library only."""
import argparse
import base64
from datetime import date, datetime, timedelta
from html import escape
import json
from pathlib import Path
from zoneinfo import ZoneInfo
from profile_data import validate

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
IVORY, GOLD, MUTED = "#F7F3ED", "#C5A05A", "#BDB7AF"
FONT = "Arial,Helvetica,sans-serif"
MONO = "Menlo,Consolas,monospace"


def text(x, y, value, size=24, fill=IVORY, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'


def svg(width, height, title, description, body, css="", defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<defs>{defs}</defs><style>text{{font-family:{FONT}}}.mono{{font-family:{MONO}}}{css}</style>
<rect width="{width}" height="{height}" fill="#000000"/>{body}</svg>\n'''


def hero(english=False, mobile=False, motion=True):
    width, height = (680, 740) if mobile else (1360, 440)
    x, cat_x, cat_y, cat_size = (40, 180, 354, 320) if mobile else (58, 940, 32, 362)
    data = base64.b64encode((ASSETS / "avatar-480.png").read_bytes()).decode()
    title = "S3rri.dev · Software & systems" if english else "S3rri.dev · Software y sistemas"
    desc = ("Luis Serrano Cardoso. Telematics Engineering student, UAH. Model, build, verify. Angular cat in dark red, ivory and gold."
            if english else "Luis Serrano Cardoso. Estudiante de Ingeniería Telemática, UAH. Modelar, construir, verificar. Gato angular rojo oscuro, marfil y dorado.")
    defs = f'''<linearGradient id="wash"><stop stop-color="#8B1722" stop-opacity=".16"/><stop offset="1" stop-color="#8B1722" stop-opacity="0"/></linearGradient>
<linearGradient id="beam" x2="0" y2="1"><stop stop-color="#C5A05A" stop-opacity="0"/><stop offset="1" stop-color="#C5A05A" stop-opacity=".3"/></linearGradient>
<image id="cat" width="480" height="480" xlink:href="data:image/png;base64,{data}"/>
<clipPath id="reveal"><rect class="reveal" width="480" height="480"/></clipPath>'''
    body = f'<rect width="{width}" height="{height}" fill="url(#wash)"/><path d="M1 1H{width-1}V{height-1}H1Z" fill="none" stroke="#30262A"/><path d="M0 30V110" stroke="#8B1722" stroke-width="6"/>'
    eyebrow_y = 58 if mobile else 71
    body += text(x, eyebrow_y, "SOFTWARE / SYSTEMS" if english else "SOFTWARE / SISTEMAS", 20, GOLD, 600, 'class="mono" letter-spacing="3"')
    # The final state is the default. Styles are enhancement, never required to read the card.
    glyphs = "".join(f'<tspan class="glyph g{i}">{escape(c)}</tspan>' for i,c in enumerate("S3rri.dev"))
    body += f'<text x="{x-4}" y="{170 if mobile else 181}" fill="{IVORY}" font-size="{108 if mobile else 112}" font-weight="700" letter-spacing="-5">{glyphs}</text>'
    body += text(x, 227 if mobile else 246, "LUIS SERRANO CARDOSO", 23 if mobile else 24, IVORY, 500, 'class="mono" letter-spacing="1.2"')
    if mobile:
        body += text(x, 275, "Telematics Engineering student" if english else "Estudiante de Ingeniería Telemática", 25, MUTED)
        body += text(x, 311, "Universidad de Alcalá · UAH", 23, MUTED)
    else:
        body += text(x, 290, "Telematics Engineering student · UAH" if english else "Estudiante de Ingeniería Telemática · UAH", 27, MUTED)
    # Thin architectural frame; the approved animal is preserved exactly.
    body += f'<g transform="translate({cat_x} {cat_y}) scale({cat_size/480})"><use xlink:href="#cat" opacity=".12"/><use xlink:href="#cat" clip-path="url(#reveal)"/><g class="scanner"><rect x="12" y="-32" width="456" height="32" fill="url(#beam)"/><path d="M12 0H468" stroke="{GOLD}" stroke-width="2"/></g><path d="M10 76V10H76 M404 10H470V76 M470 404V470H404 M76 470H10V404" fill="none" stroke="#8B1722" stroke-width="2"/><path d="M10 10H44 M436 470H470" stroke="{GOLD}" stroke-width="3"/></g>'
    line_y, motto_y = (691, 718) if mobile else (345, 390)
    body += f'<path d="M{x} {line_y}H{width-x}" stroke="#372C29"/>'
    body += text(x, motto_y, "MODEL. BUILD. VERIFY." if english else "MODELAR. CONSTRUIR. VERIFICAR.", 20 if mobile else 23, GOLD, 500, 'class="mono" letter-spacing="1.5"')
    if not mobile:
        body += text(1300, 390, "S3 / 01", 18, MUTED, 400, 'class="mono" text-anchor="end"')
    css = ".scanner{opacity:0}"
    if motion:
        css += '''@keyframes glyph{from{opacity:0}to{opacity:1}}@keyframes reveal{from{height:0}to{height:480px}}@keyframes scan{0%{transform:translateY(0);opacity:0}4%,94%{opacity:1}100%{transform:translateY(480px);opacity:0}}.glyph{animation:glyph .12s steps(1,end) both}.reveal{animation:reveal 2.1s .2s cubic-bezier(.4,0,.2,1) both}.scanner{animation:scan 2.1s .2s cubic-bezier(.4,0,.2,1) both}'''
        css += "".join(f".g{i}{{animation-delay:{.45+i*.105:.3f}s}}" for i in range(9))
        css += "@media(prefers-reduced-motion:reduce){.glyph,.reveal,.scanner{animation:none}.scanner{display:none}.reveal{height:480px}}"
    return svg(width, height, title, desc, body, css, defs)


def activity(snapshot, english=False, mobile=False, motion=True):
    width, height = (680, 530) if mobile else (1360, 352)
    end = date.fromisoformat(snapshot["through"])
    start = end - timedelta(days=364)
    stamp = datetime.fromisoformat(snapshot["fetched_at"]).astimezone(ZoneInfo("Europe/Madrid"))
    updated = stamp.strftime("%d.%m.%Y · %H:%M") + " Europe/Madrid"
    period = f"{start:%d.%m.%Y} — {end:%d.%m.%Y}"
    total, active = snapshot["total"], snapshot["active_days"]
    title = "Public activity / 365 days" if english else "Actividad pública / 365 días"
    active_en = "active day" if active == 1 else "active days"
    active_es = "día con actividad" if active == 1 else "días con actividad"
    description = (f"{total} public contributions across {active} {active_en}. {period}. Updated {updated}. Source: GitHub's anonymous public calendar. Contributions are not hours or a quality score."
                   if english else f"{total} contribuciones públicas en {active} {active_es}. {period}. Actualizado {updated}. Fuente: calendario público anónimo de GitHub. Las contribuciones no son horas ni una medida de calidad.")
    body = f'<path d="M1 1H{width-1}V{height-1}H1Z" fill="none" stroke="#30262A"/>'
    body += text(36, 44, "PUBLIC ACTIVITY / 365 DAYS" if english else "ACTIVIDAD PÚBLICA / 365 DÍAS", 20, GOLD, 500, 'class="mono" letter-spacing="1"')
    if mobile:
        body += text(38, 144, total, 86, IVORY, 700)
        body += text(38, 179, "contributions" if english else "contribuciones", 24, MUTED)
        body += text(398, 140, f"{active:02}", 64, IVORY, 600)
        body += text(398, 179, ("active day" if active == 1 else "active days") if english else ("día activo" if active == 1 else "días activos"), 24, MUTED)
        gx, gy, pitch, cell = 48, 264, 11, 8
        body += text(36, 230, period, 21, MUTED, extra='class="mono"')
        body += text(36, 414, "GITHUB · PUBLIC CALENDAR" if english else "GITHUB · CALENDARIO PÚBLICO", 19, MUTED, extra='class="mono"')
        body += text(36, 452, "Updated" if english else "Actualizado", 20, GOLD)
        body += text(36, 484, updated, 19, MUTED, extra='class="mono"')
    else:
        body += text(36, 152, total, 94, IVORY, 700)
        body += text(38, 192, "public contributions" if english else "contribuciones públicas", 24, MUTED)
        active_label = ("active day" if active == 1 else "active days") if english else ("día con actividad" if active == 1 else "días con actividad")
        body += text(38, 236, f"{active} {active_label}", 24, MUTED)
        body += text(396, 88, period, 21, MUTED, extra='class="mono"')
        gx, gy, pitch, cell = 396, 112, 17, 12
        body += text(396, 278, "SOURCE / GITHUB PUBLIC CALENDAR" if english else "FUENTE / CALENDARIO PÚBLICO DE GITHUB", 18, MUTED, extra='class="mono"')
        body += text(36, 320, ("Updated · " if english else "Actualizado · ") + updated, 20, MUTED, extra='class="mono"')
    # Monday first; 365 real dates, no padded future cells or fabricated intensity.
    origin = start - timedelta(days=start.weekday())
    colors = ["#171717", "#B64955", "#CC6971", GOLD, IVORY]
    cells = []
    for day in snapshot["days"]:
        when = date.fromisoformat(day["date"])
        col = (when-origin).days // 7
        row = when.weekday()
        label = f"{day['date']}: {day['count']}"
        cells.append(f'<rect x="{gx+col*pitch}" y="{gy+row*pitch}" width="{cell}" height="{cell}" rx="2" fill="{colors[day["level"]]}"><title>{label}</title></rect>')
    body += '<g>' + "".join(cells) + '</g>'
    legend_y = 371 if mobile else 246
    body += text(gx, legend_y, "Less" if english else "Menos", 18, MUTED)
    for index, color in enumerate(colors):
        body += f'<rect x="{gx+74+index*23}" y="{legend_y-14}" width="14" height="14" rx="2" fill="{color}"/>'
    body += text(gx+200, legend_y, "More" if english else "Más", 18, MUTED)
    if not mobile:
        body += text(1292, 320, "S3 / 02", 18, MUTED, extra='class="mono" text-anchor="end"')
    css = ""
    if motion:
        body += f'<rect class="sweep" x="{gx}" y="{gy-4}" width="2" height="{7*pitch}" fill="{GOLD}" opacity="0"/>'
        distance = 53*pitch
        css = f'@keyframes sweep{{0%{{transform:translateX(0);opacity:0}}5%,90%{{opacity:.7}}100%{{transform:translateX({distance}px);opacity:0}}}}.sweep{{animation:sweep 2.6s .2s ease-in-out both}}@media(prefers-reduced-motion:reduce){{.sweep{{animation:none;display:none}}}}'
    return svg(width, height, title, description, body, css)


def outputs(snapshot):
    result = {}
    for english in (False, True):
        for mobile in (False, True):
            for motion in (True, False):
                suffix = (".en" if english else "") + (".mobile" if mobile else "") + (".static" if not motion else "") + ".svg"
                result[ASSETS / ("header"+suffix)] = hero(english, mobile, motion)
                result[ASSETS / ("activity"+suffix)] = activity(snapshot, english, mobile, motion)
    rows = "\n".join(f"| {day['date']} | {day['count']} |" for day in snapshot["days"] if day["count"])
    stamp = datetime.fromisoformat(snapshot["fetched_at"]).astimezone(ZoneInfo("Europe/Madrid")).strftime("%d.%m.%Y · %H:%M %Z")
    first = snapshot["days"][0]["date"]
    days_es = "día con actividad" if snapshot["active_days"] == 1 else "días con actividad"
    days_en = "active day" if snapshot["active_days"] == 1 else "active days"
    result[ROOT / "docs/ACTIVITY.md"] = f'''<!-- Generated by scripts/render_profile.py; edit the generator, not this snapshot. -->
# Actividad pública · S3rri-dev

Actualización: **{stamp}**, Europe/Madrid. Periodo inclusivo: **{first} — {snapshot['through']}**, 365 días.

**{snapshot['total']} contribuciones públicas · {snapshot['active_days']} {days_es}.**

| Fecha | Contribuciones |
| --- | ---: |
{rows}

Los demás días del periodo tienen cero contribuciones en la fuente consultada. Se excluyen las fechas futuras. Las contribuciones no equivalen a horas de trabajo, dominio técnico ni calidad del código.

Fuente: [calendario público de GitHub](https://github.com/S3rri-dev?tab=overview), consultado **sin autenticación**, sin tokens y sin acceso a repositorios privados. [Respuesta pública del calendario]({snapshot['source']}). [Datos completos de los 365 días](../data/activity.json).

GitHub puede tardar en reflejar contribuciones o corregir sus recuentos. Se muestra la fecha de la última captura válida, no una promesa de tiempo real. Si la fuente falla, está incompleta o cambia de formato, el proceso falla sin publicar cifras nuevas ni sustituir datos por ceros.

Las tarjetas tienen versiones para móvil y escritorio, español e inglés, y versiones estáticas. La preferencia de movimiento reducido selecciona las estáticas; además, las animadas desactivan su movimiento por CSS. El barrido se ejecuta una vez y termina en menos de tres segundos. El avatar original no se modifica.

## Mantenimiento

[Workflow de actualización](../.github/workflows/profile.yml): programado diariamente a las 06:23 UTC, más ejecución manual. GitHub puede retrasar la programación. Usa Ubuntu, Python estándar y únicamente permiso de escritura sobre este repositorio. Los commits se atribuyen a github-actions[bot], sin atribuirlos al titular.

Reproducir desde la raíz:

```sh
python3 scripts/profile_data.py
python3 -m unittest discover -s tests -v
python3 scripts/render_profile.py
python3 scripts/render_profile.py --check
python3 scripts/check_links.py
```

El PNG de 480 px es solo una miniatura del avatar aprobado, preparada con `swift scripts/prepare_avatar.swift`. Está versionada para que el workflow no necesite macOS ni descargar dependencias.

<a id="english"></a>

# Public activity · S3rri-dev

Updated **{stamp}**, Europe/Madrid. Inclusive range: **{first} — {snapshot['through']}**, 365 days.

**{snapshot['total']} public contributions · {snapshot['active_days']} {days_en}.** The dated table above lists every nonzero day; all other dates in the range have zero contributions in the source. [Full accessible data](../data/activity.json).

The source is GitHub's anonymous public calendar. No token, private repository access or third-party card service is used. Contributions are activity, not working hours or a quality score. GitHub may delay or revise counts. The daily workflow keeps the last valid snapshot when fetching or validation fails; its visible timestamp remains unchanged. Automated commits use github-actions[bot], not the account owner's identity.

Cards support mobile/desktop and reduced motion. Animations run once for less than three seconds; static files are also available. This is an original composition using the approved cat bitmap, not GitSkins source code.
'''
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated cards differ")
    args = parser.parse_args()
    snapshot = validate(json.loads((ROOT/"data/activity.json").read_text()))
    cards = outputs(snapshot)
    if args.check:
        different = [str(path.relative_to(ROOT)) for path,value in cards.items() if not path.exists() or path.read_text() != value]
        if different:
            raise SystemExit("Outdated cards: " + ", ".join(different))
    else:
        for path,value in cards.items():
            path.write_text(value)
    print(f"16 profile cards + accessible activity document {'verified' if args.check else 'generated'}.")
