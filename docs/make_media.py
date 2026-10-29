#!/usr/bin/env python3
"""Media for the moved-repo page. Uses omo-space's own hero and fonts so it matches the main repo.

    python3 docs/make_media.py /path/to/omo-space
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SPACE = Path(sys.argv[1] if len(sys.argv) > 1 else "../omo-space")
OUT = Path(__file__).resolve().parent / "media"
FONTS = SPACE / "launcher/assets/fonts"
CREAM, INK, ESPRESSO = (245, 240, 232), (32, 26, 22), (43, 34, 28)

# The hero: omo-space's own banner, unchanged.
hero = Image.open(SPACE / "docs/media/hero.webp").convert("RGB")
hero.save(OUT / "hero.webp", quality=88, method=6)

# Social preview 1280x640: the hero scaled to 640 tall, cropped from the left so the wordmark stays in.
s = hero.resize((round(hero.width * 640 / hero.height), 640), Image.Resampling.LANCZOS)
s.crop((0, 0, 1280, 640)).save(OUT / "social-preview.png", optimize=True)


def button(label, path, w=420, h=88):
    """Same shape as omo-space's btn-install.png: cream pill, dark border, IBM Plex Mono, drawn at 2x."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, w - 3, h - 3), radius=14, fill=(*CREAM, 255), outline=(*INK, 255), width=4)
    f = ImageFont.truetype(str(FONTS / "IBMPlexMono-Medium.ttf"), 34)
    tw = d.textlength(label, font=f)
    d.text(((w - tw) / 2, h / 2), label, font=f, fill=(*INK, 255), anchor="lm")
    im.save(path, optimize=True)


button("Go to omo-space  \u2192", OUT / "btn-go.png")
print("wrote", *sorted(p.name for p in OUT.iterdir() if p.suffix in {".png", ".webp"}))
