"""The Goroshi G and the brand palette (Stefano Theofanous, 2026-10-27).

His direction: "just a g with the clean background midnight blue and solo leveling purple tone";
"the circle around it seems so weird"; "fuck pink"; no thin lines ("the way urs is done is strange
thats not even how it is on the garcias"); "i dont want this looking ai slop genned".
So: no ring, no disc, no swirl, no magenta. Midnight blue with Shadow-Monarch violet, white G.
"""
from gconstruct import g_outline

CINZEL = None  # set by the caller

# Midnight blue + Solo Leveling purple. Nothing pink, nothing magenta.
INK = "#F7F4FF"        # near-white with a cool cast
COOL = "#B9A8FF"       # periwinkle highlight (blue side of violet)
VIOLET = "#6A35FF"     # Shadow Monarch violet
ROYAL = "#3A1F9E"      # royal blue
MIDNIGHT = "#0D0B33"   # midnight blue
BLACK = "#05060F"      # blue-black


def ink_box(font, ch, size):
    """Extent of the constructed G of diameter `size`, centered on its origin (API kept for callers)."""
    r = size / 2
    return -r, -r, r, r


def g_path(cx, cy, size):
    """The constructed Goroshi G (gconstruct.py), diameter `size`, centered on (cx, cy)."""
    r = size / 2
    return g_outline(cx, cy, r, r * 0.30)


def glow(cx, cy, r, uid, strength=1.0):
    """A soft violet-to-royal light behind the G (no hard edge, no shape)."""
    return (f'<radialGradient id="{uid}glow" cx="{cx}" cy="{cy}" r="{r}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{VIOLET}" stop-opacity="{.55 * strength:.2f}"/>'
            f'<stop offset=".55" stop-color="{ROYAL}" stop-opacity="{.25 * strength:.2f}"/>'
            f'<stop offset="1" stop-color="{ROYAL}" stop-opacity="0"/></radialGradient>',
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{uid}glow)"/>')


def g_fill(uid, y0, y1):
    """White at the top to periwinkle at the foot: a cool, crisp G."""
    return (f'<linearGradient id="{uid}gf" gradientUnits="userSpaceOnUse" x1="0" y1="{y0:.0f}" x2="0" y2="{y1:.0f}">'
            f'<stop offset="0" stop-color="{INK}"/><stop offset="1" stop-color="{COOL}"/></linearGradient>')


def avatar(S=1024):
    """Square, full-bleed: midnight field, violet light, the G. Works under any circular crop."""
    size = S * 0.56
    cx = cy = S / 2
    x0, y0, x1, y1 = ink_box(CINZEL, "G", size)
    gdef, gcircle = glow(cx, cy, S * 0.46, "av")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}" role="img" aria-label="Goroshi LLC">'
            f'<title>Goroshi LLC</title><defs>'
            f'<radialGradient id="avbg" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#1A1650"/>'
            f'<stop offset=".6" stop-color="{MIDNIGHT}"/><stop offset="1" stop-color="{BLACK}"/></radialGradient>'
            f'{gdef}{g_fill("av", cy - (y1 - y0) / 2, cy + (y1 - y0) / 2)}</defs>'
            f'<rect width="{S}" height="{S}" fill="url(#avbg)"/>{gcircle}'
            f'<path fill="url(#avgf)" d="{g_path(cx, cy, size)}"/></svg>\n')
