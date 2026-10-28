"""Typeset text as SVG outlines: HarfBuzz (hb-shape) for shaping and kerning, fontTools for glyph paths.

Outlined text renders identically everywhere GitHub shows an <img> (no font loading, no fallback),
which is what makes the banner and the stack panels crisp. Fonts: Inter, Cinzel, GFS Didot (SIL OFL 1.1).
Run with the Python that has fontTools: /opt/homebrew/opt/python@3.14/bin/python3.14
"""

import functools
import json
import subprocess

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont


@functools.cache
def _font(path):
    f = TTFont(path)
    units_per_em: object = getattr(f["head"], "unitsPerEm", None)
    if type(units_per_em) is not int or units_per_em <= 0:
        f.close()
        raise ValueError("font unitsPerEm must be a positive integer")
    return f, f.getGlyphSet(), f.getGlyphOrder(), units_per_em


def shape(path, text):
    out = subprocess.run(
        ["hb-shape", "--output-format=json", "--no-glyph-names", path, text],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return json.loads(out)


def width(path, text, size, tracking=0.0):
    """Advance width in px of text at size, plus tracking (px) between letters."""
    _, _, _, upm = _font(path)
    glyphs = shape(path, text)
    return sum(g["ax"] for g in glyphs) * size / upm + tracking * max(
        len(glyphs) - 1, 0
    )


def path_d(path, text, size, x, y, tracking=0.0, anchor="start"):
    """SVG path data for text whose baseline starts at (x, y)."""
    _font_obj, gs, order, upm = _font(path)
    glyphs = shape(path, text)
    s = size / upm
    if anchor != "start":
        w = width(path, text, size, tracking)
        x -= w / 2 if anchor == "middle" else w
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    cx = x
    for g in glyphs:
        name = order[g["g"]]
        gx = cx + g["dx"] * s
        gy = y - g["dy"] * s
        gs[name].draw(TransformPen(pen, (s, 0, 0, -s, gx, gy)))
        cx += g["ax"] * s + tracking
    return pen.getCommands()


def cap_height(path):
    font, _, _, upm = _font(path)
    return font["OS/2"].sCapHeight / upm


def glyph_bounds(path, char, size):
    """(xmin, xmax) of a single glyph's ink at size, relative to its origin."""
    from fontTools.pens.boundsPen import BoundsPen

    _font_obj, gs, order, upm = _font(path)
    g = shape(path, char)[0]
    bp = BoundsPen(gs)
    gs[order[g["g"]]].draw(bp)
    bounds = bp.bounds
    if bounds is None:
        raise ValueError("glyph has no outline bounds")
    xmin, _, xmax, _ = bounds
    return xmin * size / upm, xmax * size / upm
