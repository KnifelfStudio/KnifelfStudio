# GitHub profile SELECT ITEM screen

Date: 2026-09-29  
Repo: `KnifelfStudio/KnifelfStudio` (GitHub profile README)

## Goal

Replace the plain-text profile README with a full-immersion NES Zelda pause-menu inventory. One self-contained animated SVG is the main visual; Markdown below it repeats the same facts so the page still reads if the image fails.

## Decisions (locked)

- Theme: ゼルダの伝説 / NES pixel HUD, not Sheikah slate or Game Boy LCD
- Layout: SELECT ITEM equipment grid (not quest-log header, not dungeon map)
- Animation: custom SVG SMIL only (no CSS, no JS, no third-party widgets)
- Copy: English primary, Japanese accent on Zelda lines
- README: centered SVG + short Markdown quest log (not SVG-only)

## Inventory mapping

| Slot | Name | Meaning |
|------|------|---------|
| 0 | WOODEN SWORD | Kotlin. A hero's first blade — forged in 2018. |
| 1 | HYLIAN SHIELD | Android Architecture Components. Guard against chaos. |
| 2 | SHEIKAH SLATE | Android. The tool always equipped. |
| 3 | BOOK OF MUDORA | Jetpack Compose. Currently deciphering this ancient text. |
| 4 | TRIFORCE | ゼルダの伝説. The reason this pause screen exists. |
| 5 | OCARINA | A gamer's instrument. Played when the code compiles. |
| 6 | MAP | A tech enthusiast. Every dungeon is a new API. |
| 7 | COMPASS | Knifelf Studio. Points toward the next quest. |

HUD: `KNIFELF`, `LIFE` with 8 hearts (adventure since 2018), rupee counter `$ 2018`.

## Animation (32s loop)

Each of 8 slots is 4 seconds:

1. Yellow cursor jumps to the slot (discrete SMIL) and flashes twice in the first 0.4s of the beat.
2. The matching description is visible for those 4 seconds (opacity cycle). GitHub-as-image often freezes clip-path wipes, so typing is not used; the box stays readable on the first frame.
3. Underscore blinks in the description frame.
4. Next slot.

Always-on: hearts pulse weakly (not empty/damage). Triforce gold brightens while slot 4 is selected. No walking Link, no attack VFX.

GitHub constraint: visitors cannot click slots. SMIL may freeze on some clients; Markdown fallback must carry the bio.

## Architecture

- `assets/select-item.svg` — entire pause screen (pixel icons as rects, SMIL, presentation attributes only; no `<script>`, no `<style>`)
- `README.md` — `<img>` (or equivalent) pointing at that file, long `alt`, then a short English quest log with `ゼルダの伝説`
- Icons are pixel rectangles, not emoji
- Palette stays NES brown / gold / red so it reads on GitHub light and dark

## Verification

- SVG parses as XML
- Local browser (or rasterizer) shows the 32s cycle
- Tests assert required copy, SMIL loop, README embed, and no script/style
