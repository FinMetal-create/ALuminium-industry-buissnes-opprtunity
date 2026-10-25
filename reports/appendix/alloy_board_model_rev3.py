"""Alloy strategy memo, revision 3 -- single board model (Appendix B).

Run:  python3 alloy_board_model.py   (no dependencies)
Conventions: 2027-2040, cash flows at year index 0..13, NPV10 at 1 Jan 2027, 25% tax on
positive EBIT (no loss carry-forward), straight-line depreciation over 15 years on cumulative
capex from the first revenue year, working capital released in 2040, no terminal value.
Every [est.] input is labelled in the memo with range, owner and close date.
"""
Y = list(range(2027, 2041))
FX = 2155 / 2500                      # US$1 = EUR 0.862
LME = 2155.0
P1020_DP = LME + 320 / 1.16           # board basis duty-paid P1020, EUR/t

def irr(cf):
    f = lambda r: sum(c / (1 + r) ** i for i, c in enumerate(cf))
    grid = [i / 1000 for i in range(-500, 3000)]
    for a, b in zip(grid, grid[1:]):
        if f(a) * f(b) <= 0:
            lo, hi = a, b
            for _ in range(200):
                m = (lo + hi) / 2
                lo, hi = (lo, m) if f(lo) * f(m) <= 0 else (m, hi)
            return m
    return None

def line(capex, ebitda, wc=None, grant=None, sust=None, start=2027):
    """Return per-year series for one business line (pre-tax pieces)."""
    wc = wc or {}; grant = grant or {}; sust = sust or {}
    out = {k: [] for k in ("cx", "e", "dep", "wc", "g")}
    cum = 0; wcb = 0
    for y in Y:
        cx = capex.get(y, 0) + sust.get(y, 0); cum += cx
        w = wc.get(y, 0); wcb += w
        out["cx"].append(cx); out["e"].append(ebitda.get(y, 0))
        out["dep"].append(cum / 15 if y >= start else 0)
        out["wc"].append(w - (wcb if y == 2040 else 0)); out["g"].append(grant.get(y, 0))
    return out

def combine(*ls):
    return {k: [sum(l[k][i] for l in ls) for i in range(len(Y))] for k in ls[0]}

def evaluate(name, l, show=False, quiet=False):
    cfs = []; cum = 0; pb = None; rows = []
    first = next(i for i, c in enumerate(l["cx"]) if c > 0) if any(l["cx"]) else 0
    for i, y in enumerate(Y):
        tax = max(0, l["e"][i] - l["dep"][i]) * 0.25
        cf = l["e"][i] - tax - l["cx"][i] - l["wc"][i] + l["g"][i]
        cum += cf; cfs.append(cf)
        if pb is None and cum >= 0 and i > first: pb = y
        rows.append((y, -l["cx"][i], l["e"][i], -tax, -l["wc"][i], l["g"][i], cf, cum))
    npv = sum(c / 1.1 ** i for i, c in enumerate(cfs)); r = irr(cfs)
    if show:
        print(f"  {name}\n  year   capex  EBITDA    tax     WC  grant     CF    cum")
        for rr in rows: print("  %d %7.1f %7.1f %6.1f %6.1f %6.1f %6.1f %6.1f" % rr)
    if not quiet:
        print(f"  {name}: NPV10 {npv:.1f}  IRR {('%.1f%%' % (r * 100)) if r is not None else 'n/a'}  payback {pb}")
    return npv, r, pb

# ===================================================================== CASE A
print("== CASE A")
A1 = (1.5, 4.5, 3.0)
A2 = tuple(100 * p * 21.55 / 1000 for p in (8, 12, 10))
A3 = tuple(kt * 431 / 1000 for kt in (10, 30, 15))
# A4 restated on the named-buyer shortlist: 20 kt building at EUR 50/200/100 + 8 kt crash at EUR 100/300/175
A4 = (20 * 50 / 1000 + 8 * 100 / 1000, 20 * 200 / 1000 + 8 * 300 / 1000, 20 * 100 / 1000 + 8 * 175 / 1000)
A5 = (2.0, 5.0, 3.0)
gross = [sum(x[i] for x in (A1, A2, A3, A4, A5)) for i in range(3)]
net = [g * 0.8 for g in gross]
opex = (3.0, 2.0, 2.5)
print("  A4 low/high/base", [round(x, 2) for x in A4])
print("  gross low/high/base", [round(x, 2) for x in gross], " net", [round(x, 2) for x in net])
print("  EBITDA low/high/base", [round(net[i] - opex[i], 2) for i in range(3)])
ramp = {2027: 1.0, 2028: 8.0, 2029: 18.0}
def eA(full, op, scale=1.0):
    return {y: (min(ramp[y] * scale, full) if y < 2030 else full) - (1.5 if y == 2027 else op) for y in Y}
capA = {2027: 9, 2028: 10, 2029: 6, 2030: 2}; sustA = {y: 0.5 for y in Y if y >= 2031}
LA = line(capA, eA(net[2], 2.5), sust=sustA)
evaluate("A base, no grant", LA, show=True)
evaluate("A base + IF grant 4.2", line(capA, eA(net[2], 2.5), grant={2028: 2.1, 2029: 2.1}, sust=sustA))
evaluate("A +10% capex contingency", line({k: v * 1.1 for k, v in capA.items()}, eA(net[2], 2.5), sust=sustA))
evaluate("A low (capex 35, low levers, opex 3)", line({2027: 11, 2028: 13, 2029: 8, 2030: 3}, eA(net[0], 3.0, 0.73), sust=sustA))
evaluate("A high (capex 18, high levers, opex 2)", line({2027: 6, 2028: 7, 2029: 4, 2030: 1}, eA(net[1], 2.0, 1.47), sust=sustA))
evaluate("A scrap spread 5 points (A2 10.8)", line(capA, eA(net[2] - 0.8 * (21.55 - 10.775), 2.5), sust=sustA))
evaluate("A no A2", line(capA, eA(net[2] - 0.8 * 21.55, 2.5), sust=sustA))
evaluate("A A4 = 0 (no premium)", line(capA, eA(net[2] - 0.8 * A4[2], 2.5), sust=sustA))

# ===================================================================== CAPABILITY CENTRE + 90 DAY
capC = {2027: 0.4, 2028: 2.5, 2029: 1.0}                       # lab capex 3.9
eC = {2027: -(0.9 + 0.8 + 0.4 + 0.6), 2028: -(1.5 + 0.2 + 0.5 + 0.6), 2029: -(1.8 + 0.5 + 0.5)}
eC.update({y: -2.8 for y in Y if y >= 2030})
LC = line(capC, eC)
L90 = line({}, {2027: -1.9})                                   # 90-day plan, Q4 2026-Jan 2027, shown at t0
print("  capability gross 2027-29:", round(sum(capC.values()) - sum(eC[y] for y in (2027, 2028, 2029)), 2))

# ===================================================================== B-EXT
print("== B-EXT")
capE = {2027: 4.0, 2028: 3.5}; volE = {2027: 2, 2028: 8, 2029: 12}
def eE(kt, m): return {y: (volE.get(y, kt) if y < 2030 else kt) * m / 1000 - 0.5 for y in Y}
wcE = {2028: 0.5, 2029: 0.5}; susE = {y: 0.2 for y in Y if y >= 2030}
LE = line(capE, eE(15, 400), wc=wcE, sust=susE)
evaluate("B-ext base 15 kt x 400", LE, show=True)
evaluate("B-ext stress 12 x 300", line(capE, eE(12, 300), wc=wcE, sust=susE))
evaluate("B-ext spot 20 x 400", line(capE, eE(20, 400), wc=wcE, sust=susE))
evaluate("B-ext +10% capex", line({2027: 4.4, 2028: 3.85}, eE(15, 400), wc=wcE, sust=susE))

# ===================================================================== NHT (restated contribution)
print("== NHT contribution, EUR/t of alloy")
def nht_contrib(prem=269, prim=0.40, s_pct=0.85, bm=None, si=2100, adds=55, conv=150, frt=35, wshare=0.5, remelt=100, basis="B"):
    bm = BILLET_MID if bm is None else bm
    price = P1020_DP + prem
    p = 0.89 * prim * 1.01; s = 0.89 * (1 - prim) * 1.03
    scrap_mkt = s_pct * LME; wrought = P1020_DP - remelt
    pv = P1020_DP + (bm if basis == "C" else 0)
    sv = scrap_mkt if basis == "A" else (1 - wshare) * scrap_mkt + wshare * wrought
    return price - (p * pv + s * sv + 0.10 * si + adds + conv + frt), p, s
S_HIST = {2019: 290, 2020: 220, 2021: 440, 2022: 630, 2023: 280, 2024: 240, 2025: 350, 2026: 750}
S_MID = sum(S_HIST[y] for y in range(2019, 2026)) / 7
CONV_BIL, CONV_ROD = 115, 75
bilm = lambda s: s * FX - CONV_BIL
BILLET_MID = bilm(S_MID)
for b in "ABC":
    c, p, s = nht_contrib(basis=b)
    lo = nht_contrib(prem=180, prim=0.5, s_pct=0.90, bm=bilm(630), conv=180, wshare=0.7, basis=b)[0]
    hi = nht_contrib(prem=400, prim=0.3, s_pct=0.80, bm=bilm(220), conv=120, wshare=0.3, basis=b)[0]
    print(f"  basis {b}: {c:.0f} (low {lo:.0f}, high {hi:.0f})  primary {p:.3f} t/t, scrap {s:.3f} t/t")
C_P1020 = nht_contrib(basis="B")[0]; C_BIL = nht_contrib(basis="C")[0]; PRIM_PER_T = nht_contrib()[1]; SCRAP_PER_T = nht_contrib()[2]
NHT_DRAW_PER_T = PRIM_PER_T + 0.5 * SCRAP_PER_T          # primary + hub wrought half of the scrap
print(f"  P1020 DP {P1020_DP:.0f}; billet mid-cycle margin {BILLET_MID:.1f}; NHT price {P1020_DP+269:.0f}")
print("  sensitivities (basis B): prem 180/400 ->", [round(nht_contrib(prem=x)[0]) for x in (180, 400)],
      " wrought share 0/1 ->", [round(nht_contrib(wshare=x)[0]) for x in (0, 1)])

volN = {2029: 6, 2030: 18}
def nht_kt(y, full=30): return (volN[y] * full / 30) if y in volN else (full if y >= 2031 else 0)
def LN(full=30, m=None, cont=True, fixed=1.5, grant=None):
    m = C_P1020 if m is None else m
    k = 1.1 if cont else 1.0
    cap = {2027: 1.8 * k + 0.8, 2028: 16.2 * k + 2.5, 2029: 0.7}     # capex 18 (+10%) + qualification 4.0
    e = {y: nht_kt(y, full) * m / 1000 - (fixed if y >= 2029 else 0) for y in Y}
    wc = {2029: 6 * full / 30 * 2.7 * 0.08, 2030: 12 * full / 30 * 2.7 * 0.08, 2031: 12 * full / 30 * 2.7 * 0.08}
    return line(cap, e, wc=wc, grant=grant, sust={y: 0.4 for y in Y if y >= 2031}, start=2029)
print("== NHT cash tables and runs")
evaluate("NHT decision basis: 30 kt, P1020 basis, +10% contingency, no grant", LN(), show=True)
evaluate("NHT 30 kt, P1020 basis, no contingency", LN(cont=False))
evaluate("NHT 30 kt, billet basis, +10% contingency", LN(m=C_BIL))
evaluate("NHT 30 kt at memo-r2 EUR 280, +10% contingency", LN(m=280))
evaluate("NHT 30 kt, P1020 basis, contingency, IF grant 6.3", LN(grant={2028: 3.15, 2029: 3.15}))
evaluate("NHT 30 kt, P1020 basis, contingency, fixed 2.0", LN(fixed=2.0))
evaluate("NHT 28 kt, P1020 basis, contingency", LN(full=28))
evaluate("NHT low 20 kt, billet basis", LN(full=20, m=C_BIL))
evaluate("NHT high 40 kt x 350", LN(full=40, m=350))
def npv_of(l):
    return evaluate("", l, quiet=True)[0]
def be_vol(m, cont=True):
    lo, hi = 5, 200
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv_of(LN(full=mid, m=m, cont=cont)) < 0 else (lo, mid)
    return mid
def be_m(v):
    lo, hi = 0, 2000
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv_of(LN(full=v, m=mid)) < 0 else (lo, mid)
    return mid
print(f"  break-even volume: EUR 280 no-cont {be_vol(280, False):.1f} kt; EUR 280 cont {be_vol(280):.1f}; "
      f"P1020 basis cont {be_vol(C_P1020):.1f}; billet basis cont {be_vol(C_BIL):.1f}")
for v in (20, 25, 28, 30, 35, 40):
    m = be_m(v); print(f"  {v} kt: break-even contribution {m:.0f} EUR/t; premium over P1020 DP {269 + m - C_P1020:.0f}; vol x contrib {v*m/1000:.2f} EUR M/yr")

# ===================================================================== B-ROD, matched basis + liquid-metal ledger
print("== B-ROD")
A_HIST = {2019: (200, 150, 250), 2020: (170, 120, 220), 2021: (300, 220, 380), 2022: (450, 320, 600),
          2023: (230, 170, 300), 2024: (220, 160, 290), 2025: (300, 220, 380), 2026: (700, 450, 750)}
A_R2 = {2019: 385, 2020: 350, 2021: 550, 2022: 775, 2023: 500, 2024: 520, 2025: 585, 2026: 675}   # withdrawn r2 recall, midpoints
rodm = lambda a: a * FX - CONV_ROD
print("  year  S   A   rod-v-ingot  billet-v-ingot  rod-minus-billet")
for y in range(2019, 2027):
    a = A_HIST[y][0]; print(f"  {y} {S_HIST[y]:4d} {a:4d} {rodm(a):8.0f} {bilm(S_HIST[y]):10.0f} {rodm(a)-bilm(S_HIST[y]):10.0f}")
A_MID = sum(A_HIST[y][0] for y in range(2019, 2026)) / 7
print(f"  mid-cycle: S {S_MID:.0f}, A {A_MID:.1f}, rod {rodm(A_MID):.1f}, billet {bilm(S_MID):.1f}, diff {rodm(A_MID)-bilm(S_MID):.1f}")
print(f"  rod beats billet when A >= S - {(CONV_BIL-CONV_ROD)/FX:.0f} US$/t")
ORDER = [2026, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
CYC = {y: ORDER[(y - 2028) % 8] for y in Y}
RODKT = {2028: 15, 2029: 45}
def rod_kt(y): return RODKT.get(y, 57 if y >= 2030 else 0)
def b4(y): return 0 if y < 2030 else (1.875 if y == 2030 else 3.75)    # Al-Zr 7.5 kt x EUR 500
# liquid-metal ledger (primary metal, kt/yr)
EXT_INGOT = 30.0                                                          # sold outside today [est., 20-50]
A3_FREED = {2029: 5, 2030: 15}
def a3_freed(y): return A3_FREED.get(y, 15 if y >= 2031 else 0)
def ledger(y, nht=True, ext=EXT_INGOT, nht_full=30):
    spare = ext + a3_freed(y)
    # primary-equivalent draw: hub scrap diverted from billet is backfilled in billet with primary
    n = NHT_DRAW_PER_T * (nht_kt(y, nht_full) if nht else 0)
    need = rod_kt(y) * 1.01
    ingot = min(need, max(spare - n, 0))
    return spare, n, need, ingot, need - ingot
for nh in (True, False):
    sp, n, need, ing, bil = ledger(2031, nh)
    print(f"  ledger 2031 NHT={nh}: spare {sp:.1f}, NHT primary {n:.1f}, rod primary need {need:.1f}, from ingot {ing:.1f}, from billet {bil:.1f} ({bil/need*100:.0f}%)")
print(f"  NHT at 30 kt: primary {PRIM_PER_T*30:.1f} kt + hub wrought scrap {0.5*SCRAP_PER_T*30:.1f} kt (backfilled) = draw {NHT_DRAW_PER_T*30:.1f} kt; external cast scrap {0.5*SCRAP_PER_T*30:.1f} kt")
capR = {2027: 21.6 + 1.0, 2028: 14.4 + 1.0, 2029: 0.5}
def LR(margin, inc_b4=True, cap=capR):
    e = {y: rod_kt(y) * margin(y) / 1000 + (b4(y) if inc_b4 else 0) for y in Y}
    return line(cap, e, wc={2028: 2.0}, sust={y: 0.5 for y in Y if y >= 2030}, start=2028)
def capR_k(k): return {2027: 21.6 * k + 1.0, 2028: 14.4 * k + 1.0, 2029: 0.5}
IDLE = -44
def scenarios(AA, tag, show_blend=False):
    am = sum(AA[y] for y in range(2019, 2026)) / 7
    d = lambda yr: rodm(AA[yr]) - bilm(S_HIST[yr])
    def blend(nht, switch, ext=EXT_INGOT):
        def m(y):
            if rod_kt(y) == 0: return 0
            sp, n, need, ing, bil = ledger(y, nht, ext); fb = bil / need
            dd = d(CYC[y]); return rodm(AA[CYC[y]]) - fb * bilm(S_HIST[CYC[y]]) if not switch else (1 - fb) * rodm(AA[CYC[y]]) + fb * max(dd, IDLE)
        return m
    print(f"-- {tag}")
    res = {}
    res["S1"] = evaluate("S1' rod upgrades ingot, cycle replay", LR(lambda y: rodm(AA[CYC[y]])))
    res["S1m"] = evaluate("S1m rod upgrades ingot, mid-cycle", LR(lambda y: rodm(am)))
    res["S2"] = evaluate("S2' displaces billet, mid-cycle", LR(lambda y: rodm(am) - bilm(S_MID)))
    res["S3"] = evaluate("S3' displaces billet, 2026 matched pair", LR(lambda y: d(2026)))
    res["S4"] = evaluate("S4' displaces billet, cycle replay", LR(lambda y: d(CYC[y])))
    res["S5"] = evaluate("S5' switchable (idle -44/t), cycle replay", LR(lambda y: max(d(CYC[y]), IDLE)))
    res["L"] = evaluate("L  ledger, NHT built, billet tranche switchable", LR(blend(True, True)), show=show_blend)
    res["Lns"] = evaluate("L  ledger, NHT built, not switchable", LR(blend(True, False)))
    res["L0"] = evaluate("L0 ledger, no NHT, switchable", LR(blend(False, True)))
    res["Lc"] = evaluate("L  ledger, NHT built, switchable, +10% line contingency", LR(blend(True, True), cap=capR_k(1.1)))
    res["Lb4"] = evaluate("L  ledger, NHT built, switchable, no Al-Zr", LR(blend(True, True), inc_b4=False))
    for tot in (25, 75):
        evaluate(f"L  ledger, NHT built, switchable, spare primary {tot} kt", LR(blend(True, True, ext=tot - 15)))
    return res, am
central, am = scenarios({y: A_HIST[y][0] for y in A_HIST}, "CENTRAL matched adders", show_blend=True)
scenarios({**{y: A_HIST[y][0] for y in A_HIST}, 2026: 525}, "2026 adder 525 (0.7 x spread)")
scenarios({y: A_HIST[y][1] for y in A_HIST}, "LOW adders")
scenarios({y: A_HIST[y][2] for y in A_HIST}, "HIGH adders")
scenarios(A_R2, "Withdrawn r2 recalled adders (midpoints) -- upper-bound check")
# steady-state EBITDA (mid-cycle, central adders), ledger with NHT, 2031
sp, n, need, ing, bil = ledger(2031, True); fb = bil / need
e_blend_mid = 57 * (rodm(am) - fb * bilm(S_MID)) / 1000 + 3.75
e_s1_mid = 57 * rodm(am) / 1000 + 3.75; e_s2_mid = 57 * (rodm(am) - bilm(S_MID)) / 1000 + 3.75
print(f"  rod EBITDA 2031 mid-cycle: S1 {e_s1_mid:.2f}, ledger blend {e_blend_mid:.2f} (billet share {fb*100:.0f}%), S2 {e_s2_mid:.2f}")
e26 = 57 * (rodm(700) - fb * bilm(750)) / 1000 + 3.75
print(f"  rod EBITDA at 2026 prices, ledger blend: {e26:.2f}")

# ===================================================================== PORTFOLIO
print("== PORTFOLIO (combined tax)")
Lopt = line({}, {2027: -(0.8 + 0.2)})                     # NHT pre-gate qualification + B-rod studies, expensed
Lrod_opt = line({}, {2027: -0.2})
evaluate("Case A + full capability centre", combine(LA, LC), show=False)
evaluate("Capability centre alone (cost)", LC)
P0 = combine(LA, LE, LC, L90, Lopt)
evaluate("P0 committed: A + B-ext + capability + 90-day + pre-gate options", P0, show=True)
LAc = line({k: v * 1.1 for k, v in capA.items()}, eA(net[2], 2.5), sust=sustA)
LEc = line({2027: 4.4, 2028: 3.85}, eE(15, 400), wc=wcE, sust=susE)
evaluate("P0 with 10% contingency on A and B-ext", combine(LAc, LEc, LC, L90, Lopt))
LNd = LN()
P1 = combine(LA, LE, LC, L90, Lrod_opt, LNd)
evaluate("P1 = P0 + NHT (gate passed, decision basis)", P1)
def blend_central(y):
    if rod_kt(y) == 0: return 0
    sp, n, need, ing, bil = ledger(y, True); fb = bil / need
    AA = {k: v[0] for k, v in A_HIST.items()}; dd = rodm(AA[CYC[y]]) - bilm(S_HIST[CYC[y]])
    return (1 - fb) * rodm(AA[CYC[y]]) + fb * max(dd, IDLE)
P2 = combine(LA, LE, LC, L90, LNd, LR(blend_central, cap=capR_k(1.1)))
evaluate("P2 = P1 + B-rod (ledger blend, switchable, line contingency)", P2)

# ===================================================================== B-ROD gate tests
print("== B-ROD gate tests (central adders, ledger with NHT, switchable)")
AC = {k: v[0] for k, v in A_HIST.items()}
def blend_m(ext=EXT_INGOT, nht=True, linked=False, AA=AC):
    def m(y):
        if rod_kt(y) == 0: return 0
        sp, n, need, ing, bil = ledger(y, nht, ext); fb = bil / need
        yr = CYC[y]; a = max(AA[yr], S_HIST[yr] - (CONV_BIL - CONV_ROD) / FX) if linked else AA[yr]
        dd = rodm(a) - bilm(S_HIST[yr])
        return (1 - fb) * rodm(a) + fb * (max(dd, 0) if linked else max(dd, IDLE))
    return m
def be_spare(cap, inc_b4=True):
    lo, hi = 0, 80
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv_of(LR(blend_m(ext=mid - 15), inc_b4=inc_b4, cap=cap)) < 0 else (lo, mid)
    return mid
print(f"  break-even spare primary (incl. A3 15 kt): base capex {be_spare(capR):.1f} kt; +10% line {be_spare(capR_k(1.1)):.1f} kt; +10% and no Al-Zr {be_spare(capR_k(1.1), False):.1f} kt")
evaluate("L-BL ledger + billet-linked adder (A >= S - 46), +10% line", LR(blend_m(linked=True), cap=capR_k(1.1)))
evaluate("L-BL ledger + billet-linked adder, +10% line, no Al-Zr", LR(blend_m(linked=True), inc_b4=False, cap=capR_k(1.1)))
evaluate("L-BL ledger + billet-linked adder, LOW adders, +10% line", LR(blend_m(linked=True, AA={k: v[1] for k, v in A_HIST.items()}), cap=capR_k(1.1)))
evaluate("L at EUR 40M line (+contingency 10%)", LR(blend_m(), cap={2027: 24 * 1.1 + 1.0, 2028: 16 * 1.1 + 1.0, 2029: 0.5}))
print("  ledger by year (NHT built): year spare NHTprim rodNeed fromIngot fromBillet share")
for y in range(2028, 2032):
    sp, n, need, ing, bil = ledger(y, True)
    print(f"  {y} {sp:5.1f} {n:5.1f} {need:5.1f} {ing:5.1f} {bil:5.1f} {bil/need*100 if need else 0:4.0f}%")

# ===================================================================== INVESTMENT BUILD-UP (gross, EUR M)
print("== Investment build-up, committed (gross)")
rows = {
    "90-day plan (opex)": {2026: 1.9},
    "Case A capex and development": capA,
    "B-ext capex": capE, "B-ext working capital": wcE,
    "Capability centre (gross)": {2027: 3.1, 2028: 5.3, 2029: 3.8},
    "Contingency 10% of A + B-ext capex": {y: round(0.1 * (capA.get(y, 0) + capE.get(y, 0)), 2) for y in (2027, 2028, 2029, 2030)},
    "NHT pre-gate qualification (option)": {2027: 0.8},
    "B-rod studies and quotes (option)": {2027: 0.2},
}
tot = {}
for k, v in rows.items():
    for y, x in v.items(): tot[y] = tot.get(y, 0) + x
    print(f"  {k:40s} {sum(v.values()):6.2f}  {v}")
print("  committed by year", {y: round(x, 2) for y, x in sorted(tot.items())}, " total", round(sum(tot.values()), 2))
nht_post = {2027: 1.8 * 1.1, 2028: 16.2 * 1.1 + 2.5, 2029: 0.7}
print("  NHT option after gate: capex+qual", {y: round(v, 2) for y, v in nht_post.items()}, round(sum(nht_post.values()), 2), "+ WC 6.48")
rod = capR_k(1.1); rod[2028] += 2.0
print("  B-rod option incl. 10% line contingency + WC", {y: round(v, 2) for y, v in rod.items()}, round(sum(rod.values()), 2))
print("== Decision-basis cash tables for options")
evaluate("B-rod decision basis: ledger, NHT built, switchable, +10% line contingency", LR(blend_m(), cap=capR_k(1.1)), show=True)
evaluate("B-rod decision basis without Al-Zr", LR(blend_m(), inc_b4=False, cap=capR_k(1.1)))
evaluate("B-rod decision basis, LOW adders", LR(blend_m(AA={k: v[1] for k, v in A_HIST.items()}), cap=capR_k(1.1)))
evaluate("NHT at 35 kt, P1020 basis, contingency", LN(full=35))
evaluate("NHT at 30 kt x 273 (gate EUR 8.2M/yr)", LN(full=30, m=273))
