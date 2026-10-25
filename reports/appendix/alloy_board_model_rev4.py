"""Alloy strategy memo, revision 4 -- single board model (Appendix B). Sections R4.x reconcile with the group board paper v6.

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
# ===================================================================== REVISION 4 RECONCILIATIONS
# Reconciles the alloy memo with the approved group board paper (reports/ceo-strategy-memo.md v6):
#  (1) scrap hub (#2) is GO-to-FID-gate, FID Oct 2027, start-up Q4 2028 at 12.5% load, 70% 2029, 100% 2030;
#  (2) ICC renewal / potline curtailment, closure decision 31 Dec 2029;
#  (3) A1 netted against the approved furnace-robot metal-loss saving (EUR 7.3/t).
PT = 21.55                                   # EUR/t per LME point
def cfs_of(l):
    out = []
    for i, y in enumerate(Y):
        tax = max(0, l["e"][i] - l["dep"][i]) * 0.25
        out.append(l["e"][i] - tax - l["cx"][i] - l["wc"][i] + l["g"][i])
    return out
def npv_s(cf): return sum(c / 1.1 ** i for i, c in enumerate(cf))

print("== R4.1 A1 netted against the furnace-robot case (board paper 6(b): metal-loss EUR 7.3/t)")
ROBOT_METAL = 0.003 * P1020_DP
A1_R4 = []
for lab, sw, yp, cap, keep in (("low", 2.0, 0.20, 5, 0.3), ("high", 5.0, 0.50, 15, 0.5), ("base", 3.5, 0.35, 10, 0.4)):
    s = sw / 100 * 20 * PT; yv = yp / 100 * P1020_DP; sh = yv / (s + yv)
    yc = sh * cap; ch = cap - yc; ret = yc * keep; netpt = ch + ret
    A1_R4.append(netpt * 0.3)
    print(f"  {lab}: sweetening {s:.1f} + yield {yv:.1f} = {s+yv:.1f} EUR/t pre-cap; yield share {sh*100:.1f}%; on capped {cap}: "
          f"yield {yc:.2f}, charge {ch:.2f}, retained yield {ret:.2f} -> A1 net {netpt:.2f} EUR/t = {netpt*0.3:.2f} EUR M/yr (removed {(cap-netpt)*0.3:.2f})")
A1_R4 = tuple(A1_R4)
print(f"  robot metal-loss saving 0.30% x P1020 DP = {ROBOT_METAL:.2f} EUR/t; robot + A1 base = {ROBOT_METAL + A1_R4[2]/0.3:.1f} EUR/t (rev3 {ROBOT_METAL+10:.1f})")

print("== R4.2 scrap hub (#2) on the board paper's own model (life 2027-42, loss carry-forward)")
HY = list(range(2027, 2043))
HUB_LOAD = {2028: 0.125, 2029: 0.70}
HUB_CAP_BOARD = {2027: 25, 2028: 25}
HUB_CAP_FID = {2027: 5, 2028: 40, 2029: 5}           # post-FID spend (FID Oct 2027) [est.]
SLIP = dict(cap={2027: 5, 2028: 30, 2029: 15}, load={2029: 0.30, 2030: 0.85}, dep_start=2029, wc_year=2029)
def hub_load(y, load=None):
    load = HUB_LOAD if load is None else load
    return load.get(y, 1.0 if y > max(load) else 0.0)
def hub(u=0.9, spr=12, cap=None, load=None, dep_start=2028, cost=13.5, wc_year=2028, show=False):
    cap = HUB_CAP_BOARD if cap is None else cap
    full = 100 * u * spr * PT / 1000 - cost
    dep = sum(cap.values()) / 15; pool = 0; cfs = []
    for y in HY:
        L = hub_load(y, load); e = full * L; dev = 2.5 if y == 2027 else 0
        d = dep if y >= dep_start else 0; ti = e - dev - d
        if ti < 0: pool += -ti; tax = 0
        else: rel = min(pool, ti); pool -= rel; tax = 0.25 * (ti - rel)
        sus = 1.0 if y >= dep_start + 2 else 0
        wc = 10 if y == wc_year else (-10 if y == 2042 else 0)
        cf = e - dev - tax - cap.get(y, 0) - sus - wc; cfs.append(cf)
        if show: print(f"  {y} load {L:.3f} EBITDA {e:5.2f} tax {tax:4.2f} CF {cf:6.2f}")
    return npv_s(cfs), cfs, full
print(f"  board reproduction: 12 pts NPV {hub()[0]:.1f} (EBITDA at 100% {hub()[2]:.2f}); 14 pts NPV {hub(spr=14)[0]:.1f}; 15 pts (ladder) {hub(spr=15)[0]:.1f}")
print(f"  strict windows (75% upgraded): 12 pts {hub(0.75, 12)[0]:.1f}; 14 pts {hub(0.75, 14)[0]:.1f}; 15 pts {hub(0.75, 15)[0]:.1f}")
print(f"  post-FID capex phasing 5/40/5: 12 pts {hub(cap=HUB_CAP_FID)[0]:.1f}; 14 pts {hub(spr=14, cap=HUB_CAP_FID)[0]:.1f}; 15 pts {hub(spr=15, cap=HUB_CAP_FID)[0]:.1f}")
print(f"  start-up slips to Q3 2029: 12 pts {hub(**SLIP)[0]:.1f}; 14 pts {hub(spr=14, **SLIP)[0]:.1f}")
print(f"  R1 window value (75% -> 90% upgraded), board phasing: 12 pts {hub()[0]-hub(0.75,12)[0]:.1f} NPV, {100*0.15*12*PT/1000:.2f}/yr EBITDA")
print("  uplift per input t (gate 270):", {f"u{u} s{s}": round(u * s * PT) for u, s in ((0.75, 12), (0.9, 12), (0.75, 15), (0.9, 15), (0.9, 14))},
      " share needed at 15 pts:", round(270 / (15 * PT), 3))

print("== R4.3 Case A restated: A1 netted; A2 = casthouse-side down-shift net of hub output, on the hub's Board dates")
PH_A2 = {2028: 0.28, 2029: 0.70}                     # wide-window qualification ramp (building first)
def ph(y): return PH_A2.get(y, 1.0 if y >= 2030 else 0.0)
def a2_kt(y, C=130, hub_on=True, load=None, C_curt=None):
    c = C_curt if (C_curt is not None and y >= 2030) else C
    return ph(y) * max(0.0, min(100.0, c - (90 * hub_load(y, load) if hub_on else 0)))
A3KT = (10, 30, 15)
def caseA4(lv=2, C=130, pts=8, hub_on=True, load=None, C_curt=None, a1=None, a2on=True, a3on=True, a4on=True,
           cap=None, opex=None, grant=None, show=False, name=None, ret_levers=False):
    cap = capA if cap is None else cap; opex = (3.0, 2.0, 2.5)[lv] if opex is None else opex
    a1f = A1_R4[lv] if a1 is None else a1
    e = {}; lev = {}
    for y in Y:
        l1 = a1f * (1.25 / 3.0 if y == 2027 else 1.0)
        l2 = a2_kt(y, C, hub_on, load, C_curt) * pts * PT / 1000 if a2on else 0
        l3 = ((5 if y == 2029 else (A3KT[lv] if y >= 2030 else 0)) * 431 / 1000) if a3on else 0
        l4 = (A4[lv] if y >= 2030 else 0) if a4on else 0
        l5 = A5[lv] * {2028: 1.0 / 3.0, 2029: 2.2 / 3.0}.get(y, 1.0 if y >= 2030 else 0.0)
        g = l1 + l2 + l3 + l4 + l5; lev[y] = (l1, l2, l3, l4, l5, g)
        e[y] = 0.8 * g - (1.5 if y == 2027 else opex)
    L = line(cap, e, grant=grant, sust=sustA)
    if ret_levers: return L, lev
    if name: evaluate(name, L, show=show)
    return L
LA4, levA4 = caseA4(ret_levers=True)
print("  year  A1    A2(kt)  A2    A3    A4    A5   gross  net   EBITDA")
for y in range(2027, 2032):
    l1, l2, l3, l4, l5, g = levA4[y]
    print(f"  {y} {l1:5.2f} {a2_kt(y):6.1f} {l2:5.2f} {l3:5.2f} {l4:5.2f} {l5:5.2f} {g:6.2f} {0.8*g:5.2f} {0.8*g-(1.5 if y==2027 else 2.5):6.2f}")
for lv, lab, C, pts in ((0, "low", 100, 6), (1, "high", 190, 10), (2, "base", 130, 8)):
    _, lv_ = caseA4(lv=lv, C=C, pts=pts, ret_levers=True); g = lv_[2031]
    op = (3.0, 2.0, 2.5)[lv]
    print(f"  steady state 2031 {lab}: A1 {g[0]:.2f} A2 {g[1]:.2f} A3 {g[2]:.2f} A4 {g[3]:.2f} A5 {g[4]:.2f} gross {g[5]:.2f} haircut {-0.2*g[5]:.2f} net {0.8*g[5]:.2f} opex {-op:.2f} EBITDA {0.8*g[5]-op:.2f}")
print(f"  A2 share of gross (base 2031): {levA4[2031][1]/levA4[2031][5]*100:.1f}%; A2 base rev3 {A2[2]:.2f} -> rev4 {levA4[2031][1]:.2f} ({(levA4[2031][1]/A2[2]-1)*100:.0f}%)")
print("-- Case A rev4 runs")
evaluate("A4 decision basis: hub built on Board dates, C 130 kt, 8 pts net, no grant", LA4, show=True)
evaluate("A4 +10% capex contingency", caseA4(cap={k: v * 1.1 for k, v in capA.items()}))
evaluate("A4 with IF grant 4.2", caseA4(grant={2028: 2.1, 2029: 2.1}))
evaluate("A4 low: capex 35, C 100, 6 pts, low levers, opex 3", caseA4(lv=0, C=100, pts=6, cap={2027: 11, 2028: 13, 2029: 8, 2030: 3}))
evaluate("A4 high: capex 18, C 190, 10 pts, high levers, opex 2", caseA4(lv=1, C=190, pts=10, cap={2027: 6, 2028: 7, 2029: 4, 2030: 1}))
evaluate("A4 C 100 kt (hub built)", caseA4(C=100))
evaluate("A4 C 190 kt (hub built)", caseA4(C=190))
evaluate("A4 6 pts net", caseA4(pts=6)); evaluate("A4 10 pts net", caseA4(pts=10))
evaluate("A4 hub start-up slips to Q3 2029", caseA4(load=SLIP["load"]))
evaluate("A4 hub not built, A2 on 100 kt purchased at 8 pts (needs alternative scrap source)", caseA4(hub_on=False))
evaluate("A4 potlines curtailed from 2030: scrap-fed casthouse, C >= 190 kt from 2030 (hub built)", caseA4(C_curt=190))
evaluate("A4 A2 = 0", caseA4(a2on=False))
evaluate("A4 A4 = 0 (no premium)", caseA4(a4on=False))
evaluate("A4 fallback: no scrap source at all (A2 = A3 = 0; A1 + A4 + A5 only)", caseA4(a2on=False, a3on=False))
evaluate("A4 with A1 at rev3 EUR 10/t (robot overlap not netted)", caseA4(a1=3.0))
LA4_rescope = caseA4(a2on=False, a3on=False, a4on=False, cap={2027: 5.5}, opex=1.0)
evaluate("A4 re-scoped if T2 fails by 31 Oct 2027 (T1 spend 5.5 only; A1 + A5; opex 1.0)", LA4_rescope)
print("-- bridge rev3 -> rev4 (NPV10)")
b0 = npv_of(LA)
b1 = npv_of(caseA4(a1=3.0, pts=10, hub_on=False))
b2 = npv_of(caseA4(pts=10, hub_on=False))
b3 = npv_of(caseA4(pts=8, hub_on=False))
b4_ = npv_of(LA4)
print(f"  rev3 Case A {b0:.1f}; explicit lever ramp {b1:.1f} ({b1-b0:+.1f}); A1 netted vs robots {b2:.1f} ({b2-b1:+.1f}); "
      f"A2 at 8 pts net of quality cost on purchased grades {b3:.1f} ({b3-b2:+.1f}); hub output crowds out A2 tonnes on Board dates {b4_:.1f} ({b4_-b3:+.1f})")
print("== R4.4 Case A + scrap hub as one investment (Case A rev4 cash flows + board-paper hub model)")
cfA = cfs_of(LA4) + [0.0, 0.0]
def comb(hcfs, acfs=cfA):
    s = [a + h for a, h in zip(acfs, hcfs)]; return npv_s(s), irr(s), s
for lab, kw in (("12 pts (board base)", dict(spr=12)), ("14 pts (FID gate)", dict(spr=14)), ("15 pts (public ladder central)", dict(spr=15)),
                ("12 pts, strict windows 75% (no Case A)", dict(u=0.75, spr=12))):
    hn, hc, _ = hub(**kw); n, r, _ = comb(hc)
    print(f"  {lab}: hub {hn:.1f} + Case A {npv_s(cfA):.1f} = combined {n:.1f}  IRR {r*100:.1f}%")
for spr in (12, 14, 15):
    hn, hc, _ = hub(spr=spr, cap=HUB_CAP_FID); n, r, _ = comb(hc)
    print(f"  post-FID phasing {spr} pts: hub {hn:.1f}, combined {n:.1f} IRR {r*100:.1f}%")
hs, hcs, _ = hub(**SLIP); cAs = cfs_of(caseA4(load=SLIP["load"])) + [0, 0]
print(f"  start-up slips to Q3 2029, 12 pts: hub {hs:.1f} + Case A {npv_s(cAs):.1f} = {hs+npv_s(cAs):.1f}")
cA_nohub = cfs_of(caseA4(hub_on=False)) + [0, 0]
for spr in (12, 14, 15):
    hn, hc, _ = hub(spr=spr - 1.5); n, r, _ = comb(hc, cA_nohub)
    print(f"  hub output sold externally at -1.5 pts, casthouse keeps full A2 pool, {spr} pts: hub {hn:.1f} + Case A {npv_s(cA_nohub):.1f} = {n:.1f}")
print(f"  Case A with no hub: {npv_s(cA_nohub):.1f}")
for C in (100, 130, 190):
    cAc = cfs_of(caseA4(C=C)) + [0, 0]
    print(f"  casthouse scrap capacity C {C} kt: Case A {npv_s(cAc):.1f}; + hub 12 pts {comb(hub()[1], cAc)[0]:.1f}; + hub 14 pts {comb(hub(spr=14)[1], cAc)[0]:.1f}; "
          f"Case A without hub {npv_of(caseA4(C=C, hub_on=False)):.1f}")
cA_curt = cfs_of(caseA4(C_curt=190)) + [0, 0]
for spr in (12, 14):
    hn, hc, _ = hub(spr=spr); n, r, _ = comb(hc, cA_curt)
    print(f"  potlines curtailed from 2030 (C >= 190): hub {spr} pts {hn:.1f} + Case A {npv_s(cA_curt):.1f} = {n:.1f}")
def be_hub_internal(acfs, ref):
    lo, hi = 5, 30
    for _ in range(50):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if comb(hub(spr=m)[1], acfs)[0] < ref else (lo, m)
    return m
ref = npv_s(cA_nohub)
print(f"  spread at which Case A + hub (internal) = Case A without hub: {be_hub_internal(cfA, ref):.1f} pts; external offtake route: "
      f"{be_hub_internal(cA_nohub, ref) + 1.5:.1f} pts (hub NPV = 0 at -1.5 pts)")
print(f"  spread at which hub NPV = 0 (board model): ", end="")
lo, hi = 8, 20
for _ in range(50):
    m = (lo + hi) / 2; lo, hi = (m, hi) if hub(spr=m)[0] < 0 else (lo, m)
print(f"{m:.1f} pts")
s12 = comb(hub()[1])[2]
print("  combined cash flow, 12 pts (EUR M): year capexA+hub  CF  cum")
cum = 0; capH = {2027: 25 + 2.5, 2028: 25 + 10}
for i, y in enumerate(HY):
    cum += s12[i]
    if y <= 2031 or y in (2035, 2040, 2042): print(f"  {y} CaseA {cfA[i]:6.1f} hub {hub()[1][i]:6.1f} combined {s12[i]:6.1f} cum {cum:6.1f}")
for p in (0.5,):
    for spr in (12, 14):
        w = comb(hub(spr=spr)[1])[0]
        print(f"  expected value at P(FID) {p}, {spr} pts: {p*w+(1-p)*ref:.1f} (with hub {w:.1f}, without {ref:.1f})")

print("== R4.5 potlines curtailed from 2030: ledger scenario and gate tests (B-rod, NHT)")
AC4 = {k: v[0] for k, v in A_HIST.items()}; AL4 = {k: v[1] for k, v in A_HIST.items()}; AH4 = {k: v[2] for k, v in A_HIST.items()}
PEN = 115                                                  # remelt + logistics penalty vs liquid metal, EUR/t [est., 70-160]
def rod_curt(start, pen, AA=AC4, base=None):
    base = base or blend_m(AA=AA)
    def m(y):
        if rod_kt(y) == 0: return 0
        if y < start: return base(y)
        return max(rodm(AA[CYC[y]]) - pen, IDLE)
    return m
capD = capR_k(1.1)
print(f"  purchases if curtailed: rod {57*1.01:.1f} kt + NHT {PRIM_PER_T*30:.1f} kt = {57*1.01+PRIM_PER_T*30:.1f} kt x {P1020_DP:.0f} = EUR {(57*1.01+PRIM_PER_T*30)*P1020_DP/1000:.0f}M/yr")
evaluate("B-rod ref: decision basis, ICC renewed", LR(blend_m(), cap=capD))
for start in (2030, 2031):
    for pen in (70, 115, 160):
        evaluate(f"B-rod curtailed from {start}, penalty {pen}", LR(rod_curt(start, pen), cap=capD))
evaluate("B-rod curtailed 2030, pen 115, LOW adders", LR(rod_curt(2030, PEN, AA=AL4), cap=capD))
evaluate("B-rod curtailed 2030, pen 115, HIGH adders", LR(rod_curt(2030, PEN, AA=AH4), cap=capD))
evaluate("B-rod curtailed 2030, pen 115, no Al-Zr", LR(rod_curt(2030, PEN), inc_b4=False, cap=capD))
evaluate("B-rod curtailed 2030, pen 115, + EUR 10M solid-feed melter in 2029", LR(rod_curt(2030, PEN), cap={**capD, 2029: capD[2029] + 10}))
def be_pen():
    lo, hi = 0, 300
    for _ in range(50):
        m = (lo + hi) / 2; lo, hi = (m, hi) if npv_of(LR(rod_curt(2030, m), cap=capD)) > 0 else (lo, m)
    return m
def be_A(start=2030, pen=PEN, inc_b4=True, extra=0.0):
    lo, hi = 0, 2000; c = dict(capD); c[2029] = c.get(2029, 0) + extra
    for _ in range(60):
        a = (lo + hi) / 2; base = blend_m()
        def m(y, a=a):
            if rod_kt(y) == 0: return 0
            return base(y) if y < start else a * FX - CONV_ROD - pen
        lo, hi = (a, hi) if npv_of(LR(m, inc_b4=inc_b4, cap=c)) < 0 else (lo, a)
    return a
print(f"  B-rod break-even remelt penalty (curtailed 2030): {be_pen():.0f} EUR/t")
print(f"  B-rod break-even flat adder from 2030 (US$/t over P1020 DP): pen 115 {be_A():.0f}; + EUR 10M melter {be_A(extra=10):.0f}; no Al-Zr {be_A(inc_b4=False):.0f}; pen 160 {be_A(pen=160):.0f}; mid-cycle today {A_MID:.0f}")
print(f"  rod margin from purchased ingot, mid-cycle: {rodm(A_MID):.0f} - {PEN} = {rodm(A_MID)-PEN:.0f} EUR/t; EBITDA incl. Al-Zr {57*(rodm(A_MID)-PEN)/1000+3.75:.2f}")
def LNy(full=30, mfun=None, cont=True, fixed=1.5, cap_override=None):
    k = 1.1 if cont else 1.0
    capN = {2027: 1.8 * k + 0.8, 2028: 16.2 * k + 2.5, 2029: 0.7}
    e = {y: nht_kt(y, full) * mfun(y) / 1000 - (fixed if y >= 2029 else 0) for y in Y}
    wc = {2029: 6 * full / 30 * 2.7 * 0.08, 2030: 12 * full / 30 * 2.7 * 0.08, 2031: 12 * full / 30 * 2.7 * 0.08}
    return line(capN, e, wc=wc, sust={y: 0.4 for y in Y if y >= 2031}, start=2029)
DN = PRIM_PER_T * PEN
print(f"  NHT under curtailment: basis-B contribution {C_P1020:.0f} - primary {PRIM_PER_T:.3f} t x {PEN} = {C_P1020-DN:.0f} EUR/t (scrap and price formula unchanged)")
evaluate("NHT ref: decision basis, ICC renewed", LNy(mfun=lambda y: C_P1020))
for pen in (70, 115, 160):
    evaluate(f"NHT curtailed from 2030, pen {pen}", LNy(mfun=lambda y, d=PRIM_PER_T * pen: C_P1020 - (d if y >= 2030 else 0)))
evaluate("NHT curtailed from 2031, pen 115", LNy(mfun=lambda y: C_P1020 - (DN if y >= 2031 else 0)))
evaluate("NHT curtailed 2030, pen 115, with IF grant 6.3 (not a decision basis)",
         line({2027: 1.8 * 1.1 + 0.8, 2028: 16.2 * 1.1 + 2.5, 2029: 0.7}, {y: nht_kt(y) * (C_P1020 - (DN if y >= 2030 else 0)) / 1000 - (1.5 if y >= 2029 else 0) for y in Y},
              wc={2029: 1.296, 2030: 2.592, 2031: 2.592}, grant={2028: 3.15, 2029: 3.15}, sust={y: 0.4 for y in Y if y >= 2031}, start=2029))
def be_mN(v, d):
    lo, hi = 0, 2000
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv_of(LNy(full=v, mfun=lambda y: mid - (d if y >= 2030 else 0))) < 0 else (lo, mid)
    return mid
def be_vN(m, d):
    lo, hi = 5, 300
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv_of(LNy(full=mid, mfun=lambda y: m - (d if y >= 2030 else 0))) < 0 else (lo, mid)
    return mid
print(f"  NHT break-even volume at {C_P1020:.0f}: ICC renewed {be_vN(C_P1020, 0):.1f} kt; curtailed 2030 {be_vN(C_P1020, DN):.1f} kt")
print("== R4.6 NHT gate restated: volume-specific, binding on BOTH ledger cases, + EUR 15/t margin, volume counted 25-40 kt")
MARGIN = 15
print("  kt  BE renewed  BE curtailed  gate contrib (max+15, up to 5)  price over P1020 DP  gate x vol  NPV renewed  NPV curtailed")
import math
GATE = {}
for v in (25, 28, 30, 32, 35, 38, 40):
    m0 = be_mN(v, 0); m1 = be_mN(v, DN); g = math.ceil((max(m0, m1) + MARGIN) / 5) * 5; GATE[v] = g
    n0 = npv_of(LNy(full=v, mfun=lambda y, g=g: g)); n1 = npv_of(LNy(full=v, mfun=lambda y, g=g: g - (DN if y >= 2030 else 0)))
    print(f"  {v}  {m0:6.0f}  {m1:6.0f}  {g:6d}  {269 + g - C_P1020:6.0f}  {v*g/1000:5.2f}  {n0:5.1f}  {n1:5.1f}")
print(f"  rev3 gate check: 30 kt x 273 = {30*273/1000:.2f} vs 40 kt break-even product {40*be_mN(40,0)/1000:.2f} (rev3 floor 8.2 sits below it)")
evaluate("NHT 30 kt at rev3 example EUR 273, curtailed 2030", LNy(mfun=lambda y: 273 - (DN if y >= 2030 else 0)))
evaluate("NHT 30 kt at rev4 gate contribution, curtailed 2030", LNy(mfun=lambda y: GATE[30] - (DN if y >= 2030 else 0)))
evaluate("NHT 30 kt at rev4 gate contribution, ICC renewed", LNy(mfun=lambda y: GATE[30]))
print("  board paper #5 trigger (OEM nomination >= 20 kt/yr) at today's EUR 231:", end=" ")
evaluate("NHT 20 kt, 231, ICC renewed", LNy(full=20, mfun=lambda y: C_P1020))
print("-- both options built, curtailed 2030 (pen 115), NPV10 sum:",
      round(npv_of(LR(rod_curt(2030, PEN), cap=capD)) + npv_of(LNy(mfun=lambda y: C_P1020 - (DN if y >= 2030 else 0))), 1),
      " vs ICC renewed:", round(npv_of(LR(blend_m(), cap=capD)) + npv_of(LNy(mfun=lambda y: C_P1020)), 1))

print("== R4.7 PORTFOLIO, revision 4 basis (combined tax; Case A rev4)")
evaluate("rev3 reference P0", P0)
evaluate("Case A rev4 + full capability centre", combine(LA4, LC))
P0_4 = combine(LA4, LE, LC, L90, Lopt)
evaluate("P0 rev4 committed: A + B-ext + capability + 90-day + pre-gate options", P0_4, show=True)
LA4c = caseA4(cap={k: v * 1.1 for k, v in capA.items()})
evaluate("P0 rev4 with 10% contingency on A and B-ext", combine(LA4c, LEc, LC, L90, Lopt))
evaluate("P0 rev4, hub not built (A2 on purchased 100 kt)", combine(caseA4(hub_on=False), LE, LC, L90, Lopt))
eEc = {y: v - (15 * PEN / 1000 if y >= 2030 else 0) for y, v in eE(15, 400).items()}
LE_curt = line(capE, eEc, wc=wcE, sust=susE)
evaluate("B-ext, potlines curtailed from 2030 (1370/6101 billet from purchased P1020, -115/t on 15 kt)", LE_curt)
evaluate("P0 rev4, potlines curtailed from 2030 (Case A C >= 190; B-ext remelt penalty)", combine(caseA4(C_curt=190), LE_curt, LC, L90, Lopt))
evaluate("P0 rev4, Case A low case", combine(caseA4(lv=0, C=100, pts=6, cap={2027: 11, 2028: 13, 2029: 8, 2030: 3}), LE, LC, L90, Lopt))
evaluate("P0 rev4, fallback (no scrap source: A2 = A3 = 0)", combine(caseA4(a2on=False, a3on=False), LE, LC, L90, Lopt))
evaluate("P0 rev4, Case A re-scoped after a failed T2", combine(LA4_rescope, LE, LC, L90, Lopt))
P1_4 = combine(LA4, LE, LC, L90, Lrod_opt, LNd)
evaluate("P1 rev4 = P0 + NHT (decision basis, ICC renewed)", P1_4)
P2_4 = combine(LA4, LE, LC, L90, LNd, LR(blend_central, cap=capR_k(1.1)))
evaluate("P2 rev4 = P1 + B-rod (ICC renewed)", P2_4)
LNcur = LNy(mfun=lambda y: C_P1020 - (DN if y >= 2030 else 0))
evaluate("P2 rev4, potlines curtailed from 2030 (Case A C>=190; NHT and B-rod on purchased P1020, pen 115)",
         combine(caseA4(C_curt=190), LE_curt, LC, L90, LNcur, LR(rod_curt(2030, PEN), cap=capD)))
print("  2031 EBITDA: Case A rev4", round(LA4["e"][4], 2), "; B-ext", round(LE["e"][4], 2), "; capability", round(LC["e"][4], 2),
      "; committed", round(LA4["e"][4] + LE["e"][4] + LC["e"][4], 2))
