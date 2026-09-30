import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / "assets" / "select-item.svg"
README = ROOT / "README.md"

REQUIRED_SVG_COPY = (
    "WOODEN SWORD",
    "HYLIAN SHIELD",
    "SHEIKAH SLATE",
    "BOOK OF MUDORA",
    "TRIFORCE",
    "OCARINA",
    "MAP",
    "COMPASS",
    "ゼルダの伝説",
    "Kotlin. A hero's first blade",
    "Android Architecture Components",
    "Android. The tool always equipped",
    "Jetpack Compose",
    "A gamer's instrument",
    "Every dungeon is a new API",
    "Knifelf Studio",
    "KNIFELF",
    "2018",
    "SELECT ITEM",
)


class TestSelectItemSvg(unittest.TestCase):
    def test_svg_exists_and_parses(self):
        self.assertTrue(SVG.is_file(), f"missing {SVG}")
        ET.parse(SVG)

    def test_required_copy(self):
        text = SVG.read_text(encoding="utf-8")
        for needle in REQUIRED_SVG_COPY:
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_smil_loop_without_script_or_css(self):
        text = SVG.read_text(encoding="utf-8")
        lowered = text.lower()
        self.assertIn("<animate", lowered)
        self.assertIn('dur="32s"', text)
        self.assertIn('repeatCount="indefinite"', text)
        self.assertIn('calcMode="discrete"', text)
        self.assertNotIn("<script", lowered)
        self.assertNotIn("<style", lowered)


class TestReadmeStage(unittest.TestCase):
    def test_embeds_svg_and_fallback_bio(self):
        text = README.read_text(encoding="utf-8")
        self.assertIn("assets/select-item.svg", text)
        self.assertIn("Android", text)
        self.assertIn("Jetpack Compose", text)
        self.assertIn("ゼルダの伝説", text)
        self.assertIn("2018", text)


if __name__ == "__main__":
    unittest.main()
