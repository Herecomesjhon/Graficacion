"""Herramientas para armar los documentos de Word de las investigaciones."""

from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor, Twips

NAVY = RGBColor(0x0E, 0x27, 0x44)
GOLD = RGBColor(0x8C, 0x6A, 0x22)
INK = RGBColor(0x1C, 0x1C, 0x1C)
MUTED = RGBColor(0x5C, 0x56, 0x4C)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

SERIF = "Times New Roman"
SANS = "Calibri"
MONO = "Consolas"

FIG = Path(__file__).resolve().parent / "figuras"


def _rfonts(rPr, name):
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), name)
    return rFonts


def set_run_font(run, name, size, bold=False, italic=False, color=None):
    run.bold = bold
    run.italic = italic
    run.font.name = name
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color
    rPr = run._element.get_or_add_rPr()
    _rfonts(rPr, name)
    lang = rPr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rPr.append(lang)
    lang.set(qn("w:val"), "es-MX")


def set_language(doc):
    styles = doc.styles.element
    rpr_default = styles.find(qn("w:docDefaults")).find(qn("w:rPrDefault")).find(qn("w:rPr"))
    lang = rpr_default.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr_default.append(lang)
    lang.set(qn("w:val"), "es-MX")
    lang.set(qn("w:eastAsia"), "es-MX")


def shade_cell(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")


def set_cell_margins(cell, top=60, bottom=60, left=90, right=90):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = tcPr.find(qn("w:tcMar"))
    if tcMar is not None:
        tcPr.remove(tcMar)
    tcMar = OxmlElement("w:tcMar")
    for edge, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def valign(cell, value="center"):
    tcPr = cell._tc.get_or_add_tcPr()
    v = tcPr.find(qn("w:vAlign"))
    if v is None:
        v = OxmlElement("w:vAlign")
        tcPr.append(v)
    v.set(qn("w:val"), value)


def set_table_widths(table, widths):
    table.autofit = False
    table.allow_autofit = False
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    total = sum(widths)
    tbl = table._tbl
    tblPr = tbl.tblPr
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:w"), str(int(total * 1440)))
    tblW.set(qn("w:type"), "dxa")
    grid = tbl.find(qn("w:tblGrid"))
    if grid is not None:
        tbl.remove(grid)
    grid = OxmlElement("w:tblGrid")
    for width in widths:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(int(width * 1440)))
        grid.append(gc)
    tblPr.addnext(grid)
    for row in table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = Inches(widths[idx])
            tcPr = cell._tc.get_or_add_tcPr()
            tcW = tcPr.find(qn("w:tcW"))
            if tcW is None:
                tcW = OxmlElement("w:tcW")
                tcPr.append(tcW)
            tcW.set(qn("w:w"), str(int(widths[idx] * 1440)))
            tcW.set(qn("w:type"), "dxa")


def set_table_borders(table, color="C8C2B4", sz="4"):
    tblPr = table._tbl.tblPr
    existing = tblPr.find(qn("w:tblBorders"))
    if existing is not None:
        tblPr.remove(existing)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), sz)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.append(borders)


def prevent_row_split(row):
    trPr = row._tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    trPr.append(cant)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    header = OxmlElement("w:tblHeader")
    trPr.append(header)


def paragraph_border(paragraph, color="A67C2D", sz="12"):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = pPr.find(qn("w:pBdr"))
    if pBdr is None:
        pBdr = OxmlElement("w:pBdr")
        pPr.append(pBdr)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), sz)
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)


def add_page_field(paragraph):
    run = paragraph.add_run()
    set_run_font(run, SANS, 9, color=MUTED)
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(begin)
    run2 = paragraph.add_run()
    set_run_font(run2, SANS, 9, color=MUTED)
    run2._r.append(instr)
    run3 = paragraph.add_run()
    set_run_font(run3, SANS, 9, color=MUTED)
    run3._r.append(end)


def start_page_number(section, start="1"):
    sectPr = section._sectPr
    pg = sectPr.find(qn("w:pgNumType"))
    if pg is None:
        pg = OxmlElement("w:pgNumType")
        sectPr.append(pg)
    pg.set(qn("w:start"), start)


def configure_page(section):
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.3)
    section.bottom_margin = Cm(2.2)
    section.header_distance = Cm(0.6)
    section.footer_distance = Cm(0.5)


def style_document(doc):
    set_language(doc)
    normal = doc.styles["Normal"]
    normal.font.name = SERIF
    normal.font.size = Pt(12)
    normal.font.color.rgb = INK
    _rfonts(normal.element.get_or_add_rPr(), SERIF)
    pf = normal.paragraph_format
    pf.line_spacing = 1.15
    pf.space_after = Pt(8)
    pf.space_before = Pt(0)
    pf.widow_control = True
    for level, size, before, after in (
        (1, 16, 16, 6),
        (2, 13, 14, 4),
        (3, 12, 12, 3),
    ):
        style = doc.styles[f"Heading {level}"]
        style.font.name = SANS
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.italic = False
        style.font.color.rgb = NAVY
        rPr = style.element.get_or_add_rPr()
        _rfonts(rPr, SANS)
        color = rPr.find(qn("w:color"))
        if color is None:
            color = OxmlElement("w:color")
            rPr.append(color)
        color.set(qn("w:val"), "0E2744")
        sp = style.paragraph_format
        sp.space_before = Pt(before)
        sp.space_after = Pt(after)
        sp.line_spacing = 1.08
        sp.keep_with_next = True
        sp.widow_control = True


def new_document(title, subject):
    doc = Document()
    style_document(doc)
    core = doc.core_properties
    core.author = "Cristian Muñoz Hinojosa"
    core.title = title
    core.subject = subject
    core.category = "Taller de sistemas operativos"
    core.language = "es-MX"
    core.comments = (
        "Investigación documental. Instituto Tecnológico de Morelia. "
        "Fecha de corte: 20 de noviembre de 2026."
    )
    section = doc.sections[0]
    configure_page(section)
    return doc


def open_body(doc, footer_left, header_right):
    section = doc.add_section(WD_SECTION.NEW_PAGE)
    configure_page(section)
    start_page_number(section, "1")
    header = section.header
    header.is_linked_to_previous = False
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.paragraph_format.space_after = Pt(2)
    run = hp.add_run(header_right)
    set_run_font(run, SANS, 9, color=MUTED)
    paragraph_border(hp, "C8C2B4", "8")
    footer = section.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    fp.paragraph_format.space_before = Pt(2)
    left = fp.add_run(footer_left + "   ·   ")
    set_run_font(left, SANS, 9, color=MUTED)
    add_page_field(fp)
    paragraph_border_top(fp)
    return section


def paragraph_border_top(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    top = OxmlElement("w:top")
    top.set(qn("w:val"), "single")
    top.set(qn("w:sz"), "8")
    top.set(qn("w:space"), "6")
    top.set(qn("w:color"), "C8C2B4")
    pBdr.append(top)
    pPr.append(pBdr)


def P(doc, text, *, size=12, bold=False, italic=False, align="justify",
      before=0, after=8, indent=0.75, font=SERIF, color=None):
    p = doc.add_paragraph()
    p.alignment = {
        "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
        "center": WD_ALIGN_PARAGRAPH.CENTER,
        "left": WD_ALIGN_PARAGRAPH.LEFT,
        "right": WD_ALIGN_PARAGRAPH.RIGHT,
    }[align]
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.15
    if indent:
        p.paragraph_format.first_line_indent = Cm(indent)
    run = p.add_run(text)
    set_run_font(run, font, size, bold=bold, italic=italic, color=color or INK)
    return p


def H(doc, text, level=1):
    return doc.add_heading(text, level=level)


def bullet(doc, text, *, numbered=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.15)
    p.paragraph_format.first_line_indent = Cm(-0.45)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.12
    mark = f"{numbered}.  " if numbered else "–  "
    run = p.add_run(mark + text)
    set_run_font(run, SERIF, 12)
    return p


def caption_paragraph(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.keep_together = True
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    set_run_font(run, SERIF, 10, italic=True, color=MUTED)
    return p


class Paper:
    def __init__(self, doc):
        self.doc = doc
        self.fig = 0
        self.tab = 0

    def figure(self, filename, caption, width=6.45):
        self.fig += 1
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run()
        run.add_picture(str(FIG / filename), width=Inches(width))
        caption_paragraph(self.doc, f"Figura {self.fig}. {caption}")

    def table(self, headers, rows, widths, caption):
        self.tab += 1
        cap = self.doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.paragraph_format.space_before = Pt(8)
        cap.paragraph_format.space_after = Pt(3)
        cap.paragraph_format.keep_with_next = True
        run = cap.add_run(f"Tabla {self.tab}. {caption}")
        set_run_font(run, SERIF, 10, italic=True, color=MUTED)

        table = self.doc.add_table(rows=1 + len(rows), cols=len(headers))
        set_table_widths(table, widths)
        set_table_borders(table, "D5D0C6", "4")
        for i, header in enumerate(headers):
            cell = table.rows[0].cells[i]
            shade_cell(cell, "0E2744")
            valign(cell, "center")
            set_cell_margins(cell, 50, 50, 70, 70)
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
            cell.paragraphs[0].paragraph_format.space_after = Pt(0)
            cell.paragraphs[0].paragraph_format.space_before = Pt(0)
            r = cell.paragraphs[0].add_run(header)
            set_run_font(r, SANS, 10, bold=True, color=WHITE)
        repeat_header(table.rows[0])
        prevent_row_split(table.rows[0])
        for r_idx, row in enumerate(rows):
            for c_idx, text in enumerate(row):
                cell = table.rows[r_idx + 1].cells[c_idx]
                shade_cell(cell, "FFFFFF" if r_idx % 2 == 0 else "F7F4EE")
                valign(cell, "top")
                set_cell_margins(cell, 46, 46, 70, 70)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.line_spacing = 1.05
                run = p.add_run(text)
                set_run_font(run, SANS, 9.5, color=INK)
            prevent_row_split(table.rows[r_idx + 1])
        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(6)
        spacer.paragraph_format.space_before = Pt(2)
        return table

    def callout(self, label, text):
        table = self.doc.add_table(rows=1, cols=1)
        set_table_widths(table, [6.5])
        set_table_borders(table, "E0C48A", "8")
        cell = table.cell(0, 0)
        shade_cell(cell, "FBF7EF")
        set_cell_margins(cell, 80, 80, 120, 120)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(0)
        r = p.add_run(label)
        set_run_font(r, SANS, 11, bold=True, color=NAVY)
        body = cell.add_paragraph()
        body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        body.paragraph_format.space_after = Pt(0)
        body.paragraph_format.space_before = Pt(2)
        body.paragraph_format.line_spacing = 1.12
        rb = body.add_run(text)
        set_run_font(rb, SERIF, 11)
        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_before = Pt(2)
        spacer.paragraph_format.space_after = Pt(4)

    def code(self, text):
        table = self.doc.add_table(rows=1, cols=1)
        set_table_widths(table, [6.5])
        set_table_borders(table, "E4DFD4", "4")
        cell = table.cell(0, 0)
        shade_cell(cell, "F6F3EC")
        set_cell_margins(cell, 70, 70, 110, 110)
        lines = text.strip("\n").split("\n")
        first = True
        for line in lines:
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            run = p.add_run(line if line else " ")
            set_run_font(run, MONO, 9.5, color=INK)
        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_before = Pt(1)
        spacer.paragraph_format.space_after = Pt(4)

    def reference(self, text):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Cm(1.25)
        p.paragraph_format.first_line_indent = Cm(-1.25)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.08
        run = p.add_run(text)
        set_run_font(run, SERIF, 11)
        return p


def cover(doc, investigacion, titulo, subtitulo):
    if doc.paragraphs and not doc.paragraphs[0].text:
        element = doc.paragraphs[0]._element
        element.getparent().remove(element)
    P(doc, "INSTITUTO TECNOLÓGICO DE MORELIA", size=16, bold=True, align="center",
      before=28, after=2, indent=0, font=SANS, color=NAVY)
    line = P(doc, "Departamento de Sistemas y Computación", size=12, align="center",
             before=2, after=0, indent=0, font=SANS, color=NAVY)
    paragraph_border(line, "A67C2D", "12")
    P(doc, "Ingeniería en Sistemas Computacionales", size=12, align="center",
      before=6, after=0, indent=0, font=SANS)
    P(doc, "Taller de sistemas operativos", size=13, italic=True, align="center",
      before=22, after=2, indent=0, font=SANS, color=MUTED)
    P(doc, investigacion, size=12, bold=True, align="center",
      before=26, after=6, indent=0, font=SANS, color=GOLD)
    P(doc, titulo, size=22, bold=True, align="center",
      before=2, after=6, indent=0, font=SANS, color=NAVY)
    P(doc, subtitulo, size=12, italic=True, align="center",
      before=0, after=8, indent=0, font=SERIF, color=INK)
    P(doc, "Investigación documental", size=11, align="center",
      before=0, after=0, indent=0, font=SANS, color=MUTED)

    P(doc, "Presenta", size=11, align="center", before=36, after=0, indent=0, font=SANS, color=MUTED)
    P(doc, "Cristian Muñoz Hinojosa", size=14, bold=True, align="center",
      before=2, after=0, indent=0, font=SANS, color=NAVY)
    P(doc, "Número de control  23121073", size=12, align="center",
      before=2, after=0, indent=0, font=SERIF)

    P(doc, "Docente", size=11, align="center", before=18, after=0, indent=0, font=SANS, color=MUTED)
    P(doc, "Brenda Guadalupe Gonzalez", size=13, bold=True, align="center",
      before=2, after=0, indent=0, font=SANS)

    P(doc, "Morelia, Michoacán", size=12, align="center",
      before=28, after=0, indent=0, font=SERIF)
    P(doc, "20 de noviembre de 2026", size=12, align="center",
      before=0, after=0, indent=0, font=SERIF)


def contenido(doc, entries):
    H(doc, "Contenido", 1)
    P(
        doc,
        "El número de página va en el pie. Este contenido enumera las secciones para localizarlas.",
        size=11, italic=True, align="left", indent=0, after=8, color=MUTED,
    )
    for entry in entries:
        level, text = entry
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        p.paragraph_format.left_indent = Cm(0 if level == 1 else 0.6)
        run = p.add_run(text)
        set_run_font(run, SANS, 12, bold=(level == 1), color=NAVY if level == 1 else INK)
