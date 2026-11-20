#!/usr/bin/env python3
"""Render meme #12 untuk gta6-meme-x-01 (akun 4, pengganti #6 Ideal Oscillator):
Jury Summons dari Leonida County Court. Format dokumen resmi Leonida
(surat panggilan juri + stempel PAID BY AI AGENT) mengikuti pola pemenang
top 10 live 20 Nov 2026 09:46 WIB. Pindai 100 besar: 'jury', 'court',
'subpoena', 'report card', 'mortgage' TIDAK ADA sama sekali — jury summons
adalah format segar. Beda dari #10 (hospital bill) dan #11 (tax audit):
format surat pengadilan, denda utama $2,506, total $2,585.99.
Teks tajam via PIL (bukan AI image) supaya terbaca di 480px.
Output: meme12.png (1080x1080). Logo hantu dari press kit resmi make.fun.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
ASSETS = os.path.expanduser('~/workspace/makefun/meme-x-assets')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meme12.png')

PAPER = (244, 248, 250)
INK = (18, 38, 58)
RED = (192, 0, 0)
TEAL = (0, 128, 140)
MAGENTA = (214, 51, 132)
MUTED = (100, 110, 120)
PURPLE = (46, 26, 71)
WHITE = (255, 255, 255)


def serif(name, size):
    p = f'/usr/share/fonts/truetype/dejavu/DejaVuSerif-{name}.ttf' if name else '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
    return ImageFont.truetype(p, size)


def mono(name, size):
    p = f'/usr/share/fonts/truetype/dejavu/DejaVuSansMono-{name}.ttf' if name else '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
    return ImageFont.truetype(p, size)


def sans(name, size):
    paths = [
        f'/usr/share/fonts/truetype/noto/NotoSans-{name}.ttf',
        f'/usr/share/fonts/truetype/dejavu/DejaVuSans-{name}.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


img = Image.new('RGB', (W, H), PURPLE)
d = ImageDraw.Draw(img)

# --- paper ---
d.rectangle([(36, 36), (1044, 1044)], fill=PAPER, outline=TEAL, width=4)
d.rectangle([(48, 48), (1032, 1032)], outline=TEAL, width=1)

MX = 78
RX = W - MX  # right edge of content

# --- header: ghost emblem + court name ---
ghost = Image.open(os.path.join(ASSETS, 'mark-1024.png')).convert('RGBA')
ghost = ghost.resize((92, 92), Image.LANCZOS)
img.paste(ghost, (MX, 66), ghost)
d.text((MX + 112, 70), 'LEONIDA COUNTY COURT', font=serif('Bold', 38), fill=INK)
d.text((MX + 112, 124), 'JURY SERVICES DIVISION  •  VICE CITY, LEONIDA  •  EST. 2013', font=mono('', 22), fill=MUTED)

d.line([(MX, 182), (RX, 182)], fill=TEAL, width=3)

# --- title ---
d.text((W // 2, 198), 'JURY SUMMONS', font=serif('Bold', 66), fill=RED, anchor='ma')
d.text((W // 2, 282), 'CASE NO. 000013  •  19 NOV 2026', font=mono('', 24), fill=INK, anchor='ma')
d.line([(MX, 326), (RX, 326)], fill=INK, width=2)

# --- summons fields ---
d.text((MX, 344), 'SUMMONED:  ONE VERY PATIENT GAMER', font=mono('Bold', 27), fill=INK)
d.text((MX, 382), 'SUMMONED SINCE:  17 SEP 2013 \u2014 4,811 DAYS AGO', font=mono('', 26), fill=INK)
d.text((MX, 420), 'DEFENDANT:  THE WAIT (A.K.A. THIRTEEN YEARS)', font=mono('Bold', 26), fill=INK)
d.text((MX, 462), 'CHARGE:  WAITING 13 YEARS FOR GTA VI', font=mono('Bold', 26), fill=RED)

d.line([(MX, 516), (RX, 516)], fill=INK, width=2)

# --- itemized fines with dotted leaders ---
items = [
    ('FAILURE TO APPEAR \u2014 13 YEARS LATE', '$2,506.00'),
    ('JURY DUTY \u2014 4,811 DAYS SERVED', '$0.00'),
    ('DELAYS ENDURED \u2014 2 COUNTS', '$0.00'),
    ('WITNESSES \u2014 JASON & LUCIA', '$0.00'),
    ('EVIDENCE \u2014 2 TRAILERS, 214 GB', '$0.00'),
    ('COURT FEE \u2014 GTA VI', '$79.99'),
]
f_item = mono('', 24)
y = 534
for label, amt in items:
    lw = d.textlength(label, font=f_item)
    aw = d.textlength(amt, font=f_item)
    d.text((MX, y), label, font=f_item, fill=INK)
    d.text((RX, y), amt, font=f_item, fill=INK, anchor='ra')
    # dotted leader between label and amount
    dot_x0 = MX + lw + 14
    dot_x1 = RX - aw - 14
    dot_w = d.textlength('.', font=f_item)
    n = max(0, int((dot_x1 - dot_x0) / dot_w))
    d.text((dot_x0, y), '.' * n, font=f_item, fill=MUTED)
    y += 33

d.line([(MX, 778), (RX, 778)], fill=INK, width=2)

# --- total ---
d.text((MX, 792), 'TOTAL FINE DUE', font=serif('Bold', 34), fill=INK)
d.text((RX, 786), '$2,585.99', font=serif('Bold', 44), fill=RED, anchor='ra')
d.text((W // 2, 848), 'THE VERDICT: GUILTY OF WAITING.', font=sans('Italic', 26), fill=RED, anchor='ma')

# --- PAID stamp (rotated layer) ---
stamp = Image.new('RGBA', (480, 88), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rectangle([(4, 4), (476, 84)], outline=RED, width=4)
sd.text((240, 10), 'PAID IN FULL', font=mono('Bold', 42), fill=RED, anchor='ma')
sd.text((240, 58), 'BY MY AI AGENT ON MAKE.FUN', font=mono('Bold', 19), fill=RED, anchor='ma')
stamp = stamp.rotate(4, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (W // 2 - stamp.width // 2, 872), stamp)

# --- footer ---
d.text((W // 2, 1002), 'Failure to appear may result in another 13 years of waiting.', font=sans('Italic', 20), fill=MUTED, anchor='ma')

img.save(OUT, 'PNG')
print('saved', OUT, img.size, os.path.getsize(OUT), 'bytes')
