"""Goroshi LLC logo set (Stefano Theofanous, 2026-10-27): the bare G on midnight with violet light
(avatar), and the G + GOROSHI LLC wordmark lockups for dark and light grounds. No ring, no line, no pink.
All type is outlined (Cinzel, Inter: SIL OFL 1.1). Usage: python3.14 logo_goroshi.py ASSETS_DIR OUT_DIR"""
import sys

import gmark
from gmark import COOL, INK, ROYAL, VIOLET, g_path, ink_box
from typeset import path_d, width

A, OUT = sys.argv[1:3]
CINZEL = f"{A}/Geist-600.ttf"  # display face: Geist 600 (Cinzel retired 2026-10-27)
INTER = f"{A}/Geist-600.ttf"
gmark.CINZEL = CINZEL

open(f"{OUT}/goroshi-avatar.svg", "w").write(gmark.avatar())

H, GS = 280, 176                      # lockup height; G size
for mode in ("dark", "light"):
    g_top, g_bot = (INK, COOL) if mode == "dark" else ("#1B1F6B", VIOLET)
    word_c, llc_c = (INK, COOL) if mode == "dark" else ("#11143F", ROYAL)
    x0, y0, x1, y1 = ink_box(CINZEL, "G", GS)
    gw = x1 - x0
    gx = 30 + gw / 2
    word_x = 30 + gw + 44
    base = H / 2 + 104 * 0.355
    word = path_d(CINZEL, "GOROSHI", 104, word_x, base, tracking=10)
    ww = width(CINZEL, "GOROSHI", 104, tracking=10)
    llc = path_d(INTER, "LLC", 40, word_x + ww + 24, base, tracking=8)
    W = int(word_x + ww + 24 + width(INTER, "LLC", 40, tracking=8) + 30)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Goroshi LLC">'
           f'<title>Goroshi LLC</title><defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="{H / 2 - (y1 - y0) / 2:.0f}" x2="0" y2="{H / 2 + (y1 - y0) / 2:.0f}">'
           f'<stop offset="0" stop-color="{g_top}"/><stop offset="1" stop-color="{g_bot}"/></linearGradient></defs>'
           f'<path fill="url(#g)" d="{g_path(gx, H / 2, GS)}"/>'
           f'<path fill="{word_c}" d="{word}"/><path fill="{llc_c}" d="{llc}"/></svg>\n')
    open(f"{OUT}/goroshi-lockup-{mode}.svg", "w").write(svg)
print("ok")
