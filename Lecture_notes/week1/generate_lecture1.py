# -*- coding: utf-8 -*-
"""Generates Lecture 1 ("Kirish. Dasturlash tillari. .NET Core platformasi...")
as a .pptx deck for Dasturlash 1,2 (DAS1110), O'zMU Jizzax filiali."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn
import copy

# ---------------------------------------------------------------- palette --
INK = RGBColor(0x1E, 0x1B, 0x4B)          # deep indigo (headers, title bg)
PURPLE = RGBColor(0x68, 0x3A, 0xB7)       # accent purple
CYAN = RGBColor(0x00, 0xBC, 0xD4)         # accent cyan
BG_LIGHT = RGBColor(0xF7, 0xF7, 0xFC)     # content slide background
CARD = RGBColor(0xFF, 0xFF, 0xFF)
TEXT_DARK = RGBColor(0x23, 0x23, 0x2B)
TEXT_MUTE = RGBColor(0x60, 0x60, 0x70)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
GREEN_BG = RGBColor(0xE3, 0xF2, 0xE1)
RED = RGBColor(0xC6, 0x28, 0x28)
AMBER = RGBColor(0xF5, 0x7C, 0x00)
CODE_BG = RGBColor(0x1E, 0x1E, 0x1E)
CODE_TEXT = RGBColor(0xD4, 0xD4, 0xD4)
CODE_KEYWORD = RGBColor(0x56, 0x9C, 0xD6)
CODE_TYPE = RGBColor(0x4E, 0xC9, 0xB0)
CODE_STRING = RGBColor(0xCE, 0x91, 0x78)
CODE_COMMENT = RGBColor(0x6A, 0x99, 0x55)
CODE_METHOD = RGBColor(0xDC, 0xDC, 0xAA)
OPTION_BG = RGBColor(0xEE, 0xEE, 0xF6)
FONT_BODY = "Segoe UI"
FONT_CODE = "Consolas"

SW, SH = Inches(13.333), Inches(7.5)


def new_prs():
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    return prs


def blank_slide(prs, bg=BG_LIGHT):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    rect.fill.solid()
    rect.fill.fore_color.rgb = bg
    rect.line.fill.background()
    rect.shadow.inherit = False
    _send_to_back(slide, rect)
    return slide


def _send_to_back(slide, shape):
    spTree = slide.shapes._spTree
    spTree.remove(shape._element)
    spTree.insert(2, shape._element)


def _no_shadow(shape):
    shape.shadow.inherit = False


def add_textbox(slide, l, t, w, h, text, size=18, bold=False, italic=False,
                 color=TEXT_DARK, align=PP_ALIGN.LEFT, font=FONT_BODY,
                 anchor=MSO_ANCHOR.TOP, line_spacing=1.0):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    r.font.name = font
    return box


def add_bullets(slide, l, t, w, h, items, size=17, color=TEXT_DARK,
                 font=FONT_BODY, space_after=10, line_spacing=1.05,
                 marker="•  "):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            text, level = item
        else:
            text, level = item, 0
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(space_after)
        p.line_spacing = line_spacing
        indent = "     " * level
        pre = "" if level > 0 else marker
        pre2 = "–  " if level > 0 else marker
        r = p.add_run()
        r.text = f"{indent}{pre2 if level>0 else marker}{text}"
        r.font.size = Pt(size - (2 if level else 0))
        r.font.color.rgb = color
        r.font.name = font
    return box


def add_header(slide, kicker, title, dark=False):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, Inches(1.15))
    bar.fill.solid()
    bar.fill.fore_color.rgb = INK
    bar.line.fill.background()
    _no_shadow(bar)
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.15), SW, Pt(4))
    accent.fill.solid()
    accent.fill.fore_color.rgb = CYAN
    accent.line.fill.background()
    _no_shadow(accent)
    add_textbox(slide, Inches(0.55), Inches(0.12), Inches(11), Inches(0.35),
                kicker.upper(), size=13, bold=True, color=CYAN, font=FONT_BODY)
    add_textbox(slide, Inches(0.55), Inches(0.46), Inches(12.2), Inches(0.65),
                title, size=26, bold=True, color=WHITE, font=FONT_BODY)


def add_page_number(slide, n):
    add_textbox(slide, SW - Inches(1.0), SH - Inches(0.45), Inches(0.7), Inches(0.3),
                str(n), size=11, color=TEXT_MUTE, align=PP_ALIGN.RIGHT)


def add_footer(slide, n, label="Dasturlash 1 | 1-Ma'ruza"):
    add_textbox(slide, Inches(0.55), SH - Inches(0.45), Inches(6), Inches(0.3),
                label, size=11, color=TEXT_MUTE)
    add_page_number(slide, n)


# ------------------------------------------------------------- slide kinds --

def add_title_slide(prs):
    slide = blank_slide(prs, bg=INK)
    band = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(5.55), SW, Pt(5))
    band.fill.solid(); band.fill.fore_color.rgb = CYAN; band.line.fill.background(); _no_shadow(band)
    for i, (x, y, s, col) in enumerate([
        (0.6, 0.6, 1.6, PURPLE), (11.6, 5.9, 1.0, CYAN), (0.4, 6.3, 0.8, PURPLE)
    ]):
        c = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(s), Inches(s))
        c.fill.solid(); c.fill.fore_color.rgb = col; c.line.fill.background(); _no_shadow(c)
        c.fill.fore_color.brightness = 0
        c.fill.transparency = 0
    add_textbox(slide, Inches(0.9), Inches(1.3), Inches(11.5), Inches(0.5),
                "DASTURLASH 1  •  DAS1110", size=18, bold=True, color=CYAN)
    add_textbox(slide, Inches(0.9), Inches(1.9), Inches(11.5), Inches(1.9),
                "1-Ma'ruza: Kirish", size=48, bold=True, color=WHITE)
    add_textbox(slide, Inches(0.9), Inches(2.9), Inches(11.5), Inches(2.0),
                "Dasturlash tillari. .NET Core platformasi. Visual Studio muhiti.\n"
                "Konsol rejimida ishlash. C# da birinchi dastur.",
                size=22, color=RGBColor(0xD8, 0xD8, 0xF0), line_spacing=1.2)
    add_textbox(slide, Inches(0.9), Inches(6.05), Inches(8), Inches(0.4),
                "O'zbekiston Milliy universiteti Jizzax filiali  |  Amaliy matematika fakulteti",
                size=14, color=RGBColor(0xB8, 0xB8, 0xE0))
    add_textbox(slide, Inches(0.9), Inches(6.45), Inches(8), Inches(0.4),
                "O'qituvchi: Toshpolatov Muxiddin, PhD, dotsent  |  2025/2026-o'quv yili",
                size=14, color=RGBColor(0xB8, 0xB8, 0xE0))
    return slide


def add_section_slide(prs, n, roman, title, subtitle, page):
    slide = blank_slide(prs, bg=PURPLE)
    grad = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    grad.fill.solid(); grad.fill.fore_color.rgb = PURPLE; grad.line.fill.background(); _no_shadow(grad)
    _send_to_back(slide, grad)
    tag = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.9), Inches(2.3), Inches(2.0), Inches(2.0))
    tag.fill.solid(); tag.fill.fore_color.rgb = INK; tag.line.color.rgb = CYAN; tag.line.width = Pt(2.5)
    _no_shadow(tag)
    tf = tag.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = roman; r.font.size = Pt(44); r.font.bold = True; r.font.color.rgb = WHITE
    add_textbox(slide, Inches(3.3), Inches(2.55), Inches(9.3), Inches(0.4),
                f"{n}-BO'LIM", size=16, bold=True, color=RGBColor(0xE8, 0xDC, 0xFF))
    add_textbox(slide, Inches(3.3), Inches(3.0), Inches(9.3), Inches(1.3),
                title, size=36, bold=True, color=WHITE)
    add_textbox(slide, Inches(3.3), Inches(4.15), Inches(9.3), Inches(0.9),
                subtitle, size=17, color=RGBColor(0xE8, 0xDC, 0xFF), line_spacing=1.2)
    add_page_number(slide, page)
    return slide


def add_bullet_slide(prs, kicker, title, bullets, page, note=None, size=18):
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    add_bullets(slide, Inches(0.7), Inches(1.55), Inches(11.9), Inches(4.9), bullets, size=size)
    if note:
        _add_note_box(slide, note)
    add_footer(slide, page)
    return slide


def _add_note_box(slide, text, top=None):
    import math
    full_text = "💡 " + text
    lines = max(1, math.ceil(len(full_text) / 100))
    height = Inches(0.30 + lines * 0.34)
    footer_safe_top = SH - Inches(0.65) - height
    if top is None:
        top = footer_safe_top
    else:
        top = min(top, footer_safe_top)
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), top, Inches(11.9), height)
    box.fill.solid(); box.fill.fore_color.rgb = RGBColor(0xFF, 0xF3, 0xD6)
    box.line.color.rgb = AMBER; box.line.width = Pt(1)
    box.adjustments[0] = 0.15
    _no_shadow(box)
    tf = box.text_frame; tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.2); tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.04); tf.margin_bottom = Inches(0.04)
    p = tf.paragraphs[0]
    p.line_spacing = 1.1
    r = p.add_run(); r.text = full_text
    r.font.size = Pt(14); r.font.italic = True; r.font.color.rgb = RGBColor(0x7A, 0x54, 0x00)
    r.font.name = FONT_BODY


def add_two_col_slide(prs, kicker, title, left_title, left_items, right_title,
                       right_items, page, left_color=PURPLE, right_color=CYAN):
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    colw = Inches(5.7)
    for x, ctitle, items, color in [
        (Inches(0.7), left_title, left_items, left_color),
        (Inches(6.9), right_title, right_items, right_color),
    ]:
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.55), colw, Inches(5.35))
        card.fill.solid(); card.fill.fore_color.rgb = CARD
        card.line.color.rgb = RGBColor(0xE0, 0xE0, 0xEC); card.line.width = Pt(1)
        _no_shadow(card)
        head = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.55), colw, Inches(0.6))
        head.fill.solid(); head.fill.fore_color.rgb = color; head.line.fill.background(); _no_shadow(head)
        tf = head.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = ctitle; r.font.size = Pt(17); r.font.bold = True; r.font.color.rgb = WHITE
        add_bullets(slide, x + Inches(0.3), Inches(2.35), colw - Inches(0.6), Inches(4.4),
                    items, size=15, space_after=8)
    add_footer(slide, page)
    return slide


def add_table_slide(prs, kicker, title, headers, rows, page, col_widths=None, note=None):
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    left, top = Inches(0.7), Inches(1.65)
    width, height = Inches(11.9), Inches(0.55 * (len(rows) + 1))
    ncols = len(headers)
    gtable = slide.shapes.add_table(len(rows) + 1, ncols, left, top, width, height).table
    if col_widths:
        for i, w in enumerate(col_widths):
            gtable.columns[i].width = Inches(w)
    for j, h in enumerate(headers):
        cell = gtable.cell(0, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = INK
        cell.text = ""
        tf = cell.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = h
        r.font.bold = True; r.font.size = Pt(15); r.font.color.rgb = WHITE; r.font.name = FONT_BODY
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = gtable.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD if i % 2 == 0 else RGBColor(0xF0, 0xEF, 0xFA)
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if j > 0 else PP_ALIGN.LEFT
            r = p.add_run(); r.text = val
            r.font.size = Pt(14); r.font.color.rgb = TEXT_DARK; r.font.name = FONT_BODY
            r.font.bold = (j == 0)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = Inches(0.12)
    if note:
        _add_note_box(slide, note, top=top + height + Inches(0.25))
    add_footer(slide, page)
    return slide


def add_code_slide(prs, kicker, title, code_lines, output_lines, page, caption=None):
    """code_lines: list of list-of-(text,color) run tuples, one list per line.
    Box heights are derived from actual line counts (not fixed guesses) so
    longer snippets can never overflow/clip past their rounded-rect border."""
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    n = len(code_lines)
    code_font = 16 if n <= 9 else (14 if n <= 13 else 12)
    line_spacing = 1.22
    top = Inches(1.55)
    code_h = Inches(0.55 + n * code_font * line_spacing / 72.0 + 0.35)
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), top, Inches(11.9), code_h)
    box.fill.solid(); box.fill.fore_color.rgb = CODE_BG; box.line.color.rgb = RGBColor(0x3C, 0x3C, 0x3C)
    box.adjustments[0] = 0.04
    _no_shadow(box)
    dots_y = top + Inches(0.15)
    for i, c in enumerate([RED, AMBER, GREEN]):
        d = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.9 + i * 0.28), dots_y, Inches(0.16), Inches(0.16))
        d.fill.solid(); d.fill.fore_color.rgb = c; d.line.fill.background(); _no_shadow(d)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3); tf.margin_top = Inches(0.45); tf.margin_right = Inches(0.2)
    for i, line_runs in enumerate(code_lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = line_spacing
        for text, color in line_runs:
            r = p.add_run(); r.text = text if text else " "
            r.font.name = FONT_CODE; r.font.size = Pt(code_font); r.font.color.rgb = color
    cursor_y = top + code_h + Inches(0.15)
    if output_lines:
        out_h = Inches(0.42 + len(output_lines) * 0.26)
        obox = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), cursor_y, Inches(11.9), out_h)
        obox.fill.solid(); obox.fill.fore_color.rgb = RGBColor(0xF0, 0xF0, 0xF0)
        obox.line.color.rgb = RGBColor(0xC0, 0xC0, 0xC0); _no_shadow(obox)
        otf = obox.text_frame; otf.word_wrap = True
        otf.margin_left = Inches(0.25); otf.margin_top = Inches(0.08)
        p0 = otf.paragraphs[0]
        r0 = p0.add_run(); r0.text = "► NATIJA (Console chiqishi):"
        r0.font.bold = True; r0.font.size = Pt(12); r0.font.color.rgb = TEXT_MUTE; r0.font.name = FONT_BODY
        for line in output_lines:
            p = otf.add_paragraph()
            r = p.add_run(); r.text = line
            r.font.name = FONT_CODE; r.font.size = Pt(15); r.font.color.rgb = RGBColor(0x1B, 0x5E, 0x20)
        cursor_y = cursor_y + out_h + Inches(0.12)
    if caption:
        add_textbox(slide, Inches(0.7), cursor_y, Inches(11.9), Inches(0.35),
                    caption, size=13, italic=True, color=TEXT_MUTE)
    add_footer(slide, page)
    return slide


def add_pipeline_slide(prs, kicker, title, steps, page, note=None):
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    n = len(steps)
    box_w = Inches(1.78)
    gap = Inches(0.28)
    total_w = box_w * n + gap * (n - 1)
    start_x = (SW - total_w) / 2
    y = Inches(2.9)
    box_h = Inches(1.5)
    colors = [PURPLE, INK, CYAN, PURPLE, INK, CYAN]
    for i, (label, sub) in enumerate(steps):
        x = start_x + i * (box_w + gap)
        shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, box_w, box_h)
        shp.fill.solid(); shp.fill.fore_color.rgb = colors[i % len(colors)]
        shp.line.fill.background(); _no_shadow(shp)
        tf = shp.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = Inches(0.08)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = label; r.font.bold = True; r.font.size = Pt(14); r.font.color.rgb = WHITE
        if sub:
            p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER
            r2 = p2.add_run(); r2.text = sub; r2.font.size = Pt(10.5); r2.font.color.rgb = RGBColor(0xE0, 0xE0, 0xF5)
        if i < n - 1:
            ax = x + box_w
            arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, ax, y + box_h / 2 - Inches(0.13), gap, Inches(0.26))
            arrow.fill.solid(); arrow.fill.fore_color.rgb = TEXT_MUTE; arrow.line.fill.background(); _no_shadow(arrow)
    add_textbox(slide, Inches(0.7), Inches(1.65), Inches(11.9), Inches(1.0),
                "Manba koddan mashina kodigacha bo'lgan yo'l:", size=16, color=TEXT_MUTE, italic=True)
    if note:
        _add_note_box(slide, note, top=Inches(5.0))
    add_footer(slide, page)
    return slide


def add_grid_slide(prs, kicker, title, items, page, cols=3):
    """items: list of (emoji_or_short, name, desc)"""
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    rows = -(-len(items) // cols)
    margin = Inches(0.7)
    gap = Inches(0.25)
    cell_w = (SW - 2 * margin - gap * (cols - 1)) / cols
    cell_h = Inches(1.55)
    top0 = Inches(1.6)
    for i, (icon, name, desc) in enumerate(items):
        r, c = divmod(i, cols)
        x = margin + c * (cell_w + gap)
        y = top0 + r * (cell_h + gap)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cell_w, cell_h)
        card.fill.solid(); card.fill.fore_color.rgb = CARD
        card.line.color.rgb = RGBColor(0xE0, 0xE0, 0xEC); _no_shadow(card)
        tf = card.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.15); tf.margin_right = Inches(0.1)
        tf.margin_top = Inches(0.08); tf.margin_bottom = Inches(0.08)
        p = tf.paragraphs[0]
        r1 = p.add_run(); r1.text = f"{icon}  {name}"
        r1.font.bold = True; r1.font.size = Pt(15); r1.font.color.rgb = PURPLE; r1.font.name = FONT_BODY
        p2 = tf.add_paragraph()
        r2 = p2.add_run(); r2.text = desc
        r2.font.size = Pt(12); r2.font.color.rgb = TEXT_DARK; r2.font.name = FONT_BODY
    add_footer(slide, page)
    return slide


def add_steps_slide(prs, kicker, title, steps, page):
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    y = Inches(1.65)
    step_h = Inches(0.92)
    for i, text in enumerate(steps):
        num = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.8), y, Inches(0.6), Inches(0.6))
        num.fill.solid(); num.fill.fore_color.rgb = CYAN; num.line.fill.background(); _no_shadow(num)
        tf = num.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = str(i + 1); r.font.bold = True; r.font.size = Pt(20); r.font.color.rgb = INK
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.65), y, Inches(10.95), Inches(0.68))
        card.fill.solid(); card.fill.fore_color.rgb = CARD
        card.line.color.rgb = RGBColor(0xE0, 0xE0, 0xEC); _no_shadow(card)
        tf2 = card.text_frame; tf2.vertical_anchor = MSO_ANCHOR.MIDDLE; tf2.word_wrap = True
        tf2.margin_left = Inches(0.2)
        p2 = tf2.paragraphs[0]
        r2 = p2.add_run(); r2.text = text; r2.font.size = Pt(16); r2.font.color.rgb = TEXT_DARK; r2.font.name = FONT_BODY
        y += step_h + Inches(0.1)
    add_footer(slide, page)
    return slide


def add_timeline_slide(prs, kicker, title, events, page):
    slide = blank_slide(prs)
    add_header(slide, kicker, title)
    line_y = Inches(4.0)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), line_y, Inches(11.5), Pt(3))
    line.fill.solid(); line.fill.fore_color.rgb = PURPLE; line.line.fill.background(); _no_shadow(line)
    n = len(events)
    gap = Inches(11.5) / (n - 1) if n > 1 else Inches(0)
    for i, (year, label, desc) in enumerate(events):
        x = Inches(0.9) + i * gap
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, x - Inches(0.11), line_y - Inches(0.08), Inches(0.22), Inches(0.22))
        dot.fill.solid(); dot.fill.fore_color.rgb = CYAN; dot.line.color.rgb = WHITE; dot.line.width = Pt(2)
        _no_shadow(dot)
        above = (i % 2 == 0)
        ty = line_y - Inches(1.55) if above else line_y + Inches(0.35)
        box_x = max(Inches(0.1), min(x - Inches(1.1), SW - Inches(2.3)))
        add_textbox(slide, box_x, ty, Inches(2.2), Inches(0.35), year, size=18, bold=True,
                    color=PURPLE, align=PP_ALIGN.CENTER)
        add_textbox(slide, box_x, ty + Inches(0.35), Inches(2.2), Inches(0.35), label, size=13, bold=True,
                    color=TEXT_DARK, align=PP_ALIGN.CENTER)
        add_textbox(slide, box_x, ty + Inches(0.68), Inches(2.2), Inches(0.75), desc, size=10.5,
                    color=TEXT_MUTE, align=PP_ALIGN.CENTER, line_spacing=1.05)
    add_footer(slide, page)
    return slide


QUIZ_COLORS = [PURPLE, CYAN, AMBER, RGBColor(0x8B, 0xC3, 0x4A)]


def add_quiz_question_slide(prs, quiz_no, question, options, page):
    slide = blank_slide(prs, bg=INK)
    tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.5), Inches(3.0), Inches(0.55))
    tag.fill.solid(); tag.fill.fore_color.rgb = CYAN; tag.line.fill.background(); _no_shadow(tag)
    tf = tag.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = f"🧠 VIKTORINA #{quiz_no}"; r.font.bold = True; r.font.size = Pt(16); r.font.color.rgb = INK
    add_textbox(slide, Inches(0.6), Inches(1.35), Inches(12.1), Inches(1.4),
                question, size=26, bold=True, color=WHITE, line_spacing=1.15)
    y = Inches(3.05)
    letters = ["A", "B", "C", "D"]
    for i, opt in enumerate(options):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), y, Inches(12.1), Inches(0.82))
        card.fill.solid(); card.fill.fore_color.rgb = RGBColor(0x2B, 0x27, 0x63)
        card.line.color.rgb = RGBColor(0x45, 0x40, 0x8F); _no_shadow(card)
        badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.85), y + Inches(0.16), Inches(0.5), Inches(0.5))
        badge.fill.solid(); badge.fill.fore_color.rgb = QUIZ_COLORS[i % 4]; badge.line.fill.background(); _no_shadow(badge)
        btf = badge.text_frame; btf.vertical_anchor = MSO_ANCHOR.MIDDLE
        bp = btf.paragraphs[0]; bp.alignment = PP_ALIGN.CENTER
        br = bp.add_run(); br.text = letters[i]; br.font.bold = True; br.font.size = Pt(18); br.font.color.rgb = INK
        add_textbox(slide, Inches(1.6), y, Inches(11.0), Inches(0.82), opt, size=17, color=WHITE,
                    anchor=MSO_ANCHOR.MIDDLE)
        y += Inches(0.95)
    add_textbox(slide, Inches(0.6), SH - Inches(0.55), Inches(11), Inches(0.35),
                "O'ylab ko'ring... javobingizni chatga yozing!", size=13, italic=True,
                color=RGBColor(0xA0, 0x9C, 0xD8))
    add_page_number(slide, page)
    return slide


def add_quiz_answer_slide(prs, quiz_no, question, options, correct_idx, explanation, page):
    slide = blank_slide(prs, bg=INK)
    tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.5), Inches(3.0), Inches(0.55))
    tag.fill.solid(); tag.fill.fore_color.rgb = GREEN; tag.line.fill.background(); _no_shadow(tag)
    tf = tag.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = f"✅ JAVOB #{quiz_no}"; r.font.bold = True; r.font.size = Pt(16); r.font.color.rgb = WHITE
    add_textbox(slide, Inches(0.6), Inches(1.35), Inches(12.1), Inches(1.0),
                question, size=20, bold=True, color=RGBColor(0xC8, 0xC8, 0xE8), line_spacing=1.1)
    y = Inches(2.55)
    letters = ["A", "B", "C", "D"]
    for i, opt in enumerate(options):
        is_correct = (i == correct_idx)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), y, Inches(12.1), Inches(0.72))
        card.fill.solid()
        card.fill.fore_color.rgb = GREEN_BG if is_correct else RGBColor(0x2B, 0x27, 0x63)
        card.line.color.rgb = GREEN if is_correct else RGBColor(0x45, 0x40, 0x8F)
        card.line.width = Pt(2) if is_correct else Pt(1)
        _no_shadow(card)
        badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.82), y + Inches(0.12), Inches(0.46), Inches(0.46))
        badge.fill.solid(); badge.fill.fore_color.rgb = GREEN if is_correct else RGBColor(0x55, 0x50, 0x9A)
        badge.line.fill.background(); _no_shadow(badge)
        btf = badge.text_frame; btf.vertical_anchor = MSO_ANCHOR.MIDDLE
        bp = btf.paragraphs[0]; bp.alignment = PP_ALIGN.CENTER
        br = bp.add_run(); br.text = "✓" if is_correct else letters[i]
        br.font.bold = True; br.font.size = Pt(16); br.font.color.rgb = WHITE
        add_textbox(slide, Inches(1.55), y, Inches(11.0), Inches(0.72), opt, size=15.5,
                    color=RGBColor(0x1B, 0x5E, 0x20) if is_correct else RGBColor(0xC8, 0xC8, 0xE8),
                    bold=is_correct, anchor=MSO_ANCHOR.MIDDLE)
        y += Inches(0.82)
    ebox = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), y + Inches(0.1), Inches(12.1), Inches(1.05))
    ebox.fill.solid(); ebox.fill.fore_color.rgb = RGBColor(0x2B, 0x27, 0x63)
    ebox.line.color.rgb = CYAN; ebox.line.width = Pt(1); _no_shadow(ebox)
    etf = ebox.text_frame; etf.word_wrap = True; etf.vertical_anchor = MSO_ANCHOR.MIDDLE
    etf.margin_left = Inches(0.2); etf.margin_right = Inches(0.2)
    ep = etf.paragraphs[0]
    er = ep.add_run(); er.text = "💡 Izoh: " + explanation
    er.font.size = Pt(14); er.font.color.rgb = RGBColor(0xE0, 0xE0, 0xF5); er.font.name = FONT_BODY
    add_page_number(slide, page)
    return slide


def add_closing_slide(prs, title, lines, page):
    slide = blank_slide(prs, bg=INK)
    for (x, y, s, col) in [(11.7, 0.5, 1.3, PURPLE), (0.4, 6.4, 0.9, CYAN)]:
        c = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(s), Inches(s))
        c.fill.solid(); c.fill.fore_color.rgb = col; c.line.fill.background(); _no_shadow(c)
    add_textbox(slide, Inches(0.9), Inches(2.4), Inches(11.5), Inches(1.2), title, size=44, bold=True, color=WHITE)
    add_bullets(slide, Inches(0.9), Inches(3.8), Inches(11.0), Inches(2.5), lines, size=17,
                color=RGBColor(0xD8, 0xD8, 0xF0), space_after=10)
    add_page_number(slide, page)
    return slide


# =====================================================================
prs = new_prs()
page = 1

# 1. Title
add_title_slide(prs); page += 1

# 2. Welcome / online-class ground rules
add_bullet_slide(prs, "Kirish", "Xush kelibsiz! Onlayn darsimiz qoidalari", [
    "Bu semestrda \"Dasturlash 1\" fanidan 8 soat ma'ruzani men olib boraman, qolgan mashg'ulotlarni universitetdan TA (yordamchi o'qituvchi) olib boradi.",
    "Dars onlayn tarzda o'tiladi — shuning uchun faollik juda muhim: mikrofon/chatdan foydalaning.",
    "Har bir mavzudan so'ng qisqa VIKTORINA bo'ladi — barchangiz javob bering, bu bilim darajangizni tekshirib boradi.",
    "Kamera imkon qadar yoqilgan bo'lsin, savol tug'ilsa darhol chatga yozing yoki qo'l ko'taring.",
    "Amaliy topshiriqlar, uyga vazifa va Google Forms orqali qo'shimcha testlar keyingi darslarda beriladi.",
], page); page += 1

# 3. Agenda
add_bullet_slide(prs, "Reja", "Bugungi darsning rejasi", [
    ("I-BO'LIM: Dasturlash tillari va .NET platformasi", 0),
    ("Dasturlash va dasturlash tili nima, turlari", 1),
    (".NET Core: imkoniyatlari, afzalliklari, xususiyatlari, JIT", 1),
    ("II-BO'LIM: Visual Studio muhiti va konsol rejimi", 0),
    ("IDE nima, Visual Studio bilan tanishish", 1),
    ("Konsol (Console) rejimida kiritish-chiqarish", 1),
    ("III-BO'LIM: C# da birinchi dastur", 0),
    ("\"Salom, Dunyo!\" dasturi, C# dasturi tuzilishi va yozish usullari", 1),
], page); page += 1

# 4. Objectives
add_bullet_slide(prs, "Maqsad", "Dars yakunida siz nimalarga erishasiz?", [
    "Dasturlash tili va platforma tushunchalarini o'z so'zlaringiz bilan tushuntira olasiz.",
    ".NET Core platformasining afzalliklarini va JIT kompilyatsiya nima ekanini bilasiz.",
    "Visual Studio'da yangi konsol loyihasini mustaqil yarata olasiz.",
    "Console.WriteLine() va Console.ReadLine() metodlaridan foydalana olasiz.",
    "O'zingizning birinchi ishlaydigan C# dasturingizni yozib, uning har bir qismini tushuntira olasiz.",
], page); page += 1

# 5. Section I header
add_section_slide(prs, 1, "I", "Dasturlash tillari va\n.NET platformasi",
                   "Dasturlash nima, tillar qanday tasniflanadi va nima uchun aynan .NET/C#ni o'rganamiz?",
                   page); page += 1

# 6. What is programming
add_bullet_slide(prs, "I-bo'lim", "Dasturlash nima o'zi?", [
    "Dasturlash — kompyuterga biror vazifani bajarish uchun aniq va tartibli buyruqlar ketma-ketligini yozish jarayoni.",
    "O'xshatish: oshpaz retsept bo'yicha ovqat pishiradi — retsept qanchalik aniq va tartibli bo'lsa, natija shunchalik to'g'ri chiqadi.",
    "Kompyuter dasturi ham xuddi shunday — bu \"retsept\", uni bajaruvchi esa kompyuter (protsessor).",
    "Dastur = Algoritm (yechim rejasi) + uni ma'lum bir dasturlash tilida yozib chiqish.",
], page); page += 1

# 7. Programming language definition
add_bullet_slide(prs, "I-bo'lim", "Dasturlash tili nima?", [
    "Dasturlash tili — inson kompyuterga buyruq berish uchun foydalanadigan, qat'iy qoidalarga (sintaksisga) ega sun'iy til.",
    "Inson tili (o'zbek, ingliz) kabi emas — dasturlash tilida har bir so'z va belgi aniq ma'noga ega, xatoga yo'l qo'yilmaydi.",
    "Bugungi kunda 700 dan ortiq dasturlash tili mavjud: Python, C++, Java, C#, Pascal, JavaScript va h.k.",
    "Har bir til o'z vazifasiga ega: veb-sayt uchun, mobil ilova uchun, o'yin uchun, ilmiy hisob-kitob uchun va h.k.",
], page, note="Siz allaqachon Pascal, C++ va Python bilan tanishsiz — bu yangi bilim emas, balki yangi TIL o'rganishdir!"); page += 1

# 8. Types of languages table
add_table_slide(prs, "I-bo'lim", "Dasturlash tillari turlari",
    ["Turi", "Tavsifi", "Misollar"],
    [
        ["Past darajali", "Kompyuter (protsessor)ga yaqin, inson uchun qiyin o'qiladi", "Mashina kodi, Assembler"],
        ["Yuqori darajali", "Inson tiliga yaqin, o'qish va yozish oson", "Python, C#, Java, C++, Pascal"],
        ["Kompilyatsiyalanuvchi", "Butun dastur oldindan mashina koddiga o'giriladi", "C, C++, Pascal"],
        ["Interpretatsiyalanuvchi", "Dastur qator-qator, ishga tushirilayotgan payti o'qiladi", "Python, JavaScript"],
        ["Aralash (C#)", "Avval oraliq kodga, so'ng ishga tushirish payti mashina kodiga", "C#, Java"],
    ], page, col_widths=[2.8, 5.6, 3.5]); page += 1

# 9. Why C#
add_bullet_slide(prs, "I-bo'lim", "Nima uchun aynan C# tilini o'rganamiz?", [
    "Universal til: veb-saytlar (ASP.NET), mobil ilovalar, ish stoli dasturlari, o'yinlar (Unity) va sun'iy intellekt loyihalarida qo'llaniladi.",
    "Sintaksisi C++ va Java'ga juda yaqin — C++ bilgan har bir kishi uchun C# ni o'rganish tez va oson.",
    "Microsoft tomonidan yaratilgan va qo'llab-quvvatlanadigan, doimiy rivojlanayotgan zamonaviy til.",
    "Mehnat bozorida eng ko'p talab qilinadigan dasturlash tillaridan biri — yaxshi ish topish imkoniyati yuqori.",
    "Xavfsiz (kuchli tur nazorati) va o'qish/tushunish uchun qulay strukturaga ega.",
], page); page += 1

# 10-11. Quiz 1
Q1_OPTS = [
    "Kompyuterni tozalash dasturi",
    "Inson kompyuterga buyruq berish uchun ishlatadigan, qat'iy qoidali sun'iy til",
    "Kompyuterning fizik qurilmasi (protsessor)",
    "Internetga ulanish uchun kerakli dastur",
]
add_quiz_question_slide(prs, 1, "Dasturlash tili — bu nima?", Q1_OPTS, page); page += 1
add_quiz_answer_slide(prs, 1, "Dasturlash tili — bu nima?", Q1_OPTS, 1,
    "Dasturlash tili — inson bilan kompyuter o'rtasidagi \"tarjimon\" vazifasini bajaradigan, aniq qoidalarga ega sun'iy til.",
    page); page += 1

# 13. What is .NET
add_bullet_slide(prs, "I-bo'lim", ".NET nima o'zi?", [
    ".NET — Microsoft tomonidan yaratilgan, dasturiy ta'minot ishlab chiqish uchun bepul va ochiq manbali (open-source) platforma.",
    "U dasturlash tili emas — balki dasturlarni yozish, kompilyatsiya qilish va ishga tushirish uchun kerakli barcha vositalar to'plamidir.",
    "Bitta platformada bir nechta tillarda dastur yozish mumkin: C#, F#, Visual Basic.",
    "Bu darsda biz .NET platformasi ustida C# tilida dastur yozishni o'rganamiz.",
], page); page += 1

# 14. .NET history timeline
add_timeline_slide(prs, "I-bo'lim", ".NET rivojlanish tarixi (qisqacha)", [
    ("2002", ".NET Framework", "Faqat Windows uchun, birinchi versiya"),
    ("2016", ".NET Core", "Ochiq manbali, ko'p platformali (Windows/Linux/macOS)"),
    ("2020", ".NET 5", "Barcha .NET turlari bitta platformaga birlashtirildi"),
    ("2023-25", ".NET 8 / 9", "\"Bir .NET — hamma joyda\" g'oyasi to'liq amalga oshdi"),
], page); page += 1

# 15-16. Two col: imkoniyatlari / afzalliklari
add_two_col_slide(prs, "I-bo'lim", ".NET Core: imkoniyatlari va afzalliklari",
    "Imkoniyatlari", [
        "Veb-ilovalar yaratish (ASP.NET Core)",
        "Mobil ilovalar (.NET MAUI)",
        "Ish stoli dasturlari (WPF, WinForms)",
        "Kompyuter o'yinlari (Unity)",
        "Bulutli xizmatlar va mikroservislar",
        "Sun'iy intellekt va ma'lumotlar tahlili (ML.NET)",
    ],
    "Afzalliklari", [
        "Ko'p platformali: Windows, Linux, macOS",
        "Yuqori tezkorlik va unumdorlik",
        "Bepul va to'liq ochiq manbali (GitHub'da)",
        "Katta va faol dasturchilar jamoasi",
        "Minglab tayyor kutubxonalar (NuGet)",
        "Microsoft tomonidan uzoq muddatli qo'llab-quvvatlash",
    ], page); page += 1

# 17. Distinguishing features
add_bullet_slide(prs, "I-bo'lim", ".NET Core-ning o'ziga xos xususiyatlari", [
    "CLR (Common Language Runtime) — dasturlarni ishga tushiruvchi \"yurak\": xotirani boshqarish, xavfsizlik, xatoliklarni ushlash shu yerda amalga oshadi.",
    "BCL (Base Class Library) — tayyor, oldindan yozilgan minglab funksiya va klasslar to'plami (masalan, matn, sana, fayl bilan ishlash uchun).",
    "Bir nechta tillarni bitta platformada qo'llab-quvvatlash — C# kodi va F# kodi bir loyihada birga ishlashi mumkin.",
    "NuGet paket menejeri — boshqa dasturchilar yozgan tayyor kutubxonalarni bir necha soniyada loyihangizga qo'shish imkonini beradi.",
], page); page += 1

# 18. Pipeline diagram
add_pipeline_slide(prs, "I-bo'lim", "C# kodi qanday bajariladi?", [
    ("Manba kod", "(Program.cs)"),
    ("C# Kompilyator", "(Roslyn)"),
    ("IL kod", "(oraliq til)"),
    ("CLR + JIT", "(ishga tushirish payti)"),
    ("Mashina kodi", "(protsessor tili)"),
], page, note="C# kodi to'g'ridan-to'g'ri mashina koddiga emas, avval IL (oraliq til)ga o'giriladi — bu .NET ning eng muhim g'oyasi.")
page += 1

# 19. JIT explained
add_bullet_slide(prs, "I-bo'lim", "JIT (Just-In-Time) kompilyatsiya nima?", [
    "JIT — \"Just-In-Time\" (aynan kerak bo'lgan payt) kompilyatsiya degani: IL kod dastur ISHGA TUSHIRILAYOTGAN paytda mashina kodiga o'giriladi, oldindan emas.",
    "O'xshatish: sinxron tarjimon — spikerning nutqini so'zlab turgan paytida jonli tarjima qiladi (JIT), kitobni oldindan butunlay tarjima qilib qo'yish esa AOT (Ahead-Of-Time) usuliga o'xshaydi.",
    "Shu tufayli bitta IL kod istalgan qurilmada (Windows, Linux, macOS) — o'sha qurilmaning o'z mashina koddiga o'girilib — ishlay oladi.",
    "JIT ishga tushirish paytida kompyuteringiz uchun eng maqbul, optimallashtirilgan mashina kodini yaratadi.",
], page, note="Rasmiy dastur dasturida bu qisqartma \"Just Run Time\" deb yozilgan, lekin dunyo bo'ylab qabul qilingan to'g'ri atama — \"Just-In-Time\"."); page += 1

# 21. Technologies grid
add_grid_slide(prs, "I-bo'lim", ".NET asosida qurilgan zamonaviy texnologiyalar", [
    ("🌐", "ASP.NET Core", "Veb-saytlar va veb-servislar yaratish"),
    ("📱", ".NET MAUI", "Android/iOS uchun mobil ilovalar"),
    ("🖥️", "WPF / WinForms", "Windows ish stoli dasturlari"),
    ("🎮", "Unity", "2D/3D kompyuter o'yinlari (C# skriptlar)"),
    ("☁️", "Azure", "Bulutli xizmatlar va serverlar"),
    ("🤖", "ML.NET", "Mashinaviy o'rganish (AI) loyihalari"),
], page, cols=3); page += 1

# 22-23. Quiz 2
Q2_OPTS = [
    "Dastur yozilgandan keyin uni butunlay o'chirib tashlash usuli",
    "IL (oraliq) kodni dastur ishga tushirilayotgan paytda mashina kodiga o'girish jarayoni",
    "Faqat Windows tizimida ishlaydigan eski texnologiya",
    "Internetdan dastur yuklab olish usuli",
]
add_quiz_question_slide(prs, 2, "JIT (Just-In-Time) kompilyatsiya — bu nima?", Q2_OPTS, page); page += 1
add_quiz_answer_slide(prs, 2, "JIT (Just-In-Time) kompilyatsiya — bu nima?", Q2_OPTS, 1,
    "JIT — dastur ishga tushirilayotgan aynan o'sha paytda IL kodni protsessorga tushunarli mashina kodiga o'giradi. Shu sabab bitta dastur turli qurilmalarda ishlay oladi.",
    page); page += 1

# 24. Section II header
add_section_slide(prs, 2, "II", "Visual Studio muhiti va\nkonsol rejimi",
                   "Dasturlash muhiti (IDE) bilan tanishamiz va birinchi loyihani yaratamiz.",
                   page); page += 1

# 25. What is IDE
add_bullet_slide(prs, "II-bo'lim", "IDE (dasturlash muhiti) nima?", [
    "IDE — Integrated Development Environment (Integratsiyalashgan ishlab chiqish muhiti): kod yozish, tekshirish va ishga tushirish uchun barcha vositalar bitta dasturda jamlangan.",
    "O'xshatish: oddiy oshxona (bitta pichoq bilan) va professional, to'liq jihozlangan oshxona (barcha asboblar tayyor) orasidagi farq kabi.",
    "IDE tarkibida: kod muharriri, kompilyator, xato aniqlovchi (debugger) va loyiha boshqaruvchisi bo'ladi.",
    "Biz ushbu kursda Microsoft Visual Studio dasturidan foydalanamiz.",
], page); page += 1

# 26. About Visual Studio
add_bullet_slide(prs, "II-bo'lim", "Visual Studio bilan tanishuv", [
    "Visual Studio — Microsoft tomonidan yaratilgan, C#/.NET dasturlash uchun eng mashhur va professional IDE.",
    "\"Community\" versiyasi — talabalar va shaxsiy foydalanish uchun MUTLAQO BEPUL.",
    "visualstudio.microsoft.com saytidan yuklab olinadi (o'rnatishda \".NET desktop development\" komponentini belgilash kerak).",
    "Farqi: Visual Studio Code — bu yengil matn muharriri (kichik loyihalar uchun qulay), Visual Studio esa katta, to'liq IDE (biz shundan foydalanamiz).",
], page); page += 1

# 27. IDE layout mockup
def add_ide_mockup_slide(prs, page):
    slide = blank_slide(prs)
    add_header(slide, "II-bo'lim", "Visual Studio interfeysi (sxematik ko'rinish)")
    ox, oy = Inches(0.7), Inches(1.55)
    ow, oh = Inches(11.9), Inches(5.3)
    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ox, oy, ow, oh)
    frame.fill.solid(); frame.fill.fore_color.rgb = RGBColor(0xE8, 0xE8, 0xF0)
    frame.line.color.rgb = RGBColor(0xB0, 0xB0, 0xC0); _no_shadow(frame)
    menubar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, ox, oy, ow, Inches(0.45))
    menubar.fill.solid(); menubar.fill.fore_color.rgb = INK; menubar.line.fill.background(); _no_shadow(menubar)
    add_textbox(slide, ox + Inches(0.2), oy + Inches(0.06), Inches(6), Inches(0.32),
                "File   Edit   View   Project   Build   Debug   ...", size=12, color=WHITE)
    solx = ox + ow - Inches(3.0)
    sol = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, solx, oy + Inches(0.45), Inches(3.0), oh - Inches(0.85))
    sol.fill.solid(); sol.fill.fore_color.rgb = RGBColor(0xF5, 0xF5, 0xFA); sol.line.color.rgb = RGBColor(0xB0, 0xB0, 0xC0)
    _no_shadow(sol)
    add_textbox(slide, solx + Inches(0.15), oy + Inches(0.55), Inches(2.7), Inches(0.3),
                "SOLUTION EXPLORER", size=11, bold=True, color=PURPLE)
    add_bullets(slide, solx + Inches(0.15), oy + Inches(0.95), Inches(2.7), Inches(2.0),
                ["📁 LectureDemo", "   📁 Dependencies", "   📄 Program.cs"], size=12, space_after=6)
    editx = ox
    edit = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, editx, oy + Inches(0.45), ow - Inches(3.0), oh - Inches(1.85))
    edit.fill.solid(); edit.fill.fore_color.rgb = CODE_BG; edit.line.color.rgb = RGBColor(0xB0, 0xB0, 0xC0)
    _no_shadow(edit)
    add_textbox(slide, editx + Inches(0.15), oy + Inches(0.55), Inches(6.0), Inches(0.3),
                "Program.cs — KOD MUHARRIRI (Code Editor)", size=11, bold=True, color=CYAN)
    add_textbox(slide, editx + Inches(0.2), oy + Inches(1.0), Inches(8.0), Inches(2.0),
                "Console.WriteLine(\"Salom, Dunyo!\");", size=14, color=CODE_STRING, font=FONT_CODE)
    outy = oy + oh - Inches(1.4)
    out = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, editx, outy, ow - Inches(3.0), Inches(1.4))
    out.fill.solid(); out.fill.fore_color.rgb = RGBColor(0x20, 0x20, 0x20); out.line.color.rgb = RGBColor(0xB0, 0xB0, 0xC0)
    _no_shadow(out)
    add_textbox(slide, editx + Inches(0.15), outy + Inches(0.08), Inches(6.0), Inches(0.3),
                "OUTPUT / TERMINAL (natijalar oynasi)", size=11, bold=True, color=RGBColor(0x9C, 0xCC, 0x65))
    add_textbox(slide, editx + Inches(0.2), outy + Inches(0.5), Inches(6.0), Inches(0.7),
                "Salom, Dunyo!", size=13, color=RGBColor(0x9C, 0xCC, 0x65), font=FONT_CODE)
    add_footer(slide, page)
    return slide

add_ide_mockup_slide(prs, page); page += 1

# 28. Steps to create console app
add_steps_slide(prs, "II-bo'lim", "Yangi konsol loyihasini yaratish", [
    "Visual Studio dasturini oching va \"Create a new project\" tugmasini bosing.",
    "Loyiha turlari ro'yxatidan \"Console App\" (C#) ni tanlang.",
    "Loyihangizga nom bering (masalan: LectureDemo) va saqlanadigan joyni belgilang.",
    ".NET versiyasini tanlab, \"Create\" (Yaratish) tugmasini bosing.",
    "Visual Studio avtomatik ravishda Program.cs faylini tayyor holda ochadi — bu yerda kod yozamiz!",
], page); page += 1

# 29. Console mode
add_bullet_slide(prs, "II-bo'lim", "Konsol (Console) rejimi nima?", [
    "Konsol rejimi — dastur bilan faqat MATN orqali muloqot qilinadigan rejim (grafik oynasiz, tugma va rasmlarsiz).",
    "Kiritish (input) — foydalanuvchi klaviaturadan matn kiritadi.",
    "Chiqarish (output) — dastur natijani ekranga matn ko'rinishida chiqaradi.",
    "Bu — dasturlashni o'rganishni boshlashning eng sodda va tushunarli usuli, shuning uchun barcha darsliklar shundan boshlaydi.",
], page); page += 1

# 30. Console methods table
add_table_slide(prs, "II-bo'lim", "Console klassining asosiy metodlari",
    ["Metod", "Vazifasi", "Misol"],
    [
        ["Console.WriteLine()", "Matnni chiqarib, keyingi qatorga o'tadi", "Console.WriteLine(\"Salom!\");"],
        ["Console.Write()", "Matnni chiqaradi, qatorni almashtirmaydi", "Console.Write(\"Ism: \");"],
        ["Console.ReadLine()", "Foydalanuvchidan bir qator matn qabul qiladi", "string ism = Console.ReadLine();"],
        ["Console.ReadKey()", "Bitta tugma bosilishini kutib turadi", "Console.ReadKey();"],
    ], page, col_widths=[3.3, 5.3, 3.3]); page += 1

# 31. Simple console example code slide
CODE31 = [
    [("// Oddiy konsol chiqishi misoli", CODE_COMMENT)],
    [("Console", CODE_TYPE), (".", CODE_TEXT), ("WriteLine", CODE_METHOD), ("(", CODE_TEXT),
     ('"Salom, Dunyo!"', CODE_STRING), (");", CODE_TEXT)],
    [("Console", CODE_TYPE), (".", CODE_TEXT), ("WriteLine", CODE_METHOD), ("(", CODE_TEXT),
     ('"Men C# o\'rganyapman."', CODE_STRING), (");", CODE_TEXT)],
]
add_code_slide(prs, "II-bo'lim", "Misol: konsolga matn chiqarish", CODE31,
               ["Salom, Dunyo!", "Men C# o'rganyapman."], page,
               caption="Console.WriteLine() har chaqirilganda natija yangi qatorda chiqadi."); page += 1

# 32-33. Quiz 3
Q3_OPTS = [
    "Console.ReadLine() — chiqarish, Console.WriteLine() — kiritish uchun",
    "Console.WriteLine() — foydalanuvchidan matn oladi, Console.Write() — ekranga chiqaradi",
    "Console.WriteLine() — ekranga chiqarib, qatorni almashtiradi; Console.ReadLine() — foydalanuvchidan matn qabul qiladi",
    "Ikkalasi ham bir xil vazifani bajaradi",
]
add_quiz_question_slide(prs, 3, "Quyidagilardan qaysi biri TO'G'RI?", Q3_OPTS, page); page += 1
add_quiz_answer_slide(prs, 3, "Quyidagilardan qaysi biri TO'G'RI?", Q3_OPTS, 2,
    "WriteLine — ekranga matn CHIQARADI va qatorni almashtiradi; ReadLine — foydalanuvchidan klaviatura orqali matn QABUL QILADI.",
    page); page += 1

# 34. Section III header
add_section_slide(prs, 3, "III", "C# da birinchi dastur",
                   "\"Salom, Dunyo!\" dasturini birga yozamiz va C# dasturining tuzilishini o'rganamiz.",
                   page); page += 1

# 35. Structure diagram (labeled code)
def add_structure_slide(prs, page):
    slide = blank_slide(prs)
    add_header(slide, "III-bo'lim", "C# dasturining tuzilishi")
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(1.6), Inches(6.6), Inches(4.6))
    box.fill.solid(); box.fill.fore_color.rgb = CODE_BG; box.line.color.rgb = RGBColor(0x3C, 0x3C, 0x3C); _no_shadow(box)
    tf = box.text_frame; tf.word_wrap = True
    tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.25)
    lines = [
        [("using", CODE_KEYWORD), (" System;", CODE_TEXT)],
        [("", CODE_TEXT)],
        [("namespace", CODE_KEYWORD), (" LectureDemo", CODE_TYPE)],
        [("{", CODE_TEXT)],
        [("    class", CODE_KEYWORD), (" Program", CODE_TYPE)],
        [("    {", CODE_TEXT)],
        [("        static", CODE_KEYWORD), (" void", CODE_KEYWORD), (" Main", CODE_METHOD), ("(", CODE_TEXT),
         ("string", CODE_KEYWORD), ("[] args)", CODE_TEXT)],
        [("        {", CODE_TEXT)],
        [("            Console", CODE_TYPE), (".", CODE_TEXT), ("WriteLine", CODE_METHOD), ("(", CODE_TEXT),
         ('"Salom, Dunyo!"', CODE_STRING), (");", CODE_TEXT)],
        [("        }", CODE_TEXT)],
        [("    }", CODE_TEXT)],
        [("}", CODE_TEXT)],
    ]
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = 1.2
        for text, color in line:
            r = p.add_run(); r.text = text if text else " "
            r.font.name = FONT_CODE; r.font.size = Pt(14.5); r.font.color.rgb = color
    labels = [
        ("using System;", "Kutubxonani ulash — Console kabi tayyor vositalardan foydalanish uchun."),
        ("namespace LectureDemo", "Nomlar fazosi — loyihadagi kodlarni guruhlab, chalkashlikning oldini oladi."),
        ("class Program", "Klass — dasturimizning asosiy \"qutisi\", barcha kod shu ichida yoziladi."),
        ("static void Main(...)", "Main metodi — dastur ISHGA TUSHGANDA birinchi bajariladigan joy (kirish nuqtasi)."),
        ("Console.WriteLine(...)", "Bajariladigan buyruq (statement) — ekranga matn chiqaradi."),
    ]
    ly = Inches(1.7)
    for name, desc in labels:
        add_textbox(slide, Inches(7.5), ly, Inches(5.1), Inches(0.3), name, size=14, bold=True, color=PURPLE, font=FONT_CODE)
        add_textbox(slide, Inches(7.5), ly + Inches(0.32), Inches(5.1), Inches(0.6), desc, size=12.5,
                    color=TEXT_DARK, line_spacing=1.05)
        ly += Inches(0.92)
    add_footer(slide, page)
    return slide

add_structure_slide(prs, page); page += 1

# 36. Full hello world code slide (classic)
CODE36 = [
    [("using", CODE_KEYWORD), (" System;", CODE_TEXT)],
    [("", CODE_TEXT)],
    [("namespace", CODE_KEYWORD), (" LectureDemo", CODE_TYPE)],
    [("{", CODE_TEXT)],
    [("    ", CODE_TEXT), ("class", CODE_KEYWORD), (" Program", CODE_TYPE)],
    [("    {", CODE_TEXT)],
    [("        ", CODE_TEXT), ("static", CODE_KEYWORD), (" void", CODE_KEYWORD), (" Main", CODE_METHOD),
     ("(", CODE_TEXT), ("string", CODE_KEYWORD), ("[] args)", CODE_TEXT)],
    [("        {", CODE_TEXT)],
    [("            ", CODE_TEXT), ("Console", CODE_TYPE), (".", CODE_TEXT), ("WriteLine", CODE_METHOD),
     ("(", CODE_TEXT), ('"Salom, Dunyo!"', CODE_STRING), (");", CODE_TEXT)],
    [("        }", CODE_TEXT)],
    [("    }", CODE_TEXT)],
    [("}", CODE_TEXT)],
]
add_code_slide(prs, "III-bo'lim", "\"Salom, Dunyo!\" — to'liq dastur", CODE36,
               ["Salom, Dunyo!"], page,
               caption="Bu — har bir dasturchining birinchi an'anaviy dasturi! Endi uni birga yozamiz va ishga tushiramiz."); page += 1

# 37. Line by line explanation table
add_table_slide(prs, "III-bo'lim", "Har bir qatorni tushuntiramiz",
    ["Qator", "Ma'nosi"],
    [
        ["using System;", "Standart kutubxonani (Console shu yerda) loyihaga ulaydi."],
        ["namespace LectureDemo", "Kodlarimiz qaysi \"nomlar fazosi\"ga tegishli ekanini bildiradi."],
        ["class Program", "Dastur kodini jamlovchi asosiy klass (\"quti\")."],
        ["static void Main(string[] args)", "Dastur ishga tushganda ENG BIRINCHI chaqiriladigan metod."],
        ["Console.WriteLine(\"...\");", "Ekranga matn chiqaradi — bu bajariladigan buyruq (statement)."],
        ["{ }  (figurali qavslar)", "Kod blokini — klass yoki metod chegarasini bildiradi."],
    ], page, col_widths=[4.3, 7.6]); page += 1

# 38. Modern top-level statements
CODE38 = [
    [("// Zamonaviy (qisqartirilgan) yozish usuli — .NET 6+", CODE_COMMENT)],
    [("Console", CODE_TYPE), (".", CODE_TEXT), ("WriteLine", CODE_METHOD), ("(", CODE_TEXT),
     ('"Salom, Dunyo!"', CODE_STRING), (");", CODE_TEXT)],
]
add_code_slide(prs, "III-bo'lim", "Yozish usullari: qisqartirilgan (top-level) shakl", CODE38,
               ["Salom, Dunyo!"], page,
               caption="Yangi Visual Studio loyihalarida namespace/class/Main avtomatik \"yashirilgan\" — ikkala usul ham bir xil natija beradi, ichki tuzilishini tushunish esa MUHIM.")
page += 1

# 39. Syntax rules
add_bullet_slide(prs, "III-bo'lim", "C# yozish qoidalari (sintaksis)", [
    "Har bir buyruq (statement) nuqta-vergul \";\" bilan tugaydi — bu qoidani unutmang!",
    "Figurali qavslar { } kod blokini (klass, metod, shart, sikl chegarasini) bildiradi.",
    "C# katta-kichik harflarga SEZGIR (case-sensitive): Console va console — ikki xil narsa!",
    "Izohlar (comments): // — bir qatorlik izoh, /* ... */ — ko'p qatorlik izoh. Izohlar dastur ishlashiga ta'sir qilmaydi, faqat inson uchun tushuntirish beradi.",
    "Kodni to'g'ri joylashtirish (indentation) — kodni o'qishni osonlashtiradi, Visual Studio buni avtomatik qiladi.",
], page); page += 1

# 40. Naming conventions
add_table_slide(prs, "III-bo'lim", "Nomlash qoidalari (naming conventions)",
    ["Uslub", "Qo'llanilishi", "Misol"],
    [
        ["PascalCase", "Klass va metod nomlari uchun", "class Program,  Main(),  WriteLine()"],
        ["camelCase", "O'zgaruvchi nomlari uchun", "int yosh;  string ism;"],
        ["Tavsif", "Nomlar tushunarli va mazmunli bo'lishi kerak", "yosh — yaxshi,  x1 — yomon"],
    ], page, col_widths=[3.0, 5.5, 3.4],
    note="Yaxshi nomlangan kod — o'zingiz va boshqalar uchun ham oson tushuniladigan kod!"); page += 1

# 41-42. Quiz 4
Q4_OPTS = [
    "Main() metodi — dastur ishga tushganda birinchi bajariladigan joy",
    "using System; — dasturni internetdan yuklab beradi",
    "// belgisi ko'p qatorli izoh uchun ishlatiladi",
    "C# katta-kichik harflarni farqlamaydi",
]
add_quiz_question_slide(prs, 4, "Quyidagilardan qaysi biri TO'G'RI gap?", Q4_OPTS, page); page += 1
add_quiz_answer_slide(prs, 4, "Quyidagilardan qaysi biri TO'G'RI gap?", Q4_OPTS, 0,
    "Main() metodi — C# dasturining KIRISH NUQTASI: dastur ishga tushganda protsessor birinchi bo'lib shu metodni bajaradi.",
    page); page += 1

# 43. Homework/practice
add_bullet_slide(prs, "Amaliyot", "Mustaqil bajarish uchun topshiriq", [
    "1-topshiriq: Agar hali qilmagan bo'lsangiz, o'z kompyuteringizga Visual Studio Community'ni o'rnating.",
    "2-topshiriq: Yangi Console App loyihasi yarating (nomi: MyFirstProgram).",
    "3-topshiriq: Console.WriteLine() yordamida ekranga o'z ismingiz, familiyangiz va guruhingizni chiqaring (kamida 3 qator).",
    "4-topshiriq (qo'shimcha): Console.ReadLine() yordamida ismingizni kiritishni so'rab, keyin uni ekranga chiqaring.",
    "Tayyor loyihangizni keyingi darsda ko'rsatishga tayyor bo'ling!",
], page, note="Qiynalsangiz — bemalol TA yoki menga chatda savol bering, xato qilishdan qo'rqmang!"); page += 1

# 44. Summary
add_bullet_slide(prs, "Xulosa", "Bugungi dars xulosasi", [
    "Dasturlash tili — kompyuterga buyruq berish uchun qat'iy qoidali sun'iy til.",
    ".NET — Microsoft'ning bepul, ochiq manbali, ko'p platformali dasturlash platformasi.",
    "JIT — IL kodni ishga tushirish PAYTIDA mashina kodiga o'giruvchi mexanizm.",
    "Visual Studio — kod yozish, tekshirish va ishga tushirish uchun to'liq IDE.",
    "C# dasturi: using → namespace → class → Main() → statementlar (buyruqlar) tuzilishiga ega.",
    "Console.WriteLine() — chiqarish, Console.ReadLine() — kiritish uchun ishlatiladi.",
], page); page += 1

# 45. Next lecture
add_bullet_slide(prs, "Keyingi dars", "2-Ma'ruza: C# tilining tashkil etuvchilari", [
    "Alfavit va identifikatorlar — o'zgaruvchi va metodlarga qanday nom berish mumkin.",
    "Kalit so'zlar (keywords) — C# tilida band qilingan maxsus so'zlar.",
    "Literallar, o'zgaruvchilar va o'zgarmaslar (const) tushunchalari.",
    "Izohlar (comments) yozish usullari batafsil.",
    "Tayyorgarlik: bugungi amaliy topshiriqni bajarib kelishni unutmang!",
], page); page += 1

# 46. Resources
add_two_col_slide(prs, "Manbalar", "Foydali adabiyotlar va havolalar",
    "Darsliklar", [
        "Adambayev U.E. va b. \"Algoritmik tillar va dasturlash. C# tilida dasturlash asoslari\" (2023)",
        "Mo'minov B.B. \"Dasturlash 1\" (2021)",
        "Albahari B. \"C# 7.0. Справочник\" (2018)",
        "Troelsen A., Japikse P. \"Pro C# with .NET Core\" (Apress)",
    ],
    "Onlayn manbalar", [
        "metanit.com/sharp/tutorial",
        "www.dastur.uz — o'zbek tilida dasturlash sayti",
        "learn.microsoft.com/dotnet",
        "code-live.uz, robocontest.uz — mashq qilish uchun",
    ], page); page += 1

# 47. Closing
add_closing_slide(prs, "Rahmat! Savollaringiz bormi?", [
    "📧 Aloqa uchun: (o'qituvchi email/telefon — dars vaqtida beriladi)",
    "📝 Amaliy topshiriq va mashg'ulotlar — TA bilan davom etadi",
    "📅 Keyingi ma'ruza: C# tilining tashkil etuvchilari",
    "🎯 Faol qatnashganingiz uchun rahmat!",
], page)

out_path = r"D:\class\JBNUU\Lecture1_Kirish_Dasturlash_NETCore.pptx"
prs.save(out_path)
print("Saved:", out_path, "| total slides:", len(prs.slides.__iter__.__self__._sldIdLst))
