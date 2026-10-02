"""Build the Indonesian defense guide. Requires reportlab.

Run from any directory: python skripsi/tools/build_panduan.py
The editable text is skripsi/panduan/README.md.
"""
from pathlib import Path
from html import escape
import re
import textwrap

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Preformatted, KeepTogether,
)

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "skripsi/panduan/README.md"
OUTPUT = ROOT / "output/pdf/Panduan_Sidang_Takar.pdf"
TEAL = colors.HexColor("#176B67")
INK = colors.HexColor("#21333B")
MUTED = colors.HexColor("#63737B")
PALE = colors.HexColor("#EAF4F2")
W, H = A4
LEFT, RIGHT, TOP, BOTTOM = 48, 48, 62, 48
WIDTH = W - LEFT - RIGHT


def register_fonts():
    candidates = [
        (Path("C:/Windows/Fonts"), ("arial.ttf", "arialbd.ttf", "ariali.ttf", "arialbi.ttf")),
        (Path("/usr/share/fonts/truetype/dejavu"),
         ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf", "DejaVuSans-BoldOblique.ttf")),
        (Path("/usr/share/fonts/truetype/liberation2"),
         ("LiberationSans-Regular.ttf", "LiberationSans-Bold.ttf", "LiberationSans-Italic.ttf", "LiberationSans-BoldItalic.ttf")),
    ]
    for directory, filenames in candidates:
        if all((directory / name).exists() for name in filenames):
            for name, filename in zip(("Guide", "GuideBold", "GuideItalic", "GuideBoldItalic"), filenames):
                pdfmetrics.registerFont(TTFont(name, str(directory / filename)))
            pdfmetrics.registerFontFamily("Guide", normal="Guide", bold="GuideBold",
                                         italic="GuideItalic", boldItalic="GuideBoldItalic")
            return "Guide", "GuideBold"
    return "Helvetica", "Helvetica-Bold"


FONT, BOLD = register_fonts()
STYLES = {
    "body": ParagraphStyle("Body", fontName=FONT, fontSize=10.3, leading=14.4,
                           textColor=INK, spaceAfter=7, alignment=TA_LEFT),
    "h1": ParagraphStyle("H1", fontName=BOLD, fontSize=19, leading=23,
                         textColor=TEAL, spaceAfter=13, keepWithNext=True),
    "h2": ParagraphStyle("H2", fontName=BOLD, fontSize=12.5, leading=16,
                         textColor=TEAL, spaceBefore=8, spaceAfter=6, keepWithNext=True),
    "h3": ParagraphStyle("H3", fontName=BOLD, fontSize=10.8, leading=14.5,
                         textColor=INK, spaceBefore=7, spaceAfter=4, keepWithNext=True),
    "bullet": ParagraphStyle("Bullet", fontName=FONT, fontSize=10.3, leading=14.1,
                             textColor=INK, leftIndent=12, firstLineIndent=-10, spaceAfter=5),
    "cell": ParagraphStyle("Cell", fontName=FONT, fontSize=9.1, leading=12.5,
                           textColor=INK, spaceAfter=0),
    "cellhead": ParagraphStyle("CellHead", fontName=BOLD, fontSize=9.2, leading=12.5,
                               textColor=TEAL, spaceAfter=0),
    "quote": ParagraphStyle("Quote", fontName=FONT, fontSize=10.3, leading=14.4,
                            textColor=TEAL, leftIndent=12, rightIndent=9,
                            backColor=PALE, borderPadding=7, spaceBefore=6, spaceAfter=11),
    "code": ParagraphStyle("Code", fontName="Courier", fontSize=8.1, leading=11,
                           backColor=colors.HexColor("#F3F6F7"), borderPadding=6,
                           spaceBefore=5, spaceAfter=8),
}


def inline(value):
    value = value.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    value = escape(value)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier" size="9">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", value)
    return value


def paragraph(value, kind="body"):
    return Paragraph(inline(value), STYLES[kind])


def make_table(lines):
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    rows = [row for row in rows if not all(re.fullmatch(r":?-+:?", cell.replace(" ", "")) for cell in row)]
    ncols = max(map(len, rows))
    for row in rows:
        row.extend([""] * (ncols - len(row)))
    fractions = {2: [0.32, 0.68], 3: [0.22, 0.39, 0.39], 4: [0.18, 0.29, 0.25, 0.28]}
    widths = [WIDTH * x for x in fractions.get(ncols, [1 / ncols] * ncols)]
    data = [[paragraph(cell, "cellhead" if i == 0 else "cell") for cell in row]
            for i, row in enumerate(rows)]
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PALE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, TEAL),
        ("LINEBELOW", (0, 1), (-1, -1), 0.3, colors.HexColor("#D5E1DF")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFA")]),
    ]))
    return [table, Spacer(1, 10)]


def parse_section(section):
    lines = section.strip().splitlines()
    flowables = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("<!--"):
            i += 1
            continue
        if line.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.extend(textwrap.wrap(lines[i], width=93, replace_whitespace=False) or [""])
                i += 1
            flowables.append(Preformatted("\n".join(code), STYLES["code"]))
            i += 1
            continue
        if line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            flowables.extend(make_table(block))
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flowables.append(paragraph(heading.group(2), "h" + str(len(heading.group(1)))))
            i += 1
            continue
        if line.startswith("> "):
            block = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                block.append(lines[i].strip()[2:])
                i += 1
            flowables.append(paragraph(" ".join(block), "quote"))
            continue
        bullet = re.match(r"^(?:[-*]\s+|\d+\.\s+)(.+)$", line)
        if bullet:
            ordered = re.match(r"^(\d+)\.", line)
            prefix = ordered.group(1) + ". " if ordered else "\u2022 "
            flowables.append(paragraph(prefix + bullet.group(1), "bullet"))
            i += 1
            continue
        if line == "---":
            flowables.append(Spacer(1, 9))
            i += 1
            continue
        block = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|```|[-*] |\d+\. |<!--)", lines[i].strip()):
            block.append(lines[i].strip())
            i += 1
        flowables.append(paragraph(" ".join(block)))
    return flowables


def header(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(MUTED)
    canvas.setFont(FONT, 8)
    canvas.drawString(LEFT, H - 30, "TAKAR  /  PANDUAN BELAJAR DAN SIDANG")
    canvas.drawRightString(W - RIGHT, H - 30, "2 Oktober 2026")
    canvas.setStrokeColor(colors.HexColor("#D1E3E0"))
    canvas.setLineWidth(0.6)
    canvas.line(LEFT, H - 39, W - RIGHT, H - 39)
    canvas.restoreState()


class NumberedCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.states = []

    def showPage(self):
        self.states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self.states)
        for state in self.states:
            self.__dict__.update(state)
            self.saveState()
            self.setFont(FONT, 8)
            self.setFillColor(MUTED)
            self.drawString(LEFT, 27, "Bahan belajar; cocokkan dengan naskah dan hasil penelitian.")
            self.drawRightString(W - RIGHT, 27, f"{self._pageNumber} / {total}")
            self.restoreState()
            super().showPage()
        super().save()


def main():
    text = SOURCE.read_text(encoding="utf-8")
    sections = text.split("<!-- PAGEBREAK -->")
    story = []
    for i, section in enumerate(sections):
        if i:
            story.append(PageBreak())
        story.extend(parse_section(section))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4,
                            leftMargin=LEFT, rightMargin=RIGHT,
                            topMargin=TOP, bottomMargin=BOTTOM,
                            title="Panduan Sidang Takar - Belajar dari Nol",
                            author="Proyek Barista / Takar",
                            subject="Penjelasan skripsi dan persiapan sidang dalam Bahasa Indonesia")
    doc.build(story, onFirstPage=header, onLaterPages=header, canvasmaker=NumberedCanvas)
    print(f"PDF dibuat: {OUTPUT}; bagian yang direncanakan: {len(sections)}")


if __name__ == "__main__":
    main()
