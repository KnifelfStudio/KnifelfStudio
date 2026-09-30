#!/usr/bin/env python3
"""Generate the NES Zelda SELECT ITEM SVG for the GitHub profile README."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "select-item.svg"

PALETTE = {
    "W": "#fcfcfc",
    "Y": "#fcfc54",
    "G": "#fcbc54",
    "O": "#fc9838",
    "B": "#c84c0c",
    "D": "#743010",
    "R": "#e83828",
    "P": "#fc7460",
    "U": "#3cbcfc",
    "N": "#0050d8",
    "K": "#181818",
    "C": "#58f8f8",
    "A": "#7c7c7c",
    "E": "#3c3c3c",
    "F": "#00a800",
    "T": "#fcbcb0",
    "H": "#a80020",
    "M": "#b88838",
}

ICONS = {
    "sword": [
        "................",
        "......YY........",
        "......WW........",
        "......WW........",
        "......WW........",
        "......WW........",
        "......WW........",
        "......WW........",
        ".....YYYY.......",
        "......BB........",
        "......BB........",
        ".....BBBB.......",
        "......DD........",
        "......DD........",
        "................",
        "................",
    ],
    "shield": [
        "................",
        "......WWWW......",
        "....WWWWWWWW....",
        "...WRRRRRRRRW...",
        "..WRRWWWWWRRW...",
        "..WRRWWRRWWRW...",
        "..WRRWWWWWRRW...",
        "..WRRRRRRRRRW...",
        "...WRRRRRRRW....",
        "....WRRRRRW.....",
        ".....WRRRW......",
        "......WWW.......",
        "................",
        "................",
        "................",
        "................",
    ],
    "slate": [
        "................",
        ".AAAAAAAAAAAAAA.",
        ".AEEEEEEEEEEEEA.",
        ".AECCCCCCCCCCEA.",
        ".AEC........CEA.",
        ".AEC.CCCCCC.CEA.",
        ".AEC.C....C.CEA.",
        ".AEC.C.CC.C.CEA.",
        ".AEC.C....C.CEA.",
        ".AEC.CCCCCC.CEA.",
        ".AEC...CC...CEA.",
        ".AECCCCCCCCCCEA.",
        ".AEEEEEEEEEEEEA.",
        ".AAAAAAAAAAAAAA.",
        "................",
        "................",
    ],
    "book": [
        "................",
        "..DDDDDDDDDDD...",
        ".DTMMMMMMMMMMD..",
        ".DTGGGGGGGGGMD..",
        ".DTMMMMMMMMMMD..",
        ".DT.........MD..",
        ".DTMMMMMMMMMMD..",
        ".DTGGGGGGGGGMD..",
        ".DTMMMMMMMMMMD..",
        ".DT.........MD..",
        ".DTMMMMMMMMMMD..",
        ".DDDDDDDDDDDDD..",
        "..DDDDDDDDDDD...",
        "................",
        "................",
        "................",
    ],
    "ocarina": [
        "................",
        "................",
        "......UUUU......",
        "....UUWWWWUU....",
        "...UWWKKKKWWU...",
        "...UWKKWWKKWU...",
        "...UWWKKKKWWU...",
        "....UUWWWWUU....",
        ".....UUUUUU.....",
        "....BBBBBBBB....",
        ".....BBBBBB.....",
        "................",
        "................",
        "................",
        "................",
        "................",
    ],
    "map": [
        "................",
        ".TTTTTTTTTTTTTT.",
        ".TFF........FFT.",
        ".TF.FFFF.....FT.",
        ".TF....FFF...FT.",
        ".TF......FF..FT.",
        ".TFFF.....FF.FT.",
        ".T..FFF....F.FT.",
        ".T....FFFFF..FT.",
        ".TFF........FFT.",
        ".TTTTTTTTTTTTTT.",
        "................",
        "................",
        "................",
        "................",
        "................",
    ],
    "compass": [
        "................",
        "......RRR.......",
        ".....RYYYR......",
        "....NNNNNNNN....",
        "...NNWWWWWWNN...",
        "...NWWWKWWWN....",
        "...NWWWKKWWN....",
        "...NWWWKWWWN....",
        "...NNWWWWWWNN...",
        "....NNNNNNNN....",
        "......WWW.......",
        "................",
        "................",
        "................",
        "................",
        "................",
    ],
}

HEART = [
    ".HH.HH.",
    "HRRRRRH",
    "HRPRPRH",
    "HRRRRRH",
    ".HRRRH.",
    "..HRH..",
    "...H...",
]

RUPEE = [
    "..F..",
    ".FWF.",
    "FWWWF",
    ".FWF.",
    "..F..",
]

ITEMS = [
    {
        "icon": "sword",
        "label": "SWORD",
        "name": "WOODEN SWORD",
        "lines": ["Kotlin. A hero's first blade", "— forged in 2018."],
    },
    {
        "icon": "shield",
        "label": "SHIELD",
        "name": "HYLIAN SHIELD",
        "lines": ["Android Architecture Components.", "Guard against chaos."],
    },
    {
        "icon": "slate",
        "label": "SLATE",
        "name": "SHEIKAH SLATE",
        "lines": ["Android. The tool always equipped."],
    },
    {
        "icon": "book",
        "label": "BOOK",
        "name": "BOOK OF MUDORA",
        "lines": ["Jetpack Compose.", "Currently deciphering this ancient text."],
    },
    {
        "icon": "triforce",
        "label": "TRIFORCE",
        "name": "TRIFORCE",
        "lines": ["ゼルダの伝説.", "The reason this pause screen exists."],
    },
    {
        "icon": "ocarina",
        "label": "OCARINA",
        "name": "OCARINA",
        "lines": ["A gamer's instrument.", "Played when the code compiles."],
    },
    {
        "icon": "map",
        "label": "MAP",
        "name": "MAP",
        "lines": ["A tech enthusiast.", "Every dungeon is a new API."],
    },
    {
        "icon": "compass",
        "label": "COMPASS",
        "name": "COMPASS",
        "lines": ["Knifelf Studio.", "Points toward the next quest."],
    },
]

VW, VH = 512, 428
CELL_W, CELL_H, GAP = 96, 80, 10
GRID_X = (VW - (4 * CELL_W + 3 * GAP)) // 2
GRID_Y = 108
DESC_X, DESC_Y, DESC_W, DESC_H = 36, 296, 440, 104


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def stamp(lines: list[str], x: int, y: int, scale: int) -> str:
    parts = []
    for row_i, row in enumerate(lines):
        for col_i, ch in enumerate(row):
            color = PALETTE.get(ch)
            if not color:
                continue
            parts.append(
                f'<rect x="{x + col_i * scale}" y="{y + row_i * scale}" '
                f'width="{scale}" height="{scale}" fill="{color}"/>'
            )
    return "\n".join(parts)


def cell_origin(index: int) -> tuple[int, int]:
    col, row = index % 4, index // 4
    return GRID_X + col * (CELL_W + GAP), GRID_Y + row * (CELL_H + GAP)


def opacity_keytimes(index: int) -> tuple[str, str]:
    start = index / 8
    end = (index + 1) / 8
    if index == 0:
        return "1;1;0;0", f"0;{end - 0.0001:.4f};{end:.4f};1"
    if index == 7:
        return "0;0;1;1", f"0;{start:.4f};{start + 0.0001:.4f};1"
    return (
        "0;0;1;1;0;0",
        f"0;{start:.4f};{start + 0.0001:.4f};{end - 0.0001:.4f};{end:.4f};1",
    )


def triforce(cx: int, cy: int, size: int, animate: bool) -> str:
    h = size
    w = size
    top = (
        f"{cx},{cy - h // 2} "
        f"{cx - w // 4},{cy} "
        f"{cx + w // 4},{cy}"
    )
    left = (
        f"{cx - w // 4},{cy} "
        f"{cx - w // 2},{cy + h // 2} "
        f"{cx},{cy + h // 2}"
    )
    right = (
        f"{cx + w // 4},{cy} "
        f"{cx},{cy + h // 2} "
        f"{cx + w // 2},{cy + h // 2}"
    )
    glow = ""
    if animate:
        glow = (
            '<animate attributeName="fill" values="#c89018;#c89018;#fcfc54;#fcfc54;#c89018;#c89018" '
            'keyTimes="0;0.5000;0.5001;0.6249;0.6250;1" dur="32s" repeatCount="indefinite"/>'
        )
    polys = []
    for pts in (top, left, right):
        polys.append(
            f'<polygon points="{pts}" fill="#c89018" stroke="#6c3010" stroke-width="1">'
            f"{glow}</polygon>"
        )
    return "\n".join(polys)


def build() -> str:
    parts: list[str] = [
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VW} {VH}" width="{VW}" height="{VH}" role="img" shape-rendering="crispEdges">
  <title>Knifelf — SELECT ITEM</title>
  <desc>Knifelf, an Android Developer working on Android since 2018. Currently learning Android Architecture Components and Jetpack Compose. Gamer and fan of ゼルダの伝説.</desc>
  <rect width="{VW}" height="{VH}" fill="#100808"/>
  <rect x="10" y="10" width="{VW - 20}" height="{VH - 20}" fill="#fcbc54"/>
  <rect x="16" y="16" width="{VW - 32}" height="{VH - 32}" fill="#743010"/>
  <rect x="22" y="22" width="{VW - 44}" height="{VH - 44}" fill="#1c1008"/>
  <rect x="28" y="28" width="{VW - 56}" height="{VH - 56}" fill="none" stroke="#fcbc54" stroke-width="2"/>
'''
    ]

    parts.append(
        f'<text x="{VW // 2}" y="48" text-anchor="middle" fill="#fcfcfc" '
        f'font-family="Courier New, Courier, monospace" font-size="18" '
        f'font-weight="700">{esc("— SELECT ITEM —")}</text>\n'
    )
    parts.append(
        f'<text x="{VW // 2}" y="68" text-anchor="middle" fill="#fcbc54" '
        f'font-family="Courier New, Courier, monospace" font-size="13">'
        f'{esc("KNIFELF")}</text>\n'
    )

    parts.append('<g>\n')
    parts.append(
        '<animate attributeName="opacity" values="1;0.72;1" dur="1.8s" repeatCount="indefinite"/>\n'
    )
    parts.append(
        '<text x="40" y="96" fill="#e83828" font-family="Courier New, Courier, monospace" '
        'font-size="11">LIFE</text>\n'
    )
    heart_x = 78
    for _ in range(8):
        parts.append(stamp(HEART, heart_x, 82, 2))
        parts.append("\n")
        heart_x += 18
    parts.append("</g>\n")

    rupee_x = 388
    parts.append(stamp(RUPEE, rupee_x, 80, 4))
    parts.append(
        f'<text x="{rupee_x + 28}" y="96" fill="#fcfc54" '
        f'font-family="Courier New, Courier, monospace" font-size="13">{esc("$ 2018")}</text>\n'
    )

    xs = []
    ys = []
    for i in range(8):
        x, y = cell_origin(i)
        xs.append(str(x))
        ys.append(str(y))
        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{CELL_H}" '
            f'fill="#140c08" stroke="#6c3c14" stroke-width="3"/>\n'
        )
        icon_x, icon_y = x + 24, y + 10
        icon = ITEMS[i]["icon"]
        if icon == "triforce":
            parts.append(triforce(x + CELL_W // 2, y + 36, 44, animate=True))
            parts.append("\n")
        else:
            parts.append(stamp(ICONS[icon], icon_x, icon_y, 3))
            parts.append("\n")
        parts.append(
            f'<text x="{x + CELL_W // 2}" y="{y + CELL_H - 8}" text-anchor="middle" '
            f'fill="#c89018" font-family="Courier New, Courier, monospace" font-size="8">'
            f'{esc(ITEMS[i]["label"])}</text>\n'
        )

    parts.append(
        f'<rect x="{xs[0]}" y="{ys[0]}" width="{CELL_W}" height="{CELL_H}" '
        f'fill="none" stroke="#fcfc54" stroke-width="3">\n'
        f'  <animate attributeName="x" values="{";".join(xs)}" dur="32s" '
        f'calcMode="discrete" repeatCount="indefinite"/>\n'
        f'  <animate attributeName="y" values="{";".join(ys)}" dur="32s" '
        f'calcMode="discrete" repeatCount="indefinite"/>\n'
        f'  <animate attributeName="opacity" values="1;0;1;0;1;1" '
        f'keyTimes="0;0.025;0.05;0.075;0.1;1" dur="4s" repeatCount="indefinite"/>\n'
        f"</rect>\n"
    )

    parts.append(
        f'<rect x="{DESC_X}" y="{DESC_Y}" width="{DESC_W}" height="{DESC_H}" '
        f'fill="#140c08" stroke="#a04c18" stroke-width="3"/>\n'
        f'<rect x="{DESC_X + 6}" y="{DESC_Y + 6}" width="{DESC_W - 12}" height="{DESC_H - 12}" '
        f'fill="none" stroke="#fcbc54" stroke-width="1"/>\n'
    )

    for i, item in enumerate(ITEMS):
        values, keys = opacity_keytimes(i)
        name_y = DESC_Y + 36
        parts.append(f'<g opacity="{1 if i == 0 else 0}">\n')
        parts.append(
            f'<animate attributeName="opacity" values="{values}" keyTimes="{keys}" '
            f'dur="32s" repeatCount="indefinite"/>\n'
        )
        parts.append(
            f'<text x="{DESC_X + 20}" y="{name_y}" fill="#fcfcfc" '
            f'font-family="Courier New, Courier, monospace" font-size="16">'
            f'{esc(item["name"])}</text>\n'
        )
        for line_i, line in enumerate(item["lines"]):
            fam = "sans-serif" if any("\u3040" <= ch <= "\u30ff" or "\u4e00" <= ch <= "\u9fff" for ch in line) else "Courier New, Courier, monospace"
            parts.append(
                f'<text x="{DESC_X + 20}" y="{name_y + 24 + line_i * 18}" fill="#a8fc54" '
                f'font-family="{fam}" font-size="13">{esc(line)}</text>\n'
            )
        parts.append("</g>\n")

    parts.append(
        f'<text x="{DESC_X + DESC_W - 28}" y="{DESC_Y + DESC_H - 18}" fill="#fcfc54" '
        f'font-family="Courier New, Courier, monospace" font-size="16">_\n'
        f'  <animate attributeName="opacity" values="1;0;1" dur="0.5s" repeatCount="indefinite"/>\n'
        f"</text>\n"
    )

    parts.append("</svg>\n")
    return "".join(parts)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
