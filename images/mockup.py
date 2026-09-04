#!/usr/bin/env python3
"""Genera los screenshots del README como SVG fieles a cada theme.
Render: Chrome headless (qlmanage deforma el aspect ratio de los SVG).
Uso: python3 mockup.py  (desde images/), luego render.sh
"""
W, H = 1280, 800
MONO = "SF Mono, Menlo, monospace"
UI = "-apple-system, Helvetica, sans-serif"

VARIANTS = {
    "dark": dict(
        chrome="#27282F", editor="#282C2F", divider="#393B49", accent="#AC0340",
        status="#AC0340", statusfg="#FFFFFF", seltab="#282C2F", tabfg="#FFFFFF",
        tabdim="#95999F", uifg="#D6DAE0", uidim="#95999F", selrow="#455A64",
        selrowfg="#FFFFFF", linehl="#2E3236", ln="#5C6166", lnact="#E4A900",
        FG="#D6DAE0", K="#E11E4D", S="#82BCCE", F="#5498CC", C="#E4A900",
        N="#E9BE44", COM="#7A8288",
    ),
    "light": dict(
        chrome="#F5F5F5", editor="#FFFFFF", divider="#E0E0E0", accent="#AC0340",
        status="#AC0340", statusfg="#FFFFFF", seltab="#FFFFFF", tabfg="#282C2F",
        tabdim="#6E7379", uifg="#282C2F", uidim="#6E7379", selrow="#DCEFFE",
        selrowfg="#282C2F", linehl="#F2F6F9", ln="#B3B3B3", lnact="#AC0340",
        FG="#282C2F", K="#AC0340", S="#3D7A99", F="#2E6E9E", C="#B77800",
        N="#9E7000", COM="#95999F",
    ),
    "vakyro": dict(
        chrome="#1C1B19", editor="#201D24", divider="#352D40", accent="#F3C5D9",
        status="#6F5198", statusfg="#FFFFFF", seltab="#201D24", tabfg="#FFFFFF",
        tabdim="#A99BB8", uifg="#E8E3EE", uidim="#A99BB8", selrow="#6F5198",
        selrowfg="#FFFFFF", linehl="#2A2531", ln="#5E5568", lnact="#F3C5D9",
        FG="#E8E3EE", K="#BD8BE0", S="#F3C5D9", F="#82BCCE", C="#E9BE44",
        N="#F2D06B", COM="#7C7385",
    ),
}


def build(name, P):
    def T(x, y, parts, size=15, font=MONO, weight="normal"):
        sp = "".join(
            f'<tspan fill="{c}" font-style="{st}">{t}</tspan>' for t, c, st in parts
        )
        return (
            f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" xml:space="preserve">{sp}</text>'
        )

    FG, K, S, F, C, N, COM = P["FG"], P["K"], P["S"], P["F"], P["C"], P["N"], P["COM"]
    n = "normal"
    code = [
        [(f"# Vauxoo {name.capitalize()} — official brand palette", COM, "italic")],
        [("from ", K, n), ("odoo ", FG, n), ("import ", K, n), ("api, fields, models", FG, n)],
        [],
        [("class ", K, n), ("SaleOrder", C, n), ("(models.", FG, n), ("Model", C, n), ("):", FG, n)],
        [("    _inherit ", FG, n), ("= ", FG, n), ('"sale.order"', S, n)],
        [],
        [("    vauxoo_score ", FG, n), ("= fields.", FG, n), ("Float", C, n), ("(default=", FG, n), ("100.0", N, n), (")", FG, n)],
        [],
        [("    @api.depends", F, n), ("(", FG, n), ('"order_line.price_total"', S, n), (")", FG, n)],
        [("    def ", K, n), ("_compute_score", F, n), ("(", FG, n), ("self", C, n), ("):", FG, n)],
        [("        for ", K, n), ("order ", FG, n), ("in ", K, n), ("self", C, n), (":", FG, n)],
        [("            order.vauxoo_score ", FG, n), ("= ", FG, n), ("sum", F, n), ("(", FG, n)],
        [("                line.price_total ", FG, n), ("for ", K, n), ("line ", FG, n), ("in ", K, n), ("order.lines", FG, n)],
        [("            )", FG, n)],
    ]
    rows = []
    y0, lh, xg, xc = 210, 26, 258, 300
    for i, line in enumerate(code):
        rows.append(T(xg, y0 + i * lh, [(f"{i+1:>2}", P["lnact"] if i == 9 else P["ln"], n)], size=14))
        if line:
            rows.append(T(xc, y0 + i * lh, line))

    files = ["sale_order.py", "__manifest__.py", "models/", "views/", "security/"]
    tree = []
    for i, f in enumerate(files):
        yy = 150 + i * 30
        if i == 0:
            tree.append(f'<rect x="48" y="{yy-20}" width="212" height="28" fill="{P["selrow"]}"/>')
            tree.append(T(64, yy, [(f, P["selrowfg"], n)], size=14, font=UI))
        else:
            tree.append(T(64, yy, [(f, P["uifg"], n)], size=14, font=UI))

    svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<rect width="{W}" height="{H}" rx="12" fill="{P["editor"]}"/>
<rect width="{W}" height="40" rx="12" fill="{P["chrome"]}"/><rect y="20" width="{W}" height="20" fill="{P["chrome"]}"/>
<circle cx="26" cy="20" r="7" fill="#E11E4D"/><circle cx="50" cy="20" r="7" fill="#E4A900"/><circle cx="74" cy="20" r="7" fill="#3AA55D"/>
{T(540, 25, [(f"vauxoo_sale — Vauxoo {name.capitalize()}", P["uidim"], n)], size=13, font=UI)}
<rect y="40" width="48" height="{H-68}" fill="{P["chrome"]}"/>
<rect x="0" y="60" width="3" height="36" fill="{P["accent"]}"/>
{T(14, 84, [("⧉", P["uifg"], n)], size=20, font=UI)}
{T(14, 140, [("⌕", P["uidim"], n)], size=20, font=UI)}
{T(14, 196, [("⎇", P["uidim"], n)], size=20, font=UI)}
<rect x="48" y="40" width="212" height="{H-68}" fill="{P["chrome"]}"/>
{T(64, 74, [("EXPLORER", P["uidim"], n)], size=11, font=UI, weight="bold")}
{T(64, 110, [("▾ VAUXOO_SALE", P["uifg"], n)], size=13, font=UI, weight="bold")}
{"".join(tree)}
<line x1="260" y1="40" x2="260" y2="{H-28}" stroke="{P["divider"]}" stroke-width="1"/>
<rect x="260" y="40" width="{W-260}" height="44" fill="{P["chrome"]}"/>
<rect x="260" y="40" width="180" height="44" fill="{P["seltab"]}"/>
<rect x="260" y="40" width="180" height="3" fill="{P["accent"]}"/>
{T(286, 68, [("sale_order.py", P["tabfg"], n)], size=14, font=UI)}
{T(470, 68, [("models.py", P["tabdim"], n)], size=14, font=UI)}
<rect x="260" y="418" width="{W-260}" height="27" fill="{P["linehl"]}"/>
{"".join(rows)}
<rect y="{H-28}" width="{W}" height="28" fill="{P["status"]}"/>
{T(16, H-9, [("⎇ main   ✓ prettier", P["statusfg"], n)], size=13, font=UI)}
{T(960, H-9, [(f"Ln 10, Col 9   Python   Vauxoo {name.capitalize()}", P["statusfg"], n)], size=13, font=UI)}
</svg>'''
    open(f"screenshot-{name}.svg", "w").write(svg)
    print(f"screenshot-{name}.svg")


for name, P in VARIANTS.items():
    build(name, P)
