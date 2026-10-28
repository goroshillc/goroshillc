"""At-a-glance panel and footer link pills for the GitHub profile (Stefano Theofanous, 2026-10-27:
"the part with the readme and the text isint fitting"). Same ribbon language as the stack panel.
Dated usage floors come from the README's hidden AGENTS/TOKENS lines; refresh requires a reviewed source update.
Usage: python3.14 glance.py ASSETS_DIR README OUT_DIR"""

import re
import sys

from typeset import cap_height, path_d, width

A, README, OUT = sys.argv[1:4]
INTER = {w: f"{A}/Geist-{w}.ttf" for w in (400, 500, 600)}  # Geist (SIL OFL 1.1)
PAL = {
    "dark": {
        "ink": "#F7F4FF",
        "sub": "#DDD6FF",
        "head": "#B9A8FF",
        "card": "#120F40",
        "edge": "#2E267A",
        "dot": "#6A35FF",
    },
    "light": {
        "ink": "#140E40",
        "sub": "#2E2380",
        "head": "#4A2FC4",
        "card": "#FFFFFF",
        "edge": "#DAD2FF",
        "dot": "#5A35E0",
    },
}
W = 880


def stats():
    with open(README) as source:
        t = source.read()

    def group(pattern: str, value: str) -> str:
        match = re.search(pattern, value, re.MULTILINE)
        if match is None:
            raise ValueError("required profile measurement is missing or malformed")
        return match.group(1)

    def g(key: str) -> str:
        return group(rf"^{key}\s+::\s*(.+)$", t)

    sessions, subagents = re.findall(r"([\d,]+\+)", g("AGENTS"))[:2]
    tokens = group(r"([\d.,]+[KMBT]\+)", g("TOKENS"))
    measured = group(r"\(measured ([^)]+)\)", g("TOKENS"))
    return {
        "sessions": sessions,
        "subagents": subagents,
        "tokens": tokens,
        "measured": measured,
    }


def cards():
    s = stats()
    return [
        (
            "AI agent platform",
            f"{s['sessions']} recorded sessions, {s['subagents']} subagents; {s['tokens']} cache-inclusive tokens (as of {s['measured']}).",
        ),
        (
            "Cent-exact bookkeeping",
            "Statements and receipts reconciled to the cent for operating businesses, every figure traced to its source.",
        ),
        (
            "GPU compute in Rust",
            "Hand-written Metal kernels and a native bandwidth and FP32 benchmark tool.",
        ),
        (
            "Rust at scale",
            "Rust services and native tools, with scoped formatting, lint and test gates.",
        ),
    ]


def wrap(text, font, size, maxw):
    lines, cur = [], ""
    for word in text.split(
        " "
    ):  # split on plain spaces only; NBSP keeps a number with its unit
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
    out.append(
        f'<path fill="{p["head"]}" d="{path_d(INTER[600], "WHAT I BUILD", 11.5, 2, y + 13, tracking=2.4)}"/>'
    )
    y += 34
    gap, cw, pad = 14, (W - 14) / 2, 22
    items = cards()
    rows = [items[0:2], items[2:4]]
    for row in rows:
        bodies = [wrap(body, INTER[400], 14.5, cw - 2 * pad) for _, body in row]
        ch = pad + 20 + 12 + 22 * max(len(b) for b in bodies) + pad - 6
        for i, ((title, _), lines) in enumerate(zip(row, bodies)):
            x = i * (cw + gap)
            out.append(
                f'<rect x="{x + 0.5:.2f}" y="{y + 0.5:.2f}" width="{cw - 1:.2f}" height="{ch - 1:.2f}" rx="14" fill="{p["card"]}" stroke="{p["edge"]}"/>'
            )
            out.append(
                f'<rect x="{x + pad:.2f}" y="{y + pad - 2:.2f}" width="22" height="3" rx="1.5" fill="{p["dot"]}"/>'
            )
            out.append(
                f'<path fill="{p["ink"]}" d="{path_d(INTER[600], title, 19, x + pad, y + pad + 26)}"/>'
            )
            ly = y + pad + 26 + 26
            for line in lines:
                out.append(
                    f'<path fill="{p["sub"]}" d="{path_d(INTER[400], line, 14.5, x + pad, ly)}"/>'
                )
                ly += 22
        y += ch + gap
    y += 14
    out.append(f'<circle cx="7" cy="{y - 5:.2f}" r="4" fill="{p["dot"]}"/>')
    status = (
        "Open to engineering roles and platform engagements. contact@goroshillc.com"
    )
    out.append(f'<path fill="{p["ink"]}" d="{path_d(INTER[500], status, 15, 20, y)}"/>')
    H = y + 8
    alt = "What I build. " + " ".join(f"{a}: {b}" for a, b in items) + " " + status
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{alt}">'
        f"<title>{alt}</title>" + "".join(out) + "</svg>\n"
    ), alt


def pill(mode, label):
    p = PAL[mode]
    fs, h = 14.5, 38
    w = 20 + 10 + width(INTER[500], label, fs) + 20
    base = h / 2 + fs * cap_height(INTER[500]) / 2
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h}" viewBox="0 0 {w:.0f} {h}" role="img" aria-label="{label}">'
        f'<rect x=".5" y=".5" width="{w - 1:.2f}" height="{h - 1}" rx="{(h - 1) / 2}" fill="{p["card"]}" stroke="{p["edge"]}"/>'
        f'<circle cx="22" cy="{h / 2}" r="4" fill="{p["dot"]}"/>'
        f'<path fill="{p["ink"]}" d="{path_d(INTER[500], label, fs, 34, base)}"/></svg>\n'
    )


LINKS = [
    ("site", "goroshillc.com"),
    ("linkedin", "LinkedIn"),
    ("email", "contact@goroshillc.com"),
]
for mode in ("dark", "light"):
    svg, alt = glance(mode)
    with open(f"{OUT}/glance-{mode}.svg", "w") as output:
        output.write(svg)
    for key, label in LINKS:
        with open(f"{OUT}/link-{key}-{mode}.svg", "w") as output:
            output.write(pill(mode, label))
print(alt)
