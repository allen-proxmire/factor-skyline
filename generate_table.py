from PIL import Image, ImageDraw, ImageFont
import os

TITLE = "FS Atlas \u2014 PDE Architecture Summary (All Poles, All Scores)"
FOOTER = "Poles: Diffusive \u2022 Hyperbolic \u2022 Dispersive \u2022 Geometric \u2022 Aggregation \u2022 Fluid \u2022 Integrable Apex (KdV) \u2022 Geometric Apex (RF)"

HEADERS = [
    "PDE / Architecture",
    "Pole",
    "Locality",
    "Singularity",
    "Nonlocality",
    "Integrability",
    "Gradient Flow",
    "Score (PASS)",
]

ROWS = [
    ["FP (Fokker\u2013Planck)",          "Diffusive",     "Local",           "None",                   "None",  "No",    "Yes",          "5"],
    ["PME (Porous Medium)",              "Diffusive",     "Local",           "None",                   "None",  "No",    "Yes",          "5"],
    ["TFE (Thin Film, n\u22651)",        "Diffusive",     "Local",           "None",                   "None",  "No",    "Yes",          "4"],
    ["AC (Allen\u2013Cahn)",             "Diffusive",     "Local",           "None",                   "None",  "No",    "Yes",          "3"],
    ["CH (Cahn\u2013Hilliard)",          "Diffusive",     "Local",           "None",                   "None",  "No",    "Yes",          "3"],
    ["RD (Reaction\u2013Diffusion)",     "Diffusive",     "Local",           "Constitutive",           "None",  "No",    "Constitutive", "2"],
    ["HJ (Hamilton\u2013Jacobi)",        "Hyperbolic",    "Local",           "Gradient kink",          "None",  "No",    "No",           "5"],
    ["Burgers (Inviscid)",               "Hyperbolic",    "Local",           "Shocks",                 "None",  "No",    "No",           "5"],
    ["NLS (defocusing)",                 "Dispersive",    "Local",           "None",                   "None",  "No",    "No",           "5"],
    ["NLS (focusing 1D)",                "Dispersive",    "Local",           "None",                   "None",  "Yes*",  "No",           "5"],
    ["KdV",                              "Integrable",    "Local",           "None",                   "None",  "Yes",   "No",           "5"],
    ["MCF (Mean Curvature Flow)",        "Geometric",     "Local",           "Curvature (required)",   "None",  "No",    "Yes",          "3"],
    ["RF (Ricci Flow)",                  "Geometric",     "Local",           "Curvature (classified)", "None",  "No",    "Yes",          "3"],
    ["KS (Keller\u2013Segel)",           "Aggregation",   "Nonlocal",        "Mass concentration",     "Yes",   "No",    "Yes",          "0"],
    ["NS (Navier\u2013Stokes 3D)",       "Fluid",         "Weakly nonlocal", "Unknown (open)",         "Yes",   "No",    "No",           "0"],
]

font_paths = [
    "C:/Windows/Fonts/consola.ttf",
    "C:/Windows/Fonts/cour.ttf",
    "C:/Windows/Fonts/arial.ttf",
]
font_bold_paths = [
    "C:/Windows/Fonts/consolab.ttf",
    "C:/Windows/Fonts/courbd.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]

FONT_SIZE = 22
TITLE_SIZE = 30
FOOTER_SIZE = 18

font = None
for p in font_paths:
    if os.path.exists(p):
        font = ImageFont.truetype(p, FONT_SIZE)
        break
if font is None:
    font = ImageFont.load_default()

font_bold = None
for p in font_bold_paths:
    if os.path.exists(p):
        font_bold = ImageFont.truetype(p, FONT_SIZE)
        break
if font_bold is None:
    font_bold = font

title_font = None
for p in font_bold_paths:
    if os.path.exists(p):
        title_font = ImageFont.truetype(p, TITLE_SIZE)
        break
if title_font is None:
    title_font = font_bold

footer_font = None
for p in font_paths:
    if os.path.exists(p):
        footer_font = ImageFont.truetype(p, FOOTER_SIZE)
        break
if footer_font is None:
    footer_font = font

tmp_img = Image.new("RGB", (100, 100), "white")
tmp_draw = ImageDraw.Draw(tmp_img)

def tw(txt, f):
    bb = tmp_draw.textbbox((0, 0), txt, font=f)
    return bb[2] - bb[0]

def th(txt, f):
    bb = tmp_draw.textbbox((0, 0), txt, font=f)
    return bb[3] - bb[1]

PAD_X = 18
PAD_Y = 10
ROW_H = th("Ag", font) + 2 * PAD_Y
HDR_H = th("Ag", font_bold) + 2 * PAD_Y

ncols = len(HEADERS)
col_w = [0] * ncols
for i, h in enumerate(HEADERS):
    col_w[i] = max(col_w[i], tw(h, font_bold) + 2 * PAD_X)
for row in ROWS:
    for i, cell in enumerate(row):
        col_w[i] = max(col_w[i], tw(cell, font) + 2 * PAD_X)

TW = sum(col_w)
TH = HDR_H + len(ROWS) * ROW_H

ML = 40
MR = 40
MT = 80
MB = 80
TITLE_A = 60
FOOTER_A = 50

content_w = TW + ML + MR
if content_w < 2400:
    extra = 2400 - content_w
    ML += extra // 2
    MR += extra // 2
    content_w = 2400

IW = content_w
IH = MT + TITLE_A + TH + FOOTER_A + MB

img = Image.new("RGB", (IW, IH), "#FFFFFF")
draw = ImageDraw.Draw(img)

ttw = tw(TITLE, title_font)
draw.text(((IW - ttw) // 2, MT // 2), TITLE, fill="#1a1a1a", font=title_font)

ox = ML
oy = MT + TITLE_A

HEADER_BG = "#2c3e50"
HEADER_FG = "#ffffff"
ROW_EVEN = "#f8f9fa"
ROW_ODD = "#ffffff"
GRID = "#bdc3c7"
RED = "#c0392b"
GREEN = "#27ae60"
ORANGE = "#e67e22"
TEXT = "#1a1a1a"

draw.rectangle([ox, oy, ox + TW, oy + HDR_H], fill=HEADER_BG)
x = ox
for i, h in enumerate(HEADERS):
    w = tw(h, font_bold)
    tx = x + (col_w[i] - w) // 2
    ty = oy + (HDR_H - th(h, font_bold)) // 2
    draw.text((tx, ty), h, fill=HEADER_FG, font=font_bold)
    x += col_w[i]

for r, row in enumerate(ROWS):
    ry = oy + HDR_H + r * ROW_H
    bg = ROW_EVEN if r % 2 == 0 else ROW_ODD
    draw.rectangle([ox, ry, ox + TW, ry + ROW_H], fill=bg)
    x = ox
    for i, cell in enumerate(row):
        display = cell
        use_font = font
        use_color = TEXT

        if i == 2 and "Nonlocal" in cell:
            use_font = font_bold
            use_color = RED
        if i == 3 and cell in ("Unknown (open)", "Mass concentration"):
            use_color = RED
        if i == 4 and cell == "Yes":
            use_font = font_bold
            use_color = RED
        if i == 5 and cell in ("Yes", "Yes*"):
            use_font = font_bold
            use_color = GREEN

        if i == ncols - 1:
            if cell == "5":
                use_color = GREEN
                use_font = font_bold
            elif cell == "0":
                use_color = RED
                use_font = font_bold
            elif cell in ("3", "4", "2"):
                use_color = ORANGE
                use_font = font_bold

        w = tw(display, use_font)
        if i == 0:
            tx = x + PAD_X
        else:
            tx = x + (col_w[i] - w) // 2
        ty = ry + (ROW_H - th(display, use_font)) // 2
        draw.text((tx, ty), display, fill=use_color, font=use_font)
        x += col_w[i]

for r in range(len(ROWS) + 2):
    if r == 0:
        ly = oy
    elif r == 1:
        ly = oy + HDR_H
    else:
        ly = oy + HDR_H + (r - 1) * ROW_H
    if ly <= oy + HDR_H + len(ROWS) * ROW_H:
        draw.line([ox, ly, ox + TW, ly], fill=GRID, width=1)

draw.line([ox, oy + HDR_H, ox + TW, oy + HDR_H], fill="#2c3e50", width=2)

x = ox
for i in range(ncols + 1):
    draw.line([x, oy, x, oy + HDR_H + len(ROWS) * ROW_H], fill=GRID, width=1)
    if i < ncols:
        x += col_w[i]
    else:
        x = ox + TW

draw.rectangle([ox, oy, ox + TW, oy + HDR_H + len(ROWS) * ROW_H], outline="#2c3e50", width=2)

fy = oy + HDR_H + len(ROWS) * ROW_H + 20
fw = tw(FOOTER, footer_font)
draw.text(((IW - fw) // 2, fy), FOOTER, fill="#7f8c8d", font=footer_font)

out = "FS_Atlas_Summary_Table.png"
img.save(out, "PNG", dpi=(150, 150))
print(f"Saved: {out} ({IW}x{IH})")
