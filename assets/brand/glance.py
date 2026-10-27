"""At-a-glance panel and footer link pills for the GitHub profile (Stefano Theofanous, 2026-10-27:
"the part with the readme and the text isint fitting"). Same ribbon language as the stack panel.
Numbers come from the README's hidden AGENTS/TOKENS/SCALE lines, which goroshi-stats-totals keeps current.
Usage: python3.14 glance.py ASSETS_DIR README OUT_DIR"""
import re
import sys

from typeset import cap_height, path_d, width

A, README, OUT = sys.argv[1:4]
INTER = {w: f"{A}/Inter-{w}.ttf" for w in (400, 500, 600)}
PAL = {
    "dark": dict(ink="#f5f4ff", sub="#d9d6ff", head="#cbb8ff", card="#13143a", edge="#2b2a66", dot="#BC43D3"),
    "light": dict(ink="#11123a", sub="#2a2870", head="#46439F", card="#ffffff", edge="#d9d4ff", dot="#6b3fd1"),
}
W = 880


def stats():
    t = open(README).read()
    g = lambda k: re.search(rf"^{k}\s+::\s*(.+)$", t, re.M).group(1)  # noqa: E731
    sessions, subagents = re.findall(r"([\d,]+\+)", g("AGENTS"))[:2]
    tokens = re.search(r"([\d.,]+[KMBT]\+)", g("TOKENS")).group(1)
    crates, repos = re.findall(r"([\d,]+\+)", g("SCALE"))[:2]
    return [(sessions, "AI agent sessions"), (subagents, "orchestrated subagents"),
            (tokens, "tokens processed"), (crates, "Rust crates, one workspace")]


def wrap(text, font, size, maxw):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if width(font, trial, size) > maxw and cur:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + [cur]


def glance(mode):
    p = PAL[mode]
    out, y = [], 4
    out.append(f'<path fill="{p["head"]}" d="{path_d(INTER[600], "AT A GLANCE", 11.5, 2, y + 13, tracking=2.4)}"/>')
    y += 40
    intro = ("I build production systems in Rust: multi-agent engineering platforms, financial "
             "reconciliation that is exact to the cent, and GPU compute on hardware I own.")
    for line in wrap(intro, INTER[400], 18, W - 4):
        out.append(f'<path fill="{p["ink"]}" d="{path_d(INTER[400], line, 18, 2, y)}"/>')
        y += 28
    y += 6
    n, gap = 4, 12
    cw, ch = (W - gap * (n - 1)) / n, 96
    for i, (num, label) in enumerate(stats()):
        x = i * (cw + gap)
        out.append(f'<rect x="{x + .5:.2f}" y="{y + .5:.2f}" width="{cw - 1:.2f}" height="{ch - 1}" rx="14" fill="{p["card"]}" stroke="{p["edge"]}"/>')
        out.append(f'<path fill="{p["ink"]}" d="{path_d(INTER[600], num, 30, x + 20, y + 46)}"/>')
        out.append(f'<path fill="{p["sub"]}" d="{path_d(INTER[400], label, 13.5, x + 20, y + 72)}"/>')
    y += ch + 26
    out.append(f'<circle cx="7" cy="{y - 5:.2f}" r="4" fill="{p["dot"]}"/>')
    status = "Open to engineering roles and platform engagements · architecture reviews on request"
    out.append(f'<path fill="{p["ink"]}" d="{path_d(INTER[500], status, 15, 20, y)}"/>')
    H = y + 8
    alt = "At a glance. " + intro + " " + "; ".join(f"{a} {b}" for a, b in stats()) + ". " + status + "."
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{alt}">'
            f'<title>{alt}</title>' + "".join(out) + "</svg>\n"), alt


def pill(mode, label):
    p = PAL[mode]
    fs, h = 14.5, 38
    w = 20 + 10 + width(INTER[500], label, fs) + 20
    base = h / 2 + fs * cap_height(INTER[500]) / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h}" viewBox="0 0 {w:.0f} {h}" role="img" aria-label="{label}">'
            f'<rect x=".5" y=".5" width="{w - 1:.2f}" height="{h - 1}" rx="{(h - 1) / 2}" fill="{p["card"]}" stroke="{p["edge"]}"/>'
            f'<circle cx="22" cy="{h / 2}" r="4" fill="{p["dot"]}"/>'
            f'<path fill="{p["ink"]}" d="{path_d(INTER[500], label, fs, 34, base)}"/></svg>\n')


LINKS = [("site", "goroshillc.com"), ("linkedin", "LinkedIn"), ("email", "contact@goroshillc.com")]
for mode in ("dark", "light"):
    svg, alt = glance(mode)
    open(f"{OUT}/glance-{mode}.svg", "w").write(svg)
    for key, label in LINKS:
        open(f"{OUT}/link-{key}-{mode}.svg", "w").write(pill(mode, label))
print(alt)
