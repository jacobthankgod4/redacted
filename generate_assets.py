#!/usr/bin/env python3
"""Generate $REDACTED brand assets: PFP, X banner, OG image."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, math, os

OUT = os.path.dirname(os.path.abspath(__file__))
random.seed(42)

BG = (10, 10, 11)
PANEL = (18, 18, 20)
LINE = (38, 38, 43)
PAPER = (244, 241, 232)
PAPER_SHADOW = (216, 210, 192)
INK = (26, 26, 26)
DIM = (138, 138, 147)
RED = (255, 46, 46)
RED_DARK = (179, 30, 30)
WHITE = (232, 232, 234)

MENLO = "/System/Library/Fonts/Menlo.ttc"
SFMONO = "/System/Library/Fonts/SFNSMono.ttf"

def font(size, bold=False):
    try:
        return ImageFont.truetype(MENLO, size, index=1 if bold else 0)
    except Exception:
        try:
            return ImageFont.truetype(SFMONO, size)
        except Exception:
            return ImageFont.load_default()

def paper_noise(w, h, strength=10):
    n = Image.new("L", (w, h))
    px = n.load()
    for y in range(h):
        for x in range(w):
            px[x, y] = 128 + random.randint(-strength, strength)
    return n

def draw_cbar(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(0, 0, 0))

def draw_faint_lines(draw, x, y, widths, gap=18, color=(200, 196, 184), h=6):
    for i, w in enumerate(widths):
        draw.rectangle([x, y + i * gap, x + w, y + i * gap + h], fill=color)
    return y + len(widths) * gap

def stamp(draw, cx, cy, text="CLASSIFIED", size=44, angle=-8, color=RED):
    f = font(size, bold=True)
    tmp = Image.new("RGBA", (int(size * len(text) * 0.72), int(size * 2)), (0, 0, 0, 0))
    td = ImageDraw.Draw(tmp)
    tw = td.textlength(text, font=f)
    pad = 14
    td.rectangle([2, 2, tw + pad * 2, size + pad], outline=color + (255,), width=4)
    td.text((pad, pad // 2), text, font=f, fill=color + (255,))
    tmp = tmp.rotate(angle, expand=True, resample=Image.BICUBIC)
    draw._image.paste(tmp, (int(cx - tmp.width / 2), int(cy - tmp.height / 2)), tmp)

def scanlines(img, alpha=16):
    d = ImageDraw.Draw(img)
    for y in range(0, img.height, 3):
        d.line([(0, y), (img.width, y)], fill=(0, 0, 0, alpha))

# ---------------- PFP 1000x1000 ----------------
def make_pfp():
    W = H = 1000
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # faint grid backdrop
    for i in range(0, W, 50):
        d.line([(i, 0), (i, H)], fill=(16, 16, 18))
        d.line([(0, i), (W, i)], fill=(16, 16, 18))

    # document card
    card_w, card_h = 620, 780
    cx, cy = W // 2, H // 2 + 10
    card = Image.new("RGB", (card_w, card_h), PAPER)
    cd = ImageDraw.Draw(card)

    # paper texture
    noise = paper_noise(card_w, card_h, 8).convert("RGB")
    card = Image.blend(card, noise, 0.05)
    cd = ImageDraw.Draw(card)

    # inner border
    cd.rectangle([18, 18, card_w - 18, card_h - 18], outline=PAPER_SHADOW, width=2)

    # header
    f_small = font(22, bold=True)
    f_tiny = font(16)
    cd.text((44, 42), "DOSSIER #001", font=f_small, fill=INK)
    cd.text((44, 74), "FILE: ██████████", font=f_tiny, fill=(90, 88, 80))
    cd.line([(44, 108), (card_w - 44, 108)], fill=PAPER_SHADOW, width=2)

    # field rows with censor bars
    y = 140
    fields = [
        ("NAME", 300), ("ALIAS", 220), ("NET WORTH", 340),
        ("LOCATION", 260), ("ALLEGIANCE", 300), ("LAST SEEN", 200),
    ]
    f_label = font(18, bold=True)
    for label, barw in fields:
        cd.text((44, y), label + ":", font=f_label, fill=(70, 68, 62))
        draw_cbar(cd, 200, y + 2, barw, 22)
        y += 48

    # faint readable line
    y += 10
    cd.text((44, y), "STATUS:", font=f_label, fill=(70, 68, 62))
    f_ok = font(20, bold=True)
    cd.text((200, y - 1), "ACTIVE — WAVE RIDING", font=f_ok, fill=(10, 90, 10))
    y += 56

    # more redacted block
    cd.line([(44, y), (card_w - 44, y)], fill=PAPER_SHADOW, width=2)
    y += 24
    line_widths = [500, 430, 520, 300, 470, 380, 510]
    for i, lw in enumerate(line_widths):
        # mix of faint text lines and black bars
        if i % 2 == 0:
            cd.rectangle([44, y, 44 + lw, y + 8], fill=(205, 200, 188))
        else:
            draw_cbar(cd, 44, y - 4, lw, 18)
        y += 30
        if y > card_h - 160:
            break

    # footer ticker
    f_tick = font(18, bold=True)
    cd.text((44, card_h - 70), "$REDACTED", font=f_tick, fill=RED_DARK)
    cd.text((card_w - 200, card_h - 70), "SOLANA / 0-0", font=f_tiny, fill=(120, 118, 110))

    # stamp
    stamp(cd, card_w - 170, 210, "CLASSIFIED", size=40, angle=-10)

    # scanlines only on the dark background — never over the paper
    scanlines(img, 14)

    # drop shadow + card, rotated slightly
    card = card.rotate(-2.5, expand=True, resample=Image.BICUBIC, fillcolor=None)
    shadow = card.convert("L").filter(ImageFilter.GaussianBlur(14))
    sh_card = Image.new("RGB", card.size, (0, 0, 0))
    pos = (cx - card.width // 2, cy - card.height // 2)
    img.paste(sh_card, (pos[0] + 10, pos[1] + 14), shadow.point(lambda v: min(255, v // 2)))
    img.paste(card, pos)

    img.save(os.path.join(OUT, "pfp.png"), optimize=True)
    print("pfp.png", img.size)

# ---------------- BANNER 1500x500 ----------------
def make_banner():
    W, H = 1500, 500
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # background redacted text rows
    f_bg = font(20)
    y = 14
    while y < H:
        x = 20
        while x < W - 40:
            seg = random.randint(60, 220)
            if random.random() < 0.55:
                d.rectangle([x, y, x + seg, y + 14], fill=(22, 22, 26))
            else:
                d.rectangle([x, y + 4, x + seg, y + 10], fill=(30, 30, 34))
            x += seg + 18
        y += 34

    # center readable line
    f_main = font(38, bold=True)
    text = "PRIVACY IS NOT A FEATURE. IT'S A RIGHT."
    tw = d.textlength(text, font=f_main)
    tx = (W - tw) / 2
    ty = H / 2 - 46
    # backing bar
    d.rectangle([tx - 28, ty - 16, tx + tw + 28, ty + 58], fill=BG)
    d.text((tx, ty), text, font=f_main, fill=RED)

    # subline
    f_sub = font(18)
    sub = "SOURCE: ████████  ·  CONFIDENCE: ████████  ·  CLEARANCE: PUBLIC"
    sw = d.textlength(sub, font=f_sub)
    d.text(((W - sw) / 2, ty + 74), sub, font=f_sub, fill=DIM)

    # logo top-left
    f_logo = font(28, bold=True)
    d.text((36, 28), "[", font=f_logo, fill=WHITE)
    d.text((58, 28), "████████", font=f_logo, fill=RED)
    d.text((58 + d.textlength("████████", font=f_logo), 28), "]", font=f_logo, fill=WHITE)

    # stamp
    stamp(d, W - 190, 80, "EYES ONLY", size=30, angle=-8)

    # bottom strip
    d.rectangle([0, H - 6, W, H], fill=RED)
    scanlines(img, 10)
    img.save(os.path.join(OUT, "banner.png"), optimize=True)
    print("banner.png", img.size)

# ---------------- OG 1200x630 ----------------
def make_og():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    for i in range(0, W, 40):
        d.line([(i, 0), (i, H)], fill=(14, 14, 16))

    f_h1 = font(92, bold=True)
    d.text((80, 150), "REDACT", font=f_h1, fill=WHITE)
    xoff = 80 + d.textlength("REDACT", font=f_h1)
    d.text((xoff, 150), "ED", font=f_h1, fill=RED)

    f_tag = font(26)
    d.text((84, 270), "SOURCE: ████████   CONFIDENCE: ████████   ACTION: ████████", font=f_tag, fill=DIM)
    d.text((84, 320), "The privacy narrative is live. This is its mascot.", font=f_tag, fill=WHITE)

    f_meta = font(20, bold=True)
    d.text((84, 420), "SOLANA", font=f_meta, fill=WHITE)
    d.text((210, 420), "·", font=f_meta, fill=DIM)
    d.text((240, 420), "1B SUPPLY", font=f_meta, fill=WHITE)
    d.text((400, 420), "·", font=f_meta, fill=DIM)
    d.text((430, 420), "0 / 0 TAX", font=f_meta, fill=WHITE)
    d.text((580, 420), "·", font=f_meta, fill=DIM)
    d.text((610, 420), "NO TEAM", font=f_meta, fill=RED)

    stamp(d, W - 220, 120, "CLASSIFIED", size=42, angle=-8)

    # censor strip right side
    for i, w in enumerate([200, 160, 220, 120, 190]):
        d.rectangle([W - 320, 260 + i * 36, W - 320 + w, 260 + i * 36 + 18], fill=(0, 0, 0))

    d.rectangle([0, H - 8, W, H], fill=RED)
    scanlines(img, 12)
    img.save(os.path.join(OUT, "og.png"), optimize=True)
    print("og.png", img.size)

make_pfp()
make_banner()
make_og()
print("done ->", OUT)
