# Zelda SELECT ITEM README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship an NES Zelda SELECT ITEM animated SVG as the KnifelfStudio GitHub profile README, with Markdown fallback.

**Architecture:** A Python generator writes `assets/select-item.svg` (pixel HUD + SMIL). `README.md` embeds that file and repeats the bio. `tests/test_profile_readme.py` locks copy, SMIL, and embed rules.

**Tech Stack:** SVG SMIL, Python 3 stdlib `unittest` + `xml.etree.ElementTree`

## Global Constraints

- English primary copy; Japanese accent includes the exact string `ゼルダの伝説`
- No CSS, no JavaScript, no `<style>` or `<script>` in the SVG
- 32s loop, 4s per inventory slot, yellow cursor, typing clip 0.4s–2.4s of each beat
- Item names and flavor lines match the spec table verbatim
- HUD shows `KNIFELF`, 8 hearts, `$ 2018`
- Do not git commit unless the user asks

---

### Task 1: Profile README contract tests

**Files:**
- Create: `tests/test_profile_readme.py`

**Interfaces:**
- Consumes: nothing
- Produces: unittest module that later tasks must satisfy (`assets/select-item.svg`, `README.md`)

- [ ] **Step 1: Write the failing test**

Create `tests/test_profile_readme.py` with tests that the SVG parses, contains the eight item names and flavor fragments, contains SMIL `dur="32s"` and `repeatCount="indefinite"`, contains no `script`/`style` tags, and that README embeds `assets/select-item.svg` plus Android / Compose / `ゼルダの伝説`.

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_profile_readme -v`  
Expected: FAIL because `assets/select-item.svg` is missing

- [ ] **Step 3: Write generator + SVG + README**

Create `tools/generate_select_item.py` that writes `assets/select-item.svg` meeting the spec, then rewrite `README.md` to embed it and keep a short quest log.

- [ ] **Step 4: Run the tests and make sure they pass**

Run: `python3 -m unittest tests.test_profile_readme -v`  
Expected: PASS; also `python3 -c "import xml.etree.ElementTree as ET; ET.parse('assets/select-item.svg')"`

- [ ] **Step 5: Commit**

Skip unless the user asks.
