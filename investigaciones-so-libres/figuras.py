#!/usr/bin/env python3
"""Figuras originales para las dos investigaciones de sistemas operativos libres."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "figuras"
OUT.mkdir(parents=True, exist_ok=True)

SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANSI = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"

NAVY = (14, 39, 68)
TEAL = (31, 106, 100)
GOLD = (140, 102, 32)
INK = (28, 28, 28)
MUTED = (90, 84, 74)
RED = (142, 59, 59)
BLUE = (44, 95, 138)
LINE = (214, 208, 196)
WHITE = (255, 255, 255)
CREAM = (247, 244, 238)
PALE_TEAL = (230, 241, 238)
PALE_GOLD = (247, 240, 224)
PALE_RED = (248, 236, 234)
PALE_BLUE = (232, 239, 246)
PALE_NAVY = (236, 240, 245)

font_manager.fontManager.addfont(SANS)
font_manager.fontManager.addfont(SANSB)
plt.rcParams["font.family"] = "Liberation Sans"
plt.rcParams["axes.unicode_minus"] = False


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else f"{cur} {word}"
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def paragraph(draw, xy, text, fnt, fill, max_w, leading):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def new_canvas(w, h, bg=WHITE):
    img = Image.new("RGB", (w, h), bg)
    return img, ImageDraw.Draw(img)


def footer(draw, w, h, text, y=None):
    fnt = F(SANSI, 28)
    y = h - 64 if y is None else y
    draw.line((48, y - 14, w - 48, y - 14), fill=LINE, width=2)
    draw.text((48, y), text, font=fnt, fill=MUTED)


def title(draw, text, subtitle=None):
    draw.text((48, 36), text, font=F(SANSB, 40), fill=NAVY)
    y = 92
    if subtitle:
        y = paragraph(draw, (48, 92), subtitle, F(SANS, 24), MUTED, 1800, 32)
        y += 8
    return y


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", optimize=True)
    print(path, img.size)


def fig_adopcion():
    labels = [
        "Supercomputadoras TOP500\n(noviembre de 2025)",
        "Nodos Linux en clústeres Kubernetes\nde producción (CNCF, 2025)",
        "Sesiones móviles: Android,\nnúcleo Linux (julio de 2026)",
        "Sitios web con sistema identificado\n(W3Techs, 17 de agosto de 2026)",
        "Sesiones de escritorio: Linux\n(StatCounter, julio de 2026)",
        "Equipos en Steam: Linux\n(julio de 2026)",
    ]
    values = [100, 96, 68.36, 62.1, 7.53, 4.01]
    colors = ["#0E2744", "#1F6A64", "#2C5F8A", "#3E7C72", "#A67C2D", "#8E3B3B"]
    fig, ax = plt.subplots(figsize=(6.55, 4.15), dpi=200)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    positions = list(range(len(labels) - 1, -1, -1))
    bars = ax.barh(positions, values, color=colors, height=0.64, zorder=3)
    ax.set_yticks(positions)
    ax.set_yticklabels(labels, fontsize=8, color="#1C1C1C")
    ax.set_xlim(0, 128)
    ax.set_xlabel("Porcentaje dentro de su propio universo de medición", fontsize=8.5, color="#1C1C1C")
    for bar, value in zip(bars, values):
        label = (f"{value:.0f} %" if value >= 10 else f"{value:.1f} %").replace(".", ",")
        ax.text(
            value + 1.4,
            bar.get_y() + bar.get_height() / 2,
            label,
            va="center",
            ha="left",
            fontsize=8.5,
            color="#0E2744",
            fontweight="bold",
        )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#C8C2B4")
    ax.tick_params(axis="y", length=0, pad=4, labelsize=8)
    ax.tick_params(axis="x", colors="#5A544C", labelsize=8)
    ax.grid(axis="x", color="#E7E1D6", zorder=0)
    ax.set_axisbelow(True)
    fig.suptitle(
        "El mismo núcleo no pesa igual en cada sector",
        fontsize=12,
        color="#0E2744",
        fontweight="bold",
        x=0.02,
        ha="left",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    path = OUT / "01-adopcion-por-sector.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close()
    print(path)


def fig_familias():
    img, d = new_canvas(1900, 1040)
    y = title(
        d,
        "Tres familias que suelen meterse en la misma frase",
        "Un sistema puede llevar núcleo Linux y, aun así, no ser un sistema operativo libre completo.",
    )
    cards = [
        (
            PALE_TEAL,
            TEAL,
            "GNU/Linux",
            "Núcleo Linux más herramientas GNU y el resto del espacio de usuario.",
            [
                "Debian, Ubuntu, Linux Mint",
                "Fedora, RHEL, Rocky, AlmaLinux",
                "openSUSE, Arch, CachyOS",
                "Alpine Linux",
            ],
            "La licencia del núcleo es GPL-2.0. Cada distribución agrega cientos de programas con licencias distintas.",
        ),
        (
            PALE_NAVY,
            NAVY,
            "BSD",
            "Núcleo, utilidades y compilador se distribuyen juntos, con licencia permisiva.",
            [
                "FreeBSD",
                "OpenBSD",
                "NetBSD",
            ],
            "FreeBSD es el sistema de los servidores Open Connect de Netflix. La licencia BSD no obliga a publicar los cambios.",
        ),
        (
            PALE_GOLD,
            GOLD,
            "Derivados de uso masivo",
            "Parten de un núcleo libre y le suman capas que ya no lo son.",
            [
                "Android (núcleo Linux)",
                "ChromeOS",
                "Tizen, de Samsung",
                "SteamOS, de Valve",
            ],
            "Dominan teléfonos, algunos escritorios y consolas. No cumplen, como producto completo, las cuatro libertades.",
        ),
    ]
    gap = 28
    left = 48
    width = (1900 - 96 - 2 * gap) // 3
    top = y + 18
    height = 760
    for i, (bg, accent, name, lead, items, note) in enumerate(cards):
        x = left + i * (width + gap)
        rounded(d, (x, top, x + width, top + height), 22, bg, accent, 3)
        d.rectangle((x, top, x + 12, top + height), fill=accent)
        d.text((x + 36, top + 28), name, font=F(SANSB, 34), fill=accent)
        yy = paragraph(d, (x + 36, top + 88), lead, F(SANS, 24), INK, width - 72, 32)
        yy += 18
        for item in items:
            d.ellipse((x + 40, yy + 8, x + 54, yy + 22), fill=accent)
            d.text((x + 68, yy), item, font=F(SANS, 24), fill=INK)
            yy += 42
        yy += 10
        d.line((x + 36, yy, x + width - 36, yy), fill=accent, width=2)
        paragraph(d, (x + 36, yy + 16), note, F(SANS, 22), MUTED, width - 72, 30)
    footer(
        d,
        1900,
        1040,
        "Elaboración propia a partir de las licencias públicas de cada proyecto y de la definición de software libre de la FSF.",
    )
    save(img, "02-familias.png")


def fig_gendbuntu():
    img, d = new_canvas(1900, 820)
    title(d, "GendBuntu: de la suite de oficina al sistema completo")
    milestones = [
        ("2004", "OpenOffice.org", "Sustituye a Office en el parque de la Gendarmería."),
        ("2006", "Firefox y Thunderbird", "El navegador y el correo cambian antes que el sistema."),
        ("2008", "Nace GendBuntu", "Ubuntu adaptado. Unos 5 000 equipos de prueba."),
        ("2014", "65 000 equipos", "Cierra la gran migración desde Windows XP."),
        ("2019", "Cerca del 90 %", "Unas 77 000 estaciones ya trabajan con GendBuntu."),
        ("2024", "103 164 equipos", "97 % del parque, en junio. En diciembre pasa a 24.04."),
    ]
    y_line = 430
    d.line((90, y_line, 1810, y_line), fill=NAVY, width=6)
    for i, (year, name, detail) in enumerate(milestones):
        x = 120 + i * 295
        above = i % 2 == 0
        d.ellipse((x - 14, y_line - 14, x + 14, y_line + 14), fill=GOLD, outline=NAVY, width=3)
        if above:
            box = (x - 120, 180, x + 130, 360)
            text_y = 198
            anchor_line = 360
        else:
            box = (x - 120, 500, x + 130, 700)
            text_y = 518
            anchor_line = 500
        rounded(d, box, 16, CREAM, LINE, 2)
        d.text((x, text_y), year, font=F(SANSB, 28), fill=GOLD, anchor="ma")
        d.text((x, text_y + 40), name, font=F(SANSB, 22), fill=NAVY, anchor="ma")
        paragraph(d, (x - 100, text_y + 80), detail, F(SANS, 18), INK, 200, 24)
        d.line((x, y_line + (16 if not above else -16), x, anchor_line), fill=LINE, width=2)
    footer(
        d,
        1900,
        820,
        "Cifras de la cronología pública del proyecto GendBuntu. El 97 % corresponde a junio de 2024.",
    )
    save(img, "03-gendbuntu.png")


def fig_netflix():
    img, d = new_canvas(1900, 1080)
    y = title(
        d,
        "Cómo reparte video el sistema libre de Netflix",
        "Open Connect no transcodifica en el servidor: entrega archivos ya codificados, lo más cerca posible del espectador.",
    )
    # three columns
    cols = [
        (48, PALE_BLUE, BLUE, "1. El cliente", "La aplicación pide la película al plano de control, alojado en Amazon Web Services. Ese plano no envía el video: elige un aparato cercano."),
        (660, PALE_GOLD, GOLD, "2. La red del ISP", "El aparato vive dentro de la red del proveedor de internet, o en un punto de intercambio. El video recorre pocos saltos."),
        (1272, PALE_TEAL, TEAL, "3. El aparato", "Hardware de servidor común. El software de base es libre y el equipo de Netflix devuelve mejoras a FreeBSD."),
    ]
    for x, bg, accent, head, body in cols:
        rounded(d, (x, y + 20, x + 580, y + 280), 18, bg, accent, 3)
        d.text((x + 24, y + 40), head, font=F(SANSB, 28), fill=accent)
        paragraph(d, (x + 24, y + 90), body, F(SANS, 22), INK, 530, 30)

    stack_top = y + 340
    d.text((48, stack_top), "Dentro de un Open Connect Appliance", font=F(SANSB, 28), fill=NAVY)
    layers = [
        (TEAL, WHITE, "FreeBSD-CURRENT", "Sistema operativo. Lo eligieron por la licencia BSD y se quedaron por el rendimiento."),
        (NAVY, WHITE, "NGINX", "Entrega el audio y el video por HTTP. Licencia BSD de dos cláusulas."),
        (BLUE, WHITE, "BIRD", "Demonio de rutas BGP: informa qué redes conviene servir desde ese aparato."),
        (GOLD, WHITE, "Discos y NIC comunes", "Sin un sistema de almacenamiento especial: el sistema operativo hace el trabajo fino."),
    ]
    yy = stack_top + 52
    for bg, fg, name, desc in layers:
        rounded(d, (48, yy, 1852, yy + 100), 14, bg)
        d.text((72, yy + 16), name, font=F(SANSB, 26), fill=fg)
        d.text((72, yy + 54), desc, font=F(SANS, 22), fill=(255, 255, 255))
        yy += 114
    footer(
        d,
        1900,
        1080,
        "Elaboración propia según Netflix Open Connect y los informes técnicos del equipo de FreeBSD en Netflix.",
    )
    save(img, "04-netflix.png")


def fig_top500():
    img, d = new_canvas(1900, 980)
    title(
        d,
        "Cuatro sistemas en la frontera del TOP500",
        "Lista de noviembre de 2025. Los cuatro alcanzan o superan 1 000 PFlop/s y todos pertenecen a la familia Linux.",
    )
    cards = [
        ("1", "El Capitan", "Lawrence Livermore, EE. UU.", "1 809 PFlop/s", "TOSS", "Derivado de la familia Red Hat, usado por los laboratorios del Departamento de Energía."),
        ("2", "Frontier", "Oak Ridge, EE. UU.", "1 353 PFlop/s", "HPE Cray OS", "Sistema Linux de la plataforma Cray EX. Fue la primera máquina exaescala en operar."),
        ("3", "Aurora", "Argonne, EE. UU.", "1 012 PFlop/s", "Familia Linux", "La ficha pública no fija una sola distribución comercial; entra en el 100 % Linux de la lista."),
        ("4", "JUPITER Booster", "Jülich, Alemania", "1 000 PFlop/s", "RHEL", "Primera máquina exaescala europea de la lista. El sistema publicado es Red Hat Enterprise Linux."),
    ]
    for i, (rank, name, site, perf, os_name, note) in enumerate(cards):
        x = 48 + (i % 2) * 930
        y = 200 + (i // 2) * 340
        rounded(d, (x, y, x + 890, y + 310), 18, CREAM, LINE, 2)
        d.ellipse((x + 24, y + 24, x + 110, y + 110), fill=NAVY)
        d.text((x + 67, y + 48), rank, font=F(SANSB, 40), fill=WHITE, anchor="ma")
        d.text((x + 130, y + 28), name, font=F(SANSB, 32), fill=NAVY)
        d.text((x + 130, y + 74), site, font=F(SANS, 22), fill=MUTED)
        d.text((x + 28, y + 140), perf, font=F(SANSB, 28), fill=GOLD)
        rounded(d, (x + 280, y + 138, x + 560, y + 178), 12, PALE_TEAL, TEAL, 2)
        d.text((x + 300, y + 144), os_name, font=F(SANSB, 20), fill=TEAL)
        paragraph(d, (x + 28, y + 200), note, F(SANS, 22), INK, 830, 30)
    footer(d, 1900, 980, "Fuente: TOP500, lista de noviembre de 2025. Rmax publicado, en PFlop/s.")
    save(img, "05-top500.png")


def fig_motivo_limite():
    img, d = new_canvas(1900, 980)
    title(d, "Cinco motivos reales, y el límite de cada uno")
    rows = [
        ("Costo", "No hay licencia por equipo en Debian, Ubuntu de comunidad o FreeBSD.", "El soporte empresarial de RHEL, SUSE o Ubuntu Pro sí se paga."),
        ("Control", "La organización puede parchar, auditar y adaptar el sistema.", "Hace falta gente propia o un proveedor. Sin eso, el control es teórico."),
        ("Seguridad", "El código se puede inspeccionar y los parches no dependen de un solo calendario comercial.", "Poder leer el código no significa haberlo leído. La auditoría es trabajo."),
        ("Escala", "En servidores, nube y supercomputadoras es la opción habitual.", "En el escritorio de oficina sigue siendo minoría, y ahí fallan muchas migraciones."),
        ("Soberanía", "Un Estado reduce la dependencia de un fabricante extranjero.", "Los programas de trabajo especializados pueden no tener equivalente libre."),
    ]
    y = 150
    # header
    d.rectangle((48, y, 1852, y + 48), fill=NAVY)
    d.text((70, y + 10), "Motivo", font=F(SANSB, 22), fill=WHITE)
    d.text((360, y + 10), "Lo que sí ocurre", font=F(SANSB, 22), fill=WHITE)
    d.text((1120, y + 10), "El límite", font=F(SANSB, 22), fill=WHITE)
    y += 48
    for i, (motivo, si, limite) in enumerate(rows):
        bg = WHITE if i % 2 == 0 else CREAM
        d.rectangle((48, y, 1852, y + 130), fill=bg, outline=LINE, width=1)
        d.text((70, y + 46), motivo, font=F(SANSB, 24), fill=NAVY)
        paragraph(d, (360, y + 28), si, F(SANS, 22), INK, 720, 30)
        paragraph(d, (1120, y + 28), limite, F(SANS, 22), INK, 700, 30)
        y += 130
    footer(d, 1900, 980, "Elaboración propia. Sirve para leer los casos de este trabajo: ninguno es solo un ahorro de licencias.")
    save(img, "06-motivo-limite.png")


def fig_libertades():
    img, d = new_canvas(1900, 1100)
    title(
        d,
        "Las cuatro libertades, numeradas desde cero",
        "Definición de la Free Software Foundation. Sin la 1 y la 3, el código fuente no es un deseo: es una condición.",
    )
    cards = [
        ("0", TEAL, PALE_TEAL, "Ejecutar", "Usar el programa para cualquier propósito, sin pedir permiso y sin que la licencia distinga un uso «bueno» de otro."),
        ("1", NAVY, PALE_NAVY, "Estudiar y cambiar", "Ver cómo funciona y modificarlo para que haga lo que se necesita. Sin el código fuente esta libertad no existe."),
        ("2", BLUE, PALE_BLUE, "Redistribuir", "Hacer copias y entregarlas a otras personas. Una escuela puede instalar el sistema en todo el laboratorio."),
        ("3", GOLD, PALE_GOLD, "Publicar mejoras", "Distribuir la versión modificada. Así nacen las distribuciones derivadas y los parches que devuelven las empresas."),
    ]
    for i, (num, accent, bg, name, body) in enumerate(cards):
        x = 48 + (i % 2) * 930
        y = 200 + (i // 2) * 390
        rounded(d, (x, y, x + 890, y + 360), 20, bg, accent, 3)
        d.ellipse((x + 28, y + 28, x + 130, y + 130), fill=accent)
        d.text((x + 79, y + 48), num, font=F(SANSB, 48), fill=WHITE, anchor="ma")
        d.text((x + 156, y + 48), name, font=F(SANSB, 36), fill=accent)
        paragraph(d, (x + 36, y + 170), body, F(SANS, 26), INK, 820, 36)
    footer(d, 1900, 1100, "Paráfrasis de la definición de software libre de la Free Software Foundation. La libertad 0 es la base, por eso no empieza en 1.")
    save(img, "07-libertades.png")


def fig_capas():
    img, d = new_canvas(1900, 1180)
    title(
        d,
        "Qué tiene que traer un sistema operativo libre",
        "No basta un núcleo. Cada capa de abajo tiene un requisito propio, técnico y de licencia.",
    )
    layers = [
        (GOLD, "Aplicaciones", "Navegador, oficina, compilador, servidor web. Cada una con su licencia libre."),
        (BLUE, "Inicio y servicios", "systemd, OpenRC o el rc de BSD. Arranque, red, usuarios, registros y actualizaciones."),
        (TEAL, "Bibliotecas y utilidades", "glibc o musl, coreutils, shell. Es el espacio de usuario que vuelve usable al núcleo."),
        (NAVY, "Núcleo", "Linux (GPL-2.0) o un núcleo BSD. Procesos, memoria, archivos, red y controladores."),
        (RED, "Firmware", "El punto delicado: muchos equipos solo arrancan Wi-Fi o video con un blob que no es libre."),
        ((70, 78, 90), "Hardware", "CPU, memoria, disco, red y modo de arranque UEFI. Aquí se miden los requisitos de instalación."),
    ]
    y = 190
    for bg, name, desc in layers:
        rounded(d, (180, y, 1720, y + 130), 16, bg)
        d.text((210, y + 18), name, font=F(SANSB, 30), fill=WHITE)
        d.text((210, y + 68), desc, font=F(SANS, 24), fill=(255, 255, 255))
        y += 148
    footer(d, 1900, 1180, "Elaboración propia. Se lee de abajo hacia arriba: del hardware a las aplicaciones.")
    save(img, "08-capas.png")


def fig_licencias():
    img, d = new_canvas(1900, 1080)
    y0 = title(
        d,
        "Tres maneras legales de ser libre",
        "Todas permiten usar, estudiar, copiar y modificar. Difieren en lo que se puede cerrar después.",
    )
    cards = [
        (
            NAVY,
            PALE_NAVY,
            "Copyleft fuerte",
            "GPL-2.0 y GPL-3.0",
            "Si distribuyes una versión modificada del programa, entregas también el código bajo la misma licencia.",
            ["Núcleo Linux: GPL-2.0", "coreutils y Bash: GPL-3.0", "Obliga a publicar el derivado"],
        ),
        (
            TEAL,
            PALE_TEAL,
            "Copyleft débil",
            "LGPL y MPL",
            "Protege la propia biblioteca o el propio archivo. Otro programa puede enlazarla sin volverse libre.",
            ["glibc: LGPL", "systemd: LGPL-2.1", "Firefox: MPL-2.0, por archivo"],
        ),
        (
            GOLD,
            PALE_GOLD,
            "Permisiva",
            "BSD, MIT, Apache-2.0",
            "Permite meter el código en un producto cerrado. Se conserva el aviso de autor y, en Apache, hay cláusula de patentes.",
            ["FreeBSD y nginx: BSD", "musl: MIT", "Netflix eligió BSD por esto"],
        ),
    ]
    gap = 28
    width = (1900 - 96 - 2 * gap) // 3
    top = y0 + 16
    for i, (accent, bg, name, sub, body, items) in enumerate(cards):
        x = 48 + i * (width + gap)
        rounded(d, (x, top, x + width, top + 760), 20, bg, accent, 3)
        d.rectangle((x, top, x + width, top + 16), fill=accent)
        d.text((x + 28, top + 40), name, font=F(SANSB, 30), fill=accent)
        d.text((x + 28, top + 86), sub, font=F(SANSB, 22), fill=INK)
        yy = paragraph(d, (x + 28, top + 140), body, F(SANS, 22), INK, width - 56, 30)
        yy += 16
        for item in items:
            d.rectangle((x + 28, yy + 8, x + 46, yy + 26), fill=accent)
            yy = paragraph(d, (x + 60, yy), item, F(SANS, 22), INK, width - 100, 30)
            yy += 8
    footer(
        d,
        1900,
        1080,
        "Una distribución no tiene una sola licencia: es un conjunto que debe poder redistribuirse sin contradicciones.",
    )
    save(img, "09-licencias.png")


def fig_fsdg():
    img, d = new_canvas(1900, 1040)
    title(d, "Lista de la FSF para llamar «libre» a una distribución")
    items = [
        ("Código completo", "Quien recibe el sistema puede conseguir el código fuente correspondiente de todo lo que se le entregó."),
        ("Nada privativo de fábrica", "La instalación no trae programas cerrados ni blobs de firmware, aunque sean «solo un controlador»."),
        ("No empujar al usuario", "La documentación y los menús no indican instalar software que no es libre ni activan un repositorio cerrado."),
        ("Documentación libre", "Los manuales que acompañan al sistema también se pueden copiar y modificar."),
        ("Marcas sin candado", "Una marca no puede impedir que alguien publique una versión modificada del mismo sistema."),
        ("Sin DRM contra el usuario", "El sistema no incluye un candado digital (DRM) que le quite al usuario las libertades anteriores."),
    ]
    y = 150
    for i, (name, body) in enumerate(items):
        bg = PALE_TEAL if i % 2 == 0 else CREAM
        rounded(d, (48, y, 1852, y + 120), 14, bg)
        d.ellipse((72, y + 36, 120, y + 84), fill=TEAL)
        d.text((96, y + 46), str(i + 1), font=F(SANSB, 24), fill=WHITE, anchor="ma")
        d.text((148, y + 18), name, font=F(SANSB, 26), fill=NAVY)
        paragraph(d, (148, y + 58), body, F(SANS, 22), INK, 1660, 28)
        y += 132
    footer(
        d,
        1900,
        1040,
        "Paráfrasis de las Free System Distribution Guidelines. Trisquel, PureOS, Parabola, Guix e Hyperbola han estado en esa lista.",
    )
    save(img, "10-fsdg.png")


def fig_ubuntu_trisquel():
    img, d = new_canvas(1900, 1040)
    title(
        d,
        "Ubuntu y Trisquel parten del mismo lugar y no terminan igual",
        "Trisquel se construye sobre una base Ubuntu LTS y le quita lo que la FSF no acepta.",
    )
    rows = [
        ("Base", "Ubuntu LTS, mantenida por Canonical.", "Edición LTS de Ubuntu, rehecha por la comunidad de Trisquel."),
        ("Núcleo", "Linux con firmware no libre disponible.", "linux-libre: el mismo núcleo, sin los blobs."),
        ("Repositorios", "main es libre; restricted y multiverse no lo son.", "Solo software libre. No hay repositorio privativo activo."),
        ("Controladores", "El instalador puede ofrecer el de NVIDIA, cerrado.", "Si el equipo exige un blob, esa función simplemente no aparece."),
        ("Tienda", "Snap puede distribuir programas cerrados.", "No se dirige al usuario hacia software privativo."),
        ("Para quién", "Empresas, escuelas y laptops nuevas.", "Quien quiere la definición estricta y acepta perder hardware."),
    ]
    y = 180
    d.rectangle((48, y, 1852, y + 56), fill=NAVY)
    d.text((70, y + 14), "Punto", font=F(SANSB, 22), fill=WHITE)
    d.text((340, y + 14), "Ubuntu", font=F(SANSB, 22), fill=WHITE)
    d.text((1100, y + 14), "Trisquel", font=F(SANSB, 22), fill=WHITE)
    y += 56
    for i, (punto, ubuntu, trisquel) in enumerate(rows):
        bg = WHITE if i % 2 == 0 else CREAM
        d.rectangle((48, y, 1852, y + 100), fill=bg, outline=LINE)
        d.text((70, y + 34), punto, font=F(SANSB, 22), fill=NAVY)
        paragraph(d, (340, y + 22), ubuntu, F(SANS, 20), INK, 720, 26)
        paragraph(d, (1100, y + 22), trisquel, F(SANS, 20), INK, 720, 26)
        y += 100
    footer(d, 1900, 1040, "Comparación didáctica. Ubuntu es usable y mayoritariamente abierto; Trisquel es el que cabe en la lista estricta de la FSF.")
    save(img, "11-ubuntu-trisquel.png")


def fig_ram():
    labels = [
        "Alpine, servidor sin escritorio",
        "Debian 12, sin escritorio",
        "Debian 12, con escritorio",
        "FreeBSD, escritorio de partida",
        "Ubuntu Server 24.04, sugerido",
        "Ubuntu Desktop 24.04, referencia práctica",
        "MicroStack, guía de la práctica 6",
    ]
    values = [0.13, 0.5, 2, 3, 3, 4, 16]
    colors = ["#1F6A64", "#1F6A64", "#2C5F8A", "#0E2744", "#2C5F8A", "#A67C2D", "#8E3B3B"]
    fig, ax = plt.subplots(figsize=(6.55, 4.2), dpi=200)
    fig.patch.set_facecolor("white")
    positions = list(range(len(labels) - 1, -1, -1))
    bars = ax.barh(positions, values, color=colors, height=0.62, zorder=3)
    ax.set_yticks(positions)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlim(0, 20.5)
    ax.set_xlabel("Memoria RAM de referencia (GB)", fontsize=8.5)
    for bar, value in zip(bars, values):
        label = (f"{value:.2f} GB" if value < 1 else f"{value:.0f} GB").replace(".", ",")
        ax.text(value + 0.25, bar.get_y() + bar.get_height() / 2, label, va="center", fontsize=8.5, color="#0E2744", fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#C8C2B4")
    ax.tick_params(axis="y", length=0, labelsize=8)
    ax.tick_params(axis="x", labelsize=8)
    ax.grid(axis="x", color="#E7E1D6", zorder=0)
    ax.set_axisbelow(True)
    fig.suptitle(
        "La RAM la pide la carga de trabajo, no la palabra Linux",
        fontsize=11.5,
        color="#0E2744",
        fontweight="bold",
        x=0.02,
        ha="left",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    path = OUT / "12-ram.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close()
    print(path)


def fig_escenarios():
    img, d = new_canvas(1900, 1120)
    title(d, "Tres equipos, tres requisitos distintos")
    cards = [
        (
            PALE_BLUE,
            BLUE,
            "Laboratorio de 2015",
            "20 PCs, doble núcleo, 4 GB de RAM, disco de 128 GB.",
            "Debian o una edición con Xfce.",
            "El tutorial oficial pide 25 GB de disco y no publica la RAM. Con 4 GB, GNOME y el navegador se quedan cortos. Un escritorio ligero deja memoria para trabajar.",
        ),
        (
            PALE_TEAL,
            TEAL,
            "Sitio del grupo",
            "Una máquina virtual con 1 GB de RAM y 10 GB de disco.",
            "Debian sin escritorio, o Alpine.",
            "El sistema casi no gasta. El requisito real es el de la aplicación: un sitio estático cabe; una base de datos grande, no.",
        ),
        (
            PALE_RED,
            RED,
            "Práctica 6, MicroStack",
            "Nube privada de OpenStack dentro de una VM.",
            "Ubuntu, como pide la guía.",
            "La guía del curso marca como punto ideal 4 CPU, 16 GB de RAM, 40 GB de disco y virtualización anidada. El mínimo de Ubuntu Server no alcanza para esta carga.",
        ),
    ]
    gap = 28
    width = (1900 - 96 - 2 * gap) // 3
    top = 160
    for i, (bg, accent, name, equipo, eleccion, porque) in enumerate(cards):
        x = 48 + i * (width + gap)
        rounded(d, (x, top, x + width, top + 860), 20, bg, accent, 3)
        d.rectangle((x, top, x + width, top + 14), fill=accent)
        d.text((x + 28, top + 36), f"0{i + 1}", font=F(SANSB, 28), fill=accent)
        d.text((x + 28, top + 80), name, font=F(SANSB, 30), fill=NAVY)
        d.text((x + 28, top + 150), "Equipo", font=F(SANSB, 18), fill=accent)
        yy = paragraph(d, (x + 28, top + 180), equipo, F(SANS, 22), INK, width - 56, 30)
        d.text((x + 28, yy + 16), "Elección", font=F(SANSB, 18), fill=accent)
        yy = paragraph(d, (x + 28, yy + 46), eleccion, F(SANSB, 24), INK, width - 56, 32)
        d.text((x + 28, yy + 16), "Por qué", font=F(SANSB, 18), fill=accent)
        paragraph(d, (x + 28, yy + 46), porque, F(SANS, 22), INK, width - 56, 30)
    footer(d, 1900, 1120, "Ejemplos de este trabajo. Debian y Ubuntu Server, según su documentación. Los 4 GB de escritorio son referencia práctica. MicroStack, según la guía de la práctica 6.")
    save(img, "13-escenarios.png")


def main():
    fig_adopcion()
    fig_familias()
    fig_gendbuntu()
    fig_netflix()
    fig_top500()
    fig_motivo_limite()
    fig_libertades()
    fig_capas()
    fig_licencias()
    fig_fsdg()
    fig_ubuntu_trisquel()
    fig_ram()
    fig_escenarios()


if __name__ == "__main__":
    main()
