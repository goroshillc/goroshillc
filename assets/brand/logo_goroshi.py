"""Goroshi LLC logo set (Stefano Theofanous, 2026-10-27: "a bis goroshi logo that is jerry garcia level crisp").
Monogram: Cinzel G, optically centered in a halo ring, one flowing swirl line (the Jerry Garcia tie motif)
passing behind it, on the midnight-violet field. Lockup: monogram + tracked GOROSHI wordmark.
All type is outlined (Cinzel, SIL OFL 1.1). Usage: python3.14 logo_goroshi.py ASSETS_DIR OUT_DIR"""
import sys
from fontTools.pens.boundsPen import BoundsPen
from typeset import _font, path_d, shape, width

A, OUT = sys.argv[1:3]
CINZEL = f"{A}/Cinzel-600.ttf"


def ink_box(font, ch, size):
    f, gs, order, upm = _font(font)
    bp = BoundsPen(gs)
    gs[order[shape(font, ch)[0]["g"]]].draw(bp)
    x0, y0, x1, y1 = bp.bounds
    s = size / upm
    return x0 * s, y0 * s, x1 * s, y1 * s


def monogram(cx, cy, R, field=True, ink="#f5f4ff", ring="url(#ring)", uid="m"):
    size = R * 0.98
    x0, y0, x1, y1 = ink_box(CINZEL, "G", size)
    gx = cx - (x0 + x1) / 2            # center the G's ink, not its advance box
    base = cy + (y0 + y1) / 2          # optical vertical center of the ink
    g = path_d(CINZEL, "G", size, gx, base)
    sw = R * 0.026
    swirl = (f"M{cx - R * 1.2:.1f} {cy + R * .78:.1f} C {cx - R * .7:.1f} {cy + R * .38:.1f}, "
             f"{cx - R * .35:.1f} {cy + R * .98:.1f}, {cx + R * .12:.1f} {cy + R * .66:.1f} "
             f"S {cx + R * .78:.1f} {cy + R * .02:.1f}, {cx + R * 1.25:.1f} {cy + R * .12:.1f}")
    defs = (f'<radialGradient id="{uid}bg" cx="50%" cy="38%" r="70%"><stop offset="0" stop-color="#2a2580"/>'
            f'<stop offset=".5" stop-color="#181A56"/><stop offset="1" stop-color="#07070d"/></radialGradient>'
            f'<linearGradient id="ring" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/>'
            f'<stop offset=".55" stop-color="#cbb8ff"/><stop offset="1" stop-color="#BC43D3"/></linearGradient>'
            f'<clipPath id="{uid}c"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath>'
            f'<filter id="{uid}b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{R * .22:.1f}"/></filter>')
    body = ""
    if field:
        body += (f'<g clip-path="url(#{uid}c)"><circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#{uid}bg)"/>'
                 f'<g filter="url(#{uid}b)"><ellipse cx="{cx + R * .45:.1f}" cy="{cy - R * .5:.1f}" rx="{R * .7:.1f}" ry="{R * .4:.1f}" fill="#46439F" opacity=".7"/>'
                 f'<ellipse cx="{cx - R * .5:.1f}" cy="{cy + R * .65:.1f}" rx="{R * .75:.1f}" ry="{R * .35:.1f}" fill="#BC43D3" opacity=".35"/></g>'
                 f'<path d="{swirl}" fill="none" stroke="#ffffff" stroke-opacity=".5" stroke-width="{sw * .42:.2f}" stroke-linecap="round"/></g>')
    body += (f'<circle cx="{cx}" cy="{cy}" r="{R * .86:.1f}" fill="none" stroke="{ring}" stroke-width="{sw:.2f}"/>'
             f'<path fill="{ink}" d="{g}"/>')
    return defs, body


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
