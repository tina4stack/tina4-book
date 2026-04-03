#!/usr/bin/env python3
"""Build Tina4-for-JavaScript-Developers.pdf from markdown chapters."""

import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import inch, mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Preformatted, Table, TableStyle, KeepTogether, Image
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Constants ────────────────────────────────────────────────────────
BOOK_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BOOK_DIR, "Tina4-for-JavaScript-Developers.pdf")
WIDTH, HEIGHT = A4

CHAPTERS = [
    "README.md",
    "chapters/01-getting-started.md",
    "chapters/02-signals.md",
    "chapters/03-html-templates.md",
    "chapters/04-components.md",
    "chapters/05-routing.md",
    "chapters/06-api.md",
    "chapters/07-websocket.md",
    "chapters/08-pwa.md",
    "chapters/09-debug.md",
    "chapters/10-tina4-css.md",
    "chapters/11-backend-integration.md",
    "chapters/12-building-a-complete-app.md",
    "chapters/13-patterns-and-pitfalls.md",
    "chapters/14-vibe-coding-with-ai.md",
]

# ── Colors ───────────────────────────────────────────────────────────
BRAND_BLUE = HexColor("#38bdf8")
DARK_BG = HexColor("#0f172a")
CODE_BG = HexColor("#1e293b")
LIGHT_TEXT = HexColor("#e2e8f0")
MUTED = HexColor("#64748b")

# ── Styles ───────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    'BookTitle', parent=styles['Title'],
    fontSize=28, leading=34, textColor=BRAND_BLUE,
    alignment=TA_CENTER, spaceAfter=12,
))
styles.add(ParagraphStyle(
    'BookSubtitle', parent=styles['Normal'],
    fontSize=14, leading=18, textColor=MUTED,
    alignment=TA_CENTER, spaceAfter=40,
))
styles.add(ParagraphStyle(
    'ChapterTitle', parent=styles['Heading1'],
    fontSize=22, leading=28, textColor=BRAND_BLUE,
    spaceBefore=0, spaceAfter=16,
))
styles.add(ParagraphStyle(
    'SectionHead', parent=styles['Heading2'],
    fontSize=16, leading=20, textColor=HexColor("#7dd3fc"),
    spaceBefore=18, spaceAfter=8,
))
styles.add(ParagraphStyle(
    'SubSection', parent=styles['Heading3'],
    fontSize=13, leading=16, textColor=HexColor("#94a3b8"),
    spaceBefore=12, spaceAfter=6,
))
styles.add(ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=black,
    alignment=TA_LEFT, spaceAfter=8,
))
styles.add(ParagraphStyle(
    'CodeBlock', parent=styles['Code'],
    fontSize=8, leading=11, textColor=HexColor("#1e293b"),
    backColor=HexColor("#f1f5f9"),
    borderWidth=1, borderColor=HexColor("#e2e8f0"),
    borderPadding=8, borderRadius=4,
    spaceBefore=6, spaceAfter=10,
    leftIndent=12, rightIndent=12,
))
styles.add(ParagraphStyle(
    'InlineCode', parent=styles['Normal'],
    fontSize=9, textColor=HexColor("#1e293b"),
    backColor=HexColor("#f1f5f9"),
))
styles.add(ParagraphStyle(
    'BulletItem', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=black,
    leftIndent=24, bulletIndent=12, spaceAfter=4,
))
styles.add(ParagraphStyle(
    'TOCEntry', parent=styles['Normal'],
    fontSize=11, leading=18, textColor=black,
    leftIndent=0, spaceAfter=2,
))
styles.add(ParagraphStyle(
    'TOCChapter', parent=styles['Normal'],
    fontSize=11, leading=18, textColor=BRAND_BLUE,
    leftIndent=0, spaceAfter=2, fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    'TableCell', parent=styles['Normal'],
    fontSize=9, leading=12, textColor=black,
))
styles.add(ParagraphStyle(
    'TableHeader', parent=styles['Normal'],
    fontSize=9, leading=12, textColor=black, fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    'HRule', parent=styles['Normal'],
    fontSize=2, spaceAfter=12, spaceBefore=12,
))

# ── Markdown Parser ──────────────────────────────────────────────────
def escape_xml(text):
    """Escape XML special chars for ReportLab Paragraph."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

def format_inline(text):
    """Handle inline markdown: **bold**, *italic*, `code`, [link](url)."""
    # Handle inline code BEFORE escaping (preserve backtick content)
    code_spans = {}
    counter = [0]
    def replace_code(m):
        key = f"__CODE{counter[0]}__"
        code_spans[key] = f'<font face="Courier" size="9" color="#1e293b">{escape_xml(m.group(1))}</font>'
        counter[0] += 1
        return key
    text = re.sub(r'`(.+?)`', replace_code, text)

    # Escape XML for the rest
    text = escape_xml(text)

    # Bold — but strip any code placeholders inside bold to avoid nesting issues
    def bold_replace(m):
        inner = m.group(1)
        return f'<b>{inner}</b>'
    text = re.sub(r'\*\*(.+?)\*\*', bold_replace, text)

    # Italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)

    # Links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<u><font color="#38bdf8">\1</font></u>', text)

    # Restore code spans
    for key, val in code_spans.items():
        text = text.replace(key, val)

    return text

def parse_markdown_to_flowables(filepath):
    """Parse a markdown file into ReportLab flowables."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    flowables = []
    i = 0
    in_code_block = False
    code_lines = []
    is_first_file = filepath.endswith("README.md")

    while i < len(lines):
        line = lines[i].rstrip('\n')

        # Code blocks
        if line.startswith('```'):
            if in_code_block:
                code_text = '\n'.join(code_lines)
                flowables.append(Preformatted(code_text, styles['CodeBlock']))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ('---', '***', '___'):
            flowables.append(Spacer(1, 8))
            i += 1
            continue

        # Headers
        if line.startswith('# '):
            text = line[2:].strip()
            # Remove {#anchor} suffixes
            text = re.sub(r'\s*\{#[\w-]+\}', '', text)
            if is_first_file:
                flowables.append(Spacer(1, 80))
                flowables.append(Paragraph(format_inline(text), styles['BookTitle']))
            else:
                flowables.append(Paragraph(format_inline(text), styles['ChapterTitle']))
            i += 1
            continue

        if line.startswith('## '):
            text = line[3:].strip()
            text = re.sub(r'\s*\{#[\w-]+\}', '', text)
            if is_first_file and i < 5:
                flowables.append(Paragraph(format_inline(text), styles['BookSubtitle']))
            else:
                flowables.append(Paragraph(format_inline(text), styles['SectionHead']))
            i += 1
            continue

        if line.startswith('### '):
            text = line[4:].strip()
            text = re.sub(r'\s*\{#[\w-]+\}', '', text)
            flowables.append(Paragraph(format_inline(text), styles['SubSection']))
            i += 1
            continue

        if line.startswith('#### '):
            text = line[5:].strip()
            flowables.append(Paragraph(format_inline(text), styles['SubSection']))
            i += 1
            continue

        # Table
        if '|' in line and i + 1 < len(lines) and '---' in lines[i + 1]:
            table_lines = []
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                headers = [c.strip() for c in table_lines[0].split('|') if c.strip()]
                rows = []
                for tl in table_lines[2:]:  # skip separator
                    row = [c.strip() for c in tl.split('|') if c.strip()]
                    if row:
                        rows.append(row)

                # Build table
                header_cells = [Paragraph(format_inline(h), styles['TableHeader']) for h in headers]
                data = [header_cells]
                for row in rows:
                    cells = [Paragraph(format_inline(c), styles['TableCell']) for c in row]
                    # Pad short rows
                    while len(cells) < len(headers):
                        cells.append(Paragraph('', styles['TableCell']))
                    data.append(cells[:len(headers)])

                if data:
                    col_width = (WIDTH - 2 * inch) / len(headers)
                    t = Table(data, colWidths=[col_width] * len(headers))
                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#f1f5f9")),
                        ('TEXTCOLOR', (0, 0), (-1, 0), black),
                        ('FONTSIZE', (0, 0), (-1, -1), 9),
                        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('TOPPADDING', (0, 0), (-1, -1), 4),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                        ('LEFTPADDING', (0, 0), (-1, -1), 6),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                    ]))
                    flowables.append(Spacer(1, 6))
                    flowables.append(t)
                    flowables.append(Spacer(1, 8))
            continue

        # Bullet items
        if line.startswith('- ') or line.startswith('* '):
            text = line[2:].strip()
            flowables.append(Paragraph(
                format_inline(text), styles['BulletItem'],
                bulletText='•'
            ))
            i += 1
            continue

        # Numbered list
        m = re.match(r'^(\d+)\.\s+(.+)', line)
        if m:
            num = m.group(1)
            text = m.group(2).strip()
            flowables.append(Paragraph(
                format_inline(text), styles['BulletItem'],
                bulletText=f'{num}.'
            ))
            i += 1
            continue

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Regular paragraph — collect consecutive non-empty lines
        para_lines = [line]
        i += 1
        while i < len(lines):
            next_line = lines[i].rstrip('\n')
            if (not next_line.strip() or next_line.startswith('#') or
                next_line.startswith('```') or next_line.startswith('- ') or
                next_line.startswith('* ') or next_line.startswith('|') or
                next_line.strip() in ('---', '***', '___') or
                re.match(r'^\d+\.\s+', next_line)):
                break
            para_lines.append(next_line)
            i += 1

        text = ' '.join(para_lines)
        flowables.append(Paragraph(format_inline(text), styles['Body']))

    return flowables

# ── Build PDF ────────────────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=1*inch,
        rightMargin=1*inch,
        topMargin=0.8*inch,
        bottomMargin=0.8*inch,
        title="tina4-js: The 1.5KB Reactive Core",
        author="Andre van Zuydam",
        subject="A practical guide to building modern web applications with tina4-js",
    )

    story = []

    # ── Title page (README.md) ───────────────────────────────────────
    logo_path = os.path.join(BOOK_DIR, 'logo.png')
    if os.path.exists(logo_path):
        story.append(Spacer(1, 40))
        logo = Image(logo_path, width=1.5*inch, height=1.5*inch)
        logo.hAlign = 'CENTER'
        story.append(logo)
        story.append(Spacer(1, 20))

    readme_path = os.path.join(BOOK_DIR, CHAPTERS[0])
    story.extend(parse_markdown_to_flowables(readme_path))
    story.append(PageBreak())

    # ── Table of Contents ────────────────────────────────────────────
    story.append(Paragraph("Table of Contents", styles['ChapterTitle']))
    story.append(Spacer(1, 12))

    toc_entries = [
        ("1", "Getting Started", "Your First 5 Minutes"),
        ("2", "Signals", "Reactive State Without the Drama"),
        ("3", "HTML Templates", "DOM Without the Framework Tax"),
        ("4", "Components", "Web Components That Don't Suck"),
        ("5", "Routing", "Navigation Without the Router Library"),
        ("6", "API", "Talking to Your Backend"),
        ("7", "WebSocket", "Real-Time Without the Headache"),
        ("8", "PWA", "Make It Installable"),
        ("9", "Debug Overlay", "See Everything"),
        ("10", "tina4-css", "Optional Styling"),
        ("11", "Backend Integration", "The Full Stack"),
        ("12", "Building a Complete App", "The Admin Dashboard"),
        ("13", "Patterns and Pitfalls", "What We Learned the Hard Way"),
        ("14", "Vibe Coding with AI", "Let AI Write Your tina4-js"),
    ]

    for num, title, subtitle in toc_entries:
        entry_text = f'<b>Chapter {num}:</b> {escape_xml(title)} <font color="#64748b">— {escape_xml(subtitle)}</font>'
        story.append(Paragraph(entry_text, styles['TOCEntry']))

    story.append(PageBreak())

    # ── Chapters ─────────────────────────────────────────────────────
    for chapter_file in CHAPTERS[1:]:
        filepath = os.path.join(BOOK_DIR, chapter_file)
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found, skipping")
            continue

        flowables = parse_markdown_to_flowables(filepath)
        story.extend(flowables)
        story.append(PageBreak())

    # ── Page number footer ───────────────────────────────────────────
    def add_page_number(canvas, doc):
        page_num = canvas.getPageNumber()
        if page_num > 1:  # Skip title page
            canvas.saveState()
            canvas.setFont('Helvetica', 8)
            canvas.setFillColor(MUTED)
            canvas.drawCentredString(WIDTH / 2, 0.4 * inch, f"— {page_num} —")
            canvas.drawString(1 * inch, 0.4 * inch, "tina4-js")
            canvas.restoreState()

    # Build
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF written to: {OUTPUT}")
    print(f"Size: {os.path.getsize(OUTPUT) / 1024:.0f} KB")

if __name__ == '__main__':
    build_pdf()
