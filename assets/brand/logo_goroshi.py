"""Goroshi LLC logo set (Stefano Theofanous, 2026-10-27: "a bis goroshi logo that is jerry garcia level crisp").
Monogram: Cinzel G, optically centered in a halo ring, one flowing swirl line (the Jerry Garcia tie motif)
passing behind it, on the midnight-violet field. Lockup: monogram + tracked GOROSHI wordmark.
All type is outlined (Cinzel, SIL OFL 1.1). Usage: python3.14 logo_goroshi.py ASSETS_DIR OUT_DIR"""
import sys
import gmark
from gmark import monogram
from typeset import path_d, width

A, OUT = sys.argv[1:3]
CINZEL = f"{A}/Cinzel-600.ttf"
gmark.CINZEL = CINZEL


def svg(w, h, defs, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">'
            f'<title>{label}</title><defs>{defs}</defs>{body}</svg>\n')


# Avatar: full-bleed square so GitHub's circular crop shows the field edge to edge.
d, b = monogram(512, 512, 512, uid="a")
d2, b2 = monogram(512, 512, 512, field=False, uid="a2")
open(f"{OUT}/goroshi-avatar.svg", "w").write(svg(1024, 1024, d, b, "Goroshi LLC"))

# Lockups: monogram + wordmark, dark and light.
for mode, ink, sub in (("dark", "#f5f4ff", "#cbb8ff"), ("light", "#11123a", "#46439F")):
    R = 120
    d, b = monogram(140, 140, R, uid=f"l{mode}")
    word = path_d(CINZEL, "GOROSHI", 96, 300, 140 + 96 * 0.35, tracking=18)
    ww = width(CINZEL, "GOROSHI", 96, tracking=18)
    llc = path_d(f"{A}/Inter-600.ttf", "LLC", 30, 300 + ww + 24, 140 + 96 * 0.35, tracking=8)
    W = int(300 + ww + 22 + width(f"{A}/Inter-600.ttf", "LLC", 30, tracking=8) + 24)
    open(f"{OUT}/goroshi-lockup-{mode}.svg", "w").write(
        svg(W, 280, d, b + f'<path fill="{ink}" d="{word}"/><path fill="{sub}" d="{llc}"/>', "Goroshi LLC"))
print("ok")
