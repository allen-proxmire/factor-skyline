"""
Convert FS_monograph.md to a polished PDF using reportlab.
Handles: headings, body text, bold, italic, tables, code blocks,
theorem/definition blocks, horizontal rules, and the reference list.
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
from reportlab.lib import colors


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(HERE, "FS_monograph.md")
PDF_PATH = os.path.join(HERE, "FS_monograph.pdf")

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
    "author": ParagraphStyle(
        "FSAuthor", parent=_ss["Normal"],
        fontSize=13, leading=16, alignment=TA_CENTER,
        spaceAfter=2, textColor=HexColor("#444444"),
    ),
    "date": ParagraphStyle(
        "FSDate", parent=_ss["Normal"],
        fontSize=11, leading=14, alignment=TA_CENTER,
        spaceAfter=24, textColor=HexColor("#666666"),
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
    "code": ParagraphStyle(
        "FSCode", parent=_ss["Code"],
        fontSize=8.5, leading=11, leftIndent=24, rightIndent=12,
        spaceBefore=4, spaceAfter=4,
        backColor=HexColor("#f5f5f5"),
        borderColor=HexColor("#cccccc"),
        borderWidth=0.5, borderPadding=4,
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
# Markdown → inline XML for reportlab Paragraphs
# ---------------------------------------------------------------------------
def _inline(text):
    """Convert **bold**, *italic*, `code`, and clean up for XML."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # italic (but not inside bold markers)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    # inline code
    text = re.sub(r"`([^`]+)`", r'<font face="Courier" size="9">\1</font>', text)
    return text


def _safe_para(text, style):
    """Create a Paragraph, falling back to plain text on XML errors."""
    try:
        return Paragraph(text, style)
    except Exception:
        safe = re.sub(r"<[^>]+>", "", text)
        return Paragraph(safe, style)


# ---------------------------------------------------------------------------
# Table parser
# ---------------------------------------------------------------------------
def _parse_table(lines):
    """Parse a list of markdown table lines into a reportlab Table."""
    rows = []
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if i == 1 and all(set(c.strip()) <= set("-: ") for c in cells):
            continue  # separator row
        rows.append(cells)
    if not rows:
        return None

    # Build reportlab table data
    data = []
    for i, row in enumerate(rows):
        style = STYLES["table_header"] if i == 0 else STYLES["table_cell"]
        data.append([_safe_para(_inline(c), style) for c in row])

    ncols = max(len(r) for r in data)
    # Pad short rows
    for r in data:
        while len(r) < ncols:
            r.append(Paragraph("", STYLES["table_cell"]))

    col_width = (6.5 * inch) / ncols
    t = Table(data, colWidths=[col_width] * ncols)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#e8e8e8")),
        ("TEXTCOLOR", (0, 0), (-1, 0), black),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#bbbbbb")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


# ---------------------------------------------------------------------------
# Page template with header/footer
# ---------------------------------------------------------------------------
_page_num = [0]

def _on_page(canvas_obj, doc):
    _page_num[0] += 1
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(HexColor("#888888"))
    canvas_obj.drawCentredString(
        letter[0] / 2, 0.5 * inch,
        f"— {_page_num[0]} —"
    )
    canvas_obj.drawString(
        inch, 0.5 * inch,
        "Factor Skyline Monograph"
    )
    canvas_obj.restoreState()


# ---------------------------------------------------------------------------
# Main conversion
# ---------------------------------------------------------------------------
def convert():
    with open(MD_PATH, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=0.9 * inch,
        bottomMargin=0.9 * inch,
    )

    story = []
    lines = [l.rstrip("\n") for l in raw_lines]
    i = 0
    n = len(lines)

    # Track whether we've processed the title block
    title_done = False

    while i < n:
        line = lines[i]

        # --- Blank line ---
        if not line.strip():
            i += 1
            continue

        # --- Horizontal rule ---
        if re.match(r"^-{3,}$", line.strip()):
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=0.5,
                                     color=HexColor("#cccccc"),
                                     spaceAfter=6, spaceBefore=6))
            i += 1
            continue

        # --- Code block ---
        if line.strip().startswith("```"):
            i += 1
            code_lines = []
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_text = "\n".join(code_lines)
            code_text = code_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            code_text = code_text.replace("\n", "<br/>")
            story.append(_safe_para(code_text, STYLES["code"]))
            continue

        # --- Table ---
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

        # --- Title (first # line) ---
        m_h1 = re.match(r"^# (.+)$", line)
        if m_h1 and not title_done:
            story.append(Spacer(1, 48))
            story.append(Paragraph(_inline(m_h1.group(1)), STYLES["title"]))
            # Next non-blank lines might be author + date
            i += 1
            while i < n and not lines[i].strip():
                i += 1
            if i < n and not lines[i].startswith("#") and not lines[i].startswith("---"):
                story.append(Paragraph(_inline(lines[i].strip()), STYLES["author"]))
                i += 1
            while i < n and not lines[i].strip():
                i += 1
            if i < n and not lines[i].startswith("#") and not lines[i].startswith("---"):
                story.append(Paragraph(_inline(lines[i].strip()), STYLES["date"]))
                i += 1
            story.append(Spacer(1, 36))
            title_done = True
            continue

        # --- H1 (Part headings) ---
        if m_h1 and title_done:
            story.append(PageBreak())
            story.append(Paragraph(_inline(m_h1.group(1)), STYLES["h1"]))
            i += 1
            continue

        # --- H2 ---
        m_h2 = re.match(r"^## (.+)$", line)
        if m_h2:
            story.append(Paragraph(_inline(m_h2.group(1)), STYLES["h2"]))
            i += 1
            continue

        # --- H3 ---
        m_h3 = re.match(r"^### (.+)$", line)
        if m_h3:
            story.append(Paragraph(_inline(m_h3.group(1)), STYLES["h3"]))
            i += 1
            continue

        # --- Indented block (4 spaces = code/formula) ---
        if line.startswith("    "):
            code_lines = []
            while i < n and (lines[i].startswith("    ") or not lines[i].strip()):
                code_lines.append(lines[i])
                i += 1
            code_text = "\n".join(l[4:] if l.startswith("    ") else l for l in code_lines)
            code_text = code_text.strip()
            code_text = code_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            code_text = code_text.replace("\n", "<br/>")
            story.append(_safe_para(code_text, STYLES["code"]))
            continue

        # --- Regular paragraph ---
        # Collect consecutive non-blank, non-special lines
        para_lines = []
        while i < n and lines[i].strip() and \
              not lines[i].startswith("#") and \
              not lines[i].startswith("```") and \
              not re.match(r"^-{3,}$", lines[i].strip()) and \
              not ("|" in lines[i] and i + 1 < n and "|" in lines[i + 1] and "-" in lines[i + 1]) and \
              not lines[i].startswith("    "):
            para_lines.append(lines[i])
            i += 1

        if para_lines:
            text = " ".join(l.strip() for l in para_lines)
            story.append(_safe_para(_inline(text), STYLES["body"]))

    # Build PDF
    doc.build(story, onFirstPage=_on_page, onLaterPages=_on_page)
    print(f"PDF written to: {PDF_PATH}")
    print(f"Pages: {_page_num[0]}")


if __name__ == "__main__":
    convert()
