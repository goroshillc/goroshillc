"""At-a-glance panel and footer link pills for the GitHub profile (Stefano Theofanous, 2026-10-27:
"the part with the readme and the text isint fitting"). Same ribbon language as the stack panel.
Numbers come from the README's hidden AGENTS/TOKENS/SCALE lines, which goroshi-stats-totals keeps current.
Usage: python3.14 glance.py ASSETS_DIR README OUT_DIR"""
import re
import sys

from typeset import cap_height, path_d, width

A, README, OUT = sys.argv[1:4]
INTER = {w: f"{A}/Geist-{w}.ttf" for w in (400, 500, 600)}  # Geist (SIL OFL 1.1)
PAL = {
    "dark": dict(ink="#F4F5FF", sub="#D3D8FF", head="#AEB8FF", card="#0E1440", edge="#26307A", dot="#5B45F0"),
    "light": dict(ink="#0E1240", sub="#232A80", head="#3B33C4", card="#FFFFFF", edge="#D2D7FF", dot="#4B3FD8"),
}
W = 880


def stats():
    t = open(README).read()
    g = lambda k: re.search(rf"^{k}\s+::\s*(.+)$", t, re.M).group(1)  # noqa: E731
    sessions, subagents = re.findall(r"([\d,]+\+)", g("AGENTS"))[:2]
    tokens = re.search(r"([\d.,]+[KMBT]\+)", g("TOKENS")).group(1)
    crates, repos = re.findall(r"([\d,]+\+)", g("SCALE"))[:2]
    return dict(sessions=sessions, subagents=subagents, tokens=tokens, crates=crates, repos=repos)


def cards():
    s = stats()
    return [
        ("AI agent platform", f"{s['sessions']} sessions, {s['subagents']} subagents and {s['tokens']} tokens across model families."),
        ("Cent-exact bookkeeping", "Statements and receipts reconciled to the cent for operating businesses, every figure traced to its source."),
        ("GPU compute in Rust", "Hand-written Metal kernels measured at 294\u00a0GB/s and 2.8\u00a0TFLOP/s\u00a0FP32."),
        ("Rust at scale", f"{s['crates']} crates in one workspace across {s['repos']} repositories, every change formatted, linted and tested."),
    ]


def wrap(text, font, size, maxw):
    lines, cur = [], ""
    for word in text.split(" "):  # split on plain spaces only; NBSP keeps a number with its unit
        trial = f"{cur} {word}".strip()
        if width(font, trial, size) > maxw and cur:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + [cur]


def glance(mode):
    """'What I build': a 2x2 capability grid, each card a title and one line of evidence
    (Stefano 2026-10-27: "the at a glance senences also is kind of strange")."""
    p = PAL[mode]
    out, y = [], 4
    out.append(f'<path fill="{p["head"]}" d="{path_d(INTER[600], "WHAT I BUILD", 11.5, 2, y + 13, tracking=2.4)}"/>')
    y += 34
    gap, cw, pad = 14, (W - 14) / 2, 22
    items = cards()
    rows = [items[0:2], items[2:4]]
    for row in rows:
        bodies = [wrap(body, INTER[400], 14.5, cw - 2 * pad) for _, body in row]
        ch = pad + 20 + 12 + 22 * max(len(b) for b in bodies) + pad - 6
        for i, ((title, _), lines) in enumerate(zip(row, bodies)):
            x = i * (cw + gap)
            out.append(f'<rect x="{x + .5:.2f}" y="{y + .5:.2f}" width="{cw - 1:.2f}" height="{ch - 1:.2f}" rx="14" fill="{p["card"]}" stroke="{p["edge"]}"/>')
            out.append(f'<rect x="{x + pad:.2f}" y="{y + pad - 2:.2f}" width="22" height="3" rx="1.5" fill="{p["dot"]}"/>')
            out.append(f'<path fill="{p["ink"]}" d="{path_d(INTER[600], title, 19, x + pad, y + pad + 26)}"/>')
            ly = y + pad + 26 + 26
            for line in lines:
                out.append(f'<path fill="{p["sub"]}" d="{path_d(INTER[400], line, 14.5, x + pad, ly)}"/>')
                ly += 22
        y += ch + gap
    y += 14
    out.append(f'<circle cx="7" cy="{y - 5:.2f}" r="4" fill="{p["dot"]}"/>')
    status = "Open to engineering roles and platform engagements. contact@goroshillc.com"
    out.append(f'<path fill="{p["ink"]}" d="{path_d(INTER[500], status, 15, 20, y)}"/>')
    H = y + 8
    alt = "What I build. " + " ".join(f"{a}: {b}" for a, b in items) + " " + status
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
