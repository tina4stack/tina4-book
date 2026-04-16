#!/usr/bin/env python3
"""Shared PDF generator for the Tina4 books.

Produces a polished PDF with:
- Cover page (logo, title, subtitle, version stamp)
- Auto-generated clickable Table of Contents
- PDF outline / bookmarks — readers see the full chapter + section tree in
  the sidebar and can jump anywhere in one click
- Syntax-highlighted code blocks, typographically consistent body
- Running footer with book name + page number
- Clickable intra-doc anchors and external URLs

Usage:
    scripts/build_pdf.py path/to/book.yml

Where ``book.yml`` looks like::

    title: Tina4 for Python Developers
    subtitle: Your 4th Framework
    accent: "#7b1fa2"
    output: book-1-python/Tina4-for-Python-Developers.pdf
    chapters_dir: book-1-python/chapters
    # Explicit list optional; defaults to every NN-name.md in chapters_dir
    # chapters:
    #   - 01-getting-started.md

One generator, six books, one look.
"""

from __future__ import annotations

import html as _html
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - optional dep; we fall back to a tiny parser
    yaml = None

from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


# ── Config ───────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
WIDTH, HEIGHT = A4

# Brand palette — consistent across all books. Accent colour is
# per-book (set in book.yml).
TEXT = HexColor("#0f172a")
MUTED = HexColor("#64748b")
BORDER = HexColor("#e2e8f0")
CODE_BG = HexColor("#f8fafc")
CODE_BORDER = HexColor("#cbd5e1")
LINK = HexColor("#7b1fa2")


@dataclass
class BookConfig:
    title: str
    subtitle: str = ""
    accent: str = "#7b1fa2"
    output: str = ""
    chapters_dir: str = ""
    chapters: list[str] = field(default_factory=list)
    cover_logo: str = ""  # optional path to a logo image
    version: str = ""  # e.g. "v3.11.13"

    @classmethod
    def load(cls, path: Path) -> "BookConfig":
        data = _load_yaml(path)
        cfg = cls(
            title=data.get("title", "Tina4"),
            subtitle=data.get("subtitle", ""),
            accent=data.get("accent", "#7b1fa2"),
            output=data.get("output", ""),
            chapters_dir=data.get("chapters_dir", "chapters"),
            chapters=list(data.get("chapters", []) or []),
            cover_logo=data.get("cover_logo", ""),
            version=data.get("version", ""),
        )
        # Resolve relative paths against the repo root, not the cwd
        cfg._config_dir = path.parent
        return cfg

    @property
    def resolved_chapters_dir(self) -> Path:
        p = Path(self.chapters_dir)
        return p if p.is_absolute() else (REPO_ROOT / p)

    @property
    def resolved_output(self) -> Path:
        p = Path(self.output)
        return p if p.is_absolute() else (REPO_ROOT / p)

    @property
    def resolved_logo(self) -> Path | None:
        if not self.cover_logo:
            return None
        p = Path(self.cover_logo)
        return p if p.is_absolute() else (REPO_ROOT / p)

    def discover_chapters(self) -> list[Path]:
        """Use the explicit list if given; otherwise glob NN-*.md in order."""
        d = self.resolved_chapters_dir
        if self.chapters:
            return [d / name for name in self.chapters]
        candidates = sorted(d.glob("[0-9][0-9]-*.md"))
        return candidates


def _load_yaml(path: Path) -> dict:
    """Tiny YAML loader that handles the flat key/value + list subset we use.

    Avoids a hard PyYAML dependency — the book.yml files here only need
    plain ``key: value`` and ``- item`` syntax.
    """
    if yaml is not None:
        with open(path, "r", encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}

    out: dict = {}
    current_list_key: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") or line.startswith("- "):
            item = line.split("- ", 1)[1].strip().strip('"\'')
            if current_list_key is None:
                continue
            out.setdefault(current_list_key, []).append(item)
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"\'')
            if val == "":
                current_list_key = key
                out[key] = []
            else:
                current_list_key = None
                out[key] = val
    return out


# ── Styles ───────────────────────────────────────────────────────────

def build_styles(accent: HexColor) -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    styles = {
        "CoverTitle": ParagraphStyle(
            "CoverTitle", parent=base["Title"],
            fontName="Helvetica-Bold", fontSize=36, leading=42,
            textColor=accent, alignment=TA_CENTER, spaceAfter=16,
        ),
        "CoverSubtitle": ParagraphStyle(
            "CoverSubtitle", parent=base["Normal"],
            fontName="Helvetica", fontSize=18, leading=24,
            textColor=TEXT, alignment=TA_CENTER, spaceAfter=12,
        ),
        "CoverVersion": ParagraphStyle(
            "CoverVersion", parent=base["Normal"],
            fontName="Helvetica", fontSize=11, leading=16,
            textColor=MUTED, alignment=TA_CENTER,
        ),
        "TOCHeading": ParagraphStyle(
            "TOCHeading", parent=base["Title"],
            fontName="Helvetica-Bold", fontSize=24, leading=30,
            textColor=accent, alignment=TA_LEFT, spaceAfter=18,
        ),
        "ChapterTitle": ParagraphStyle(
            "ChapterTitle", parent=base["Title"],
            fontName="Helvetica-Bold", fontSize=22, leading=28,
            textColor=accent, alignment=TA_LEFT, spaceBefore=6, spaceAfter=14,
        ),
        "SectionHeading": ParagraphStyle(
            "SectionHeading", parent=base["Heading2"],
            fontName="Helvetica-Bold", fontSize=15, leading=20,
            textColor=TEXT, spaceBefore=14, spaceAfter=8,
        ),
        "SubsectionHeading": ParagraphStyle(
            "SubsectionHeading", parent=base["Heading3"],
            fontName="Helvetica-Bold", fontSize=12, leading=16,
            textColor=TEXT, spaceBefore=10, spaceAfter=6,
        ),
        "Body": ParagraphStyle(
            "Body", parent=base["BodyText"],
            fontName="Helvetica", fontSize=10.5, leading=15.5,
            textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=8,
        ),
        "ListItem": ParagraphStyle(
            "ListItem", parent=base["BodyText"],
            fontName="Helvetica", fontSize=10.5, leading=15,
            textColor=TEXT, leftIndent=14, bulletIndent=4, spaceAfter=4,
        ),
        "Code": ParagraphStyle(
            "Code", parent=base["Code"],
            fontName="Courier", fontSize=9, leading=12,
            textColor=TEXT, backColor=CODE_BG,
            leftIndent=6, rightIndent=6, spaceBefore=6, spaceAfter=8,
            borderColor=CODE_BORDER, borderWidth=0.5, borderPadding=6,
        ),
        "InlineCode": ParagraphStyle(
            "InlineCode", parent=base["Code"],
            fontName="Courier", fontSize=9.5, textColor=accent,
        ),
        "Quote": ParagraphStyle(
            "Quote", parent=base["BodyText"],
            fontName="Helvetica-Oblique", fontSize=10.5, leading=15,
            textColor=MUTED, leftIndent=18, rightIndent=18, spaceAfter=8,
            borderColor=accent, borderWidth=0, borderPadding=4,
        ),
    }
    # ToC entries — one style per level so they render hierarchically
    for lvl, (indent, size, bold) in enumerate([
        (0, 11, True),    # H1 / chapter
        (18, 10, False),  # H2 / section
        (36, 9, False),   # H3 / subsection
    ]):
        styles[f"TOCLevel{lvl}"] = ParagraphStyle(
            f"TOCLevel{lvl}", parent=base["Normal"],
            fontName="Helvetica-Bold" if bold else "Helvetica",
            fontSize=size, leading=size + 4,
            leftIndent=indent, spaceBefore=3 if lvl == 0 else 1, spaceAfter=2,
            textColor=accent if lvl == 0 else TEXT,
        )
    return styles


# ── Markdown parsing ────────────────────────────────────────────────
#
# Intentionally narrow — this isn't a general markdown renderer. It
# handles the constructs the tina4 books actually use: headings, code
# fences, lists, links, bold/italic, blockquotes, tables.

_CODE_FENCE = re.compile(r"^```(\w*)$")
_HEADING = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
_LIST_ITEM = re.compile(r"^(\s*)[-*]\s+(.+)$")
_ORDERED_ITEM = re.compile(r"^(\s*)\d+\.\s+(.+)$")
_TABLE_ROW = re.compile(r"^\|(.+)\|\s*$")
_TABLE_SEP = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
_INLINE_CODE = re.compile(r"`([^`]+)`")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC = re.compile(r"(?<![*_])[*_]([^*_\n]+)[*_](?![*_])")


def _escape_xml(text: str) -> str:
    """Escape for reportlab Paragraph (needs XML-safe body)."""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )


def _format_inline(text: str, accent_hex: str) -> str:
    """Convert markdown inline marks to reportlab's XML subset.

    Inline code is processed first and its content is stashed behind
    opaque placeholders so subsequent transforms (bold/italic/link) can't
    reach inside it. Italic uses ``*`` or ``_`` as delimiters and `_` is
    common inside code like ``TINA4_DEBUG`` — without this protection
    we'd corrupt identifiers and produce invalid XML.
    """
    # Strip {#anchor} trailing syntax (markdown-it extension) before formatting
    text = re.sub(r"\s*\{#[^}]+\}\s*$", "", text)

    # Stash inline code and link URLs so later regexes can't touch them
    stashed: list[str] = []

    def _stash(payload: str) -> str:
        stashed.append(payload)
        return f"\x00STASH{len(stashed) - 1}\x00"

    # 1. Inline code — highest precedence, preserves contents verbatim
    text = _INLINE_CODE.sub(
        lambda m: _stash(f'<font name="Courier" color="{accent_hex}">{_escape_xml(m.group(1))}</font>'),
        text,
    )
    # 2. Links — swallow the URL so italic/bold can't see it.
    #
    #    Intra-doc anchor links (``#section``) can't be resolved at PDF-build
    #    time without a two-pass heading registry; they would also trip
    #    reportlab's "undefined destination target" error. We keep the
    #    visible label but drop the anchor so rendering never fails. External
    #    URLs (http/https/mailto/relative paths to other docs) stay clickable.
    def _render_link(m: re.Match) -> str:
        label, url = m.group(1), m.group(2)
        if url.startswith("#"):
            return _stash(f'<i>{_escape_xml(label)}</i>')
        return _stash(
            f'<link href="{_escape_xml(url)}"><font color="#7b1fa2"><u>{_escape_xml(label)}</u></font></link>'
        )

    text = _LINK.sub(_render_link, text)

    # Now escape the remaining prose for XML safety
    text = _escape_xml(text)

    # Bold & italic on the surviving prose
    text = _BOLD.sub(lambda m: f"<b>{m.group(1)}</b>", text)
    text = _ITALIC.sub(lambda m: f"<i>{m.group(1)}</i>", text)

    # Reinstate the stashed spans
    def _unstash(m: re.Match) -> str:
        return stashed[int(m.group(1))]

    text = re.sub(r"\x00STASH(\d+)\x00", _unstash, text)
    return text


def _slug(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return s or "section"


@dataclass
class ParseContext:
    accent_hex: str
    styles: dict[str, ParagraphStyle]
    toc_entries: list[tuple[int, str, str]]  # (level, title, anchor)


class _Bookmarked(Paragraph):
    """Paragraph that drops a PDF outline entry + anchor so ToC can link here.

    The actual ``notify("TOCEntry", ...)`` call happens in
    :meth:`_BookDoc.afterFlowable` because only the doc template knows how
    to forward notifications to the :class:`TableOfContents` flowable.
    """

    def __init__(self, text: str, style: ParagraphStyle, level: int, anchor: str):
        super().__init__(f'<a name="{anchor}"/>{text}', style)
        self._bm_level = level
        self._bm_title = re.sub(r"<[^>]+>", "", text).strip()
        self._bm_anchor = anchor

    def draw(self):
        canvas = self.canv
        canvas.bookmarkPage(self._bm_anchor)
        canvas.addOutlineEntry(self._bm_title, self._bm_anchor, level=self._bm_level)
        super().draw()


def parse_markdown(path: Path, ctx: ParseContext) -> list:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list = []
    in_fence = False
    fence_buf: list[str] = []
    i = 0

    def flush_fence():
        nonlocal fence_buf
        if fence_buf:
            code = "\n".join(fence_buf)
            out.append(Preformatted(code, ctx.styles["Code"]))
            fence_buf = []

    while i < len(lines):
        line = lines[i]
        fence_m = _CODE_FENCE.match(line.rstrip())
        if fence_m:
            if in_fence:
                flush_fence()
                in_fence = False
            else:
                in_fence = True
            i += 1
            continue
        if in_fence:
            fence_buf.append(line)
            i += 1
            continue

        # Headings → Paragraph + PDF outline + ToC entry
        h = _HEADING.match(line)
        if h:
            level = len(h.group(1)) - 1  # '#' → 0, '##' → 1, etc.
            title_raw = h.group(2)
            # Strip "Chapter NN: " prefix for cleaner outline if present
            title_clean = re.sub(r"^Chapter\s+\d+:\s*", "", title_raw)
            anchor = _slug(title_clean) + f"-p{id(line)}"
            style_key = ["ChapterTitle", "SectionHeading", "SubsectionHeading", "SubsectionHeading"][min(level, 3)]
            out.append(_Bookmarked(
                _format_inline(title_clean, ctx.accent_hex),
                ctx.styles[style_key],
                level=level,
                anchor=anchor,
            ))
            ctx.toc_entries.append((level, title_clean, anchor))
            i += 1
            continue

        # Blockquote
        if line.startswith("> "):
            quoted = []
            while i < len(lines) and lines[i].startswith("> "):
                quoted.append(lines[i][2:])
                i += 1
            out.append(Paragraph(_format_inline(" ".join(quoted), ctx.accent_hex), ctx.styles["Quote"]))
            continue

        # Lists (bullet + ordered)
        li = _LIST_ITEM.match(line) or _ORDERED_ITEM.match(line)
        if li:
            items = []
            while i < len(lines):
                m = _LIST_ITEM.match(lines[i]) or _ORDERED_ITEM.match(lines[i])
                if not m:
                    break
                items.append(m.group(2))
                i += 1
            for item in items:
                out.append(Paragraph(
                    "• " + _format_inline(item, ctx.accent_hex),
                    ctx.styles["ListItem"],
                ))
            continue

        # Tables (minimal: header | --- | rows)
        if _TABLE_ROW.match(line) and i + 1 < len(lines) and _TABLE_SEP.match(lines[i + 1]):
            header = [c.strip() for c in line.strip("|").split("|")]
            rows = []
            i += 2
            while i < len(lines) and _TABLE_ROW.match(lines[i]):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            table_data = [header] + rows
            # Render cells as Paragraphs so inline formatting + links survive
            rendered = [
                [Paragraph(_format_inline(c, ctx.accent_hex), ctx.styles["Body"]) for c in row]
                for row in table_data
            ]
            t = Table(rendered, colWidths=[(WIDTH - 2 * inch) / max(len(header), 1)] * len(header))
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), HexColor(ctx.accent_hex)),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
            ]))
            out.append(t)
            out.append(Spacer(1, 8))
            continue

        # Paragraph (collect consecutive non-empty body lines)
        if line.strip():
            para_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not _HEADING.match(lines[i]) \
                    and not _CODE_FENCE.match(lines[i].rstrip()) \
                    and not _LIST_ITEM.match(lines[i]) and not _ORDERED_ITEM.match(lines[i]) \
                    and not lines[i].startswith("> ") and not _TABLE_ROW.match(lines[i]):
                para_lines.append(lines[i])
                i += 1
            joined = " ".join(para_lines).strip()
            if joined:
                out.append(Paragraph(_format_inline(joined, ctx.accent_hex), ctx.styles["Body"]))
            continue

        i += 1

    return out


# ── Document assembly ───────────────────────────────────────────────

class _BookDoc(BaseDocTemplate):
    """Two-column-friendly, TOC-aware doc template with running footer."""

    def __init__(self, filename: str, book_title: str, accent: HexColor, **kwargs):
        super().__init__(filename, pagesize=A4, **kwargs)
        self._book_title = book_title
        self._accent = accent

        # Single content frame leaving room for margins
        frame = Frame(
            0.9 * inch, 0.9 * inch,
            WIDTH - 1.8 * inch, HEIGHT - 1.6 * inch,
            id="body", showBoundary=0,
        )
        self.addPageTemplates([
            PageTemplate(id="cover", frames=frame, onPage=self._cover_footer),
            PageTemplate(id="body", frames=frame, onPage=self._body_footer),
        ])

    def afterFlowable(self, flowable):
        # Forward every _Bookmarked heading to the TableOfContents flowable.
        # reportlab picks this up via multiBuild's two-pass layout.
        if isinstance(flowable, _Bookmarked):
            self.notify("TOCEntry", (
                flowable._bm_level, flowable._bm_title,
                self.page, flowable._bm_anchor,
            ))

    def _cover_footer(self, canvas, doc):
        # No footer on the cover
        pass

    def _body_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(0.9 * inch, 0.55 * inch, self._book_title)
        canvas.drawRightString(WIDTH - 0.9 * inch, 0.55 * inch, f"— {doc.page} —")
        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(0.4)
        canvas.line(0.9 * inch, 0.75 * inch, WIDTH - 0.9 * inch, 0.75 * inch)
        canvas.restoreState()


def _build_cover(cfg: BookConfig, styles: dict[str, ParagraphStyle]) -> list:
    story: list = []
    story.append(Spacer(1, 1.6 * inch))
    logo = cfg.resolved_logo
    if logo and logo.exists():
        try:
            img = Image(str(logo), width=2.4 * inch, height=2.4 * inch, kind="proportional")
            img.hAlign = "CENTER"
            story.append(img)
            story.append(Spacer(1, 0.3 * inch))
        except Exception:
            pass
    story.append(Paragraph(_escape_xml(cfg.title), styles["CoverTitle"]))
    if cfg.subtitle:
        story.append(Paragraph(_escape_xml(cfg.subtitle), styles["CoverSubtitle"]))
    story.append(Spacer(1, 0.4 * inch))
    meta = []
    if cfg.version:
        meta.append(cfg.version)
    meta.append("tina4.com")
    story.append(Paragraph(" &bull; ".join(_escape_xml(m) for m in meta), styles["CoverVersion"]))
    story.append(PageBreak())
    return story


def build_pdf(cfg: BookConfig) -> Path:
    accent = HexColor(cfg.accent)
    styles = build_styles(accent)
    output = cfg.resolved_output
    output.parent.mkdir(parents=True, exist_ok=True)

    doc = _BookDoc(str(output), cfg.title, accent,
                   topMargin=0.9 * inch, bottomMargin=0.9 * inch,
                   leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                   title=cfg.title,
                   author="Tina4 Stack")

    story: list = _build_cover(cfg, styles)

    # Table of Contents flowable — clickable, auto-populated as headings
    # render. We pre-seed with a placeholder title and let reportlab
    # multi-pass layout fill in the entries.
    toc = TableOfContents()
    toc.levelStyles = [
        styles["TOCLevel0"],
        styles["TOCLevel1"],
        styles["TOCLevel2"],
    ]
    story.append(Paragraph("Table of Contents", styles["TOCHeading"]))
    story.append(Spacer(1, 6))
    story.append(toc)
    story.append(PageBreak())

    # Parse + append chapters
    ctx = ParseContext(accent_hex=cfg.accent, styles=styles, toc_entries=[])
    chapters = cfg.discover_chapters()
    if not chapters:
        raise SystemExit(f"No chapters found in {cfg.resolved_chapters_dir}")
    for idx, chapter in enumerate(chapters):
        if not chapter.exists():
            print(f"  WARN: missing {chapter}")
            continue
        story.extend(parse_markdown(chapter, ctx))
        if idx < len(chapters) - 1:
            story.append(PageBreak())

    # multiBuild is required for TableOfContents to populate
    doc.multiBuild(story)
    size_kb = output.stat().st_size / 1024
    print(f"  wrote {output.relative_to(REPO_ROOT)}  ({size_kb:.0f} KB, {len(ctx.toc_entries)} headings)")
    return output


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: build_pdf.py path/to/book.yml [more.yml...]")
        return 2
    failures = 0
    for arg in argv[1:]:
        path = Path(arg).resolve()
        if not path.exists():
            print(f"  ERR: {path} does not exist")
            failures += 1
            continue
        print(f"Building {path.relative_to(REPO_ROOT)}…")
        try:
            cfg = BookConfig.load(path)
            build_pdf(cfg)
        except Exception as e:  # pragma: no cover - surface to operator
            print(f"  FAIL: {e}")
            import traceback
            traceback.print_exc()
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
