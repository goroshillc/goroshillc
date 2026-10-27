"""The Goroshi LLC mark: Alpha, Chi Rho, Omega as one set (Stefano Theofanous, 2026-10-27).

His notes: the Rho had "really weird spacing on the x"; use real Greek Alpha and Omega.
Geometry: the Chi's arms span the capital height of the flanking letters exactly; the Rho's bowl sits
fully above the Chi with a clear gap of one stroke width plus air; the stem runs through the crossing.
Alpha and Omega are GFS Didot outlines (Greek Font Society, SIL OFL 1.1) at the size whose capital
height equals the Chi's height, and both sit on the same baseline with equal ink-to-ink gaps.
"""
from typeset import cap_height, glyph_bounds, path_d

DIDOT = None  # set by caller to the GFS Didot path


def chi_rho(cx, base, cap, sw):
    """Stroke paths for a Chi Rho whose Chi spans [base-cap, base] centered on cx."""
    a = cap / 2                      # half-size of the Chi (arms at 45 degrees)
    cy = base - a                    # crossing point, on the stem
    gap = sw * 1.6                   # clear air between the Chi's top arms and the bowl
    r = cap * 0.27                   # bowl radius
    bowl_bottom = base - cap - gap   # bowl clears the top of the Chi
    top = bowl_bottom - 2 * r
    stem_bottom = base + sw * 0.6    # stem drops just below the baseline, as in the classic form
    h = r * 0.35                     # short flat before the bowl's curve
    return [
        f"M{cx:.2f} {top:.2f} V{stem_bottom:.2f}",
        f"M{cx:.2f} {top:.2f} H{cx + h:.2f} A{r:.2f} {r:.2f} 0 0 1 {cx + h:.2f} {bowl_bottom:.2f} H{cx:.2f}",
        f"M{cx - a:.2f} {cy - a:.2f} L{cx + a:.2f} {cy + a:.2f}",
        f"M{cx + a:.2f} {cy - a:.2f} L{cx - a:.2f} {cy + a:.2f}",
    ], top, stem_bottom


def mark(didot, cx, base, cap, sw, letter_fill, rho_stroke, gap_ratio=0.85):
    """SVG group: Alpha, Chi Rho and Omega centered on cx with matched cap heights and equal gaps."""
    size = cap / cap_height(didot)               # Didot size whose capitals are exactly `cap` tall
    a_l, a_r = glyph_bounds(didot, "Α", size)
    o_l, o_r = glyph_bounds(didot, "Ω", size)
    half_chi = cap / 2 + sw / 2                  # ink half-width of the Chi including stroke
    gap = cap * gap_ratio
    ax = cx - half_chi - gap - a_r               # Alpha origin so its right ink edge sits `gap` from the Chi
    ox = cx + half_chi + gap - o_l               # Omega origin so its left ink edge sits `gap` from the Chi
    paths, top, bottom = chi_rho(cx, base, cap, sw)
    strokes = "".join(f'<path d="{d}"/>' for d in paths)
    return (f'<g><path fill="{letter_fill}" d="{path_d(didot, "Α", size, ax, base)}"/>'
            f'<g fill="none" stroke="{rho_stroke}" stroke-width="{sw:.2f}" stroke-linecap="round" stroke-linejoin="round">{strokes}</g>'
            f'<path fill="{letter_fill}" d="{path_d(didot, "Ω", size, ox, base)}"/></g>'), top, bottom
