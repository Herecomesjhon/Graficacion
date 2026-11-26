#!/usr/bin/env python3
"""Llena la práctica de Lenguajes de interfaz conservando la portada del libro."""

import shutil
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/ubuntu/.cursor/projects/agent-repos-Graficacion/uploads/Practica_4_f9ed.docx")
OUT = ROOT / "Unidad4-Practica1-Microchip-CristianMunoz-ZabdiPerez.docx"
FIG = ROOT / "figuras"
FIG.mkdir(parents=True, exist_ok=True)

SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

BROWN = (78, 42, 32)
WINE = (164, 6, 62)
INK = (22, 23, 24)
CREAM = (247, 243, 239)
WHITE = (255, 255, 255)
LINE = (214, 196, 188)


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else f"{cur} {word}"
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def rounded(draw, box, r, fill, outline=None, width=2):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def fig_conexion():
    w, h = 1700, 860
    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    d.text((40, 24), "Una línea por pin, todas cierran en GND", font=F(SANSB, 36), fill=BROWN)
    d.line((40, 78, 1660, 78), fill=WINE, width=4)

    rows = [
        ("A0", "PC0", "entrada", "Botón 1", False),
        ("D1", "PD1", "entrada", "Botón 2", False),
        ("D10", "PB2", "salida", "LED", True),
        ("D11", "PB3", "salida", "LED", True),
        ("D12", "PB4", "salida", "LED", True),
    ]
    y = 120
    for pin, reg, kind, part, is_led in rows:
        rounded(d, (40, y, 1660, y + 130), 18, CREAM, LINE, 2)
        d.rectangle((40, y, 250, y + 130), fill=WINE)
        d.text((145, y + 36), pin, font=F(SANSB, 36), fill=WHITE, anchor="ma")
        d.text((145, y + 82), reg, font=F(SANS, 22), fill=WHITE, anchor="ma")
        d.line((250, y + 65, 430, y + 65), fill=BROWN, width=4)
        if is_led:
            d.rectangle((430, y + 38, 620, y + 92), outline=INK, width=3)
            d.text((525, y + 50), "330 Ω", font=F(SANSB, 26), fill=INK, anchor="ma")
            d.line((620, y + 65, 760, y + 65), fill=BROWN, width=4)
            d.ellipse((760, y + 28, 850, y + 102), outline=WINE, width=4)
            d.polygon([(792, y + 48), (818, y + 65), (792, y + 82)], fill=WINE)
            d.text((805, y + 108), "LED", font=F(SANS, 18), fill=WINE, anchor="ma")
            d.line((850, y + 65, 1040, y + 65), fill=BROWN, width=4)
            end = 1040
        else:
            d.rectangle((430, y + 34, 700, y + 96), outline=INK, width=3)
            d.text((565, y + 50), part, font=F(SANSB, 26), fill=INK, anchor="ma")
            d.line((700, y + 65, 1040, y + 65), fill=BROWN, width=4)
            end = 1040
        d.rectangle((end, y + 40, end + 150, y + 90), fill=INK)
        d.text((end + 75, y + 52), "GND", font=F(SANSB, 26), fill=WHITE, anchor="ma")
        d.text((1280, y + 36), kind, font=F(SANSB, 26), fill=WINE)
        note = "pull-up interno, suelto = 1" if not is_led else "SBI lo pone en 1 y enciende"
        d.text((1280, y + 74), note, font=F(SANS, 22), fill=BROWN)
        y += 146
    img.save(FIG / "01-conexion.png", "PNG")


def fig_flujo():
    w, h = 1700, 1180
    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    d.text((48, 28), "El programa no sale de este ciclo", font=F(SANSB, 40), fill=BROWN)
    d.line((48, 86, 1652, 86), fill=WINE, width=4)

    def box(xy, title, body, fill, fg=WHITE):
        x, y, x2, y2 = xy
        rounded(d, xy, 16, fill)
        d.text((x + 24, y + 16), title, font=F(SANSB, 26), fill=fg)
        yy = y + 56
        for line in wrap(d, body, F(SANS, 22), x2 - x - 48):
            d.text((x + 24, yy), line, font=F(SANS, 22), fill=fg)
            yy += 28

    box((80, 130, 620, 280), "Config", "DDRB en salida para D10, D11 y D12. Pull-up en A0 y en D1.", INK)
    d.line((350, 280, 350, 330), fill=WINE, width=4)
    box((80, 330, 620, 500), "Botón 1  ·  A0", "Lee PINC y se queda con el bit 0. Si el bit vale 0, el botón está apretado.", WINE)
    d.line((620, 400, 760, 400), fill=BROWN, width=4)
    d.text((640, 360), "A0 = 0", font=F(SANSB, 22), fill=WINE)
    box((760, 320, 1580, 490), "LED_ON", "SBI enciende PB2, PB3 y PB4. Los tres LEDs pasan a 1 y el programa vuelve a Botón 1.", (120, 48, 62))

    d.line((350, 500, 350, 560), fill=BROWN, width=4)
    d.text((366, 512), "A0 = 1, suelto", font=F(SANS, 22), fill=BROWN)
    box((80, 560, 620, 730), "Botón 2  ·  D1", "Lee PIND y se queda con el bit 1. Suelto vale 1. Apretado vale 0.", INK)
    d.line((620, 630, 760, 630), fill=BROWN, width=4)
    d.text((640, 590), "D1 = 0", font=F(SANSB, 22), fill=WINE)
    box((760, 560, 1580, 730), "LED_OFF", "CBI apaga los mismos tres pines. Después también regresa a Botón 1.", (90, 70, 64))

    rounded(d, (80, 800, 1580, 1080), 18, CREAM, WINE, 3)
    d.text((110, 828), "Si los dos botones están sueltos", font=F(SANSB, 30), fill=WINE)
    yy = 890
    for line in wrap(
        d,
        "Botón 2 encuentra D1 en 1 y salta otra vez a Botón 1. Los LEDs no se tocan: se quedan como la última vez que alguien apretó un botón. Si los dos se aprietan juntos, gana el botón 1, porque el programa enciende y ni siquiera llega a leer D1.",
        F(SANS, 26),
        1420,
    ):
        d.text((110, yy), line, font=F(SANS, 26), fill=BROWN)
        yy += 38
    img.save(FIG / "02-flujo.png", "PNG")


def fig_bits():
    w, h = 1700, 420
    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    d.text((48, 24), "DDRB  =  0b00011100   ·   28 en decimal", font=F(SANSB, 36), fill=BROWN)
    labels = ["PB7", "PB6", "PB5", "PB4", "PB3", "PB2", "PB1", "PB0"]
    bits = list("00011100")
    roles = ["entrada", "entrada", "entrada", "D12 LED", "D11 LED", "D10 LED", "entrada", "entrada"]
    x0 = 70
    for i, (lab, bit, role) in enumerate(zip(labels, bits, roles)):
        x = x0 + i * 200
        fill = WINE if bit == "1" else CREAM
        fg = WHITE if bit == "1" else BROWN
        rounded(d, (x, 110, x + 180, 360), 16, fill, WINE if bit == "1" else LINE, 3)
        d.text((x + 90, 140), lab, font=F(SANSB, 28), fill=fg, anchor="ma")
        d.text((x + 90, 200), bit, font=F(SANSB, 54), fill=fg, anchor="ma")
        d.text((x + 90, 280), role, font=F(SANS, 20), fill=fg, anchor="ma")
    img.save(FIG / "03-bits.png", "PNG")


def shade(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")


def set_run_font(run, name, size, bold=False, color=None):
    run.bold = bold
    run.font.name = name
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = RGBColor(*color)
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), name)


def add_heading_book(doc, text):
    p = doc.add_paragraph(text, style="heading 1")
    pPr = p._p.get_or_add_pPr()
    numPr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), "0")
    numId = OxmlElement("w:numId")
    numId.set(qn("w:val"), "5")
    numPr.append(ilvl)
    numPr.append(numId)
    pPr.append(numPr)
    return p


def add_body(doc, text):
    p = doc.add_paragraph(text, style="Normal")
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.space_before = Pt(2)
    return p


def add_picture(doc, path, width=6.45):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.add_run().add_picture(str(path), width=Inches(width))
    return p


def add_caption(doc, text):
    p = doc.add_paragraph(text, style="Normal")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(12)
    for run in p.runs:
        run.italic = True
        run.font.size = Pt(11)
    return p


def add_code(doc, text):
    table = doc.add_table(rows=1, cols=1)
    table.autofit = True
    cell = table.cell(0, 0)
    shade(cell, "161718")
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for edge, val in (("top", "80"), ("left", "120"), ("bottom", "80"), ("right", "120")):
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:w"), val)
        node.set(qn("w:type"), "dxa")
        mar.append(node)
    tcPr.append(mar)
    lines = text.strip("\n").split("\n")
    for i, line in enumerate(lines):
        p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(line if line else " ")
        set_run_font(run, "Consolas", 9, color=(255, 255, 255))
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(6)


def set_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "E6D5CC")
        borders.append(el)
    tblPr.append(borders)


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    set_table_borders(table)
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        shade(cell, "4E2A20")
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(header)
        set_run_font(run, "Calibri", 11, bold=True, color=(255, 255, 255))
    for r, row in enumerate(rows):
        for c, text in enumerate(row):
            cell = table.rows[r + 1].cells[c]
            if r % 2:
                shade(cell, "F7F3EF")
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(text)
            set_run_font(run, "Calibri", 11, color=BROWN)
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(8)
    return table


CODE = r'''.include "m328pdef.inc"
; Configuracion de pines
Config:
        LDI R16, 0b00011100
        OUT DDRB, R16

        LDI R17, 0b00000000
        OUT DDRC, R17

        LDI R18, 0b00000000
        OUT DDRD, R18

        SBI PORTC, 0        ; boton 1, pull-up en A0
        SBI PORTD, 1        ; boton 2, pull-up en D1

BOTON1:
        LDI R21, 0b00000001
        NOP
        NOP
        IN  R20, PINC
        AND R21, R20
        CPI R21, 0b00000001
        BRNE LED_ON

BOTON2:
        LDI R21, 0b00000010
        NOP
        NOP
        IN  R20, PIND
        AND R21, R20
        CPI R21, 0b00000010
        BREQ BOTON1
        BRNE LED_OFF

LED_ON:
        SBI PORTB, 3        ; D11
        SBI PORTB, 4        ; D12
        SBI PORTB, 2        ; D10
        JMP BOTON1

LED_OFF:
        CBI PORTB, 3
        CBI PORTB, 4
        CBI PORTB, 2
        JMP BOTON1
'''


def preparar_fotos():
    from PIL import ImageOps

    origen = {
        "04-montaje.jpg": "/home/ubuntu/.cursor/projects/agent-repos-Graficacion/assets/d33297b4-9f16-445c-b85c-ca38e44aa45d.jpg",
        "05-nano.jpg": "/home/ubuntu/.cursor/projects/agent-repos-Graficacion/assets/1f4486b2-43e9-4a26-99be-aa1e7d901d6f.jpg",
        "06-nano-boton.jpg": "/home/ubuntu/.cursor/projects/agent-repos-Graficacion/assets/bc9f893d-c93b-4d96-bb86-051e8ed5e691.jpg",
        "07-leds-boton.jpg": "/home/ubuntu/.cursor/projects/agent-repos-Graficacion/assets/9c6391bf-883f-46f9-b376-1981016a4ce1.jpg",
        "08-leds.jpg": "/home/ubuntu/.cursor/projects/agent-repos-Graficacion/assets/bae8dc80-881e-4521-af04-9aaf11ab9ed9.jpg",
    }
    for nombre, ruta in origen.items():
        im = ImageOps.exif_transpose(Image.open(ruta))
        im = im.convert("RGB")
        im.thumbnail((1600, 1600))
        im.save(FIG / nombre, "JPEG", quality=85, optimize=True)


def main():
    fig_conexion()
    fig_flujo()
    fig_bits()
    preparar_fotos()
    shutil.copy(TEMPLATE, OUT)
    doc = Document(OUT)
    doc.core_properties.author = "Cristian Muñoz Hinojosa y Zabdi Emmanuel Pérez Peguero"
    doc.core_properties.title = "Unidad 4 Práctica 1. Microchip, Arduino Nano y LEDs"
    doc.core_properties.subject = "Lenguajes de interfaz. Tecnológico de Morelia. 26 de noviembre de 2026."
    doc.core_properties.category = "Lenguajes de interfaz"

    add_body(
        doc,
        "En esta práctica el ATmega328P de un Arduino Nano enciende y apaga tres LEDs con dos botones armados en una protoboard. El programa está escrito en ensamblador AVR. La librería m328pdef.inc solo entrega los nombres de los registros del microcontrolador: DDRB, PORTC, PINC y los demás. La portada de este documento corresponde a Lenguajes de interfaz, Unidad 4, Práctica 1, con fecha 26 de noviembre de 2026.",
    )
    add_body(
        doc,
        "Los tres LEDs se mueven juntos. No hay secuencia ni parpadeo. El botón 1 los enciende y el botón 2 los apaga. Mientras ninguno está apretado, el programa sigue leyendo y los LEDs se quedan como estaban.",
    )

    add_heading_book(doc, "Objetivo")
    add_body(
        doc,
        "Configurar los puertos del ATmega328P para leer dos botones por las entradas A0 y D1, y manejar tres LEDs por las salidas D10, D11 y D12. Comprobar en la protoboard que un botón pone las tres salidas en 1 y el otro las regresa a 0.",
    )

    add_heading_book(doc, "Material y conexiones")
    add_body(
        doc,
        "Se usa un Arduino Nano, porque su microcontrolador es el ATmega328P. En la protoboard van tres LEDs, tres resistencias de 330 Ω, dos botones y el cable de tierra común. Cada LED sale del pin del Nano, pasa por su resistencia y termina en GND. Cada botón va entre su pin y GND. La resistencia de pull-up ya la pone el programa, así que el botón no necesita resistencia externa.",
    )
    add_table(
        doc,
        ["En el programa", "Pin del Nano", "En la protoboard"],
        [
            ["PORTB, bits 2, 3 y 4", "D10, D11 y D12", "Los tres LEDs"],
            ["PORTC, bit 0", "A0", "Botón 1, a tierra"],
            ["PORTD, bit 1", "D1", "Botón 2, a tierra"],
        ],
    )
    add_picture(doc, FIG / "01-conexion.png")
    add_caption(doc, "Figura 1. Pines del Nano y el camino de cada botón y de cada LED hasta tierra.")
    add_body(
        doc,
        "D1 en el Nano también es el pin TX del USB. El botón funciona, y mientras está apretado ese pin queda en tierra. Conviene no usar el monitor serie en el mismo momento de la prueba.",
    )

    add_heading_book(doc, "Configuración de los puertos")
    add_body(
        doc,
        "DDR dice la dirección del pin. Un 1 lo deja como salida y un 0 lo deja como entrada. La primera carga escribe 0b00011100 en DDRB. Ese número es 28 en decimal, y solo levanta los bits 2, 3 y 4: PB2, PB3 y PB4, que en el Nano son D10, D11 y D12. DDRC y DDRD se escriben en cero, así que A0 y D1 quedan como entradas.",
    )
    add_picture(doc, FIG / "03-bits.png", width=6.5)
    add_caption(doc, "Figura 2. Los tres unos de DDRB son las únicas salidas. El resto del puerto B se queda como entrada.")
    add_body(
        doc,
        "SBI PORTC,0 y SBI PORTD,1 encienden el pull-up de cada botón. Como el pin es entrada, escribir 1 en PORT no manda un voltaje hacia afuera: conecta la resistencia interna a 5 V. Suelto, el pin lee 1. Apretado, el botón lo pone en 0.",
    )

    add_heading_book(doc, "Cómo se leen los botones")
    add_body(
        doc,
        "Botón 1 carga en R21 la máscara 0b00000001, espera dos instrucciones NOP y lee PINC completo en R20. AND R21, R20 deja en R21 únicamente el bit 0. CPI compara ese resultado con 1. BRNE salta a LED_ON cuando no son iguales, es decir, cuando A0 está en 0 y el botón está apretado. Si A0 sigue en 1, no hay salto y el programa sigue con el botón 2.",
    )
    add_body(
        doc,
        "Botón 2 repite la misma idea con la máscara 0b00000010 y con PIND, para mirar solo el bit 1. Si ese bit sigue en 1, BREQ regresa a BOTON1 y los LEDs no cambian. Si el bit está en 0, BRNE entra a LED_OFF. De esas dos comparaciones siempre se cumple una, así que el programa no se queda detenido entre los dos botones.",
    )
    add_body(
        doc,
        "Cada NOP gasta un ciclo de reloj. A 16 MHz, dos NOP son 125 nanosegundos. Alcanza como pausa mínima entre la máscara y la lectura. No alcanza como antirrebote: si el contacto del botón rebota, la lectura puede entrar y salir varias veces en el mismo clic. Como los tres LEDs hacen lo mismo, a simple vista se nota poco.",
    )

    add_heading_book(doc, "Encendido y apagado")
    add_body(
        doc,
        "LED_ON ejecuta tres SBI. Cada uno pone en 1 un solo bit de PORTB sin tocar los demás: primero el bit 3 (D11), luego el bit 4 (D12) y al final el bit 2 (D10). LED_OFF hace lo contrario con CBI y apaga los mismos tres pines. Las dos rutinas terminan con JMP BOTON1, de modo que la lectura vuelve a empezar.",
    )
    add_picture(doc, FIG / "02-flujo.png")
    add_caption(doc, "Figura 3. Recorrido del programa. El botón 1 se revisa antes y, si está apretado, el botón 2 no se lee.")

    add_heading_book(doc, "Código de la práctica")
    add_body(
        doc,
        "El listado de abajo es el programa de la protoboard. Se conservan las mismas instrucciones. Los comentarios nombran el pin del Nano que corresponde a cada una.",
    )
    add_code(doc, CODE)

    add_heading_book(doc, "Lo que se observa")
    add_table(
        doc,
        ["Botones", "Lectura", "Salto", "LEDs D10, D11 y D12"],
        [
            ["Ninguno", "A0 = 1 y D1 = 1", "Regresa a Botón 1", "Se quedan igual"],
            ["Solo botón 1", "A0 = 0", "LED_ON", "Encendidos"],
            ["Solo botón 2", "D1 = 0", "LED_OFF", "Apagados"],
            ["Los dos", "A0 = 0", "LED_ON", "Encendidos. D1 no se lee"],
        ],
    )
    add_body(
        doc,
        "La prueba en la protoboard consiste en soltar los dos botones, apretar el botón 1 y ver los tres LEDs encenderse juntos, y después apretar el botón 2 y verlos apagarse juntos. Si se mantienen los dos apretados, siguen encendidos, porque la revisión de A0 ocurre primero. Las fotos de abajo son de ese mismo armado: el Nano alimentado por USB, las tres resistencias, los dos botones y los LEDs rojo, amarillo y azul encendidos al mismo tiempo.",
    )
    add_picture(doc, FIG / "04-montaje.jpg", width=5.6)
    add_caption(doc, "Figura 4. Protoboard completa. El Nano está arriba, los LEDs y las resistencias al centro, y los dos botones a los lados.")
    add_picture(doc, FIG / "05-nano.jpg", width=5.6)
    add_caption(doc, "Figura 5. Acercamiento del Arduino Nano. Se ve el ATmega328P, el conector USB y el LED de encendido de la placa.")
    add_picture(doc, FIG / "06-nano-boton.jpg", width=5.6)
    add_caption(doc, "Figura 6. El Nano con un botón al lado y los cables que salen hacia los LEDs. La placa está alimentada.")
    add_picture(doc, FIG / "07-leds-boton.jpg", width=5.6)
    add_caption(doc, "Figura 7. Los tres LEDs encendidos juntos mientras se aprieta un botón. Cada LED pasa por su resistencia.")
    add_picture(doc, FIG / "08-leds.jpg", width=5.6)
    add_caption(doc, "Figura 8. Otra toma del mismo resultado: rojo, azul y amarillo encendidos a la vez, con el botón y las resistencias a la vista.")

    add_heading_book(doc, "Conclusión")
    add_body(
        doc,
        "Con DDR se elige qué pines salen y cuáles entran. Con PORT, en una entrada, se activa el pull-up que deja al botón en 1 cuando está suelto. Con PIN se lee el puerto, y una máscara con AND separa el bit del botón. SBI y CBI alcanzan para encender o apagar un LED sin reescribir el puerto completo. En esta práctica esos cinco registros bastan para que dos botones manden sobre tres LEDs del Arduino Nano.",
    )

    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
