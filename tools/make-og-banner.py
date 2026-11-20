"""Build the 1200x630 Open Graph banner from the site's own vector emblem."""
import subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP  = Path(tempfile.gettempdir()) / "emblem-og.png"
from PIL import Image, ImageDraw, ImageFont

W, H   = 1200, 630
BG     = (10, 13, 18)       # #0a0d12
TEXT   = (230, 237, 243)    # #e6edf3
MUTED  = (154, 167, 184)    # #9aa7b8
AMBER  = (240, 165, 0)      # #f0a500
SAFE   = 72                 # keep content inside this margin

SF = "/System/Library/Fonts/SFNS.ttf"
def sf(size, weight="Bold"):
    f = ImageFont.truetype(SF, size)
    try: f.set_variation_by_name(weight)
    except Exception: pass
    return f

img  = Image.new("RGB", (W, H), BG)

# Amber glow behind the emblem, same radial treatment as the site hero.
GX, GY, GR = 330, H // 2, 420
glow = Image.new("RGB", (W, H), BG)
gd   = ImageDraw.Draw(glow)
for i in range(GR, 0, -4):
    t = 1 - (i / GR)
    a = (t ** 2.2) * 0.30
    gd.ellipse([GX - i, GY - i, GX + i, GY + i],
               fill=tuple(round(BG[c] + (AMBER[c] - BG[c]) * a) for c in range(3)))
img = Image.blend(img, glow, 1.0)

# Emblem, rendered from assets/emblem.svg so it stays crisp.
EM = 360
subprocess.run(["rsvg-convert", "-w", str(EM), "-h", str(EM),
                str(ROOT / "assets" / "emblem.svg"),
                "-o", str(TMP)], check=True)
em = Image.open(TMP).convert("RGBA")
img.paste(em, (GX - EM // 2, GY - EM // 2), em)

d = ImageDraw.Draw(img)
X  = 600                      # text column start
AVAIL = W - X - SAFE          # usable width

def width(txt, font): return d.textlength(txt, font=font)

# --- wordmark ---
f_mark = sf(40, "Bold")
f_sub  = sf(40, "Regular")
d.text((X, 150), "Open Skies", font=f_mark, fill=TEXT)
d.text((X + width("Open Skies ", f_mark), 150), "PhotoForecast", font=f_sub, fill=MUTED)

# --- headline, auto-fitted then wrapped ---
HEAD = "Know when the light will be right."
size = 66
while size > 34:
    f_head = sf(size, "Bold")
    words, lines, cur = HEAD.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if width(trial, f_head) <= AVAIL: cur = trial
        else: lines.append(cur); cur = w
    lines.append(cur)
    if len(lines) <= 2 and all(width(l, f_head) <= AVAIL for l in lines): break
    size -= 2

y = 228
for line in lines:
    d.text((X, y), line, font=f_head, fill=TEXT)
    y += int(size * 1.18)

# --- amber rule + footer ---
y += 18
d.rectangle([X, y, X + 64, y + 4], fill=AMBER)
y += 30
f_foot = sf(27, "Medium")
d.text((X, y), "Free on iOS & Android · openskiesapp.com", font=f_foot, fill=MUTED)

# --- checks ---
bottom = y + 34
assert bottom < H - SAFE + 40, f"content runs past the safe area: {bottom}"
for line in lines:
    assert X + width(line, f_head) <= W - SAFE + 1, f"headline overflows: {line}"

out = str(ROOT / "assets" / "og-banner.png")
img.save(out, "PNG", optimize=True)
print(f"  headline size {size}px, {len(lines)} line(s)")
for l in lines: print(f"    │ {l}")
print(f"  saved {out}")
