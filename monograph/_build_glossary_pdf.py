"""
Convert FS_glossary.md to a polished PDF using reportlab.
Reuses the same rendering engine as the monograph builder.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(HERE, "FS_glossary.md")
PDF_PATH = os.path.join(HERE, "FS_glossary.pdf")

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
_ss = getSampleStyleSheet()

STYLES = {
    "title": ParagraphStyle(
        "FSTitle", parent=_ss["Title"],
        fontSize=22, leading=28, spaceAfter=6,
        textColor=HexColor("#1a1a2e"),
    ),
    "h1": ParagraphStyle(
        "FSH1", parent=_ss["Heading1"],
        fontSize=18, leading=22, spaceBefore=24, spaceAfter=10,
        textColor=HexColor("#1a1a2e"),
    ),
    "h2": ParagraphStyle(
        "FSH2", parent=_ss["Heading2"],
        fontSize=14, leading=18, spaceBefore=18, spaceAfter=8,
        textColor=HexColor("#16213e"),
    ),
    "h3": ParagraphStyle(
        "FSH3", parent=_ss["Heading3"],
        fontSize=12, leading=15, spaceBefore=12, spaceAfter=6,
        textColor=HexColor("#0f3460"),
    ),
    "body": ParagraphStyle(
        "FSBody", parent=_ss["Normal"],
        fontSize=10, leading=13.5, alignment=TA_JUSTIFY,
        spaceAfter=6,
    ),
    "term_def": ParagraphStyle(
        "FSTermDef", parent=_ss["Normal"],
        fontSize=10, leading=13.5, alignment=TA_JUSTIFY,
        spaceAfter=2, leftIndent=0,
    ),
    "term_meta": ParagraphStyle(
        "FSTermMeta", parent=_ss["Normal"],
        fontSize=9, leading=12, alignment=TA_LEFT,
        spaceAfter=10, leftIndent=12,
        textColor=HexColor("#555555"),
    ),
    "code": ParagraphStyle(
        "FSCode", parent=_ss["Code"],
        fontSize=8.5, leading=11, leftIndent=24, rightIndent=12,
        spaceBefore=4, spaceAfter=4,
        backColor=HexColor("#f5f5f5"),
        fontName="Courier",
    ),
    "table_header": ParagraphStyle(
        "FSTableHeader", parent=_ss["Normal"],
        fontSize=8.5, leading=11, fontName="Helvetica-Bold",
    ),
    "table_cell": ParagraphStyle(
        "FSTableCell", parent=_ss["Normal"],
        fontSize=8.5, leading=11,
    ),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _inline(text):
    """Convert **bold**, *italic*, `code` for reportlab XML."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r'<font face="Courier" size="9">\1</font>', text)
    return text


def _safe_para(text, style):
    try:
        return Paragraph(text, style)
    except Exception:
        safe = re.sub(r"<[^>]+>", "", text)
        return Paragraph(safe, style)


def _parse_table(lines):
    rows = []
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if i == 1 and all(set(c.strip()) <= set("-: ") for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return None
    data = []
    for i, row in enumerate(rows):
        style = STYLES["table_header"] if i == 0 else STYLES["table_cell"]
        data.append([_safe_para(_inline(c), style) for c in row])
    ncols = max(len(r) for r in data)
    for r in data:
        while len(r) < ncols:
            r.append(Paragraph("", STYLES["table_cell"]))
    col_width = (6.5 * inch) / ncols
    t = Table(data, colWidths=[col_width] * ncols)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#e8e8e8")),
        ("TEXTCOLOR", (0, 0), (-1, 0), black),
        ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#bbbbbb")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


_page_num = [0]

def _on_page(canvas_obj, doc):
    _page_num[0] += 1
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(HexColor("#888888"))
    canvas_obj.drawCentredString(letter[0] / 2, 0.5 * inch, f"— {_page_num[0]} —")
    canvas_obj.drawString(inch, 0.5 * inch, "Factor Skyline — Glossary")
    canvas_obj.restoreState()


# ---------------------------------------------------------------------------
# Main conversion — glossary-aware parser
# ---------------------------------------------------------------------------
def convert():
    with open(MD_PATH, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    doc = SimpleDocTemplate(
        PDF_PATH, pagesize=letter,
        leftMargin=inch, rightMargin=inch,
        topMargin=0.9 * inch, bottomMargin=0.9 * inch,
    )

    story = []
    lines = [l.rstrip("\n") for l in raw_lines]
    i = 0
    n = len(lines)
    title_done = False

    while i < n:
        line = lines[i]

        # Blank
        if not line.strip():
            i += 1
            continue

        # HR
        if re.match(r"^-{3,}$", line.strip()):
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=0.5,
                                     color=HexColor("#cccccc"),
                                     spaceAfter=6, spaceBefore=6))
            i += 1
            continue

        # Title (first # heading)
        m_h1 = re.match(r"^# (.+)$", line)
        if m_h1 and not title_done:
            story.append(Spacer(1, 36))
            story.append(Paragraph(_inline(m_h1.group(1)), STYLES["title"]))
            story.append(Spacer(1, 24))
            title_done = True
            i += 1
            continue

        # H1
        if m_h1 and title_done:
            story.append(PageBreak())
            story.append(Paragraph(_inline(m_h1.group(1)), STYLES["h1"]))
            i += 1
            continue

        # H2 — section headings
        m_h2 = re.match(r"^## (.+)$", line)
        if m_h2:
            story.append(Paragraph(_inline(m_h2.group(1)), STYLES["h2"]))
            i += 1
            continue

        # H3
        m_h3 = re.match(r"^### (.+)$", line)
        if m_h3:
            story.append(Paragraph(_inline(m_h3.group(1)), STYLES["h3"]))
            i += 1
            continue

        # Table
        if "|" in line and i + 1 < n and "|" in lines[i + 1]:
            table_lines = []
            while i < n and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            t = _parse_table(table_lines)
            if t:
                story.append(Spacer(1, 4))
                story.append(t)
                story.append(Spacer(1, 4))
            continue

        # Glossary entry: **Term.** on its own line
        # Collect term block: definition line, *Introduced...*, Cross-references:
        m_term = re.match(r"^\*\*(.+?)\.\*\*$", line.strip())
        if m_term:
            term_name = m_term.group(1)
            i += 1
            # Collect the definition (next non-blank line(s) until *Introduced or Cross-ref)
            def_lines = []
            meta_lines = []
            while i < n and lines[i].strip():
                l = lines[i].strip()
                if l.startswith("*Introduced") or l.startswith("Cross-references:"):
                    meta_lines.append(l)
                else:
                    def_lines.append(l)
                i += 1

            definition = " ".join(def_lines)
            meta = " ".join(meta_lines)

            # Build a KeepTogether block for the entry
            entry_parts = []
            entry_parts.append(
                _safe_para(f"<b>{_inline(term_name)}.</b> {_inline(definition)}",
                           STYLES["term_def"])
            )
            if meta:
                entry_parts.append(
                    _safe_para(_inline(meta), STYLES["term_meta"])
                )
            else:
                entry_parts.append(Spacer(1, 8))

            story.append(KeepTogether(entry_parts))
            continue

        # Regular paragraph
        para_lines = []
        while i < n and lines[i].strip() and \
              not lines[i].startswith("#") and \
              not re.match(r"^-{3,}$", lines[i].strip()) and \
              not re.match(r"^\*\*(.+?)\.\*\*$", lines[i].strip()):
            para_lines.append(lines[i])
            i += 1

        if para_lines:
            text = " ".join(l.strip() for l in para_lines)
            story.append(_safe_para(_inline(text), STYLES["body"]))

    doc.build(story, onFirstPage=_on_page, onLaterPages=_on_page)
    print(f"PDF written to: {PDF_PATH}")
    print(f"Pages: {_page_num[0]}")


if __name__ == "__main__":
    convert()
