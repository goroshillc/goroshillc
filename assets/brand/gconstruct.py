"""The Goroshi G logomark (Stefano Theofanous, 2026-10-27: "actually logo", "max clean", Solo Leveling).

A constructed G, drawn as one filled outline so its cuts stay razor-crisp at any size:
- a thick circular bowl, open at the upper right;
- the top terminal and the crossbar's inner end are cut on a sharp diagonal (a blade edge), which
  keeps it clearly distinct from the familiar geometric G with square, radial terminals;
- the crossbar sits on the horizontal axis and runs inward from the bowl.
"""
import math


def g_outline(cx, cy, R, t, gap_deg=40, bar=0.62, cut=0.9, n=96):
    """Closed path data for the G. R = outer radius, t = stroke thickness.

    gap_deg: how far above the 3 o'clock axis the top terminal sits (outer edge).
    bar:     crossbar reach from the outer edge toward the center, as a fraction of R.
    cut:     diagonal cut length of both blade terminals, as a fraction of t.
    """
    Ri = R - t
    pt = lambda r, a: (cx + r * math.cos(a), cy + r * math.sin(a))  # noqa: E731  (screen coords, y down)
    a_top = math.radians(-gap_deg)
    # Outer edge: from the top terminal, the long way round (over the top, down the left, along the
    # bottom) to the 3 o'clock axis. Decreasing angle in screen coordinates.
    outer = [pt(R, a_top - (2 * math.pi - (-a_top)) * i / n) for i in range(n + 1)]
    outer[-1] = (cx + R, cy)
    # Crossbar: top edge on the axis minus half a stroke, bottom edge t below that.
    y_top, y_bot = cy - t * 0.42, cy + t * 0.58
    x_in = cx + R - R * bar
    # Where the crossbar's bottom edge meets the inner edge of the bowl.
    xb = cx + math.sqrt(max(Ri * Ri - (y_bot - cy) ** 2, 0))
    ab = math.atan2(y_bot - cy, xb - cx)
    # Inner edge: back from the crossbar to the top terminal (increasing angle toward a_top + 2pi).
    a_inner_top = a_top - math.radians(14)   # inner point of the top cut sits further round: a diagonal blade
    a_from = ab
    a_to = a_inner_top + 2 * math.pi if a_inner_top < 0 else a_inner_top
    inner = [pt(Ri, a_from + (a_to - a_from) * i / n) for i in range(n + 1)]
    pts = outer + [(cx + R, y_top), (x_in, y_top), (x_in - t * cut, y_bot), (xb, y_bot)] + inner
    d = "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + " Z"
    return d
