# Alloy Design in the Age of AI: Strategy Memo (revision 5)

**To:** CEO, Executive Committee, Board Technology & Strategy Committee
**From:** CTO and Chief Strategy Officer
**Date:** 25 October 2026 (revised after the CEO's review of revision 4, which scored 8.8/10)

**Board planning basis (used in every business case):**
- LME aluminium is US$2,500/t, which is EUR 2,155/t at EUR/USD 1.16 (US$1 = EUR 0.862). One LME point is EUR 21.55/t.
- Duty-paid P1020 (Rotterdam) is LME + US$320/t (EUR 276), so **P1020 DP = EUR 2,431/t**.
- Normalised LME copper is US$9,500/t [est., CFO to sign off]. The Cu/Al ratio on the board basis is therefore **3.80x**.
- Spot on 15 Oct 2026 was Cu US$14,400/t and Al US$2,940/t, a ratio of 4.90x ([S&P Global, 15 Oct 2026](https://www.spglobal.com/energy/en/pricing-benchmarks/our-methodology/corrections/20261015)). EUR/USD was 1.1215 ([ECB](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)). Spot prices are used only for upside sensitivities.
- **Same-basis rule.** A ratio or a margin comparison may only combine a same-date or same-basis pair. This applies to premiums as well as to metal prices: each year's rod adder is set against that same year's billet spread.
- **Metal-ledger rule.** Every tonne of primary metal and every tonne of scrap is given to exactly one use. Each use is valued against the alternative that the ledger actually gives up (Section 4.3).
- **Group-paper rule.** Any asset that already sits in the approved board paper (`reports/ceo-strategy-memo.md`, v6, 21 Oct 2026) is taken on that paper's own status, dates and model. There are three such assets:
  - the scrap hub (#2): GO to FID gate, FID at M12 (Oct 2027);
  - the furnace charge-and-skim robots (#1): GO, EUR 15.1/t, of which EUR 7.3/t is metal loss;
  - ICC renewal and the potlines: no-ICC contingency plan due at M9 (Jul 2027), closure decision on 31 Dec 2029.

  This memo claims none of their value, and every gate below is consistent with their dates.
- **Contracted-tonnes rule (new in revision 5).** Every tonne of scrap that a value lever books must be a tonne that a gate secures by contract. Case A's A2 tonnes in each year are `min(contracted lower-rung tonnes, qualification ramp × purchased pool)`. A3 is booked on its contracted 15 kt. T2 condition (c) contracts exactly those tonnes (Section 4.5).
- **Valuation:**
  - 10% hurdle rate.
  - 25% tax on positive EBIT, with no loss carry-forward.
  - Straight-line depreciation over 15 years, starting from first revenue.
  - Horizon 2027–2040, with no terminal value. Working capital is released in 2040.
  - NPVs are discounted to 1 Jan 2027.
  - The hub keeps the board paper's own conventions: life to 2042 and loss carry-forward.
  - **Every investment decision must clear the hurdle with 10% capex contingency included and without grants. Investments that depend on liquid metal must also clear it with the potlines curtailed from 2030 (Section 4.6).**
- **Reproducibility (Appendix B):** every cash table, NPV, IRR, ledger line and build-up in this memo is printed by one dependency-free script in the strategy repository:
  - Script: `/home/user/ALuminium-industry-buissnes-opprtunity/reports/appendix/alloy_board_model.py`
  - Full output: `/home/user/ALuminium-industry-buissnes-opprtunity/reports/appendix/alloy_board_model_output.txt`
  - Sections **R5.1–R5.7** of the output are new. Everything above them is byte-identical to the revision 4 output. The revision 4 script and output are kept beside them as `alloy_board_model_rev4.py` and `alloy_board_model_output_rev4.txt`. The revision 3 copies are also kept.
  - The CFO will mirror the script into the finance model repository by 6 Nov 2026 (open item 1).

**Evidence convention:**
- Linked figures are sourced.
- **[est.]** marks an estimate from the research reports.
- **[CTO est.]** marks an assumption added in this memo.
- **[calc]** marks a value derived in the board model.
- **[unverified]** marks a figure from a secondary source or from recollection that we could not check against the primary source.
- **[recall]** marks a fact recalled from our own knowledge and not re-verified this round.

**Data limits in this revision:**
- Direct page access (WebFetch) was refused for fastmarkets.com, argusmedia.com, alcircle.com, spglobal.com, recyclingeurope.org, european-metals.eu, brd.nrw.de, speira.com and carbon-pulse (DNS failure or proxy 403).
- The revision 5 figures on scrap contracts, scrap prices and curtailed casthouses therefore come from **search-engine extracts of the cited URLs**. They are treated as secondary until the owner in Section 11.3 opens the primary document.
- **No public EU scrap contract discloses its price as a % of LME.** The Fastmarkets MB-AL-0426 (taint/tabor) and MB-AL-0282 (UK old rolled) levels are behind the paywall. Every affected number is labelled, given a range, and assigned an owner and a close date in Section 11.3.

### What changed in revision 5

| CEO point | Fix | Where |
|---|---|---|
| (1) The no-hub route is valued at one size (115 kt) and gated at another (55 kt). With the contract actually required, Case A is EUR 42.1M | **Case A is now booked on contracted tonnes in both routes.** The script reproduces your re-run (EUR 42.1M). Your re-run applies the ramp to the contract; revision 5 caps A2 at `min(contracted, ramp × pool)` instead. The two routes then give the same value at the same contracted tonnes. On revision 4 levers the no-hub route at 55 kt is EUR 44.8M. On revision 5 levers it is **EUR 31.1M** | 4.5, 5.4, 5.4A |
| (1) The 80.6 / 76.2 / 59.0 / 68.6 figures and the 16.5 / 14.3-point thresholds rest on 115 kt the gate never secures | **All restated as a function of contracted tonnes** (40–115 kt). The table shows the 55 kt gate minimum and a 70 kt central contracting estimate taken from public deal evidence. 80.6 → 31.1 (55 kt) / 40.7 (70 kt). 76.2 → 26.6 / 36.2. 59.0 / 68.6 → 27.1 / 36.7 (55 kt) and 32.0 / 41.5 (70 kt). Internal threshold 16.5 → **12.8** (55 kt) / **13.8** (70 kt). The external threshold stays at 14.3 | 5.4A |
| (1) The recommended amendment to the hub FID test rests on the 115 kt basis | **The 16.5-point amendment is withdrawn.** At the tonnes we can realistically contract, the hub's own 14-point FID gate already binds. A narrower test linked to tonnage applies only if procurement contracts more than 72.5 kt before M12 | 5.4A |
| (1) "Sorted wrought" must not count toward a down-shift test | **T2(c) is now grade-specific.** The A2 tonnes must be lower-rung grades (mixed wrought / old rolled, taint/tabor). They must replace the same tonnage of current higher-grade purchases. Sorted wrought, LIBS-sorted 6xxx and clean extrusion scrap do not count toward A2, because they are the grades A2 moves away from | 4.5 |
| (1) Can ~115 kt be contracted without a hub? | **Public evidence says probably not on firm terms.** The largest disclosed EU deal is about 25 kt/yr for 3 years (TSR to Novelis). We estimate that 40–90 kt/yr can be contracted by 31 Oct 2027, central 70 kt. 115 kt probably costs a security-of-supply premium of 1–2 points. That gives Case A EUR 59.0M / 50.9M instead of 67.0M | 5.4A, 5.5 |
| (2) A3 at 80% of LME contradicts our own ladder (83–90% for billet-usable grades); A3 is 29% of gross value and not gated | **A3 is re-valued on published post-consumer prices.** The anchors are Fastmarkets MB-AL-0405 (post-consumer 95/5 6063 at LME − EUR 278/t, about 89% of LME), plus Argus and Recycling Europe for taint/tabor. A 50/50 billet/sheet blend is 85.75% of LME, a gross spread of 14.25 points. We deduct 5.3 points of casthouse cost against hot metal (melt loss, remelt energy, QA). That leaves **9 net points = EUR 194/t (range 6–13)**. A3 falls from EUR 6.46M to **EUR 2.91M/yr** | 5.2 |
| (2) A1 sweetening uses the same EUR 431/t | **A1 sweetening is re-priced at the A3 net spread.** A1 falls from EUR 7.8/t to **EUR 6.7/t (EUR 2.00M/yr)**. The T2(a) shadow-run threshold moves from EUR 4/t to **EUR 3/t**, which keeps it at 63% of the base charge-cost saving, as before | 5.2, 4.5 |
| (2) No gate checks A3's spread, and no owner or date | **T2(d) now verifies both spreads:** A2 ≥6 net points and **A3 ≥6 net points**. The evidence is contract prices, MB-AL-0405/0426 history and a 2 × 50 t casthouse trial. Case A is re-booked at the verified spreads before release. Owners: Head of Scrap Procurement (15 Dec 2026), Casthouse Manager (31 Mar 2027), CFO (re-booking at T2) | 4.5, 11.3 |
| Public analogue for C ≥190 kt under curtailment | **Added (Section 4.6).**<br>- Speira Rheinwerk reached about 166 kt of dedicated recycling melt after two furnace projects costing EUR 85M.<br>- Trimet Essen runs about 100 kt of scrap alongside full potlines.<br>- Slovalco and Aldel, the stranded sites, melted only 21–31% of their former primary, and both made losses.<br>**C ≥190 kt is therefore booked only as a funded option-C configuration**, with EUR 36–110M of melt capex in the board paper, not here. The curtailed headline now uses the stranded case | 4.6 |
| Consequence | **Case A NPV10 EUR 31.1M, IRR 31.3%** (was EUR 45.3M).<br>**Committed portfolio NPV10 EUR 26.6M, IRR 21.0%** (was EUR 40.9M); with contingency EUR 23.8M.<br>2031 EBITDA is EUR 14.8M (was 17.9).<br>These figures are below your 30–37M ladder range, because we also deduct casthouse costs from A3 and re-price A1. The portfolio still clears the hurdle. The envelope (EUR 54.05M), the EUR 18.4M tranche and the GO / WATCH / NO-GO slate are unchanged | 4.2, 4.4, 4.5 |

---

## 1. Executive summary

1. **AI shortens alloy design. It does not shorten qualification.**
   - Composition screening falls from 2–4 years to 3–12 months. MIT evaluated 40 compositions where conventional design would need more than 1 million simulations ([MIT](https://news.mit.edu/index%2Ephp/2025/printable-aluminum-alloy-sets-strength-records-may-enable-lighter-aircraft-parts-1007)). ORNL's RidgeAlloy went from concept to a full-scale HPDC part in 15 months ([ASM](https://www.asminternational.org/?p=1161707)).
   - Customer qualification is unchanged: 2–4 years in automotive and 5–15 years in aerospace ([NASA](https://ntrs.nasa.gov/api/citations/20110013659/downloads/20110013659.pdf)).
   - An automotive alloy now takes about 3–5 years in total, against 10–20 years classically [est.]. **We start customer programmes now, with named customers.**

2. **Our advantage is integration, not algorithms.**
   - Smelter, casthouse, rolling and extrusion can share one data chain: sorter spectra, then melt chemistry, then certified properties.
   - The group board paper's 100 kt/yr AI sorting hub (#2) would add to that chain. It is **GO to FID gate, not approved capex**: FID is in Oct 2027, and the IRR is 7.7% at 12 points.
   - Hydro (CREATe, US$2.5M over 5 years; [Recycling Today](https://www.recyclingtoday.com/news/hydro-university-of-michigan-partnership)) and Constellium (CirConAl, GBP 10M; [APC](https://www.apcuk.co.uk/impact/funded-projects/constellium-circular-and-constant-aluminium-circonal/)) are building this through universities. We build it in-house and keep it proprietary.

3. **Business case A (scrap-tolerant alloys plus AI casthouse blending) remains GO, now booked on contracted tonnes and on published scrap prices.**
   - **What changed.**
     - A2 is booked only on the lower-rung tonnes T2 contracts (40 kt/yr in the hub route).
     - A3 is valued at 9 net points (EUR 194/t), not 20.
     - A1's sweetening value uses the same 9 points.
   - **EBITDA is EUR 12.1M/yr from 2030** after EUR 2.5M/yr of opex (range EUR 2.8–33.7M).
   - **Investment is EUR 27.0M** over 2027–30 (range EUR 18–35M), before grants.
   - **Returns (decision basis: hub built on its Board dates, 55 kt contracted, no grant):** NPV10 **EUR 31.1M**, IRR **31.3%**, payback 2032. With 10% contingency: NPV EUR 28.9M, IRR 28.4%.
   - **Carrying the whole capability centre**, Case A still returns NPV EUR 10.3M and IRR 15.9%.
   - **At the T2(d) floors** (A2 and A3 both verified at only 6 net points, with contingency) Case A is EUR 18.6M, IRR 22.2%.
   - **The all-low stack does not clear:** NPV −EUR 17.9M. That is why only EUR 5.5M of Case A spend is released at day 90, and the scrap-dependent spend waits for T2.
   - **Bridge from revision 4 (EUR M):**

     | Step | NPV10 after the step | Change |
     |---|---|---|
     | Revision 4 | 45.3 | |
     | A2 capped at the 40 kt contracted in 2029 (was 46.9 kt) | 44.8 | −0.6 |
     | A3 at 9 net points on the public post-consumer ladder (was 20) | 32.7 | −12.0 |
     | A1 sweetening re-priced at the A3 spread | **31.1** | −1.6 |

   - **Shares of gross lever value:** A2 38%, A3 16% (was 29%).
     - With A2 at zero, Case A is NPV EUR 2.5M (IRR 11.8%) and barely clears.
     - A2 and its contracts are therefore the case, and T2 tests them directly.
   - **Named targets:**
     - Building systems: Hueck, Aluprof and Reynaers first; Schüco and Kawneer as a second wave.
     - Crash management: BMW with Benteler; Volvo Cars in reserve.
     - The A4 premium of EUR 3.4M/yr is unchanged (Section 5.5).

4. **Case A and the hub, shown as one investment, on contracted tonnes (Section 5.4A).**
   - **Combined NPV10 at the board paper's 12 points is EUR 23.2M** (IRR 14.7%) for EUR 89.5M of combined spend.
   - At the hub's 14-point FID gate it is EUR 42.3M. 14 points is also the central Zorba-to-sorted spread on the revision 5 ladder.
   - **Without the hub, Case A is worth what we can contract:**
     - EUR 31.1M at 55 kt, the T2 minimum. This is identical to the hub route.
     - EUR 40.7M at the 70 kt central estimate.
     - EUR 67.0M only if 115 kt is contracted at 8 net points.
   - **The 16.5-point crowd-out threshold is withdrawn.** On contracted tonnes, the hub adds group value inside our casthouse above these spreads:
     - **12.8 points at 55 kt**, which is the hub's own break-even;
     - **13.8 points at 70 kt**.

     Both are below the hub's 14-point FID gate, so **the existing gate already protects the group**. The external-offtake threshold stays at 14.3 points.
   - **If the potlines are curtailed from 2030:**
     - With a stranded casthouse, the pair is worth EUR 19.9–39.0M (12/14 points).
     - It reaches EUR 57.1–76.2M only in the funded option-C configuration with 100 kt of A2 contracted.
   - **T2 now requires contracts for the tonnes we book**, whichever way the hub decision goes: ≥40 kt/yr of lower-rung grades plus ≥15 kt/yr of A3 grades, on terms of 3 years or more.

5. **Quick win in 6–12 months: an AI charge optimiser (lever A1), netted against the furnace robots and re-priced.**
   - The approved robot case owns furnace-practice melt loss: EUR 7.3/t, 0.30%.
   - A1 keeps the charge-cost saving plus the chemistry-driven share of yield.
   - Sweetening is now valued at the A3 net spread (EUR 194/t). That gives **EUR 6.7/t (range 3.1–10.8), or EUR 2.00M/yr on 300 kt**, for EUR 2.5M. Payback is about 1.6 years.
   - Combined, the robots and A1 claim EUR 14.0/t (about 0.39 pp of metal loss).
   - Speira is already rolling out SMS Metallics Optimizer at three sites ([Foundry Planet](https://www.foundry-planet.com/d/digital-solution-enhances-efficiency-reduces-costs-and-promotes-sustainable-circular-economy/)).

6. **Business case B: B-ext is GO; B-rod stays WATCH, also tested with the potlines curtailed.** (Unchanged from revision 4.)
   - **B-ext (busbar and thermal extrusions on our existing presses): GO.** Capex EUR 7.5M; EBITDA EUR 5.5M/yr; NPV10 EUR 19.1M; IRR 49.2%; payback 2030.
     - It survives curtailment: if 1370/6101 billet has to be made from purchased P1020, NPV is EUR 12.1M.
   - **B-rod (60 kt rod line): WATCH.**
     - Decision basis (ledger, 10% contingency, matched adders): **NPV −EUR 0.5M, IRR 9.8%**.
     - **With the potlines curtailed from 2030:** −EUR 1.8M at a EUR 115/t remelt penalty. Break-even is a EUR 108/t penalty or a US$313/t adder.
     - Its gate is **30 Sep 2027, after the M9 contingency plan**. GO requires NPV10 ≥ 0 under both ledgers. Otherwise it waits for the 31 Dec 2029 ICC decision.

7. **The NHT structural casting alloy stays WATCH, behind the volume-specific gate.** (Unchanged from revision 4.)
   - **Contribution** is EUR 231/t on a P1020 basis. If the potlines close it is **EUR 190/t**, because only the 0.36 t of primary per tonne must then be bought and remelted.
   - **Returns at 30 kt** (contingency included, no grant):

     | Ledger | NPV10 | IRR | Break-even volume |
     |---|---|---|---|
     | ICC renewed | −EUR 4.1M | 7.3% | 35.0 kt |
     | Potlines curtailed from 2030 | −EUR 8.8M | 3.8% | 43.3 kt |

   - **Gate.**
     - The signed contribution must be at least the binding break-even at the signed volume, plus EUR 15/t.
     - Counted volume is 25–40 kt.
     - Example: 30 kt needs ≥EUR 325/t, a price of ≥P1020 DP + EUR 363/t.
   - **This gate supersedes the board paper's 20 kt nomination trigger.** Only the EUR 0.8M pre-gate qualification option is spent in 2027, the same amount as in the board paper.

8. **Capability:** an alloy-informatics centre of 6 FTE rising to 12.
   - Cost is **EUR 12.2M gross over 2027–29** (est. range EUR 8–14M), then EUR 2.8M/yr. The NPV of this cost is −EUR 26.1M.
   - EUR 1.2M of Horizon co-funding if MAT-PROD-22 is won.
   - In 2027 we buy software and lab access. We build our own rapid-prototyping lab only in 2028, behind a gate.

9. **Commercial model: own the chemistry window, sell the metal, license only outside the EU.**
   - The branded premium is EUR 50–300/t [est.].
   - Non-EU royalties are EUR 60–140/t, which is 2.2–5.2% of a EUR 2,700/t licensee net sales price.
   - Families to clear: Rheinfelden (Castasil-37, Magsimal-59, Castaduct), Trimet Trimal-37, Alcoa C611, Tesla, Kaiser US 2023/0416879 A1, and Novelis, Constellium and Hydro.
   - The four outstanding publication numbers come from IP counsel by 6 Nov 2026.
   - The white space is **Fe 0.4–0.8% scrap-based NHT and 6xxx windows tied to in-line sorted-scrap chemistry**.

10. **Funding:**
    - **Horizon CL4-2027-01-MAT-PROD-22:**
      - The deadline is **2 Feb 2027** according to a third-party aggregator ([euacc.ai](https://www.euacc.ai/calls/HORIZON-CL4-2027-01-MAT-PROD-22)). It is [unverified] on the official portal; the Grants Office confirms it by 30 Oct 2026.
      - Our realistic grant share is **EUR 1.2M** (range 0.5–1.5).
    - **Innovation Fund small-scale (IF26):**
      - Case A casthouse adaptation: EUR 4.2M.
      - NHT: EUR 6.3M, filed but accepted only if the NHT gate passes.
    - **Grants never enter a decision.**

11. **Portfolio:**
    - **Committed (GO) portfolio:**
      - **EUR 14.8M/yr EBITDA in 2031** for **EUR 54.1M gross investment**, or EUR 48.7M net if all committed grants are awarded.
      - **Portfolio NPV10 EUR 26.6M, IRR 21.0%, payback 2033**, including the capability centre and the 90-day plan (Section 4.4). With contingency: NPV EUR 23.8M, IRR 19.3%.
    - **Across the group paper's states, on contracted tonnes:**

      | State | Portfolio NPV10 |
      |---|---|
      | Hub not built, 55 kt contracted (T2 minimum) / 70 kt (central estimate) / 115 kt (only if contracted) | EUR 26.6M / 36.2M / 62.5M |
      | Potlines curtailed from 2030, stranded casthouse on existing melt (C 130) / option-C configuration at 40 kt A2 | EUR 16.4M / 19.7M (alloy portfolio only) |
      | Potlines curtailed, stranded casthouse with C only 100 kt | −EUR 1.0M |
      | A2 and A3 verified only at the T2(d) floors (6 points each) | EUR 16.3M |
      | T2 fails and Case A is re-scoped | +EUR 2.2M (IRR 11.7%) |
      | All-low stack, with every gate passed | −EUR 22.6M |

    - **Gated options:**
      - NHT: +EUR 5.4M/yr for EUR 29.5M.
      - B-rod: +EUR 6.8M/yr mid-cycle for EUR 44.1M.
      - Both are NPV-negative on both ledgers at today's terms. Adding them lowers portfolio NPV to EUR 23.5M.
    - **The day-90 tranche is EUR 18.4M** for 2027. Only EUR 10.6M is released unconditionally, and it contains **no NHT or B-rod capex**.
    - **WATCH:** NHT, B-rod, Al-Zr HTLS, high-conductivity HPDC and robot-grade alloys, 5/7 crossover sheet, twin-roll casting, Al-Ce.
    - **NO-GO:** Al-Sc master alloy, AM powder/WAAM (atomiser or tolling), a greenfield battery-foil mill, our own Al-Li production, high-entropy alloys, generative-crystal-model R&D.

---

## 2. How AI changes alloy development

### 2.1 Proven, promising and hype

| Status | Technique / claim | Evidence | Decision relevance for us |
|---|---|---|---|
| **Proven** | CALPHAD + ML surrogates + Bayesian optimisation for composition search | MIT: 40 compositions instead of >1M simulations; 50% stronger than design without ML ([MIT](https://news.mit.edu/index%2Ephp/2025/printable-aluminum-alloy-sets-strength-records-may-enable-lighter-aircraft-parts-1007)). Citrine/HRL: 11.5M combinations narrowed to 100 candidates, commercial about 2 years after publication ([Citrine](https://CITRINE.IO/wp-content/uploads/2021/04/Case-Study-HRL-AM-powder-development.pdf)). PatSnap: 800,000 compositions and 36 experiments for +12.6% modulus ([PatSnap](https://www.patsnap.com/resources/blog/articles/ai-accelerated-alloy-design-landscape-2026/)), summary only | **Core tool.** Applies directly to designing for scrap windows |
| **Proven** | ICME shortens the whole programme | QuesTek M54: about 6 years against 15–20 typical ([NIST](https://www.nist.gov/document/materialsinnovationcasestudyquestek090616pdf)). GE: 15 to 9 years ([NIST/MGI](https://www.nist.gov/node/1507161)) | Realistic expectation: roughly halves the time, not 100x |
| **Proven** | ML rationalisation of an alloy portfolio | Brunel: 42 6xxx grades reduced to 10 "optimal alloys" using 292 datasets ([Springer](https://link.springer.com/article/10.1007/s40831-025-01112-4)) | Low cost. Enlarges scrap pools |
| **Proven** | Scrap-tolerant alloy design | ORNL RidgeAlloy: more than 2M calculations, 15 months to a full-scale part ([ASM](https://www.asminternational.org/?p=1161707)). ML-guided Sc addition to recycled Al validated at +4.37% UTS ([BIT](https://pure.bit.edu.cn/zh/publications/design-of-high-strength-and-ductile-recycled-al-alloys-by-machine/)). JMI 2024: >190 W/m·K and >220 MPa thermal alloy ([JMI](https://www.oaepublish.com/articles/jmi.2024.21)) | **Our main use case** |
| **Proven, scaling** | High-throughput and self-driving labs | MPIE: 50 conditions in about 5 days ([MPIE](https://www.mpie.de/4151172/combinatorial-metallurgy-and-processing)). AlloyBot: >100 compositions/week ([TMS](https://www.programmaster.org/PM/PM.nsf/ApprovedAbstracts/C51BFD5FCD57FCD785258CBB00102E33)). Texas A&M ARM-MIP: US$24.9M, 50 rising to more than 200 alloys/month, industry access on negotiated IP terms ([TAMU](https://stories.tamu.edu/news/2026/08/05/texas-am-to-build-self-driving-laboratory-for-metals-open-to-researchers-nationwide/)) | Buy access first, build later |
| **Proven, narrow** | ML charge optimisation in the casthouse | SMS Metallics Optimizer: forecasts tramp elements before melting and picks the cheapest compliant mix; claims lower energy and "raw material losses" **without a published % or EUR/t** ([SMS](https://www.sms-group.com/product/metallics-optimizer)). GHI ALEA: "up to 20% shorter cycle time and lower gas use" ([GHI](https://www.ghifurnaces.com/digitalize/)) | Documented value is **charge cost first, energy second**. No vendor publishes a yield figure (Section 5.2, A1) |
| **Promising** | LLM multi-agent design assistants | EGA at ICSOBA 2025 ([ICSOBA](https://icsoba.org/assets/files/publications/2025/Papers/CH08%20-%20Physics-Aware%20Multi-Agent%20AI%20Framework%20for%20Property%20Prediction%20and%20Design%20of%20Aluminium%20Alloys.pdf)). AlloyGPT ([ASM](https://asm.confex.com/asm/imat2025/webprogram/Paper63852.html)). MIT PNAS 2025 ([DSpace](https://dspace.mit.edu/handle/1721.1/163619)) | They orchestrate tools; they are not autonomous designers. Pilot only |
| **Hype for us** | Generative crystal models (MatterGen, GNoME) | Some "discoveries" are disordered versions of known compounds ([HU Berlin](https://edoc.hu-berlin.de/18452/38430)). Our properties come from microstructure and processing | NO-GO. No spend |
| **Discount heavily** | Vendor claims of "100x faster" and "days or weeks" | Phaseshift ([BetaKit](https://betakit.com/phaseshift-technologies-raises-4-1-million-cad-to-fuse-material-discovery-with-ai/)), Fehrmann ([Euroguss](https://euroguss.de/en/exhibitors-products/fehrmann-materials-x-2233786/matgpttm-2265714)). Intellegens "about 15 years / US$10M saved" was a Ni alloy, not Al ([Metal AM](https://www.metal-am.com/machine-learning-algorithm-designs-new-alloy-for-metal-additive-manufacturing-2/)) | These describe design-loop speed only |

### 2.2 Time and cost evidence

| Phase | Classic | AI/ICME-enabled | Basis |
|---|---|---|---|
| Composition screening | 2–4 yrs, hundreds of casts | 3–12 months, 30–100 casts | MIT, PatSnap; [est.] |
| Lab validation | 1–2 yrs | 3–6 months | MPIE RAP |
| Plant scale-up | 1–3 yrs | 1–2 yrs | [est.] |
| Customer qualification | Auto 2–4 yrs; aero 5–15 yrs | **Little change** | NASA; [est.] |
| **Total lab to market** | **10–20 yrs** ([U-Michigan/MGI](https://msewww.engin.umich.edu/?p=3343)) | **Auto 3–5 yrs; building extrusion 1–2 yrs; conductor 1.5–3 yrs** | [est.] |
| Cost per new wrought alloy | EUR 10–30M [est.] | EUR 4–12M [est.] | Report 1 |
| Cost per structural casting alloy | EUR 10–20M [est.] | EUR 3–8M [est.] | Report 3 |
| Cost per conductor alloy family | n/a | EUR 1–3M [est.] | Report 4 |
| Cost per alloy-OEM qualification pair (auto) | EUR 1–5M [est.] | Unchanged | Report 6 |

**Conclusion:**
- AI is worth about 1–3 years and 50–60% of development cost per alloy. It does not change the qualification clock.
- Qualification is therefore the critical path in every case below.
- Every alloy programme now has named target customers (Sections 5.5, 6.5, 6A.5) before lab work starts.

### 2.3 What competitors are doing

- **Hydro:** CREATe with U-Michigan on Fe-tolerant extrusion alloys, plus SFI FAST (2026–33) on post-consumer scrap in safety-critical parts ([NAV](https://arbeidsplassen.nav.no/stillinger/stilling/2ba31115-971a-4398-ae69-87b76c53d954)). Hydro Nowa Sól is a 120 kt sorting hub with 2 HySort units ([Hydro](https://integration.hydro.com/en/global/about-hydro/hydro-worldwide/europe/poland/nowa-sol/hydro-aluminium-nowa-sol/)).
- **Constellium:** AI work with 3ALP and MIT on Fe/Mn in 6xxx. CirConAl crash systems are made from >90% post-consumer scrap ([Constellium](https://constellium.com/news/showcase-aluminum-solutions-collaborative-research-project-circonal-cenex2025)). R&D spend is about US$50M with about 300 staff ([Constellium](https://www.constellium.com/innovation)).
- **Novelis:** hiring for AI alloy discovery ([Novelis](https://careers-novelis.icims.com/jobs/47609/ai-%26-advanced-modeling-co-op/job)).
- **Speira:** SMS Metallics Optimizer at Töging, Grevenbroich and Deizisau, with no site results published.
- **EGA:** LLM framework.

None of Hydro, Novelis or Constellium has a public AI conductor-alloy programme (Report 4).

---

## 3. Alloy opportunity map

**Column notes:**
- Market figures give the year and say whether they are EU or global.
- "Ours" marks our own target volume, kept separate from market size.
- **[CTO est., reasoned]** marks a bounded estimate with its logic shown.
- (x) marks a CTO extrapolation to 2035.
- Every row carries one decision, which is repeated in Section 4.

| Alloy family | End market | Market size (year, scope) | 2035 | Premium EUR/t over standard | Qualification | Right to win | **Decision** |
|---|---|---|---|---|---|---|---|
| Scrap-tolerant HRC 6xxx extrusion billet (Fe 0.4–0.8, Mn/Cr) | Building, auto extrusions | EU 6xxx billet 3–4 Mt/yr, 2030 [est.]. Named shortlist pool 200–310 kt building + 60–100 kt crash management [est., Section 5.5]. Ours: 40–60 kt | Ours 60–100 kt (x) | 50–200 [est.]. Plus two cost savings [est., Section 5.2]:<br>- casthouse-side down-shift of 6–10 net LME points (EUR 129–216/t) **on contracted lower-rung tonnes only** (40 kt in the hub route; up to 100 kt without the hub, if contracted);<br>- post-consumer substitution of 6–13 net points (booked 9, EUR 194/t) on 15 kt.<br>**The Zorba-to-sorted spread belongs to the hub** | ~1 yr building; 2–4 yrs auto [est.] | **High.** The scrap-chemistry-to-casthouse data chain is hard to copy | **GO** (Case A) |
| HRC 5xxx/6xxx sheet | Auto body, building | EU auto and building flat-rolled 1.0–1.5 Mt/yr, 2030 [CTO est., reasoned: EU flat-rolled about 4.5–5 Mt × 20–30% auto/building panel share]. Ours: 50–150 kt | Ours 100–150 kt (x) | 50–200 [est.] | 2–4 yrs | **Medium-high.** Novelis is ahead at 63% average recycled content and up to 85% in auto ([Novelis](https://investors.novelis.com/news-events/press-releases/detail/1415/novelis-wins-award-for-100-recycled-end-of-life-vehicle-scrap-product)) | **GO** (Case A) |
| Certified ≥75% post-consumer brand | Auto, building, foundry | EU certified high-recycled-content demand 0.4–0.8 Mt/yr, 2030 [CTO est., reasoned: EU semis about 8 Mt × 5–10% bought under Scope-3 recycled-content clauses]. Ours: 28 kt sold to named buyers (20 building + 8 crash) | 0.6–1.2 Mt (x) | Building 50–200 (base 100); crash management 100–300 (base 175) [est., Section 5.5]. The exchange low-carbon differential alone is only US$25–40/t ([Fastmarkets](https://fastmarkets.com/insights/low-carbon-aluminium-differentials-in-europe-widen-for-p1020-vaps)) | 12–18 months | **Medium.** Competes with Hydro CIRCAL (1.9 kg CO2e/kg), the incumbent at Schüco | **GO** (lever A4) |
| NHT structural HPDC (AlSi10MnMg / AlMg5Si2Mn class, plus a scrap-based Fe-tolerant variant) | Giga- and megacasting, NHT structural parts | EU structural HPDC pool 250–420 kt/yr, 2030 [CTO est., reasoned: Ducker 145 kg of castings per car ([Ducker/European Aluminium](https://european-aluminium.eu/wp-content/uploads/2023/05/23-05-02Aluminum-Content-in-Cars_Public-Summary.pdf)) × 11.5M cars × 15–25% structural]. Of which mega-casting alloy **128 kt (50–256)** [est., programme build-up, Section 6A.1]. Ours: 30 kt (23% of mega-casting central) | EU mega-casting 150–300 kt (x) | Price today P1020 DP + 269. **Contribution against the metal's alternative use: 231 (P1020 basis, range 24–532); 190 if potlines curtailed; 164 (billet basis)** [calc] | 2–4 yrs after the alloy is ready | **Medium.** Non-Russian EU origin. Peers with primary access (Hydro/Alumetal, Trimet, Speira, Rio Tinto, Alcoa) make a 10–20% entrant share (13–26 kt) realistic [est.] | **WATCH** (volume-specific gate on both ledgers) |
| EC 1370 / 8xxx / 6101-6201 conductor rod | Grid, LV/MV cable | EU 0.6–0.9 Mt/yr, 2030 [est.]. Demand proof: Nexans–Hydro offtake of about 17 kt/yr (about 85 kt over 5 years) at <4.0 kg CO2/kg, price not disclosed ([Nexans, Jul 2026](https://www.nexans.com/app/uploads/2026/07/2026-07-06-pr-nexans-and-hydro-secure-long-term-low-carbon-aluminium-supply-agreement.pdf)) | 0.75–1.2 Mt (x) | Matched rod adder over P1020 US$170–700 by year, mid-cycle US$267 [est.; no public series found]. Margin over ingot EUR 155/t mid-cycle from liquid metal, **EUR 40/t from purchased ingot** (Sections 6.2, 4.6) | 6–12 months | **High on cost while the potlines run; weak if they close.** About par with billet on margin | **WATCH** |
| Heat-resistant Al-Zr (TAl/ZTAl) | HTLS reconductoring | EU 20–50 kt/yr, 2030 [est.] | 40–80 kt (x) | 300–800 over EC rod [est.] | 24–48 months | **Medium.** Needs the rod line first | **WATCH** |
| Busbar and high-thermal-conductivity extrusions | Data centres, BESS, switchgear | EU addressable 40–80 kt/yr, 2030 [est.]. Cu→Al substitution in the EU is 80–120 kt Al in 2030 [est.]: global 27 Mt Cu × 6% displacement × 0.494 = 0.80 Mt Al (JPMorgan via [TimesLive/Reuters](https://www.timeslive.co.za/motoring/2026-06-30-ferrari-and-bmw-follow-tesla-and-chinese-brands-in-shift-to-cheaper-aluminium-wiring)) × 10–15% EU share. Ours: 15 kt | 60–120 kt (x) | Conversion 1,500–3,000; incremental margin over standard profiles 300–600 [CTO est.] | 6–12 months OEM | **Medium-high.** Existing presses; survives curtailment | **GO** (B-ext) |
| High-conductivity thin-wall HPDC (≥45% IACS, ≥150 MPa) | E-motor, inverter housings | Global 30–80 kt/yr, 2030 [est.] | 50–120 kt (x) | 500–1,000 [est.] | 24–48 months | **Medium-low.** Tesla holds patents at 46–55% IACS; Alcoa AT237 is about 41% IACS | **WATCH** |
| Robot-grade 6xxx/7xxx bar, plate, extrusion | Humanoids, cobots, drones | Global semis 50–200 kt/yr, 2030 [est.]. CRU moderate case of 10 Mt by 2050 ([CRU](https://www.crugroup.com/en/communities/thought-leadership/2025/the-next-commodity-battleground-humanoid-robots/)). The board paper's robotics demand is 88 kt (2030) | n/a | 800–2,000 [est.] | 12–30 months | **Medium.** Mg is cheaper per tonne; our pitch is EU supply security | **WATCH** |
| 5/7 crossover AlMgZn(Cu) sheet | Auto structural, rail | EU 10–30 kt/yr, 2030 [est.] | 20–50 kt (x) | 150–400 [CTO est., by analogy to HSA6-type crash extrusions] | 3–5 yrs | **Low.** AMAG CrossAlloy.57 leads by about 7 years ([AMAG](https://www.amag-al4u.com/produkte/crossalloy/automotive)) | **WATCH** |
| Al-Ce / ACMZ high-temperature cast | E-drive, turbo, H2 | Global 5–20 kt/yr, 2032 [est.] | 10–25 kt (x) | 300–800 over A356 [est.] | 2–4 yrs | **Low-medium.** Would be licensed in from ORNL/Eck; Ce supply is China-dependent | **WATCH** |
| Al-Sc / Al-Sc-Zr master alloy | Defence, AM | Global about 855 t/yr of Al-2Sc ([Valuates](https://reports.valuates.com/market-reports/QYRE-Auto-34R6611/global-aluminium-scandium); no year given, low reliability; treated as 2024–25 [unverified]) | Doubles if Syerston ramps (x) | US$60–75/kg conversion; 0.3% Sc adds about EUR 4,000/t of metal cost | 1.5–3 yrs | **Low.** China export-controlled Sc from 4 Apr 2025 ([USGS MCS 2025](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-scandium.pdf)) | **NO-GO** |
| AM powder / WAAM wire (own atomiser or tolling) | Aero, motorsport, defence | Global Al AM powder 1–3 kt/yr, 2025 [est.] | 2–6 kt (x) | EUR 70–125/kg | 2–4 yrs industrial; 4–7 yrs aero | **Low.** Equispheres, Elementum 3D, ECKART and Colibrium already cover it | **NO-GO** |
| Battery foil (greenfield mill) | Li-ion, Na-ion, BESS | EU foil 100–300 kt/yr, 2030 [est.]. China added about 1.27 Mt of capacity ([AlCircle](https://www.alcircle.com/news/growing-demand-for-aluminium-battery-foil-prompts-china-to-commission-17-new-capacities-98896)) | Uncertain | Conversion 600–1,500 [est.] | 12–24 months | **Low** | **NO-GO** |
| Al-Li (own production) | Aerospace | Global Al-Li semis 25–50 kt/yr, 2030 = US$0.6–1.5bn at US$25–30/kg [CTO est., reasoned from commercial-aircraft build rates] | n/a | 1.5–2.5x 7xxx plate [est.] | 5–10+ yrs | **None.** Incumbents locked in | **NO-GO** |
| Twin-roll casting (process route) | Foil stock, 3xxx/8xxx strip | EU strip-cast foil stock and 3xxx/8xxx strip 0.3–0.6 Mt/yr, 2030 [CTO est., reasoned from EU foil and fin-stock demand] | n/a | Capex EUR 30–60M against >EUR 300M for a DC-cast plus hot-mill route [est.] | 12–24 months | **Low-medium.** Limited product mix | **WATCH** |
| High-entropy alloys | Niche | No commercial Al market [CTO est.] | n/a | n/a | n/a | None | **NO-GO** |

---

## 4. Ranked portfolio, metal ledgers, ICC risk and portfolio build-up

### 4.1 Ranked decisions

**What each decision means:**
- **GO:** fund to the next gate. Capex is released only when that gate is passed.
- **WATCH:** no capex. A capped option budget and a named, quantified trigger.
- **NO-GO:** zero spend.

The score is out of 10. It weights value (30%), right to win (25%), time to revenue (20%), risk (15%) and capital intensity (10%). Revision 5 lowers Case A's score again, because its value now rests on contracted lower-rung tonnes and a smaller A3.

| # | Opportunity | Decision | Spend 2027–30 (EUR M) | IRR / NPV10 (decision basis) | Time to revenue | Score | Next gate (date) |
|---|---|---|---|---|---|---|---|
| 1 | AI charge optimiser and property-window specification (lever A1, netted against furnace robots) | **GO** | 2.5 (inside Case A) | EUR 2.00M/yr on 2.5; payback about 1.6 yrs | 6–12 months | **8.7** | Shadow run shows ≥EUR 3/t **charge-cost** saving (primary sweetening plus alloy additions) on the optimiser's cost logs (30 Jun 2027) |
| 2 | Scrap-tolerant "house" 6xxx extrusion and HRC sheet family (Case A, levers A2, A3, A5) | **GO** | 27.0 for all of Case A | 31.3% / EUR 31.1M (whole Case A, 55 kt contracted); 15.9% / EUR 10.3M carrying the capability centre | 12–24 months building; 2–4 yrs auto | **7.9** | **T2** (earliest 30 Jun, latest 31 Oct 2027). All of:<br>- ≥1 signed LOI from Hueck, Aluprof or Reynaers;<br>- **≥3-year contracts for ≥40 kt/yr of lower-rung grades (A2) and ≥15 kt/yr of A3 grades**;<br>- verified net spreads A2 ≥6 and A3 ≥6 points;<br>- existing scrap intake C ≥100 kt.<br>Then ML variants meet EN 755 in the lab, plus a signed building JDA (31 Dec 2027) |
| 3 | Certified ≥75% post-consumer brand (lever A4) | **GO** | 1.5 (inside Case A) | EUR 3.4M/yr on 1.5; payback <1 yr | 12–18 months | **8.0** | ASI chain-of-custody and EPD issued (30 Sep 2027); priced LOIs from 2 building and 1 automotive buyer (30 Jun 2027). Depends on the same A3 contracts as T2 |
| 4 | Data-centre busbar and thermal extrusions (B-ext) | **GO** | 7.5 + 1.0 WC | 49.2% / EUR 19.1M; EUR 12.1M if potlines are curtailed from 2030 | 9–18 months | **7.8** | First qualification order from Schneider, Vertiv, Siemens or ABB (target 30 Jun 2027, releases tranche T3); framework order (31 Dec 2027) |
| 5 | Portfolio rationalisation and closed-loop scrap contracts (lever A5) | **GO** | <1 | Inside Case A | 12–36 months | **7.3** | SKU count cut ≥30% without customer loss; first take-back contract (31 Dec 2027) |
| 6 | Low-carbon EU NHT structural HPDC alloy (the board paper's #5) | **WATCH** | 0.8 pre-gate qualification option; 29.5 only after the gate | 7.3% / −EUR 4.1M (ICC renewed); 3.8% / −EUR 8.8M (curtailed 2030); 30 kt, P1020 basis, contingency | 24–36 months serial | **6.2** | **30 Sep 2027, after M9:** volume-specific gate on both ledgers (Section 6A.4). Supersedes the board paper's 20 kt trigger |
| 7 | High-conductivity HPDC and robot-grade 6xxx/7xxx via start-up partners (Alloyed, Phaseshift, Fehrmann) | **WATCH** | ≤0.5/yr | n/a | 24–48 months | **6.0** | A partner shows ≥45% IACS at ≥150 MPa in trial castings and a motor OEM signs a co-development deal |
| 8 | 60 kt conductor rod line (B-rod; the board paper's #4 rod-line FID) | **WATCH** | 0.2 for studies and quotes; 44.1 only after the gate | 9.8% / −EUR 0.5M (ICC renewed); 9.3% / −EUR 1.8M (curtailed 2030) | 18–30 months | **5.7** | **30 Sep 2027, after M9:** Section 6.6 tests, including the curtailment test. Otherwise it waits for the 31 Dec 2029 ICC decision |
| 9 | Al-Zr HTLS rod and ML Al-Zr-Er conductor alloys | **WATCH** | ≤0.3 R&D, grant-funded | n/a | 24–48 months | **5.6** | B-rod upgraded to GO and one TSO pilot letter signed |
| 10 | 5/7 crossover sheet by licence (AMAG/Leoben) | **WATCH** | ≤0.1 (exploratory talks) | n/a | 3–5 yrs | **5.5** | AMAG open to a licence or JV (talks in 2027) |
| 11 | Twin-roll casting | **WATCH** | 0.2–0.4 toll trials on the MAT-PROD-22 pilot line, if won | n/a | 2029+ | **5.2** | Toll trials show 5xxx/6xxx meeting specification with ≥60% sorted scrap |
| 12 | Al-Ce / ACMZ | **WATCH** | ≤0.3, only as casting partner in a Horizon consortium | n/a | 2–4 yrs | **5.0** | An OEM asks for a specification and Ce is available from a non-Chinese source |
| 13 | Al-Sc master alloy | **NO-GO** | 0 | Metal cost +EUR 4,000/t | n/a | 3.5 | Re-open only if non-Chinese Sc2O3 is secured below US$1,000/kg (e.g. Syerston, 1H 2028 ([ASX](https://announcements.asx.com.au/asxpdf/20260810/pdf/072l1673ycxhhl.pdf))) |
| 14 | AM powder / WAAM: own atomiser or tolling | **NO-GO** | 0 | Market of a few kt | n/a | 3.0 | None |
| 15 | Greenfield battery-foil mill | **NO-GO** | 0 | n/a | n/a | 3.0 | Re-open only if the EU foil market tightens |
| 16 | Own Al-Li production | **NO-GO** | 0 | n/a | n/a | 2.5 | None |
| 17 | High-entropy alloys | **NO-GO** | 0 | n/a | n/a | 2.0 | None |
| 18 | Generative-crystal-model R&D | **NO-GO** | 0 | n/a | n/a | 2.0 | Review in 2028 |

**Board-paper items this memo depends on but does not decide:**
- **Scrap hub (#2):** EUR 50M, GO to FID gate, FID at M12 (Oct 2027).
- **Furnace robots (#1):** EUR 7.5M, FID at day 90.
- **No-ICC contingency plan:** M9 (Jul 2027). The option-C melt configuration (Section 4.6) belongs to that plan.

Their value is not in any number here, except where Section 5.4A shows the hub combined with Case A.

**No-regret actions (operational, not opportunities):**
- Add Al-Li and Sc scrap segregation channels to the hub's sorter specification now, within the hub budget.
- Add a strict-versus-wide alloy-window run to the hub's M3 LIBS trial (Section 5.2).
- Foil-stock and can-sheet sales from the existing rolling mill continue as normal business, outside this programme.

### 4.2 EBITDA build-up at maturity (2031, EUR M/yr)

| Line | Status | 2031 EBITDA (ICC renewed) | If potlines curtailed from 2030 | Build-up |
|---|---|---|---|---|
| Case A | GO | 12.06 | Lower if the casthouse is stranded, because A1 scales with throughput. Unchanged in the option-C configuration at 40 kt A2 (Section 4.6) | Section 5.2: 18.20 gross − 3.64 overlap haircut − 2.50 opex |
| B-ext | GO | 5.50 | 3.78 | 15 kt × EUR 400/t − 0.50 opex; curtailed: − 15 kt × EUR 115 remelt penalty |
| Capability centre running cost | GO | −2.80 | −2.80 | Team 1.8 + software 0.5 + external 0.5 |
| **Committed portfolio** | | **14.76** | | |
| NHT option, if the gate passes at today's price | WATCH | +5.43 | +4.19 | 30 kt × EUR 231/t − 1.50 fixed opex; curtailed 30 × 190 − 1.50 |
| B-rod option, mid-cycle, after NHT's metal claim | WATCH | +6.76 | +6.05 | Section 6.3: rod margin 8.85 − billet displacement 5.84 + Al-Zr 3.75; curtailed 57 kt × EUR 40/t + 3.75 |
| **Portfolio with both options** | | **26.95** | | |

**Not counted (upside):**
- Alloy-development services: EUR 1–3M/yr from 2029.
- Out-licensing royalties: EUR 1–3M/yr from 2030.
- The low-carbon differential on rod (US$20–30/t on ingot-sourced rod).
- **A3 on a P1020 basis.**
  - If A3 avoids purchased P1020, or frees our own metal for sale as ingot, its net spread is about 19–22 points instead of 9 (Section 5.2).
  - It is booked only after S&OP confirms the casthouse mass balance (6 Nov 2026, open item 6).
  - Each extra point of A3 is worth about EUR 1.1M of Case A NPV.
- A2 tonnes above 40 kt/yr. These exist only if the hub is not built, and are booked only when contracted (Section 5.4A).
- Grants.
- The hub's own EBITDA (EUR 9.77M at 12 points; board paper).

### 4.3 Metal ledgers: one owner (CFO), every tonne used once

**Allocation rule:**
- Spare primary goes first to the use with the highest value per tonne of metal drawn. NHT is worth about EUR 364/t drawn; rod displacing ingot about EUR 154/t.
- A later claimant is charged the margin of whatever it actually displaces.
- **Billet capacity is assumed full.** That is why about 30 kt of primary leaves as ingot today. So the alternative use of spare metal is P1020 sale, and any metal drawn beyond the spare displaces billet.
- S&OP confirms the billet-capacity assumption by 6 Nov 2026 (open item 6).
- Hub scrap that is diverted from billet counts as a primary draw, because billet must backfill it with primary.
- The ledger has two states, **ICC renewed** (below) and **potlines curtailed from 2030** (Section 4.6). Every case that depends on liquid metal is valued in both.

**Liquid-metal (primary-equivalent) ledger, ICC renewed, kt/yr, with NHT and B-rod both assumed built**

| Year | Spare primary: external ingot sales today [est., 20–50] + primary freed by A3 | NHT draw: 0.360 t primary + 0.275 t hub wrought scrap per t of alloy | Rod need: 57 kt × 1.01 | Rod drawn from spare | Rod drawn from billet | Billet share of rod |
|---|---|---|---|---|---|---|
| 2028 | 30.0 + 0 = 30.0 | 0 | 15.2 | 15.2 | 0 | 0% |
| 2029 | 30.0 + 5 = 35.0 | 3.8 | 45.5 | 31.2 | 14.3 | 31% |
| 2030 | 30.0 + 15 = 45.0 | 11.4 | 57.6 | 33.6 | 24.0 | 42% |
| **2031 on** | **45.0** | **19.0** (10.8 primary + 8.3 hub scrap) | **57.6** | **26.0** | **31.6** | **55%** |
| 2031, NHT not built | 45.0 | 0 | 57.6 | 45.0 | 12.6 | 22% |

- **Ingot left over in 2031: 0 kt.** No tonne is counted twice.
- **Spare primary range:** 25–75 kt, made up of 20–50 external plus 5–25 from A3. It is the main swing variable for B-rod: break-even is 45.5 kt including NHT's claim (Section 6.6).
- **A3's freed primary:**
  - This applies only if the casthouse buys no external primary or sow.
  - If it does, A3 cuts purchases instead and this line is zero. A3's value then rises to the P1020 basis (Section 4.2 upside).
  - S&OP confirms by 6 Nov 2026.

**Scrap ledger, kt/yr in 2031 (restated in revision 5 on contracted tonnes)**

| Consumer | kt | Valued at | Owner of the value | Secured by |
|---|---|---|---|---|
| Hub intake: Zorba / ELV shred (board paper planning feed) | 100 | The hub's 12-point Zorba-to-sorted uplift on 90 kt | **The hub (board paper 5.3), not Case A** | Hub M6 feed MoUs |
| Hub sorted output into our casthouse | 90 | Market transfer price | Hub | Hub FID |
| … of which clean wrought scrap to NHT (if built) | 8.3 | Its billet-substitution value, P1020 DP − EUR 100; backfilled with primary in the ledger above | NHT | NHT gate |
| … of which clean 1xxx scrap to B-rod (if built) | up to 5.8 | Neutral; inside rod's 57.6 kt primary-equivalent need | B-rod | B-rod gate |
| **Purchased casthouse scrap still bought after the hub runs: C − 90** | **40** (C = 130 [est.]) | **A2:** bought one rung lower (mixed wrought / old rolled, taint/tabor) once wide windows are qualified, 8 net points | **Case A** | **T2(c): ≥40 kt/yr of lower-rung grades contracted, ≥3 years** |
| A3 post-consumer scrap replacing primary in billet and sheet | 15 | **9 net points (EUR 194/t):** 85.75% of LME delivered, less 5.3 points of casthouse cost against hot metal. Frees 15 kt of primary (ledger above). On top of today's intake C | Case A | **T2(c): ≥15 kt/yr of A3 grades contracted; T2(d) verifies the spread** |
| NHT external cast scrap and OEM returns (if built) | 8.3 | 85% of LME | NHT | NHT gate |
| B2 (rod scrap lever in revision 2) | 0 | Removed; its tonnes belong to A3 | — | — |

- **C is the casthouse's existing scrap intake**, the pool A2 can down-shift. It is 130 kt central, range 100–190 [est.].
  - Head of Casthouse Metallurgy confirms it by alloy (open item 22).
  - Head of Scrap Procurement prices it by grade (open item 23).
  - The hub's 90 kt replaces part of that purchased pool and does not add to it. That is the board paper's own treatment ("not counted: sorted scrap replacing primary").
- **A2 tonnes are re-specification, not new supply.**
  - They are today's purchased tonnes, bought one grade lower.
  - Existing suppliers can cover much of them by changing the grade they ship.
  - That is why 40 kt is realistic even though the largest public EU contract is about 25 kt/yr (Section 5.4A).
- The 20% haircut inside Case A (EUR 3.64M in 2031) covers the remaining overlap between A1, A2 and A3 on the same tonnes.

### 4.4 Portfolio NPV, including the capability centre (combined tax)

| Run (no grants) | NPV10 (EUR M) | IRR | Payback |
|---|---|---|---|
| Revision 4 P0 (withdrawn; reference) | 40.9 | 26.1% | 2032 |
| **P0 committed:** Case A + B-ext + capability centre + 90-day plan + pre-gate options (EUR 1.0M) | **26.6** | **21.0%** | 2033 |
| P0 with 10% contingency on Case A and B-ext | 23.8 | 19.3% | 2033 |
| Case A carrying the whole capability centre | 10.3 | 15.9% | 2034 |
| Capability centre on its own (cost) | −26.1 | n/a | n/a |
| P0, hub not built, 55 kt contracted (T2 minimum; equals the hub route) | 26.6 | 21.0% | 2033 |
| P0, hub not built, 70 kt contracted (central contracting estimate) | 36.2 | 24.5% | 2032 |
| P0, hub not built, 115 kt contracted at 8 net points (upper bound; no public precedent) | 62.5 | 32.7% | 2031 |
| P0, potlines curtailed from 2030, stranded casthouse on existing melt (C 130) | 16.4 | 17.2% | 2033 |
| P0, potlines curtailed from 2030, option-C configuration (C 190), A2 at the 40 kt contracted | 19.7 | 18.5% | 2033 |
| P0, potlines curtailed from 2030, stranded casthouse with C 100 | −1.0 | 9.5% | 2035 |
| P0, A2 and A3 both verified at the T2(d) floor of 6 net points | 16.3 | 16.9% | 2033 |
| P0, A3 at 13 net points (top of the published range) | 31.0 | 22.5% | 2032 |
| P0, T2 fails and Case A is re-scoped to A1 + A5 (only the EUR 5.5M of T1 Case A spend is incurred) | 2.2 | 11.7% | 2034 |
| P0, Case A all-low stack (capex 35, C 100, A2 6 points, A3 10 kt × 6 points, low levers), every gate assumed passed | −22.6 | −0.3% | never |
| P1 = P0 + NHT at today's price, ICC renewed | 23.7 | 16.2% | 2034 |
| P2 = P1 + B-rod, ICC renewed | 23.5 | 13.8% | 2034 |
| P2, potlines curtailed from 2030, stranded casthouse (C 130) | 8.0 | 11.3% | 2035 |

**Check:**
- The standalone NPVs sum to 21.2: Case A 31.1 + B-ext 19.1 − capability 26.1 − 90-day 1.9 − options 1.0.
- The combined figure is EUR 5.4M higher because, at portfolio level, the capability and 90-day costs shelter Case A's taxable profit.

**Reading the robustness rows:**
- **The committed portfolio clears the hurdle in every state the board paper defines**, on the tonnes T2 contracts:
  - hub built or not;
  - ICC renewed, or curtailed with the casthouse on its existing melt.
- It also clears the hurdle at the T2(d) floors and after a failed T2, because the gates cap what is spent before the contracts and spreads are known.
- **It fails in two states:**
  - **The all-low stack.** T2, the 31 Dec 2027 gate and the 2028 budget would stop the scrap-dependent EUR 21.5M before it is spent.
  - **Curtailment with a casthouse whose existing intake is only 100 kt** (−EUR 1.0M). T2(d)'s C ≥100 kt test still admits that case. Open item 22 (C by alloy, 13 Nov 2026) and open item 34 (solid-melt capacity by furnace, 30 Nov 2026) establish before T2 whether it is realistic.
- **Curtailment no longer raises the portfolio** (revision 4 showed EUR 67.2M).
  - That figure assumed C ≥190 kt with no melt capex, and 100 kt of A2 that no gate secured.
  - The public analogues in Section 4.6 show that a stranded casthouse melts far less. C ≥190 kt is booked only in the funded option-C configuration.
  - The board paper's own smelter loss (−EUR 38M/yr on the planning curve if ICC lapses) dwarfs every alloy figure here.

**P0 combined cash flow, EUR M**

| Year | Capex | EBITDA | Tax | WC | Cash flow | Cumulative |
|---|---|---|---|---|---|---|
| 2027 (90-day plan shown at t0) | −13.4 | −6.1 | 0.0 | – | −19.5 | −19.5 |
| 2028 | −16.0 | 3.7 | −0.4 | −0.5 | −13.3 | −32.8 |
| 2029 | −7.0 | 8.7 | −1.6 | −0.5 | −0.4 | −33.2 |
| 2030 | −2.2 | 14.8 | −3.0 | – | +9.5 | −23.7 |
| 2031 | −0.7 | 14.8 | −3.0 | – | +11.0 | −12.7 |
| 2032 | −0.7 | 14.8 | −3.0 | – | +11.0 | −1.6 |
| 2033 | −0.7 | 14.8 | −3.0 | – | +11.1 | **+9.4** |
| 2034–2040 (each year) | −0.7 | 14.8 | −3.0 to −2.9 | +1.0 in 2040 | +11.1 (+12.1 in 2040) | +88.1 by 2040 |

**Conclusion:**
- The committed portfolio clears the hurdle on the group's basis with the capability centre fully charged, on contracted tonnes and on published scrap prices. The margin is smaller than revision 4 claimed: NPV EUR 26.6M against EUR 40.9M.
- Neither option adds value at today's terms under either ledger. Their gates (Sections 6.6 and 6A.4) release capex only once the option's own NPV is at least zero under both ledgers.

### 4.5 Investment build-up and the gate-conditional 2027 tranche (EUR M, gross, before grants)

**Committed envelope** (unchanged from revision 4)

| Line | Total | Q4 2026–Jan 2027 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|---|
| 90-day plan (opex) | 1.90 | 1.90 | – | – | – | – |
| Case A capex and development (Section 5.3) | 27.00 | – | 9.00 | 10.00 | 6.00 | 2.00 |
| B-ext capex | 7.50 | – | 4.00 | 3.50 | – | – |
| B-ext working capital | 1.00 | – | – | 0.50 | 0.50 | – |
| Capability centre (Section 7.6) | 12.20 | – | 3.10 | 5.30 | 3.80 | – |
| Contingency, 10% of Case A + B-ext capex (34.5) | 3.45 | – | 1.30 | 1.35 | 0.60 | 0.20 |
| NHT pre-gate qualification option | 0.80 | – | 0.80 | – | – | – |
| B-rod studies and quotes | 0.20 | – | 0.20 | – | – | – |
| **Committed gross** | **54.05** | **1.90** | **18.40** | **20.65** | **10.90** | **2.20** |
| Committed grants if awarded: Horizon 1.2 + IF Case A 4.2 | −5.40 | – | – | −2.70 | −2.70 | – |
| **Committed net, grants awarded** | **48.65** | | | | | |
| Probability-weighted grants (20%) | −1.08 | | | | | net **52.97** |

**Check:** 1.90 + 18.40 + 20.65 + 10.90 + 2.20 = 54.05.

Sustaining capex from 2030–31 (Case A EUR 0.5M/yr, B-ext EUR 0.2M/yr) is inside each cash table and is not repeated here.

**Not in this envelope:**
- The scrap hub's EUR 50M capex, EUR 2.5M development and EUR 10M working capital. They sit in the board paper's Tier A envelope (EUR 69.5M) and its M12 FID.
- Section 5.4A shows Case A and the hub combined: EUR 89.5M.
- Any solid-melt capacity for a scrap-fed casthouse (EUR 36–110M for C ≥190 kt, Section 4.6). It belongs to the board paper's option C.

**Gated options (separate Board decisions; not in the envelope)**

| Option | Total | 2027 | 2028 | 2029 | 2030 | 2031 | Ties to |
|---|---|---|---|---|---|---|---|
| NHT after the joint gate: capex 19.8 incl. contingency + qualification 3.2 | 23.0 | 1.98 (Q4, after gate) | 20.32 | 0.70 | – | – | Section 6A.3 cash table (2027 row −2.8 includes the 0.8 pre-gate option) |
| NHT working capital, 8% × EUR 2,700/t | 6.5 | – | – | 1.30 | 2.59 | 2.59 | Same |
| **NHT option total** | **29.5** | | | | | | |
| B-rod after its gate: line 39.6 incl. contingency + alloy development 2.5 + WC 2.0 | **44.1** | 24.8 | 18.8 (16.8 capex + 2.0 WC) | 0.5 | – | – | Section 6.4 decision-basis cash table, line by line |

- The 2027 amounts are long-lead deposits placed at the gate [CTO est.].
- If a gate decision slips into 2028, each option moves one year. Its NPV then changes by less than its sign does today.
- An option that fails only the curtailment test is re-tested after the 31 Dec 2029 ICC decision. Its cash table then starts in 2030 (Section 4.6).

**2027 tranche (EUR 18.4M): released in parts, against named triggers**

| Release | Contents (EUR M) | Trigger | Owner | Date |
|---|---|---|---|---|
| **T1 at day 90** | Capability centre 3.1; A1 optimiser 2.5; Case A alloy development 2.0; A4 certification 1.0; B-ext dies and samples 1.0; NHT pre-gate qualification 0.8; B-rod studies 0.2 = **10.6** | Approval of this plan | CEO | 23 Jan 2027 |
| **T2** | Case A casthouse-adaptation long-lead items 2.5 + first OEM qualification 1.0 = **3.5** | All four conditions must hold (restated in revision 5; see below) | CTO + Head of Sales + Head of Scrap Procurement + CFO | Earliest 30 Jun 2027; latest 31 Oct 2027. **If (c) or (d) fails by 31 Oct 2027, Case A is re-scoped to A1 + A5, at NPV +EUR 6.7M, IRR 26.7%** |
| **T3** | B-ext fabrication and finishing cell **3.0** | First qualification order from Schneider, Vertiv, Siemens or ABB | Head of Extrusion Operations | target 30 Jun 2027 |
| **Contingency** | **1.3**, held by the CFO | Drawn only against documented overruns on released items | CFO | – |
| **Not in the tranche** | NHT capex; B-rod capex | Board decisions after the gates in Sections 6A.4 and 6.6, both after the M9 contingency plan | Board | 30 Sep 2027 |

**Check:** 10.6 + 3.5 + 3.0 + 1.3 = 18.4.

**T2 conditions (revision 5)**

- **(a) Optimiser.** The A1 shadow run shows a charge-cost saving of **≥EUR 3/t** on the optimiser's cost logs.
  - Revision 4's threshold was EUR 4/t.
  - It is re-scaled because the base charge-cost saving fell from EUR 6.39/t to EUR 4.44/t when sweetening was re-priced at the A3 spread.
  - EUR 3/t keeps the same ratio to base (63%).
- **(b) Customer.** At least 1 signed LOI from Hueck, Aluprof or Reynaers.
- **(c) Contracted scrap, sized to the tonnes the booked value uses.** Contracts or binding offtakes of ≥3 years, grade-certified, priced as a % of LME. They are indexed to Fastmarkets MB-AL-0405 / MB-AL-0426 where a series exists.

  | Pool | Grades that count | Grades that do **not** count | Minimum tonnes | Books |
  |---|---|---|---|---|
  | **A2 (down-shift)** | Mixed wrought / old rolled; taint/tabor; lower rungs only if a casthouse trial passes | Sorted wrought, LIBS-sorted 6xxx, clean new extrusion scrap: these are the grades A2 moves **away from** | **≥40 kt/yr**. They must replace at least the same tonnage of current higher-grade purchases, shown against the 2025–26 invoices (open item 23) | A2 EUR 6.90M/yr |
  | **A3 (substitution for primary)** | Post-consumer 95/5 6063 or LIBS-sorted 6xxx (billet); taint/tabor or old rolled (sheet) | Clean new production scrap (it is not post-consumer and does not count toward A4) | **≥15 kt/yr from 2030** (5 kt in 2029) | A3 EUR 2.91M/yr |
  | **Total** | | | **≥55 kt/yr** | Case A EUR 31.1M |

  - **The same 55 kt applies in both routes.**
    - If the hub reaches FID at M12, the residual purchased pool is 40 kt and A2 cannot exceed it.
    - If the hub is not built, the same contracts book the same EUR 31.1M.
    - Without the hub, A2 tonnes above 40 kt are booked only when contracted. Each is worth about **EUR 0.64M of NPV per extra kt** (Section 5.4A).
  - **Contracts above 40 kt of A2 that are signed before M12 must carry a volume-reduction option**, exercisable if the hub reaches FID. Otherwise they become surplus once the hub's 90 kt displaces the purchased pool.
  - **Hub FID is no longer a scrap-source condition for Case A.**
    - The hub does not secure lower-rung tonnes for the casthouse; it shrinks the pool A2 can use.
    - The hub decision changes only which ceiling applies: 40 kt with the hub, up to 100 kt without.
- **(d) Verified spreads and pool.** All three must hold:
  - (i) **A2 net down-shift spread ≥6 points.** The test compares contracted lower-rung prices with the 2025–26 invoice prices of the grades they replace, net of quality cost (open item 4).
  - (ii) **A3 net substitution spread ≥6 points on the LME basis.** It is (100 − contracted A3 price as % of LME) minus the casthouse deductions measured in a 2 × 50 t trial against hot metal (melt loss, energy, trim). The evidence is:
    - ≥2 firm quotes or contracts per A3 grade family;
    - 12 months of MB-AL-0405 and MB-AL-0426 history;
    - the trial (open item 32).
  - (iii) **C ≥100 kt** (open item 22).
  - **Before T2 is released, the CFO re-books Case A at the verified spreads and tonnes.** At the floors (A2 6 and A3 6 points, with contingency) Case A is still NPV EUR 18.6M, IRR 22.2%.

The 2028 Case A main casthouse capex (EUR 6.0M) is released at the 2028 budget only if three conditions hold:
- the 31 Dec 2027 gate is passed (lab variants pass EN 755 and the JDA is signed);
- T2 has been released;
- the M9 contingency plan has been tabled. It fixes C and the melt configuration if the potlines close (Section 4.6).

### 4.6 ICC and potline risk: the "potlines curtailed from 2030" case

**Why it matters.** The approved board paper puts ICC at the centre:
- ICC is worth EUR 682–852/t, or EUR 205–256M/yr in 2031.
- Without ICC the smelter needs commodity power at no more than EUR 64/MWh.
- The no-ICC contingency plan goes to the Board at **M9 (Jul 2027)**. The decision date for curtailment, closure or continued operation is **31 Dec 2029**.
- The board paper's capital rule defers potroom capex whose payback runs past 2030 until ICC is decided. It exempts casthouse items because the casthouse runs in every option.

B-rod and NHT are casthouse lines, but their economics rest on liquid metal from the potlines. Case A runs on scrap. Its throughput (A1) and its A2 pool still depend on how much the casthouse can melt once hot metal stops. Every line is therefore tested in a second ledger state.

**1. Post-2030 ICC: the timeline problem**

- **Current scheme [S].** The 2021–30 ETS State-aid Guidelines are OJ C 317, 25 Sep 2020 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52020XC0925(01))).
  - Aid intensity is 75%. Inputs are the 14.256 MWh/t aluminium benchmark and 0.72 tCO₂/MWh.
  - Aid is paid in year t+1, so the last guaranteed receipt is in 2031, for 2030 costs.
- **Dec 2025 amendment [S].** It widened eligibility to more sectors ([EU Reporter](https://www.eureporter.co/environment/2025/12/30/commission-amends-ets-state-aid-guidelines-to-tackle-carbon-leakage-for-more-energy-intensive-industries/)).
  - Nothing in the repo record says it extends the scheme beyond 2030.
  - The board paper's 80% high-case aid intensity goes to its day-45 legal opinion.
- **Precedent for lead time [recall]:**
  - The 2013–20 guidelines were adopted in May 2012, about 7 months before the period began.
  - The 2021–30 guidelines were adopted in Sep 2020, about 3 months before the period began and about 30 months after the ETS Directive amendment (EU) 2018/410.
  - The likely sequence now is an ETS review proposal in 2026, co-decision in 2027–28, then guidelines between mid-2029 and Q3 2030. National notification adds 3–9 months.
- **Estimate.** There is a **25–40% chance [est.]** that a final post-2030 guideline exists by 31 Dec 2029. The Board will most likely decide on a draft.
- **Further risk [recall].** CBAM for aluminium covers direct emissions only. If the Commission adds indirect emissions to CBAM, it may argue that ICC is less needed.
- **Consequence for this memo.** Any line built in 2028 must be robust to curtailment, because the guideline will probably not exist before both lines are built.
- **Owner:** Regulatory Affairs with European Aluminium, inside the board paper's CEO-led ICC campaign (open item 26).

**2. Public analogue: what curtailed EU casthouses actually melt (new in revision 5)**

All figures come from search-engine extracts of the cited pages; the primary documents could not be opened this round. [est.] marks our own arithmetic.

| Site | Former primary (kt/yr) | Casthouse (kt/yr) | Solid melt during or after curtailment | Outcome | Source |
|---|---|---|---|---|---|
| **Speira Rheinwerk, Neuss** | ~160 nameplate, ~140 run; cut 50% Oct 2022, fully closed Mar 2023 | Permit: 435 rolling ingot; 370.5 solid melt | The UBC line (2016, EUR 45M, 50 kt) took site recycling to ~100 kt. The new furnace S4 (Oct 2026, EUR 40M) takes **83 kt of scrap in and gives 66 kt of liquid out**. Dedicated recycling furnaces ~166 kt [est.]. One secondary profile says ~65 kt is actually recycled | Casthouse runs as a recycling hub, helped by the scrap loop from the neighbouring Alunorf mill | [EUWID permit application](https://www.euwid-recycling.de/news/wirtschaft/speira-beantragt-neuen-recyclingofen-in-neuss-170724/); [drweb](https://www.drweb.de/speira-neuss-recyclingofen-40-millionen/); [BRD 2015 permit](https://www.brd.nrw.de/system/files/media/document/2022-01/20150625_5_53_UIB_neus005_%C3%84nderungsgenehmigung_Aluminium_Giesserei.pdf); [Recycling Today 2016](https://www.recyclingtoday.com/news/hydro-aluminum-recycling-ubcs-germany); [mining.com 2022](https://www.mining.com/web/german-aluminum-smelter-considers-halving-output-on-energy-costs/); [AlCircle](https://www.alcircle.com/news/60kt-a-year-red-bull-backs-speiras-40m-aluminium-recycling-furnace-at-rheinwerk-121519) |
| **Trimet Essen** | 165; cut 50% Mar 2022 | >240 cast (record); ~265 [est.] | **100 kt of scrap and dross recycling** alongside primary. A scrap hall was added in 2026 (+16 kt storage). No public data on how much scrap replaced the lost primary during the cut | Integrated site, potlines running | [AlCircle ASI](https://www.alcircle.com/news/trimet-s-aluminium-facility-in-essen-enters-asi-performance-standard-certification-94983); [produktion.de](https://www.produktion.de/wirtschaft/trimet-aluminium-ag-steigert-umsatz-um-61-prozent/1748761); [Euronews factbox](https://www.euronews.com/2022/08/25/metals-aluminium-factbox) |
| **Slovalco (Hydro), Žiar** | 175; stopped Aug 2022 to Jan 2023 | ~200 | A remelt centre for clean process scrap (opened Jun 2022) is rated 45–55 kt; Hydro guided "75 kt recycled". In 2023 sales fell from EUR 650M to EUR 99.5M, staff from 417 to 216, and the net loss was EUR 9.1M. Implied 2023 tonnage is **37–55 kt** [est.] | Loss-making. A 75 kt restart (EUR 100M) is conditional on Slovak ICC approval and a 10-year hydro power contract | [Hydro 2019](https://hydro.com/en/media/news/2019/slovalco-to-partially-curtail-production); [Recycling Today](https://www.recyclingtoday.com/news/slovaco-shuttering-primary-aluminum-production); [Penta](https://www.pentainvestments.com/en/?p=3303); [Symsite](https://www.symsite.sk/single-post/slovalco-lost-9-1m-in-2023); [Hydro 2026](https://www.hydro.com/en/global/media/news/2026/slovalco-to-restart-75000-tonnes-of-curtailed-aluminium-capacity-supplying-a-critical-raw-material-for-europe/) |
| **Aldel, Delfzijl** | 115–150; primary stopped Oct 2021 | 160 | 45 kt recycled input in normal operation. Ran on recycling only for about 10 months | Care and maintenance Sep 2022, bankruptcy Oct 2022 | [WoodMac summary](https://woodmac.com/reports/metals-aldel-aluminium-smelter-16049236); [mining.com](https://www.mining.com/web/dutch-aluminum-maker-aldel-halts-remaining-production/); [AlCircle](https://www.alcircle.com/news/dutch-aluminium-producer-aldel-ceases-all-remaining-production-83474) |
| **Trimet Voerde** | ~95; cut 30% Oct 2021 | n/a | No public data | – | [Euronews factbox](https://www.euronews.com/2022/08/25/metals-aluminium-factbox) |

**Ratio of solid-melt capacity to former primary liquid:**

| Case | Ratio | Reading |
|---|---|---|
| Rheinwerk (best case) | 166 ÷ 160 = **~104%** | Took two furnace projects (2016 and 2026) and EUR 85M, plus a neighbouring mill's scrap loop |
| Trimet Essen (integrated, potlines running) | 100 ÷ 165 = **61%** | What an integrated casthouse runs every day |
| Slovalco and Aldel (stranded) | **21–31%** | Scrap melting alone did not carry the fixed costs |
| **Our C ≥190 kt claim** | 190 ÷ 300 = **63%** | Trimet-level. Reachable only with a Rheinwerk-type configuration: dedicated multi-chamber or side-well furnaces, 6.5–16 kt of scrap storage, and secured scrap supply |

- **Yield check.**
  - The S4 permit gives 66 ÷ 83 = **79.5%** metal yield on coated UBC.
  - 190 kt of liquid C needs about **200 kt of scrap at 95% yield (clean process scrap), and up to 238 kt at 80% (post-consumer)** [est.]. That is 16–19% of the 1.27 Mt the EU exported in 2025.
  - Press coverage of Speira's S4 says the next bottleneck there is scrap supply, not furnace capacity.
- **Capex per t/yr of solid-melt capacity** (search extracts; [Speira/drweb](https://www.drweb.de/speira-neuss-recyclingofen-40-millionen/), [EUWID 2015](https://www.euwid-recycling.com/news/business/hydro-to-invest-EUR45m-in-new-recycling-line-in-neuss/), [Novelis](https://novelis.com/news/ten-years-of-innovation-and-sustainability-at-novelis-nachterstedt-revolutionizing-the-aluminium-industry/), [Constellium](https://www.constellium.com/news/the-grand-opening-of-its-new-recycling-center-in-neuf-brisach), [WAM/EGA](https://www.wam.ae/en/article/bnaj92w-ega-expand-german-aluminium-recycling-capacity), [SMM/REMET](https://news.metal.com/newscontent/103680979-tin-nhanh-nhôm-smmnhà-máy-remet-58-triệu-euro-thúc-đẩy-tái-chế-nhôm-tại-hungary), [Investment Monitor](https://www.investmentmonitor.ai/news/norsk-hydro-recycling-plant-in-michigan-nears-completion), [Hydro Torija](https://hydro.com/en/media/news/2024/hydro-invests-eur-180-million-in-new-spanish-aluminium-recycler-to-decarbonize-european-industries)):

  | Project | Capex | Capacity | EUR per t/yr |
  |---|---|---|---|
  | Speira S4, Rheinwerk (2026, brownfield furnace + casting line + 6.5 kt store) | EUR 40M | 66 kt liquid (83 kt input) | **606** (482 per t input) |
  | Hydro UBC line, Neuss (2016, incl. sorting and delacquering) | EUR 45M | 50 kt | **900** |
  | Novelis Nachterstedt (2014, greenfield) | >EUR 300M | 400 kt | **750** |
  | Constellium Neuf-Brisach (2024, brownfield) | EUR 130M | 130 kt | **1,000** |
  | EGA Hannover (FID 2025, melt + cast + 110 kt sorting) | ≈EUR 155M | 153 kt | **~1,010** |
  | REMET, Hungary (2025) | EUR 58M | ~54 kt | **~1,075** |
  | Hydro Cassopolis (2023, greenfield billet) | ≈EUR 137M | 120 kt | **~1,140** |
  | Hydro Torija (2024 FID, greenfield) | EUR 180M | 120 kt | **1,500** |

  - **Planning range** for a brownfield furnace added to an existing casthouse: **EUR 600–1,000 per t/yr, central 800**.
  - **Lead time:** Speira filed in July 2024 and commissioned in October 2026, about 27 months. Plan on 2.5–3 years, so capacity in 2030 needs FID by mid-2027.
- **What C ≥190 kt implies for us [est.].**
  - Integrated casthouses run 25–40% solid charge (Essen ~38%, Aldel 28%).
  - On an assumed ~330 kt casthouse, existing solid melt is about **80–130 kt**. Our 2025–26 intake C (130 kt est.) sits at the top of that range.
  - The gap to 190 kt is 60–110 kt. That costs **EUR 36M (60 × 600) to EUR 110M (110 × 1,000), central EUR 68M (85 × 800)**.
- **Consequence for this memo.**
  - C ≥190 kt is a **funded option-C configuration** (the board paper's scrap-fed casthouse, decided after M9), not a passive outcome.
  - This memo books it only in that configuration, and only on contracted A2 tonnes.
  - The curtailed headline uses the **stranded casthouse on existing melt**.
- **Owners** (all in open item 34):
  - Casthouse Engineering: current solid-melt capacity and charge mix by furnace.
  - EHS and Permitting: permitted solid melt under the emissions permit.
  - Capex Controlling: furnace RFQ for 60–110 kt.
  - Market Intelligence: 2022–23 remelt tonnages at Trimet and Slovalco, from the Bundesanzeiger and the Slovak register.

**3. Remelt penalty: purchased ingot against liquid metal** [est., first principles; no public cost disclosure]

| Component | Range | Basis |
|---|---|---|
| Melting energy | **EUR 29–64/t** | 0.55–0.75 MWh/t in a stack melter, 0.8–1.2 in a reverberatory furnace. Gas plus CO₂ costs about EUR 53/MWh (EUR 35 gas + 0.202 t × EUR 90) |
| Melt loss on clean ingot | EUR 12–49/t | 0.5–2% × EUR 2,431/t, net of dross recovery |
| Labour, refractory, flux, dross handling | EUR 15–35/t | |
| Inbound logistics from Rotterdam | EUR 10–30/t | |
| **Penalty against liquid metal** | **EUR 70–160/t; central EUR 115/t** | |

**Cross-checks:**
- The model already values wrought scrap at P1020 DP − EUR 100.
- Scrap-to-cast-alloy remelt conversion costs EUR 200–350/t [S, repo report 07].
- Rod conversion from purchased ingot comes to about EUR 190/t in total (EUR 75 + 115).
- The B-rod curtailment run includes a EUR 10M solid-feed melter, about EUR 174 per t/yr on 57.6 kt.
  - That melter is a clean-ingot stack melter. It is a lighter asset than the scrap-recycling furnaces with casting lines in the table above (EUR 600–1,500 per t/yr) [est.].
  - The stack-melter quote (open item 25) closes it.

**Owners:** Controlling closes this from our own remelt-furnace cost centre. Casthouse Engineering provides a stack-melter quote (open item 25).

**4. Ledger, potlines curtailed from 2030** [calc]

| kt/yr | 2028 | 2029 | 2030 on |
|---|---|---|---|
| Spare primary | 30.0 | 35.0 | **0** |
| NHT draw (primary + hub scrap backfill while the potlines run) | 0 | 3.8 (6 kt) | **10.8 primary, purchased P1020** |
| Rod need (57 kt × 1.01) | 15.2 from spare | 45.5 (31.2 spare + 14.3 billet) | **57.6, purchased P1020** |
| Hub wrought scrap to NHT backfilled in billet | – | – | No longer needed: billet itself runs on scrap and purchased metal |
| **Purchased P1020 for the two options** | – | – | **68.4 kt × EUR 2,431 ≈ EUR 166M/yr** |

- That adds about EUR 7M of working capital, roughly −EUR 3M of NPV that is **not** in the runs below [est.].
- From 2030 rod is judged on its margin over purchased ingot, not on displaced billet, because the casthouse no longer rations liquid metal.

**5. Results by line** (NPV10 EUR M, decision basis, contingency included unless stated, no grant)

| Line | ICC renewed | Curtailed from 2030 (penalty 70 / **115** / 160) | Curtailed from 2031 (115) | Reading |
|---|---|---|---|---|
| **Case A** (scrap-fed; no contingency, as in Section 5.4) | 31.1 | **Stranded casthouse on existing melt: 27.8 at C 130, 10.5 at C 100.** Option-C configuration (C 190): 31.1 at the 40 kt contracted, 65.0 only with 100 kt of A2 contracted | — | Robust on existing melt, though lower, because A1 scales with casthouse throughput (145/300 at C 130). The revision 4 figure of 78.7 assumed C ≥190 without melt capex or contracts, and is withdrawn. With contingency: 25.6 at C 130, 8.3 at C 100 |
| **B-ext** (1370/6101 billet from purchased P1020 at −EUR 115/t on 15 kt) | 19.1 | **12.1** | — | Robust |
| **NHT** 30 kt (contribution 231 → 190) | −4.1 | −7.0 / **−8.8** / −10.7 | −8.4 | Basis B survives purchased P1020 except for the remelt cost, but it was negative to start with. Break-even volume rises from 35.0 to **43.3 kt** |
| **B-rod** central adders | −0.5 | +9.2 / **−1.8** / −10.2 | +1.6 | Barely worse, because 55% of rod displaced billet anyway. **Highly sensitive to the penalty:** each EUR 45/t moves NPV by about EUR 10M; break-even is **EUR 108/t** |
| B-rod, LOW / HIGH adders | −15.2 / +14.5 | — / −21.0 / +16.3 (at 115) | — | |
| B-rod, no Al-Zr | −11.7 (base capex) | — / −17.6 / — | — | |
| B-rod + EUR 10M solid-feed melter charged | — | — / **−9.4** / — | — | Fails clearly if it must fund its own melting |
| Both options together | −4.6 | **−10.6** | — | Before the WC effect of about −3 |
| **P0 committed** | 26.6 | **16.4** (stranded, C 130); 19.7 (option C, 40 kt); −1.0 (stranded, C 100) | — | Alloy portfolio only |

- **Mid-cycle rod margin from purchased ingot is EUR 40/t** (230 − 75 − 115), against EUR 155/t from liquid metal. Steady-state B-rod EBITDA is EUR 6.05M/yr including Al-Zr.

**6. Capital rule adopted in this memo (consistent with the board paper's ICC-cliff rule)**
- **Capex that depends on liquid metal (B-rod, NHT) must clear NPV10 ≥ 0 under both ledgers at its gate:** ICC renewed, and potlines curtailed from 2030 at the measured remelt penalty.
- Both gates sit on **30 Sep 2027, after the M9 contingency plan**. The plan's fixed-cost split, option ranking, melt configuration and C for a scrap-fed casthouse are then known.
- An option that passes only the ICC-renewed test is **deferred, not rejected**. It is re-tested after the **31 Dec 2029** decision, with first metal no earlier than 2031.
- Casthouse lines that run on scrap or purchased metal pass both ledgers today.
  - Case A clears with contingency even when stranded at C 100 (EUR 8.3M).
  - B-ext clears at EUR 12.1M.
  - Like the board paper's casthouse exemption, they are not held to the ICC date.

---

## 5. Business case A: scrap-tolerant alloys and AI casthouse blending (GO)

### 5.1 Logic

Sorting alone creates no value if our alloy specifications still force us to dilute the sorted scrap with primary metal. Value comes from three steps together:
1. **Scrap with a known composition distribution.** The source is grade-certified purchased lots under contract, plus our own inline chemistry. The hub's LIBS/XRF data are added if the hub reaches FID.
2. **Alloys designed for that distribution:** Fe 0.4–0.8 with Mn/Cr to convert β-AlFeSi to the α-phase.
   - There is industrial evidence for this ([AIT](https://publications.ait.ac.at/en/publications/tolerance-of-almgsi-wrought-alloys-for-high-fe-contents-the-role-/)).
   - A Kaiser application, US 2023/0416879 A1, claims Fe and Mn up to 0.8% at >75–90% scrap ([Justia](https://patents.justia.com/patent/20230416879)).
3. **A charge optimiser** that aims each melt at the cheapest compliant mix, with products specified by property window rather than a tight composition window.

**How Case A and the hub divide the value:**
- **The hub owns** the Zorba/ELV-shred-to-sorted spread on its own intake (board paper: 12 points × 90 kt × EUR 21.55 = EUR 23.3M uplift).
- **Case A owns** what the wide alloy windows let the casthouse do with the scrap it still buys under contract:
  - buy it one rung lower (A2);
  - use more of it in place of primary (A3);
  - sell the brand (A4).
- **The wide windows are also what make the hub's 90% upgraded share achievable** [est.]. With strict EN AW-6063 windows the share is about 75%, and the hub falls from −EUR 7.9M to −EUR 27.1M.
  - Case A claims none of that EUR 19.2M. It is the hub's, and the board paper already counts it.
  - The M3 LIBS trial tests it (Section 5.2).

### 5.2 Value levers at steady state (2030), with every sum shown

| Lever | Mechanism | EUR/t | Volume | Low | High | Base |
|---|---|---|---|---|---|---|
| A1 AI charge optimisation (netted against the furnace robots; **sweetening re-priced in revision 5**) | Charge cost (2–5 pp less sweetening at the A3 net spread, plus alloy additions) plus the **chemistry-driven** share of yield only. Oxidation and dross loss belong to the robot case | 3.1–10.8 (base 6.7) per t of output | 300 kt | 0.92 | 3.25 | 2.00 |
| A2 Casthouse-side down-shift (**on contracted tonnes**) | Wide Fe/Cu/Zn windows let the casthouse buy its remaining purchased scrap one rung lower (to mixed wrought / old rolled or taint/tabor). Net of about 2 points of quality cost, that is 6–10 net points (base 8) × EUR 21.55. **Tonnes = min(contracted, ramp × pool)** | 129–216 (base 172) | 10 / 100 / 40 kt (C = 100 / 190 / 130; the base is the 40 kt T2 contracts) | 1.29 | 21.55 | 6.90 |
| A3 Higher recycled content (**re-valued in revision 5**) | Post-consumer scrap replaces primary in billet and sheet. The delivered price is 85.75% of LME (50/50 billet/sheet blend on the public ladder), a gross spread of 14.25 points. Less 5.3 points of casthouse cost against hot metal, that is **9 net points** × EUR 21.55 | 129–280 (base 194) | 10–30 kt (base 15, contracted) | 1.29 | 8.40 | 2.91 |
| A4 Certified ≥75% post-consumer brand, sold to the named shortlist (Section 5.5) | Recycled and low-carbon premium, ASI/DNV verified, EPD < 2 kg CO2e/kg | Building 50–200 (base 100); crash 100–300 (base 175) | 20 kt building + 8 kt crash | 1.80 | 6.40 | 3.40 |
| A5 Portfolio rationalisation | Fewer alloy changes, larger segregated pools, less downgrading | — | Group-wide | 2.00 | 5.00 | 3.00 |
| **Gross** | | | | **7.30** | **44.60** | **18.20** |
| Overlap haircut, 20% (A1, A2 and A3 share scrap tonnes) [CTO est.] | | | | −1.46 | −8.92 | −3.64 |
| **Net lever value** | | | | **5.84** | **35.68** | **14.56** |
| Incremental opex (Section 5.3) | | | | −3.00 | −2.00 | −2.50 |
| **EBITDA, 2030 onward** | | | | **2.84** | **33.68** | **12.06** |

**A4 build-up (unchanged):**
- Base: 20 kt × EUR 100 + 8 kt × EUR 175 = EUR 3.40M.
- Low: 20 × 50 + 8 × 100 = EUR 1.80M.
- High: 20 × 200 + 8 × 300 = EUR 6.40M.

**CO2:** A3 avoids 15 kt × 15.5 t = 233 kt CO2/yr in the base case, and 465 kt at 30 kt.

**A3 restated against published post-consumer scrap prices** (model section R5.1)

*What has been published, 2024–26* (search extracts; levels behind a paywall are marked):

| Grade (feeds) | Published price | Date | % of LME | Source |
|---|---|---|---|---|
| Clean new 6063 production scrap (billet) | LME **+EUR 48/t** | 2026 average to Mar 2026 | ~102 | [Fastmarkets webinar, Mar 2026](https://www.fastmarkets.com/uploads/2026/03/Fastmarkets-aluminium-scrap-on-demand-webinar-slides.pdf) (MB-AL-0404) |
| European extrusion-grade scrap, as reported by Hydro (process and post-consumer not separated) | 107 / 106 / 104 / ~108 / ~110 | Q3 25 to Q3 26 | 104–110 | Hydro [Q4 2025](https://www.hydro.com/globalassets/06-investors/reports-and-presentations/quarterly-reports/2026/q4vs2ln9p/fourth-quarter-report-2025.pdf), [Q1 2026](https://www.hydro.com/globalassets/06-investors/reports-and-presentations/quarterly-reports/2026/q1a0n5lk/first-quarter-report-2026.pdf), [Q3 2026](https://www.hydro.com/globalassets/06-investors/reports-and-presentations/quarterly-reports/2026/q3u7ns/third-quarter-report-2026.pdf) reports. Q3 metric label not confirmed from the extract |
| **Post-consumer 95/5 6063 extrusions (billet)** | LME **−EUR 278/t** | 2026 average to Mar 2026 | **89.8** at the Q1 2026 LME of EUR 2,734 ([ALRO](https://m.bvb.ro/infocont/infocont26/ALR_20260529150444_Quarterly-Report-Q1-2026-ENG.pdf)); 87.1 if the EUR discount is held at the normalised EUR 2,155 | Same Fastmarkets deck; spec in [MB-AL-0405](https://www.fastmarkets.com/commodity-prices/aluminium-scrap-post-consumer-95-5-extrusions-6063-differential-to-lme-delivered-consumer-europe-euro-tonne-mb-al-0405/). The series was briefly pulled after a publication error on 16 Jul ([notice](https://www.fastmarkets.com/insights/incorrect-publication-of-aluminium-scrap-and-secondary-alloy-prices/)) |
| Taint/tabor, shredded and sorted (sheet, some billet) | Level paywalled | Weekly since 28 Nov 2025 | n/a | [MB-AL-0426](https://www.fastmarkets.com/commodity-prices/MB-AL-0426) |
| Taint/tabor, delivered EU works | EUR 1,550–1,600/t, then EUR 1,600–1,700/t on 25 Apr | 2024 | ~77–78 (Jan 2024); ~66–70 (Apr 2024, scrap lagging an LME spike) [our conversion] | [Argus, May 2024](https://www.argusmedia.com/en/news-and-insights/market-opinion-and-analysis-blog/al-scrap-shortage-worries-european-alloy-producers) |
| Secondary grades (twitch, Zorba, taint/tabor), EU buyers | **70–85** (one grade 75–85); clean primary scrap 100–110 | Q4 2025 | 70–85 | [Recycling Europe CfE feedback, Feb 2026](https://recyclingeurope.org/wp-content/uploads/2026/02/UPDATED-Recycling-Europe-feedback-CfE-aluminium-measures-16-Februrary-2026.pdf) (advocacy source). The Commission's CfE cites "93% of LME" with no source |
| Old rolled, baled (UK) | Level paywalled | – | – | [MB-AL-0282](https://www.fastmarkets.com/commodity-prices/aluminium-scrap-baled-old-rolled-lme-discount-delivered-consumer-uk-pound-tonne-mb-al-0282/) |
| German dealer buying prices, small lots (yard, not delivered) | Clean profiles EUR 1,850–1,900/t; painted profiles EUR 1,730–1,780/t; old sheet EUR 1,800/t | Oct 2026 | 64–70 against LME of ~EUR 2,700 ([aluminiumpreis.eu](https://www.aluminiumpreis.eu/)) | [hein-schrotthandel](https://www.hein-schrotthandel.de/schrottpreise/), [pur-umwelt](https://www.pur-umwelt.com/schrottpreise/) |

**Yard-to-consumer markup.**
- Clean profiles cost about 70% of LME at a German yard. Sorted post-consumer 6063 is about 90% delivered to the consumer.
- The ~20-point gap covers collection, sorting, baling, freight and trader margin.
- Applying a 15–20 point markup to the 67% yard price for old sheet gives **old rolled / mixed wrought at about 82–87% delivered [est.]**.

*Ladder for the grades A3 can use, and the booked spread:*

| Step | Low | High | Central | Basis |
|---|---|---|---|---|
| Post-consumer 95/5 6063 / LIBS-sorted 6xxx (billet half) | 87 | 90 | **89** | MB-AL-0405 print |
| Taint/tabor (sheet) | 78 | 85 | **82** | Recycling Europe, Argus |
| Old rolled / mixed wrought (sheet) | 80 | 86 | **83** [est.] | Yard price + markup |
| 50/50 billet/sheet blend [est.], % of LME delivered | 83.00 | 87.75 | **85.75** | 0.5 × 89 + 0.5 × (82 + 83)/2 |
| **Gross spread against primary at LME** | 12.25 | 17.00 | **14.25** | 100 − blend |
| Extra melt loss net of dross recovery (bare extrusion 1.5–2.5%, shredded painted sheet 3–5%) | 2.0 | 3.0 | 2.5 | ~3% loss × scrap value, less 30–50% recovered [est.] |
| Remelt energy and CO2 against hot metal | 1.4 | 2.1 | 1.8 | 0.65–0.8 MWh gas × EUR 30–40 + 0.13 t CO2 × EUR 75 = EUR 30–45/t [est.] |
| Decoating, sampling, LIBS QA, Mg/Si trim | 0.5 | 1.4 | 1.0 | EUR 10–30/t [est.] |
| **Net A3 spread (points)** | 5.75 | 13.10 | **8.95 → booked 9 (EUR 194/t); booked range 6–13** | [calc] |

- **The revision 4 figure of 80% of LME (20 points, EUR 431/t) is withdrawn.**
  - It holds only for twitch, Zorba and shred, which are the grades that need the hub.
  - It carried no casthouse deductions. A2 already netted 2 points of quality cost; A3 now does the same on its own cost items.
- **A3 = 15 kt × EUR 194/t = EUR 2.91M/yr** (was 6.46). Range: 10 kt × 6 points = EUR 1.29M to 30 kt × 13 points = EUR 8.40M.
- **Why our number is below the CEO's 10–16 point ladder range.**
  - That range is the gross spread of the billet-usable grades.
  - We deduct 5.3 points of casthouse cost on top, because the scrap replaces liquid hot metal, not ingot.
  - Case A is EUR 38.8M at 16 net points, EUR 35.5M at 13 and EUR 31.1M at 9.
- **Upside not booked: the P1020 basis.**
  - The memo values displaced primary at LME flat, but values yield at P1020 DP (EUR 2,431, +12.8 points).
  - If the casthouse buys external P1020, A3 avoids those purchases at the DP price. The net spread is then about **22 points**.
  - If A3 frees our own metal for sale as ingot, the gain is +12.8 less about 3 points of casting and freight, for about **19 points**.
  - Either would restore roughly the old 20 points, on a different logic.
  - It is booked only after S&OP confirms the casthouse mass balance (due 6 Nov 2026, open item 6). Until then the booked figure stays at 9 points.
- **Gate (T2(d)(ii), Section 4.5).** A3 must verify at ≥6 net points, using firm quotes or contracts, MB-AL-0405/0426 history and a 2 × 50 t trial. Case A is re-booked at the verified figure.
- **Who closes it (open item 32):**

  | Owner | Action | Date |
  |---|---|---|
  | Head of Market Intelligence | Fastmarkets subscription for MB-AL-0404 / 0405 / 0426 / 0282 (about EUR 5–15k/yr [est.], inside the 90-day budget) | 13 Nov 2026 |
  | Head of Scrap Procurement | ≥2 firm supplier quotes per A3 grade family, priced as a differential to LME delivered | 15 Dec 2026 |
  | CFO / Controller | Model re-run on the quotes; premium-basis ruling (LME or P1020 DP), using the S&OP mass balance due 6 Nov 2026 | 15 Dec 2026 |
  | Casthouse Manager | Melt-loss, energy and trim trial on 2 × 50 t lots against hot metal | 31 Mar 2027 |
  | Head of Scrap Procurement + CFO | Contract-based confirmation and re-booking | At T2: earliest 30 Jun 2027, latest 31 Oct 2027 |

**A1 netted against the furnace-robot case, re-priced** (model sections R4.1, R5.2)

*What is published:*

| Source | Claim | What it covers |
|---|---|---|
| **SMS Metallics Optimizer** ([SMS](https://www.sms-group.com/product/metallics-optimizer)) | Cheapest mix that meets spec; "lower raw material losses"; **no % or EUR/t** | Mostly charge cost |
| **Speira rollout** ([Foundry Planet](https://www.foundry-planet.com/d/digital-solution-enhances-efficiency-reduces-costs-and-promotes-sustainable-circular-economy/)) | 3 sites plus an option for 6; **no site results** | Charge cost, scrap share |
| **GHI ALEA** ([GHI](https://www.ghifurnaces.com/digitalize/)) | "Up to 20% shorter cycle time, lower gas" | Energy and throughput |
| **RiA charge and skim** ([AlCircle](https://www.alcircle.com/news/maximise-productivity-and-safety-of-your-casthouse-with-ria-charge-and-skim-at-the-earliest-and-safest-time-every-time-104304); [ICSOBA 2023](https://icsoba.org/assets/files/publications/2023/Papers/CH06%20-%20Safe,%20Autonomous,%20and%20Energy%20Efficient%20Furnace%20Tending,%20Minimizing%20Waste.pdf)) | 1.5 t Al saved per 500 t = **0.30%** | **100% melt loss / dross.** This is the board paper's robot benchmark |
| **Dynamic Concept/EPIQ ARFT** ([AlCircle](https://www.alcircle.com/news/epiq-and-dynamic-concept-partner-to-deliver-advanced-solutions-across-the-gulf-118544)) | Skimming, cleaning, stirring; no metal-loss figure | — |

The only quantified public metal-loss benchmark is RiA's 0.30%, and the robot case already uses it. No charge optimiser publishes a yield figure.

*Split of A1 on its own unit values (revision 5):*
- **Sweetening:** 2 / 3.5 / 5 pp × the A3 net spread of EUR 194/t = EUR 3.9 / 6.8 / 9.7 per t. Revision 4 used EUR 431/t: 8.6 / 15.1 / 21.6.
- **Yield:** 0.2 / 0.35 / 0.5 pp × P1020 DP EUR 2,431 = EUR 4.9 / 8.5 / 12.2 per t. This is the same basis that gives the robots 0.3% × 2,431 = **EUR 7.29/t**.
- The yield share is 55.6% in all three cases (was 36.1%).
- Applied to A1's capped EUR 5 / 10 / 15 per t:
  - the yield component is EUR 2.78 / 5.56 / 8.34;
  - the charge-cost component is EUR 2.22 / **4.44** / 6.66.

*Overlap test (unchanged):*
- Together, the two papers claimed 0.5–0.8 pp of melt-loss reduction on the same 300 kt.
- Melt loss that charging and skimming practice can address is about 1.0–2.5% of throughput [est.].
- Removing 25–50% of it with two levers that do not change melting technology is not credible. The overlap is therefore real.

*Mechanism split of A1's yield* [est.]:
- **50–70% is oxidation and dross** (charge sequencing, time at temperature, door-open time). **The robot case owns this part. A1 gets zero.**
- **30–50% is chemistry-driven** (fewer off-spec melts, less dilution and rework). **A1 keeps this part.**

| Case | Charge cost | Retained yield | **A1 net EUR/t** | EUR M/yr | Revision 4 (EUR/t / EUR M) |
|---|---|---|---|---|---|
| Low | 2.22 | 2.78 × 0.3 = 0.83 | **3.05** | 0.92 | 3.74 / 1.12 |
| Base | 4.44 | 5.56 × 0.4 = 2.22 | **6.66** | 2.00 | 7.84 / 2.35 |
| High | 6.66 | 8.34 × 0.5 = 4.17 | **10.83** | 3.25 | 12.30 / 3.69 |

**Board view:**
- Robot metal loss EUR 7.3/t + A1 EUR 6.7/t = **EUR 14.0/t**. That is about 0.39 pp of metal loss in total (0.30 robots + 0.09 A1).
- The effect of the re-pricing on Case A NPV10 is **−EUR 1.6M** (bridge, Section 5.4).

*Rules:*
1. **One owner per loss pool.** The robots own furnace-practice melt loss, measured at M12 (≥0.25%).
2. The A1 shadow run gate is **≥EUR 3/t on charge cost alone**, from the optimiser's cost logs.
   - Revision 4's EUR 4/t was 63% of a EUR 6.39/t base. EUR 3/t is the same 63% of the restated EUR 4.44/t base, so the test is not loosened.
   - Robots are not on the furnaces before M9, so the 30 Jun 2027 run measures a pre-robot baseline.
   - A yield credit is booked only where the melt-by-melt balance shows loss reduction beyond the robots' measured saving.
3. **A1/A3 tonnage overlap.**
   - A1's 2–5 pp less sweetening is 6–15 kt of primary replaced by scrap, at the same EUR 194/t as A3's 15 kt.
   - The 20% haircut (EUR 3.64M) exceeds A1's whole charge-cost component (EUR 1.33M), so a full overlap stays inside the haircut.
   - The CFO confirms the tonnes by 15 Dec 2026 (open item 27).

**A2 against the public scrap ladder and the hub's Board dates** (model sections R4.2, R5.3)

*European scrap price ladder, 2024–26, % of LME delivered EU (revision 5).* Rows marked [est.] are reasoned ranges; the anchors are the prints above.

| Grade | Range | Central | EUR/t at 2,155 | Public anchor |
|---|---|---|---|---|
| Clean new 6063 extrusion | 100–104 | **102** | 2,198 | MB-AL-0404, LME + EUR 48/t |
| Post-consumer 95/5 6063 / LIBS-sorted 6xxx | 87–90 | **89** | 1,918 | MB-AL-0405, LME − EUR 278/t (was 90 [est.] in revision 4) |
| Mixed wrought / old rolled | 80–86 | **83** [est.] | 1,789 | Yard prices + 15–20 point markup; MB-AL-0282 paywalled (was 84) |
| Taint/tabor | 78–85 | **82** | 1,767 | Recycling Europe 70–85 (Q4 2025); Argus 2024; MB-AL-0426 paywalled (was 83) |
| Twitch | 73–82 | **78** [est.] | 1,681 | Argus reports Twitch oversupply ([Argus](https://www.argusmedia.com/en/news-and-insights/latest-market-news/1803797-twitch-oversupply-weighs-on-aluminium-scrap-in-europe)); Recycling Europe 70–85 |
| Zorba 90/2 | 68–80 | **75** [est.] | 1,616 | Record 1.27 Mt of EU scrap exports in 2025 points to the tight end ([EUWID](https://www.euwid-recycling.de/news/maerkte/eu-aluschrottexporte-2025-auf-rekordhoch-270326/)) |
| ELV shred (not floated) | 58–72 | **65** [est.] | 1,401 | No print found |

**Cross-checks:**
- UBC was 84% of LME in Sep 2026 in the US ([AlCircle](https://www.alcircle.com/news/ubc-scrap-prices-in-q3-2026-values-rise-in-august-and-september-after-july-decline-121581)).
- EU restrictions on scrap shipments to non-OECD countries have been delayed to September ([Engineering News](https://www.engineeringnews.co.za/article/eu-aluminium-scrap-export-curbs-delayed-until-september-group-and-sources-say-2026-06-26)). When they apply, they should widen low-grade discounts by about 2–5 points [est.].
- **The implied Zorba-to-sorted spread is 14 points central (7–22) [est.].**
  - It is down from 15 because LIBS-sorted 6xxx is now anchored at 89.
  - That equals the hub's 14-point FID gate.
  - The board paper's 12 points (Zorba 80%, output 92%) remains conservative. 15 points is kept below as a sensitivity.
- **The A2 down-shift gap is unchanged in substance.** Moving from sorted 6xxx (89) or clean extrusion (102) down to mixed wrought (83) or taint/tabor (82) is 6–20 points. After 2 points of quality cost, that is 6–10 net points, central 8.

*Sorter evidence on window width (unchanged):*
- **What is published** covers purity and throughput only:
  - TOMRA AUTOSORT PULSE: 4–7 t/h, purity above 95% ([TOMRA](https://www.tomra.com/waste-metal-recycling/media-center/customer-stories/gerhard-lang)).
  - Steinert PLASMAX: up to 11 t/h, purity above 99% ([Steinert](https://steinertglobal.com/stemin-plasmax/)).
  - Hydro Nowa Sól: 120 kt with 2 HySort units ([Hydro](https://integration.hydro.com/en/global/about-hydro/hydro-worldwide/europe/poland/nowa-sol/hydro-aluminium-nowa-sol/)).
- **What is missing.** No vendor publishes a curve linking alloy-window width to upgraded share.
- **Estimate [est.].** Widening from strict 6063 (Fe ≤0.35, Cu ≤0.10, Zn ≤0.10) to scrap-tolerant 6xxx (Fe about 0.6, Cu about 0.3, Zn about 0.25) lifts the upgraded share from about 75% to about 90%, with a range of +10 to +20 points.
- **Who closes it.** The hub's M3 LIBS trial runs the same Zorba lot twice, once with strict and once with wide windows, for about EUR 20–50k inside the hub's trial budget (open item 24).

*Two ways A2 could be valued. Only R2 is booked:*
- **R1, a higher upgraded share inside the hub, belongs to the hub.**
  - The uplift per input tonne is share × spread × EUR 21.55.
    - At 12 points that is EUR 194 (75%) or EUR 233 (90%).
    - At 14 points it is EUR 272 at 90%.
    - At 15 points it is EUR 242 or EUR 291.
  - The hub's EUR 270 gate needs a 90% share at 13.9 points, or ≥83.5% at 15 points.
  - The window value is **EUR 3.88M/yr of hub EBITDA and EUR 19.2M of hub NPV** at 12 points. The board paper's 90% base already counts it.
- **R2, a casthouse-side saving on contracted tonnes, is booked in Case A.**
  - Under the T2(c) contracts, the casthouse buys part of its remaining purchased scrap one rung lower. For example, it moves from sorted 6xxx or clean extrusion down to mixed wrought or taint/tabor.
  - **Tonnes = min(contracted lower-rung tonnes, qualification ramp × min(100, C − 90 × hub load)).**
  - The ramp is 28% in 2028 and 70% in 2029 (building windows first), then 100%. The hub load follows the board paper: 12.5% in 2028, 70% in 2029, 100% from 2030.

| Year | Hub load (board paper) | Hub sorted output into casthouse | Purchased pool left (C = 130) | × qualification ramp | Contracted lower-rung tonnes (T2(c)) | **A2 kt booked** | A2 gross EUR M (8 points) |
|---|---|---|---|---|---|---|---|
| 2028 | 12.5% | 11.3 kt | 100 (capped) | 28.0 | 40 | **28.0** | 4.83 |
| 2029 | 70% | 63.0 kt | 67.0 | 46.9 | 40 | **40.0** (revision 4: 46.9) | 6.90 |
| 2030 on | 100% | 90.0 kt | 40.0 | 40.0 | 40 | **40.0** | **6.90** |

**Result:**
- **A2 is EUR 6.90M/yr gross from 2029.** It is now 38% of gross lever value because A3 fell.
- **Why the cap is `min(contracted, ramp × pool)`.**
  - The CEO's re-run applied the ramp to the contract (`ramp × min(100, 40)`). That gives EUR 42.1M on revision 4 levers, and the script reproduces it.
  - That form books only 11 kt in 2028, although 40 kt is under contract and 28 kt can be used.
  - Our form books the smaller of what is contracted and what the qualified windows can absorb.
  - On revision 4 levers it gives EUR 44.8M at 55 kt, the same in both routes.
- If the hub is not built, A2 can rise to 100 kt × 8 points = EUR 17.24M, but **only on tonnes that are contracted** (Section 5.4A).

### 5.3 Investment and opex [CTO est. unless noted]

| Item | Low | High | Base (EUR M) | 2027 / 2028 / 2029 / 2030 |
|---|---|---|---|---|
| Charge optimiser: SMS Metallics Optimizer or GHI ALEA, integration, inline chemistry | 2.0 | 3.0 | 2.5 | 2.5 / – / – / – |
| Casthouse adaptation for lower-grade scrap: melt treatment, Mn/Cr master-alloy dosing, a contaminated-scrap furnace | 8.0 | 15.0 | 12.0 | 2.5 / 6.0 / 3.0 / 0.5 |
| Development of 3 alloys (HRC 6060/6063, 6082, 5xxx/6xxx sheet); the informatics team is costed in Section 7 | 4.0 | 6.0 | 5.0 | 2.0 / 2.0 / 1.0 / – |
| Customer qualification, 2–3 alloy-OEM pairs at EUR 1–5M per pair [est.] | 3.0 | 9.0 | 6.0 | 1.0 / 1.5 / 2.0 / 1.5 |
| Certification and brand: ASI chain-of-custody, EPDs, trademark | 1.0 | 2.0 | 1.5 | 1.0 / 0.5 / – / – |
| **Total investment** | **18.0** | **35.0** | **27.0** | **9.0 / 10.0 / 6.0 / 2.0** |
| Grant: Innovation Fund small-scale on the casthouse adaptation, 35% × 12.0 | 0 | 7.2 (60% maximum) | 4.2 if awarded | |
| **Incremental opex per year:** optimiser licence 0.5, scrap QA and inline-chemistry consumables 0.8, application engineering 0.8, certification audits 0.4 | 2.0 | 3.0 | **2.5** (1.5 in 2027) | |

**The 100 kt scrap hub is not in Case A.**
- It is a separate Board decision in the group paper: GO to FID gate, EUR 50M capex + EUR 2.5M development + EUR 10M working capital, FID at M12 (Oct 2027).
- Its FID risk is carried explicitly in Section 5.4A, not assumed away.
- **Scrap contracts carry no capex.** The ≥55 kt/yr of T2(c) contracts are purchases at market-indexed prices. The A2 and A3 savings are already net of their price.

### 5.4 Cash table and runs, base case (EUR M)

**Lever ramp, gross and net of the 20% haircut (model section R5.3):**

| Year | A1 | A2 (kt) | A2 | A3 | A4 | A5 | Gross | Net | EBITDA (net − opex) |
|---|---|---|---|---|---|---|---|---|---|
| 2027 | 0.83 (one furnace) | 0 | 0 | 0 | 0 | 0 | 0.83 | 0.67 | −0.83 |
| 2028 | 2.00 | 28.0 | 4.83 | 0 | 0 | 1.00 | 7.83 | 6.26 | 3.76 |
| 2029 | 2.00 | 40.0 | 6.90 | 0.97 (5 kt) | 0 | 2.20 | 12.06 | 9.65 | 7.15 |
| 2030 on | 2.00 | 40.0 | 6.90 | 2.91 | 3.40 | 3.00 | 18.20 | 14.56 | 12.06 |

| Year | Capex | EBITDA | Tax | Cash flow | Cumulative | IF grant (if awarded) |
|---|---|---|---|---|---|---|
| 2027 | −9.0 | −0.8 | 0.0 | −9.8 | −9.8 | – |
| 2028 | −10.0 | 3.8 | −0.6 | −6.9 | −16.7 | +2.1 |
| 2029 | −6.0 | 7.2 | −1.4 | −0.2 | −16.9 | +2.1 |
| 2030 | −2.0 | 12.1 | −2.6 | +7.5 | −9.4 | – |
| 2031 | −0.5 (sustaining) | 12.1 | −2.6 | +9.0 | −0.4 | – |
| 2032 | −0.5 | 12.1 | −2.5 | +9.0 | **+8.6** | – |
| 2033–2040 (each year) | −0.5 | 12.1 | −2.5 | +9.0 to +9.1 | +81.0 by 2040 | – |

**Tax check for 2028:** depreciation = cumulative capex 19.0 / 15 = 1.27. EBIT = 3.76 − 1.27 = 2.49. Tax = 25% × 2.49 = 0.62.

| Run | NPV10 (EUR M) | IRR | Payback |
|---|---|---|---|
| **Decision basis: hub built on its Board dates, 55 kt contracted (A2 40 kt at 8 net points, A3 15 kt at 9 net points), C 130 kt, no grant** | **31.1** | **31.3%** | **2032** |
| Base, +10% capex contingency | 28.9 | 28.4% | 2032 |
| **Base carrying the whole capability centre** (Section 4.4) | **10.3** | **15.9%** | 2034 |
| Base, with IF grant of 4.2 | 34.7 | 36.3% | 2031 |
| Low: capex 35, C 100, A2 6 points, A3 10 kt × 6 points, low levers, opex 3.0 | −17.9 | −3.8% | never |
| High: capex 18, C 190 (100 kt contracted), A2 10 points, A3 30 kt × 13 points, high levers, opex 2.0 | 133.7 | 108.9% | 2029 |
| C = 100 kt / 190 kt (hub built; 190 needs 100 kt of A2 contracted) | 12.9 / 67.0 | 19.9% / 49.5% | 2033 / 2031 |
| A2 net down-shift 6 / 10 points | 24.0 / 38.2 | 26.6% / 36.1% | 2032 / 2031 |
| A3 net spread 6 / 8 / 13 / 16 points | 27.8 / 30.0 / 35.5 / 38.8 | 29.5% / 30.7% / 33.7% / 35.5% | 2032 / 2032 / 2031 / 2031 |
| A3 at the withdrawn 20 points (reference) | 43.1 | 37.7% | 2031 |
| **T2(d) floors: A2 6 and A3 6 points, +10% contingency** | **18.6** | **22.2%** | 2033 |
| Hub start-up slips to Q3 2029 (A2 is capped by the 40 kt contracts either way) | 31.1 | 31.3% | 2032 |
| **Hub not built, booked on contracted tonnes** (Section 5.4A): 55 / 70 / 115 kt | **31.1 / 40.7 / 67.0** | 31.3% / 37.0% / 49.5% | 2032 / 2031 / 2031 |
| Potlines curtailed from 2030, stranded casthouse on existing melt (C 130 / 100) | 27.8 / 10.5 | 29.6% / 18.7% | |
| Potlines curtailed, option-C configuration (C 190): 40 / 100 kt of A2 contracted | 31.1 / 65.0 | 31.3% / 47.1% | |
| A2 = 0 | 2.5 | 11.8% | 2035 |
| A4 = 0 (no buyer pays a premium) | 20.1 | 25.1% | 2032 |
| No scrap contracts at all, but full EUR 27M spent (A2 = A3 = 0) | −7.5 | 3.9% | 2038 |
| **Re-scoped after a failed T2:** only the EUR 5.5M T1 spend, A1 + A5, opex 1.0 | **6.7** | **26.7%** | 2031 |

**Bridge from revision 4:**

| Step | NPV10 after the step | Change |
|---|---|---|
| Revision 4 decision basis | 45.3 | |
| A2 capped at the 40 kt contracted in 2029 (was 46.9 kt) | 44.8 | −0.6 |
| A3 at 9 net points on the public post-consumer ladder (was 20) | 32.7 | −12.0 |
| A1 sweetening re-priced at the A3 spread | **31.1** | −1.6 |

(Steps are computed unrounded: −0.59, −12.04, −1.62.)

**What drives the case:**
- **Low-capex levers.** The high IRR comes from cheaper purchased scrap and recycled content once the alloy window allows it.
- **Three variables:**
  - **Contracted lower-rung tonnes** (A2): EUR 31.1M at 40 kt of A2. If the hub is not built, each extra contracted kt adds about EUR 0.64M.
  - **The two verified spreads:** each net point of A2 is worth about EUR 3.6M of NPV; each net point of A3 about EUR 1.1M.
  - **C**, the casthouse's existing scrap intake: EUR 12.9M at 100 kt.
- **Downside protection.**
  - In the all-low stack Case A does not clear (−EUR 17.9M).
  - The protection is that T2 and the 31 Dec 2027 gate hold EUR 21.5M of the EUR 27.0M until the contracts, both spreads and C are verified.
  - If they fail, the re-scoped case still returns +EUR 6.7M.

### 5.4A Case A and the scrap hub as one investment, on contracted tonnes (model sections R4.4, R5.4, R5.5)

**Basis:**
- **Hub:** the board paper's own model, reproduced exactly.
  - Inputs: EUR 50M split 25/25 over 2027–28, EUR 2.5M development, EUR 10M working capital, EUR 13.5M/yr operating cost, life to 2042, loss carry-forward.
  - Result: −EUR 7.9M at 12 points, +EUR 11.2M at 14 points and +EUR 20.8M at 15 points.
  - Its NPV is zero at 12.8 points and moves about EUR 9.56M per point.
- **Case A:** revision 5 above, booked on contracted tonnes.
- **Combination:** cash flows are summed year by year.
- **Combined spend:** 27.0 + 50.0 + 2.5 + 10.0 WC = **EUR 89.5M**. Combined EBITDA at maturity is 12.06 + 9.77 = **EUR 21.83M/yr**.

**1. Can the no-hub tonnes be contracted? Public evidence on EU scrap supply contracts** (search extracts)

| Deal / data point | Volume | Tenor | Pricing basis | Source |
|---|---|---|---|---|
| TSR (Remondis) to Novelis Nachterstedt, presorted end-of-life TSR130/TSR136, Oct 2024 | 75 kt in total, **about 25 kt/yr** | 3 years | Not disclosed | [Recycling Today](https://recyclingtoday.com/news/novelis-parters-with-tsr), [Fastmarkets](https://fastmarkets.com/insights/tsr-and-novelis-sign-supply-deal-for-sustainable-p1020-substitute-high-grade-aluminium-scrap), [Aluminium Today](https://aluminiumtoday.com/news/novelis-and-tsr-strategic-partnership-to-advance-circularity-in-the-aluminium-industry) |
| Novelis Europe scrap intake | About 700 kt/yr; the TSR deal adds about 50 kt | — | — | Same sources |
| Hydro and Sims Alumisource (US benchmark), Mar 2024 | About 36 kt/yr post-consumer | Multi-year | Not disclosed | [AlCircle](https://www.alcircle.com/news/hydro-to-source-processed-aluminium-scrap-from-sims-alumisource-for-its-north-american-extrusion-unit-110234) |
| Hydro post-consumer scrap use | 444 kt (2023), target 850–1,200 kt by 2030 | — | — | [S&P Global](https://www.spglobal.com/commodity-insights/en/news-research/latest-news/metals/102424-interview-hydro-pushes-to-boost-post-consumer-aluminum-scrap-consumption-in-europe) |
| Constellium recycled input | 717 kt (2025); more than 750 kt/yr capacity | Historically "generally not bound by long-term contracts" | — | [Waste Recycling Mag](https://www.wasterecyclingmag.com/news/recycling/constellium-lifts-recycled-aluminium-share-to-47-in-2025), [SEC F-1](https://www.sec.gov/Archives/edgar/data/0001563411/000119312513408105/d613544df1.htm) |
| STEMIN (Bergamo, Steinert LIBS) | About 180 kt/yr processed | — | — | [Recycling Product News](https://www.recyclingproductnews.com/article/44533/stemin-processes-180000-tonnes-of-aluminum-annually-with-steinert-alloy-sorting-system) |
| TSR–Schüco, Gerhard Lang–TOMRA, Scholz, Galloo, Speira | No volumes or offtakers disclosed. Scholz is reportedly being sold to Derichebourg (May 2026, [unverified]) | — | — | [windoorexpert](https://www.windoorexpert.eu/news/news,36557,w,for-a-closed-aluminium-material-cycle-collaboration-between-the-tsr-group-and-schuco.html), [TOMRA](https://www.tomra.com/waste-metal-recycling/media-center/customer-stories/gerhard-lang) |
| How contracts are priced | Payable % of LME, applied to the lower of LME cash and 3-month, set within the delivery month. Taint/tabor assessed weekly by Fastmarkets (MB-AL-0426) since Nov 2025 | — | % of LME | [Fastmarkets ext.](https://fastmarkets.com/insights/launch-of-european-domestic-aluminium-extrusion-scrap-assessments), [MB-AL-0426](https://www.fastmarkets.com/commodity-prices/MB-AL-0426) |
| How tenor is trending | Buyers booking more spot and quarterly deals in 2026 (US prime scrap) | Getting shorter | — | [S&P Global](https://www.spglobal.com/energy/en/news-research/latest-news/metals/020226-us-aluminum-historically-wide-spreads-in-prime-scrap-market-change-2026-contract-behavior) |
| EU exports | 1.27 Mt in 2025, a record, mostly to India. Restrictions on non-OECD shipments delayed | — | — | [Engineering News](https://www.engineeringnews.co.za/article/eu-aluminium-scrap-export-curbs-delayed-until-september-group-and-sources-say-2026-06-26), [European Aluminium](https://www.european-aluminium.eu/circular-economy/) |

**Reading [est.]:**
- **What a deal looks like.**
  - The largest disclosed EU deal is about 25 kt/yr for 3 years, from Europe's largest recycler (7.2 Mt/yr across all metals).
  - The benchmark is roughly 25–40 kt/yr per counterparty, on 1–3 year tenors.
  - No public contract discloses its % of LME.
- **55 kt is realistic; 115 kt is not proven.**
  - 55 kt is 2–3 firm contracts plus re-specification of existing suppliers. The A2 tonnes are today's purchases, bought one grade lower.
  - 115 kt would need 3–5 firm contracts. We would compete with Hydro (adding 400–750 kt of post-consumer demand by 2030), Novelis and Constellium.
- **What helps.** The lower rungs we need (mixed wrought, taint/tabor) are oversupplied or exported. Argus reports Twitch oversupply, and the 1.27 Mt of exports is about 11 times 115 kt.
- **Estimate.** Contractable on firm terms of 3 years or more by 31 Oct 2027: **40–90 kt/yr, central 70 kt** (A2 55 + A3 15).
- **Cost of reaching 115 kt.** It probably needs a security-of-supply premium of 1–2 points. At 7 or 6 net A2 points instead of 8, Case A at 115 kt is **EUR 59.0M or 50.9M**.

**2. Case A without the hub, on contracted tonnes, and what that does to the hub comparison** (model section R5.4)

| Contracted (A2 + A3 15) | Case A, no hub | IRR | Portfolio P0, no hub (revision 4: 76.2) | EV at 50% hub FID, 12 / 14 pts (revision 4: 59.0 / 68.6) | Hub internal threshold (revision 4: 16.5) | Hub external threshold |
|---|---|---|---|---|---|---|
| 40 kt (below T2 minimum) | 21.2 | 25.0% | 16.7 | 22.2 / 31.8 | 11.8 | 14.3 |
| **55 kt (T2(c) minimum)** | **31.1** | 31.3% | **26.6** | **27.1 / 36.7** | **12.8** | 14.3 |
| **70 kt (central contracting estimate)** | **40.7** | 37.0% | **36.2** | **32.0 / 41.5** | **13.8** | 14.3 |
| 85 kt | 50.3 | 42.5% | 45.8 | 36.8 / 46.3 | 14.8 | 14.3 |
| 100 kt | 58.6 | 46.1% | 54.2 | 40.9 / 50.5 | 15.7 | 14.3 |
| 115 kt (revision 4 basis; no public precedent) | 67.0 | 49.5% | 62.5 | 45.1 / 54.7 | 16.6 | 14.3 |

How the figures are built:
- **No-hub bridge (EUR M):**
  - Revision 4's 80.6 assumed 115 kt, with A3 at 20 points.
  - Booked on the 55 kt that T2(c) actually requires, it is **44.8** (−35.9).
  - With A3 at 9 points and A1 re-priced, it is **31.1** (−13.7).
  - Your re-run of 42.1 uses the ramp-on-contract form (Section 5.2).
- **At 55 kt the two routes are identical (EUR 31.1M).**
  - With the hub, the residual pool is 40 kt; without it, the contracts are 40 kt.
  - Each extra contracted kt of A2 is worth about **EUR 0.64M of NPV** between 55 and 70 kt, and 0.60 on average up to 115.
- **Expected value at 50% hub FID** is 0.5 × combined value with the hub (23.2 at 12 points, 42.3 at 14) + 0.5 × Case A with no hub at the contracted tonnes. It assumes the contracts are signed in either state.
- **Internal threshold** is the spread at which hub value + Case A with the hub built (31.1) equals Case A with no hub at the contracted T.
  - At 55 kt it is the hub's own break-even of 12.8 points, because there is nothing to crowd out.
  - Each extra 15 kt of contracted A2 raises it about 1 point.
- **The 14.3-point external threshold does not move with tonnes.** In that route the casthouse keeps its contracted tonnes and the hub sells outside at −1.5 points. The test therefore reduces to "hub NPV > 0 at −1.5 points".

**Tonnage break-evens (total contracted kt, no hub):**
- **≥42.7 kt** beats the combined value with the hub at 12 points (23.2).
- **≥55.0 kt** equals Case A with the hub built (31.1).
- **≥72.5 kt** beats the combined value at the hub's 14-point FID gate (42.3). This is also the tonnage at which the internal threshold reaches 14 points.
- **≥87.8 kt** beats the combined value at 15 points (51.9).

**3. Combined view on the revision 5 basis** (model section R5.5)

| EUR M, NPV10 at 1 Jan 2027 | Hub alone | Case A | **Combined** | IRR |
|---|---|---|---|---|
| **12 points (board base)** | −7.9 | 31.1 | **23.2** | 14.7% (payback 2034) |
| **14 points (hub FID gate; revision 5 ladder central)** | 11.2 | 31.1 | **42.3** | 18.2% |
| 15 points (sensitivity) | 20.8 | 31.1 | **51.9** | 19.8% |
| Post-FID capex phasing 5/40/5 (12 / 14 / 15 points) | −5.7 / 13.5 / 23.0 | 31.1 | 25.4 / 44.6 / 54.1 | 15.5% / 19.3% / 21.1% |
| Hub start-up slips to Q3 2029, 12 points | −8.1 | 31.1 | 23.0 | |
| C = 100 kt (12 / 14 points) | −7.9 / 11.2 | 12.9 | 5.0 / 24.2 | |
| C = 190 kt, 100 kt of A2 contracted (12 / 14 points) | −7.9 / 11.2 | 67.0 | 59.1 / 78.2 | |
| Hub output sold externally at −1.5 points; casthouse keeps its contracted 55 kt (12 / 14 / 15 points) | −22.3 / −3.1 / 6.5 | 31.1 | 8.8 / 28.0 / 37.5 | |
| Same, casthouse keeps 70 kt contracted | −22.3 / −3.1 / 6.5 | 40.7 | 18.4 / 37.6 / 47.2 | |
| **Potlines curtailed from 2030, stranded casthouse (C 130)**, 12 / 14 points | −7.9 / 11.2 | 27.8 | **19.9 / 39.0** | |
| Potlines curtailed, option-C configuration with 100 kt of A2 contracted, 12 / 14 points | −7.9 / 11.2 | 65.0 | 57.1 / 76.2 | |
| Hub without Case A's wide windows (75% upgraded share), 12 / 14 points | −27.1 / −11.1 | — | — | |
| **Case A with no hub: 55 / 70 kt contracted** | — | **31.1 / 40.7** | **31.1 / 40.7** | 31.3% / 37.0% |
| Expected value at a 50% chance of hub FID (12 / 14 points), 55 / 70 kt | | | 27.1 / 36.7; 32.0 / 41.5 | |

**Combined cash flow at 12 points (EUR M)**

| Year | Case A | Hub | Combined | Cumulative |
|---|---|---|---|---|
| 2027 | −9.8 | −27.5 | −37.3 | −37.3 |
| 2028 | −6.9 | −33.8 | −40.6 | −78.0 |
| 2029 | −0.2 | +6.8 | +6.6 | −71.4 |
| 2030 | +7.5 | +7.4 | +14.9 | −56.4 |
| 2031 | +9.0 | +7.2 | +16.2 | −40.2 |
| 2032 | +9.0 | +7.2 | +16.2 | −24.1 |
| 2033 | +9.0 | +7.2 | +16.2 | −7.9 |
| 2034–2040 (each year) | +9.0 to +9.1 | +7.2 | +16.2 | +8.3 in 2034; +105.7 by 2040 |
| 2041–2042 | 0 | +7.2 / +17.2 (WC release) | | +130.0 by 2042 |

**What the combined view shows:**
1. **Revision 3 double-counted, and revision 4 over-sized the no-hub route.** Revision 4's no-hub value of EUR 80.6M rested on 115 kt that no gate secured. On contracted tonnes, the no-hub route is worth EUR 31.1M at the T2 minimum and EUR 40.7M at the central contracting estimate.
2. **The crowd-out is small at the tonnes we can contract.**
   - While the potlines run, the hub and Case A still compete for the same casthouse pool.
   - At 55 kt the hub costs Case A nothing. At 70 kt the hub needs only 13.8 points to add group value.
   - Both are below its 14-point FID gate.
3. **If the potlines are curtailed, the pair is worth EUR 19.9–39.0M on the existing melt.**
   - Revision 4's EUR 70.8–89.9M "complements" figure required C ≥190 kt and 100 kt of A2 that no gate secured.
   - That figure is reached (EUR 57.1–76.2M) only in the funded option-C configuration with those tonnes contracted.
   - The hub's value to the group is therefore mainly feed security for option C, which is the board paper's own rationale.
4. **The hub's base case depends on Case A.** Its 90% upgraded share needs wide alloy windows [est.]. Without them it is −EUR 27.1M at 12 points. The two should be decided together.

**Decisions this leads to:**
- **Case A is approved on its own terms.** The decision basis assumes the hub is built and 55 kt is contracted. It counts no hub value, and no tonnes beyond those contracts.
- **T2 is conditional on contracted tonnes and verified spreads** (Section 4.5), with the same 55 kt in either hub state. A2 tonnes above 40 kt are booked only after M12 confirms there is no hub, and only when contracted.
- **The revision 4 amendment to the hub FID test (a 16.5-point internal spread) is withdrawn.** On the tonnes we can contract, the hub's own EUR 270 / 14-point gate already ensures that the hub adds group value. The CSO takes a narrower test, **linked to tonnage**, to the M12 Board instead:
  - If contracted lower-rung plus A3 tonnes at M12 are **≤72.5 kt/yr**, the existing gate stands unchanged.
  - If they are **above 72.5 kt**, the hub must also show one of the following:
    - an internal spread at or above the threshold in the table in part 2 for those tonnes (14.8 points at 85 kt, 16.6 at 115);
    - external offtake at ≥14.3 points for its tonnes above the casthouse's free capacity;
    - that the M9 plan selects option C.
  - Contracts above 40 kt of A2 signed before M12 carry a volume-reduction option if the hub reaches FID (Section 4.5).
- **The M3 LIBS trial runs strict and wide windows on the same lot.** One trial then answers both the hub's EUR 270 gate and Case A's window claim.

### 5.5 Named customers, partners and the evidence for A4

**Building-systems houses** (Hydro-owned Wicona, Technal and Domal excluded). All commitments are **[unverified]**, taken from company disclosures as recalled. The Head of Sales and the Sustainability team verify each row against the company's own report by 6 Nov 2026 (about 1 day of work).

| # | Company | Stated commitment [unverified] | Where to verify | Al volume [est.] | Why it fits Case A | JDA rank |
|---|---|---|---|---|---|---|
| B4 | **Hueck** (DE) | Sells low-carbon / high-recycled-content system profiles; customers ask for EPDs | hueck.com: EPDs, sustainability page | 20–30 kt/yr | Mid-sized, own extrusion; fastest JDA counterparty | **1** |
| B3 | **Aluprof** (PL, Grupa Kęty) | Group ESG strategy with Scope 1–2 reduction targets to 2030; low-carbon billet offer | grupakety.com ESG/annual report; aluprof.eu | 40–60 kt/yr | Own presses and casthouse, but buys primary and alloying units | **2** |
| B2 | **Reynaers Aluminium** (BE) | Low Carbon and Ultra Low Carbon profile options; net-zero/SBTi-aligned roadmap | reynaers.com ESG report | 40–60 kt/yr | Extrusion outsourced or mixed, so open to a new billet source | **3** |
| B1 | **Schüco** (DE) | CO2-neutral by 2040; "Low Carbon" and "Ultra Low Carbon" tiers, ULC CIRCAL-based at ≤2.3 kg CO2e/kg under a Hydro partnership | schueco.com: sustainability report, "Carbon Control" | 80–120 kt/yr | Largest EU buyer; Hydro is the incumbent, so a second-source play only. **The case does not rely on B1** | 4 |
| B5 | **Kawneer EMEA** (Arconic) | Low-carbon / recycled-content options tied to EPDs | kawneer.com (EU sites): EPDs | 20–40 kt/yr | No captive primary since the Alcoa split; buys billet | 5 |

**Crash-management OEMs and Tier-1s**

| # | Company | Stated commitment [unverified] | Where to verify | Relevance |
|---|---|---|---|---|
| C1 | **BMW Group** | Supply-chain CO2 per vehicle −20% by 2030 versus 2019 (−40% over the life cycle); "Secondary First", with Neue Klasse targeting about 50% secondary material; buys about 43 kt/yr of solar aluminium from EGA | bmwgroup.com: annual and sustainability report | Specifies crash-management systems (CMS) and castings; Landshut light-metal foundry |
| C3 | **Benteler Automotive** | SBTi-aligned Scope 1–3 path; aluminium CMS from its own extrusion (ex-Raufoss) | benteler.com: sustainability report | Tier-1 that buys 6xxx/7xxx CMS billet |
| C2 | **Volvo Cars** (reserve) | Climate-neutral by 2040; EX30 about 25% recycled aluminium; internal carbon price about SEK 1,000/t CO2 (about EUR 90) | volvocars.com: annual and sustainability report | Buys CMS extrusions; also the NHT target (Section 6A.5) |
| Reserve | Gestamp | SBTi-validated 2030 targets | gestamp.com | Small aluminium share. Kirchhoff is mainly steel, so it is low priority |

- **Recommended JDA pair for automotive:** BMW (OEM pull) plus Benteler (Tier-1 buyer).
- **Named pool:** B1–B5 200–310 kt plus C1–C3 CMS 60–100 kt [est.].
- **Year-3 capture:** 8% of building and 10% of automotive, which gives the 20 kt + 8 kt used for A4.

**Evidence that buyers will pay for A4 (EUR/t)**

| Basis | Calculation | EUR/t |
|---|---|---|
| Exchange low-carbon differential | US$10–40/t ÷ 1.16 (repo report 08) | 9–34 (floor) |
| Branded bilateral premium (CIRCAL- or REDUXA-type) | Repo report 07 [est.]; r2-07 high case EUR 100 | 50–300 |
| Building customer's CO2 value ceiling | (6.7 [est.] − 2.0) kg/kg = 4.7 t CO2 per t Al × EUR 50–100/t CO2 | 235–470 |
| Volvo's internal carbon price applied | 4.7 × EUR 90 | about 423 |

- **Conclusion:** the base premiums (EUR 100 building, EUR 175 crash) take 20–40% of what each buyer's own stated CO2 values would justify.
- **Willingness to pay is proven only by priced LOIs** (T2 trigger). Open item 15 also buys one Fastmarkets differential print to anchor the floor.

**Scrap suppliers for the T2(c) contracts (restated in revision 5):**
- **Targets:**
  - TSR (Remondis). Its Novelis deal is the template, at about 25 kt/yr for 3 years.
  - STEMIN (LIBS-sorted, about 180 kt/yr processed).
  - Gerhard Lang Recycling.
  - Scholz (ownership change reported).
  - Galloo.
  - The 2 regional shredders named by day 60 in the board paper.
- **Structure:**
  - ≥3 MoUs of 20–30 kt/yr each for grade-certified **lower-rung** grades (mixed wrought / old rolled, taint/tabor) and A3 grades. They are priced as % of LME and indexed to MB-AL-0405 / 0426.
  - In parallel, existing suppliers re-specify their current shipments one grade lower. That covers much of the A2 tonnage without new counterparties.
- **Hub-FID clause:** any A2 volume above 40 kt/yr carries a volume-reduction option if the hub reaches FID.

**Other partners**

| Role | Partners |
|---|---|
| Science | Montanuniversität Leoben (Pogatscher group, "dirty alloys"; [TU Wien PDF](https://repositum.tuwien.at/bitstream/20.500.12708/158251/1/Raabe-2022-Progress%20in%20Materials%20Science-vor.pdf)); AIT (Fe tolerance); RWTH; MPIE (RAP). No exclusive ties with NTNU/SINTEF, which are close to Hydro |
| Software and vendors | Thermo-Calc (TCAL11/MOBAL); SMS group (Metallics Optimizer) or GHI (ALEA), with Speira reference calls under NDA; Citrine or Intellegens on trial |
| Sorters (via the hub) | TOMRA (AUTOSORT PULSE), Steinert (PLASMAX) |
| Standards | CEN TC 132, EN 573 / EN 1706 revision, which already aims to raise allowable impurity levels ([BSI](https://standardsdevelopment.bsigroup.com/projects/9026-13536)) |
| Consortia | Horizon CLEANMAT (EUR 7.33M) and RecAL (EUR 10.6M) ([CORDIS](https://cordis.europa.eu/project/id/101294748/de)); our MAT-PROD-22 bid |

### 5.6 Milestones

**Next 12 months**

| Date | Milestone |
|---|---|
| 28 Oct 2026 | Our own 2025–26 scrap purchase invoices by grade, in points of LME (board paper attachment 3; open item 23) |
| 6 Nov 2026 | 8 customer commitment rows verified against company disclosures (Head of Sales + Sustainability). S&OP casthouse mass balance, which decides A3's LME or P1020 basis (open item 6) |
| 13 Nov 2026 | Casthouse existing scrap intake C by alloy confirmed (open item 22). Fastmarkets MB-AL-0404 / 0405 / 0426 / 0282 and Zorba series subscribed (open items 30, 32) |
| 30 Nov 2026 | Optimiser vendor shortlist (SMS vs GHI vs in-house), with Speira reference calls. Data-lake scope frozen. Solid-melt capacity by furnace and permitted solid melt (open item 34) |
| 15 Dec 2026 | NDAs signed with Hueck and Aluprof. Net A2 down-shift spread verified (open item 4). ≥2 firm quotes per A3 grade family and model re-run (open item 32). Melt-loss baseline split by cause (open item 28). A1/A3 tonnage overlap confirmed (open item 27) |
| 31 Dec 2026 | Thermo-Calc installed; first CALPHAD+ML screen of HRC 6063/6082 at Fe 0.4–0.8 |
| 15 Jan 2027 | NDAs with BMW and Benteler; JDA term sheets out to Hueck, Aluprof and Reynaers |
| Jan 2027 (hub M3) | LIBS trial with strict and wide windows on the same Zorba lot (open item 24) |
| 23 Jan 2027 | MAT-PROD-22 proposal complete and signed off (day 90). ≥3 scrap MoU drafts of 20–30 kt/yr for lower-rung and A3 grades (open item 33). **T1 released** |
| **Q1 2027 (by 30 Jan; deadline 2 Feb)** | **MAT-PROD-22 submitted**; data lake v1 live; optimiser vendor chosen |
| 31 Mar 2027 | 20–30 trial casts of ML-designed variants (MPIE/Leoben). A3 casthouse trial on 2 × 50 t lots (open item 32) |
| Apr 2027 | Innovation Fund IF26 small-scale bid for the casthouse adaptation filed (deadline about Apr [est.]). Hub M6 sorted-scrap availability test and feed MoUs |
| **30 Jun 2027** | Optimiser shadow run ≥EUR 3/t charge cost. Priced LOIs from 2 building and 1 automotive buyer. **T2 decision if the 55 kt of contracts and both spreads are in hand** |
| Jul 2027 (M9) | No-ICC contingency plan to the Board (board paper); fixes C and the melt configuration for option C |
| 30 Sep 2027 | ASI chain-of-custody and EPD issued (A4); lab properties of the first variants pass |
| **31 Oct 2027** | Hub FID (M12), with the test linked to tonnage. **T2 decision at the latest; otherwise Case A is re-scoped.** Trial extrusions at Hueck/Aluprof. First building-systems JDA signed |

**Later years**

| Year | Milestone |
|---|---|
| 2028 | Optimiser live on all furnaces; first commercial HRC billet; A2 on 28 kt of contracted lower-rung scrap; hub start-up in Q4 at 12.5% load if FID passed |
| 2029 | A2 at the 40 kt contracted; A3 at 5 kt; BMW/Benteler qualification complete; AA Teal Sheet filed after 12 months of commercial supply ([AA form](https://www.aluminum.org/sites/default/files/2021-11/TEMPLATEWROUGHTALLOYREGISTRATIONFORM20180.docx)); ≥75% post-consumer brand at volume; 31 Dec 2029 ICC decision |
| 2030 | Hub at 100% (if built); A3 at 15 kt contracted; full house-alloy portfolio; any A2 above 40 kt only if the hub was not built and the tonnes are contracted |

---

## 6. Business case B: conductor and thermal-management alloys (B-ext GO; B-rod WATCH)

### 6.1 Logic and the copper-substitution numbers on one basis

**Equal-conductance mass ratio:** Al/Cu = (1/0.61) × 2.70 / 8.96 = **0.494**. One tonne of aluminium replaces 2.02 t of copper.

**Metal-cost saving per unit of conductance** is 1 − 0.494 / (Cu/Al ratio):

| Basis | Ratio | Saving |
|---|---|---|
| Board basis | 3.80x | 87.0% |
| 2026 average [est.] | 4.45x | 88.9% |
| Spot | 4.90x | 89.9% |

**Customer metal saving per tonne of copper replaced:**
- Board basis: (9,500 − 0.494 × 2,500) / 1.16 = **EUR 7,125**.
- Spot: (14,400 − 0.494 × 2,940) / 1.1215 = **EUR 11,545**.

**Installed-system saving** is 20–40% [est.]. It is lower than the metal saving because aluminium needs 1.64x the cross-section, plus joints and terminations.

**Our capture:** a gross conversion premium of EUR 1,200/t Al [est.] equals EUR 593 per t of copper replaced. That is about 8% of the customer's saving on the board basis.

**What our 15 kt of B-ext replaces:** 30.4 kt of copper, a customer metal saving of 30.4 × 7,125 = EUR 216M/yr.

**Switching band:** the board-basis 3.80x sits inside the 3.5–4.0x band where switching starts ([AlCircle](https://www.alcircle.com/news/rising-copper-prices-accelerate-shift-towards-aluminium-wiring-in-automotive-industry-120125)). B-ext is therefore sized at 15 kt on the board basis and 20 kt at spot.

**Demand:**
- EU grid investment of EUR 584bn ([EC](https://energy.ec.europa.eu/publications/eu-action-plan-grids_en)).
- Data-centre aluminium of 0.6–0.9 Mt/yr at peak inside the asset, 55% of it in cooling ([Wood Mackenzie](https://www.woodmac.com/press-releases/wood-mackenzie-data-centre-metals-demand-isnt-an-asset-story.-its-a-grid-story)).
- Prysmian is at about 40% aluminium by weight ([AlCircle](https://www.alcircle.com/news/rising-copper-prices-accelerate-shift-towards-aluminium-wiring-in-automotive-industry-120125)).
- EU cable makers import rod; Hydro Karmøy supplies about 70 kt/yr ([Hydro](https://hydro.com/en/aluminium/products/casthouse-products/wire-rod-for-cable-and-wire-solutions/)).

**Where AI helps:**
- A model of conductivity as a function of scrap mix, boron treatment and ageing, aimed at 61% IACS with 30–50% recycled content. Midal's MiRecAL benchmark is 15–30% ([EPD](https://www.environdec.com/library/epd28974)).
- If the potlines close, this model decides how much clean 1xxx scrap can replace purchased P1020 in rod and busbar.

### 6.2 Rod against billet on one basis: the matched adder table

**What the public record holds:**
- **No published 2019–26 EC/1370 rod-adder series was found.**
- As far as we know, European rod is priced in bilateral annual contracts: LME + duty-paid P1020 premium + a rod adder.
- Benchmarks for billet and P1020 are published. For example, SMM put the P1020A premium at US$317.5/t in Dec 2025 ([SMM](https://news.metal.com/newscontent/103467009/Announcement-on-the-European-P1020A-aluminium-premium-price-[SMM-Price-Announcement])).
- Cable makers' results commentary does not give the adder, and the Nexans–Hydro deal has no disclosed price.
- The low-carbon differential on value-added products is US$20–30/t ([Fastmarkets](https://fastmarkets.com/insights/fastmarkets-low-carbon-aluminium-differentials-to-bring-transparency-to-emerging-trend)).

**Owners of the rod-premium series** (open item 3):
- **Head of Market Intelligence:** Fastmarkets/CRU 2019–26 pull, by 13 Nov 2026.
- **Head of Sales Ops:** our own billet invoices net of freight, by 6 Nov 2026.
- **Head of Casthouse Products:** adder indications in RFQs to Nexans, Prysmian, NKT, Lamifil, Tratos and De Angeli, by 15 Jan 2027.

**Assumptions:**
- **Billet spread S:** the billet premium minus the P1020 premium.
  - These are annual averages recalled from memory [est., unverified].
  - The only sourced points are a billet premium of about US$500/t in Dec 2025 and US$1,175–1,250/t in May 2026 ([AlCircle](https://www.alcircle.com/news/european-aluminium-premium-reaches-a-record-472-t-in-march-is-it-a-build-up-from-last-year-or-the-hormuz-crisis-117803)).
- **Rod adder A** [est.].
  - Rod contracts are annual, so A lags billet and moves about 0.7–0.9× as far.
  - The 2026 value is calibrated so that rod ≈ billet today, consistent with the CEO's reading of a US$600–750 adder.
- **Conversion versus ingot:**
  - Rod from liquid metal: EUR 75/t [est., range 50–100]. This includes rod-line opex.
  - Rod from purchased ingot: EUR 75 + EUR 115 remelt penalty = about EUR 190/t (Section 4.6).
  - Billet: EUR 115/t [est., range 90–150].
  - Owner: Plant Controller (open item 7).

**Formulas:**
- Rod margin over ingot = A × 0.862 − 75.
- Billet margin over ingot = S × 0.862 − 115.
- Rod − billet = (A − S) × 0.862 + 40.
- **Rod beats billet whenever A ≥ S − US$46/t.**

| Year | Billet DDP / P1020 DP (US$/t over LME) | Billet spread S | Rod adder A (range) | Rod vs ingot EUR/t | Billet vs ingot EUR/t | **Rod − billet EUR/t** |
|---|---|---|---|---|---|---|
| 2019 | 420 / 130 | 290 | 200 (150–250) | 97 | 135 | −38 |
| 2020 | 330 / 110 | 220 | 170 (120–220) | 72 | 75 | −3 |
| 2021 | 700 / 260 | 440 | 300 (220–380) | 184 | 264 | −81 |
| 2022 | 1,050 / 420 | 630 | 450 (320–600) | 313 | 428 | −115 |
| 2023 | 520 / 240 | 280 | 230 (170–300) | 123 | 126 | −3 |
| 2024 | 500 / 260 | 240 | 220 (160–290) | 115 | 92 | +23 |
| 2025 | 650 / 300 | 350 | 300 (220–380) | 184 | 187 | −3 |
| 2026 YTD | 1,200 / 450 | 750 | 700 (450–750) | 528 | 532 | **−3** |
| **Mid-cycle (2019–25 average)** | | **350** | **267** | **155** | **187** | **−31** |

- **On the CEO's own 2026 range** (US$600–750) and our EUR 75 rod conversion cost, 2026 rod − billet is −EUR 89 to +40/t.
- **Revision 2's rod-adder column** (US$350–850) **is withdrawn** and kept only as an upper-bound sensitivity in Section 6.4.

### 6.3 Value levers at maturity (EUR M/yr, mid-cycle, central adders)

**Rod line:** 60 kt nameplate, 57 kt output (about 34 kt EC 1370, 14 kt 8xxx, 9 kt 6101/6201).

| Lever | S1′: all rod metal from spare ingot | **Ledger: NHT built, 45% from spare / 55% from billet** | S2′: all rod metal displaces billet | Potlines curtailed: all rod metal purchased P1020 |
|---|---|---|---|---|
| B1 Rod margin over ingot: 57 kt × EUR 155.3 | 8.85 | 8.85 | 8.85 | 57 kt × EUR 40.3 = 2.30 (after EUR 115 remelt) |
| Billet displacement: rod tonnes sourced from billet × EUR 186.7 | 0 | −5.84 (31.3 kt) | −10.64 (57 kt) | 0 |
| B4 Al-Zr TAl/ZTAl rod: 7.5 kt × EUR 500 (300–800), 50% in 2030 | 3.75 | 3.75 | 3.75 | 3.75 |
| B2 scrap / B3 green premium (revision 2) | Removed: the scrap belongs to A3; billet earns the same green premium under A4 | | | |
| **B-rod EBITDA** | **12.60** | **6.76** | **1.96** | **6.05** |

At 2026 prices, the ledger case gives EUR 17.24M/yr.

**B-ext: busbar and thermal extrusions on existing presses**

| Item | Low | High | Base |
|---|---|---|---|
| Volume, kt (12 at stress, 20 at spot) | 12 | 20 | 15 |
| Incremental margin over standard profiles, EUR/t | 300 | 600 | 400 |
| Margin, EUR M | 3.60 | 12.00 | 6.00 |
| Application engineers (opex) | −0.50 | −0.50 | −0.50 |
| **B-ext EBITDA** | **3.10** | **11.50** | **5.50** |
| If potlines curtailed from 2030: 15 kt × EUR 115 remelt penalty on 1370/6101 billet | | | −1.73 → **3.78** |

**Case B total at maturity:**
- B-ext alone (committed): EUR 5.5M.
- With B-rod on the ledger: EUR 12.3M.

### 6.4 Investment, opex, cash tables and scenarios

**Investment [CTO est.]**

| Item | Low | High | Base (EUR M) |
|---|---|---|---|
| Continuous rod line, 8–10 t/h (Properzi CCR or Southwire SCR type), brownfield on existing furnaces, with boron treatment and degassing. Equipment about US$12–25M; installed cost EUR 400–830 per t/yr; consistent with the repo estimate of EUR 40–80M per 100 kt (Report 3). **No vendor quote yet: open item 5** | 24.0 | 50.0 | 36.0, or **39.6 with 10% contingency** (60% in 2027, 40% in 2028) |
| Solid-feed (stack) melter, needed only if the potlines close and the option-C casthouse cannot supply melt capacity | — | — | 10 [est.], not in the base case (Section 4.6) |
| Conductor alloy development and type tests (EN 50182/50183, IEC 62641/62004) | 1.5 | 4.0 | 2.5 (1.0 / 1.0 / 0.5) |
| Rod working capital | | | 2.0 (2028, released in 2040) |
| Rod sustaining capex | | | 0.5/yr from 2030 |
| B-ext: dies, fabrication and finishing cell, coolant-compatible surface treatment | 5.0 | 10.0 | 7.5 (4.0 in 2027, 3.5 in 2028) |
| B-ext working capital / sustaining capex | | | 1.0 (2028–29) / 0.2 per yr from 2030 |
| B-ext opex | | | 0.5/yr |

**Ramps:**
- **Rod:** 15 kt in 2028, 45 kt in 2029, 57 kt from 2030.
- **B4 (Al-Zr):** 50% in 2030, 100% from 2031.
- **B-ext:** 2 kt in 2027, 8 kt in 2028, 12 kt in 2029, 15 kt from 2030.
- **Cycle replay:** from 2028 the rod margin replays the matched pairs in the order 2026, 2019, 2020 … 2025. So 2028 and 2036 carry 2026 prices.

**B-ext cash table, base (EUR M)**

| Year | Capex | EBITDA | Tax | WC | Cash flow | Cumulative |
|---|---|---|---|---|---|---|
| 2027 | −4.0 | 0.3 | 0.0 | – | −3.7 | −3.7 |
| 2028 | −3.5 | 2.7 | −0.6 | −0.5 | −1.8 | −5.6 |
| 2029 | 0.0 | 4.3 | −0.9 | −0.5 | +2.8 | −2.7 |
| 2030 | −0.2 | 5.5 | −1.2 | – | +4.1 | **+1.3** |
| 2031–2040 (each year) | −0.2 | 5.5 | −1.2 | +1.0 in 2040 | +4.1 | +43.1 by 2040 |

| B-ext run | NPV10 (EUR M) | IRR | Payback |
|---|---|---|---|
| **Base, 15 kt × EUR 400** | **+19.1** | **49.2%** | 2030 |
| Stress, 12 kt × EUR 300 | +7.9 | 28.1% | 2031 |
| Spot ratio, 20 kt × EUR 400 | +27.1 | 58.7% | 2030 |
| +10% capex | +18.5 | 44.9% | 2030 |
| **Potlines curtailed from 2030** (EUR 115/t remelt on 15 kt) | **+12.1** | **39.2%** | 2030 |

**B-rod decision-basis cash table** (ICC-renewed ledger with NHT's claim, billet tranche switchable, 10% line contingency, central matched adders, no grant), EUR M

| Year | Capex | EBITDA | Tax | WC | Cash flow | Cumulative |
|---|---|---|---|---|---|---|
| 2027 | −24.8 | 0.0 | 0.0 | – | −24.8 | −24.8 |
| 2028 | −16.8 | 7.9 | −1.3 | −2.0 | −12.2 | −37.0 |
| 2029 | −0.5 | 2.5 | 0.0 | – | +2.0 | −35.0 |
| 2030 | −0.5 | 4.2 | −0.3 | – | +3.3 | −31.6 |
| 2031 | −0.5 | 7.1 | −1.1 | – | +5.5 | −26.1 |
| 2032 | −0.5 | 10.4 | −1.9 | – | +8.0 | −18.1 |
| 2033 | −0.5 | 6.8 | −1.0 | – | +5.4 | −12.7 |
| 2034 | −0.5 | 7.4 | −1.1 | – | +5.8 | −6.9 |
| 2035 | −0.5 | 8.4 | −1.3 | – | +6.5 | −0.4 |
| 2036 | −0.5 | 17.2 | −3.5 | – | +13.2 | **+12.8** |
| 2037–2039 | −0.5/yr | 5.1 / 5.5 / 7.1 | −0.5 / −0.6 / −1.0 | – | +4.1 / +4.4 / +5.6 | +26.9 |
| 2040 | −0.5 | 10.4 | −1.8 | +2.0 | +10.1 | +37.0 |

**Result:**
- NPV10 −EUR 0.5M, IRR 9.8%, payback 2036, which is six years past the 31 Dec 2029 ICC decision.
- Option phasing (Section 4.5) is taken from this table: 24.8 / 18.8 (16.8 + 2.0 WC) / 0.5 = 44.1.

**B-rod scenarios, matched basis, ICC renewed (NPV10 EUR M; IRR at central adders)**

| Run | Central | IRR | 2026 adder US$525 | Low adders | High adders | Revision 2 recall (upper bound) |
|---|---|---|---|---|---|---|
| S1′ rod upgrades ingot, cycle replay | +29.8 | 21.6% | +25.5 | +8.6 | +47.1 | +79.8 |
| S1m rod upgrades ingot, mid-cycle flat | +19.4 | 18.0% | +19.4 | +2.4 | +37.6 | +78.6 |
| S2′ displaces billet, mid-cycle | −33.4 | neg. | −33.4 | −55.8 | −13.0 | +28.6 |
| **S3′ displaces billet, 2026 matched pair** (revision 2: −93.0) | **−24.3** | neg. | −77.1 | −100.2 | −12.0 | −31.0 |
| S4′ displaces billet, cycle replay | −35.5 | neg. | −41.1 | −63.0 | −15.2 | +17.8 |
| S5′ switchable (idles at −EUR 44/t), cycle replay | −29.7 | neg. | −31.2 | −37.5 | −15.2 | +17.8 |
| Ledger, NHT built, switchable | +2.6 | 11.2% | −0.6 | −12.0 | +17.6 | +50.4 |
| Ledger, NHT built, not switchable | +0.2 | 10.1% | −4.0 | −21.9 | +17.6 | +50.4 |
| Ledger, NHT not built, switchable | +18.4 | 17.6% | +14.6 | −0.1 | +34.8 | +67.6 |
| **Decision basis: ledger, NHT built, switchable, +10% line contingency** | **−0.5** | **9.8%** | −3.7 | −15.2 | +14.5 | +47.3 |
| Ledger, switchable, no Al-Zr (base capex) | −11.7 | 3.3% | −14.9 | −28.0 | +3.5 | +36.3 |
| Ledger, switchable, spare primary 25 kt | −18.1 | neg. | −20.2 | −28.1 | −4.2 | +28.7 |
| Ledger, switchable, spare primary 75 kt | +28.5 | 21.2% | +24.3 | +7.7 | +45.7 | +78.5 |

**B-rod, potlines curtailed (decision basis with contingency; model section R4.5)**

| Run | NPV10 | IRR | Payback |
|---|---|---|---|
| Curtailed from 2030, remelt penalty EUR 70 / **115** / 160 | +9.2 / **−1.8** / −10.2 | 13.6% / **9.3%** / 5.3% | 2035 / 2036 / 2036 |
| Curtailed from 2031, penalty 70 / 115 / 160 | +10.6 / +1.6 / −6.9 | 14.2% / 10.7% / 6.8% | 2035 / 2036 / 2036 |
| Curtailed 2030, penalty 115, LOW / HIGH adders | −21.0 / +16.3 | −0.2% / 16.3% | never / 2033 |
| Curtailed 2030, penalty 115, no Al-Zr | −17.6 | 1.2% | 2040 |
| Curtailed 2030, penalty 115, + EUR 10M solid-feed melter charged to B-rod | −9.4 | 6.4% | 2036 |
| **Break-evens (curtailed 2030):** remelt penalty **EUR 108/t**; flat adder from 2030 **US$313/t** over P1020 DP (US$350 with the melter; US$384 without Al-Zr; US$365 at a EUR 160 penalty). Mid-cycle today is US$267 | | | |

**What this shows:**
- **On a matched basis rod is about at par with billet in most years.** The billet-displacing cases therefore lose roughly the present value of the capex. That is a stranded line, not a margin collapse.
- **Rod creates value only on metal that would otherwise leave as ingot.** The ledger, NHT's prior claim on that metal, and now the potlines, decide the case.
- **If the potlines close, rod loses its liquid-metal advantage** (EUR 155 → 40/t margin over ingot).
  - Its NPV barely moves at a EUR 115/t penalty, because the billet displacement it suffered also goes away.
  - It turns sharply negative if the penalty is high or the line must fund its own melter.
- **The spread across adder cases** is the value of the open data items: −15.2 to +14.5 on the decision basis, −21.0 to +16.3 curtailed. That is why the gate waits for the verified series and the measured penalty.

### 6.5 Partners and vendors

| Segment | Partners |
|---|---|
| Cable makers (rod offtake, only if B-rod passes its gate) | Nexans (template: the Hydro offtake of about 17 kt/yr), Prysmian, NKT, Lamifil, Tratos, De Angeli |
| Rod-line vendors | Properzi (CCR), Southwire (SCR): budget quotes requested |
| Melter vendors (curtailment case) | Stack-melter quote via Casthouse Engineering (open item 25) |
| HTLS | CTC Global ACCC licensees (50,000+ km installed; [CTC](https://ctcglobal.com/?p=266860)); one EU TSO for a pilot line |
| Data centres and electrical (B-ext) | Schneider, Vertiv, Siemens, ABB; Hitachi Energy and Siemens Energy for busbar and transformer strip; EU busway makers |
| Science | Alloyed/BCAST (heat-conducting scrap-based alloy; [The Engineer](https://www.theengineer.co.uk/content/news/525k-to-accelerate-ai-alloy-design)); TECNALIA MetalIA; Leoben/RWTH for Al-Zr-Er |

### 6.6 B-rod gate (30 Sep 2027, after the M9 contingency plan) and 12-month milestones

**This gate supersedes, and includes, the board paper's #4 condition** ("rod-line FID only with two offtakes of 5+ years"). Tests (3) and (6) require ≥5-year offtakes with ≥2 cable makers.

**Tests:**
- **(1) Data (mandatory):** the verified 2019–26 adder and billet series is loaded (open items 2 and 3). The decision-basis case is re-run on it.
- **(2) Mass balance at the full 57 kt (ICC-renewed ledger):**
  - The line needs 57.6 kt/yr of primary-equivalent metal.
  - S&OP must confirm **at least 27 kt/yr of spare primary left after any NHT claim**. That is 45.5 kt in total if NHT is built.
- **(3) Offtake price (ICC-renewed ledger):**
  - At least 5-year offtakes with ≥2 cable makers, covering the billet-sourced tranche (about 31 kt of rod).
  - These must be priced with a **billet-linked adder: A ≥ (billet − P1020 spread) − US$46/t**.
  - Effect: decision-basis NPV +EUR 7.2M, IRR 13.1% (+6.7M even at low adders); −EUR 7.0M without Al-Zr.
- **(4) Capex (mandatory):**
  - A firm installed quote of **≤EUR 36M before contingency**, including building scope.
  - At EUR 40M plus contingency the ledger case is −EUR 4.2M (IRR 8.3%).
- **(5) Al-Zr (mandatory):** a pilot letter from one TSO for Al-Zr rod. Without Al-Zr, every central case is negative unless spare primary reaches 61 kt.
- **(6) Curtailment (mandatory, new): NPV10 ≥ 0 with the potlines curtailed from 2030**, at the measured remelt penalty, central verified adders and contingency. Today it is −EUR 1.8M, so it **fails**. It passes on either route:
  - **(6a)** Controlling's measured remelt and logistics penalty is **≤EUR 108/t**, **and** the M9 plan confirms that the option-C casthouse supplies solid-melt capacity at no charge to B-rod.
  - **(6b)** ≥5-year offtakes carry a contractual **adder floor of ≥US$313/t over P1020 DP from 2030 on the full 57 kt**. The floor is US$350/t if a melter is charged to B-rod.

**Decision rule:**
- **GO = (1) + (4) + (5) + (6) + either (2) or (3).**
- If spare primary is ≥61 kt, (5) is not needed for (2) or (3); it is still needed for (6).
- **If everything passes except (6), B-rod is deferred, not rejected.**
  - It is re-tested after the 31 Dec 2029 ICC decision, with a 2030–31 build and first metal in 2032.
  - This is the memo's version of the board paper's ICC-cliff rule.
- **Otherwise B-rod stays WATCH** and is re-tested at the 2028 budget. Spend is capped at EUR 0.2M.

| Date | Milestone |
|---|---|
| 30 Oct 2026 | Verified Fastmarkets billet and P1020 annual averages loaded (Treasury) |
| 6 Nov 2026 | Casthouse mass balance 2025–26: ingot/sow/T-bar sold outside, billet utilisation, A3-freed primary (S&OP); own billet invoices (Sales Ops) |
| 13 Nov 2026 | Fastmarkets/CRU 2019–26 rod-adder pull (Market Intelligence); conversion-cost deltas EUR 75/115 (Plant Controller) |
| 15 Dec 2026 | Remelt penalty from our own remelt-furnace cost centre (Controlling; test 6a) |
| 31 Dec 2026 | Busbar and manifold samples to ≥1 data-centre OEM (B-ext) |
| 15 Jan 2027 | Properzi and Southwire quotes plus building scope (test 4); cable-maker RFQ adder indications (test 1) |
| 31 Jan 2027 | Stack-melter quote (Casthouse Engineering; test 6) |
| Q1 2027 | Billet-linked adder and post-2030 floor term sheets with ≥2 of the 6 cable makers (tests 3 and 6b); TSO Al-Zr pilot talks (test 5); first B-ext qualification order targeted |
| 30 Jun 2027 | **T3 release** on a B-ext qualification order |
| Jul 2027 (M9) | No-ICC contingency plan: melt capacity in option C (test 6a) |
| **30 Sep 2027** | **B-rod gate decision** |
| 31 Oct 2027 | B-ext at 2 kt run-rate; conductivity-vs-scrap ML model validated on lab casts (≥61% IACS at ≥30% scrap) |

---

## 6A. NHT structural HPDC alloy (WATCH; capex behind a volume-specific gate)

**What we would sell:**
- **NHT-P:** a primary-based low-Fe grade, from 2029.
- **NHT-R:** an ML-designed Fe-tolerant grade with ≥50% recycled content, from 2030. It targets the white space in Section 8.2.
- **Blended recipe:** 0.89 t of Al units per tonne, 40% primary and 60% scrap.

**Relationship to the board paper.**
- This is the board paper's #5 ("recycled-content structural casting alloy"), shown there as "GO (qualification only, EUR 0.8M)".
- This memo shows it as WATCH with the same EUR 0.8M pre-gate option. **The spend is identical and no capex is released in either paper.**
- The capex trigger in Section 6A.4 supersedes the board paper's 20 kt nomination trigger.

### 6A.1 Demand, rebuilt from named programmes (2030, EU)

Anchors are carried from earlier rounds; the URLs were not re-opened in this revision:
- **Volvo Torslanda:** EX60 rear underbody on Bühler Carat 840 (8,400 t) cells ([Euroguss](https://www.euroguss.de/en/euroguss-365/2026/02/megacasting-at-volvo), [Foundry Mag](https://www.foundrymag.com/molds-cores/article/21242517/volvo-orders-two-megacasting-machines-buhler-ag)).
- **VW Group:** 16 Bühler 9,000 t cells reported. VW has not confirmed this ([Castings SA](https://castingssa.com/volkswagen-group-orders-16-of-9-000-ton-gigacasting-machines-from-buhler/)).
- **Bühler:** more than 50 megacasting orders worldwide ([Bühler](https://www.buhlergroup.com/global/vi/stories/buhler-celebrates-50-megacasting-solutions.html)).
- **Industry share:** about 70% of large structural castings expected to be giga-castings by 2030, mostly in-house at OEMs ([Light Metal Age](https://www.lightmetalage.com/news/industry-news/automotive/giga-castings-in-the-automotive-industry-an-updated-review/)).
- **Casting weight:** Model Y castings about 130 kg ([ChargedEVs](https://chargedevs.com/newswire/first-model-y-megacasting-produced-at-teslas-gigafactory-texas)).
- **Not verified:** Tesla Berlin's IDRA cell count, Volvo Košice timing, Mercedes and the Chinese transplants.

| Programme | Vehicles k (L/C/H) | kg cast per vehicle | Good castings kt (L/C/H) |
|---|---|---|---|
| Tesla Berlin (IDRA) | 150 / 250 / 375 [est.] | 130 | 19.5 / 32.5 / 48.8 |
| Volvo Torslanda (Bühler Carat 840) | 80 / 120 / 150 [est.] | 45 / 50 / 60 [est.] | 3.6 / 6.0 / 9.0 |
| Volvo Košice | 50 / 150 / 250 [est.] | 60 / 80 / 100 [est.] | 3.0 / 12.0 / 25.0 |
| VW SSP (16 × 9,000 t reported) | 200 / 500 / 900 [est.] | 80 / 90 / 100 [est.] | 16 / 45 / 90 |
| Mercedes | 0 / 100 / 250 [est.] | 50–60 [est.] | 0 / 5 / 15 |
| Chinese transplants (BYD Szeged, Chery Barcelona) | 50 / 150 / 300 [est.] | 60–90 [est.] | 3.0 / 10.5 / 27.0 |
| Others / Tier-1s | 0 / 100 / 300 [est.] | 50–60 [est.] | 0 / 5 / 18 |
| **Total good castings** | 530 / 1,370 / 2,525 | | **45 / 116 / 233** |
| **Alloy purchased (×1.10 for scrap rate and melt loss)** | | | **50 / 128 / 256** |

**Cross-checks:**
- **Machine count.** About 2.2M castings a year at 98–162k castings per cell implies 22–28 cells of ≥6,000 t. That is consistent with an EU installed and ordered base of 25–40 cells by 2030 [est.].
- **Value.** A global gigacasting market of US$1.2bn in 2030 ([GII](https://giikorea.co.kr/report/tsci1764226-gigacasting-market-global-industry-size-share.html)) at about US$3,000/t is about 400 kt. A 20–30% EU share gives 80–120 kt. The board paper's central EU figure of about 150 kt (range 75–375) is close to our 128 kt central.
- **Wider pool.** Ducker's 145 kg/car × 11.5M cars × 15–25% structural gives **250–420 kt**. That is the whole structural HPDC pool, heat-treated and NHT.

**Share test:**
- 30 kt is 23% of the central mega-casting market: 60% of the low case and 12% of the high case.
- A realistic entrant share is 10–20%, or 13–26 kt [est.]. This is because Hydro/Alumetal, Trimet, Speira, Rheinfelden licensees, Rio Tinto and Alcoa all have primary access.
- So 30 kt also needs conventional NHT structural parts from the wider pool. **The gate therefore rests on signed nominations, not on market share.**

### 6A.2 Contribution restated against the metal's alternative use

**Inputs per tonne of alloy:**
- Price EUR 2,700, which is P1020 DP (2,431) + EUR 269.
- Primary 0.360 t (1% melt loss).
- Scrap 0.550 t (3% melt loss), in two halves:
  - external cast scrap and OEM returns at 85% of LME;
  - clean wrought hub scrap valued at its billet-substitution value, P1020 DP − EUR 100 remelt [est.].
- Silicon 0.10 t × EUR 2,100 [est.].
- Mn/Mo/Zr/Sr additions EUR 55, variable conversion EUR 150 and freight EUR 35 [est.].

| Basis | Primary valued at | Scrap valued at | Contribution EUR/t (range) | When it applies |
|---|---|---|---|---|
| Revision 2 | AlSi9Cu3 benchmark | — | 280 | **Withdrawn:** an alloy we do not make |
| A: market scrap | P1020 DP | 85% of LME | 368 (149–649) | Not used: ignores the hub scrap's internal value |
| **B: P1020 (decision basis, ICC renewed)** | P1020 DP | Half market, half billet substitution | **231 (24–532)** | NHT draws spare primary first in the ledger (Section 4.3), so the primary's alternative is P1020 sale |
| **B, potlines curtailed from 2030** | Purchased P1020 DP + EUR 115 remelt | As B | **190** (231 − 0.360 × 115) | No liquid metal. The price formula is indexed to P1020 DP, so the only loss is the remelt cost on the primary share |
| C: billet | P1020 DP + EUR 187 (mid-cycle billet margin) | As B | 164 (−169 to +512) | Only if spare primary is exhausted while the potlines run (stress case) |

**Worked basis B:**
- Primary 0.360 × 2,431 = 874.
- Scrap 0.550 × (½ × 1,832 + ½ × 2,331) = 1,145.
- Silicon 210.
- Additions, conversion and freight 240.
- Cost total 2,469, so contribution = 2,700 − 2,469 = **EUR 231/t**.

**Sensitivities (basis B):**
- Premium over P1020 DP of EUR 180 / 400 gives a contribution of EUR 142 / 362.
- A wrought-scrap share of 0% / 100% gives EUR 368 / 94. Each 10 points of the mix shifted from wrought scrap to OEM returns adds about EUR 27/t [calc].
- **Supply contracts should therefore bring OEM returns back to us.**

### 6A.3 Investment, cash table and runs

**Inputs:**
- Capex EUR 18M (14–24), or **EUR 19.8M with 10% contingency**: ingot/T-bar casting, melt treatment, liquid-metal crucible logistics. The filed Innovation Fund scope stays at EUR 18M, below the EUR 20M small-scale threshold.
- Phasing: 2027 Q4 EUR 2.0M after the gate, 2028 EUR 17.8M.
- OEM qualification EUR 4.0M: 0.8 pre-gate in 2027, then 2.5 and 0.7.
- Volume ramps to 6 kt in 2029, 18 kt in 2030 and 30 kt from 2031.
- Fixed opex EUR 1.5M/yr.
- Working capital 8% × EUR 2,700/t = EUR 6.5M.
- Sustaining capex EUR 0.4M/yr.

**EBITDA** = 30 × 231 / 1,000 − 1.5 = **EUR 5.4M/yr** (EUR 4.19M/yr if the potlines are curtailed).

**NHT decision-basis cash table** (30 kt, P1020 basis, ICC renewed, contingency, no grant), EUR M

| Year | Capex and qualification | EBITDA | Tax | WC | Cash flow | Cumulative |
|---|---|---|---|---|---|---|
| 2027 | −2.8 (0.8 pre-gate + 2.0 after gate) | 0.0 | 0.0 | – | −2.8 | −2.8 |
| 2028 | −20.3 | 0.0 | 0.0 | – | −20.3 | −23.1 |
| 2029 | −0.7 | −0.1 | 0.0 | −1.3 | −2.1 | −25.2 |
| 2030 | 0.0 | 2.7 | −0.3 | −2.6 | −0.2 | −25.4 |
| 2031 | −0.4 | 5.4 | −1.0 | −2.6 | +1.5 | −23.9 |
| 2032–2036 (each year) | −0.4 | 5.4 | −0.9 | – | +4.1 | −3.4 by 2036 |
| 2037 | −0.4 | 5.4 | −0.9 | – | +4.1 | **+0.7** |
| 2038–2040 | −0.4/yr | 5.4 | −0.9 | +6.5 in 2040 | +4.1/yr (+10.6 in 2040) | +19.5 |

| Run | NPV10 (EUR M) | IRR | Payback |
|---|---|---|---|
| **Decision basis: 30 kt × EUR 231, +10% contingency, no grant, ICC renewed** | **−4.1** | **7.3%** | 2037 |
| **Potlines curtailed from 2030, penalty EUR 70 / 115 / 160** | −7.0 / **−8.8** / −10.7 | 5.2% / **3.8%** / 2.3% | 2039 / 2039 / 2040 |
| Potlines curtailed from 2031, penalty 115 | −8.4 | 4.1% | 2039 |
| Curtailed 2030, with IF grant of 6.3 (not a decision basis) | −3.4 | 7.3% | 2038 |
| Same as decision basis, no contingency | −2.6 | 8.2% | 2037 |
| Billet basis (EUR 164) | −12.1 | 1.3% | 2040 |
| At revision 2's EUR 280, with contingency | +1.7 | 11.1% | 2036 |
| With IF small-scale grant of 6.3, ICC renewed (not a decision basis) | +1.4 | 11.1% | 2036 |
| Fixed opex EUR 2.0M | −6.5 | 5.6% | 2038 |
| 28 kt | −5.7 | 6.1% | 2038 |
| 35 kt | 0.0 | 10.0% | 2036 |
| **20 kt at today's EUR 231 (the board paper's trigger volume)** | **−12.4** | **0.3%** | 2040 |
| Low: 20 kt, billet basis | −17.8 | −5.2% | never |
| High: 40 kt × EUR 350 | +23.0 | 22.4% | 2033 |

**Break-even volumes at EUR 231 (contingency included):**
- ICC renewed: **35.0 kt**.
- Potlines curtailed from 2030: **43.3 kt**.
- Earlier references: EUR 280 with contingency 28.3 kt; billet basis 51.9 kt.

### 6A.4 Volume-specific gate on both ledgers (30 Sep 2027, after M9); supersedes the board paper's 20 kt trigger

**Why revision 3's gate is withdrawn.**
- Revision 3 used a single floor of volume × contribution ≥ EUR 8.2M/yr.
- The break-even product rises with volume, from EUR 7.72M at 20 kt to EUR 8.21M at 40 kt, so the single floor sat below the 40 kt break-even.
- Its own example, 30 kt × EUR 273 = EUR 8.19M, did not clear the floor.
- It gave no rule above 40 kt.
- It ignored curtailment. The example's NPV is +EUR 0.9M if ICC is renewed but **−EUR 3.8M if the potlines close**.

**Restated gate (model section R4.6).**
- The required contracted contribution is the higher of two volume-specific break-evens:
  - ICC renewed;
  - potlines curtailed from 2030 at EUR 115/t.

  To that higher break-even it adds **EUR 15/t**, rounded up to the next EUR 5.
- The curtailed case binds at every volume.

| Signed volume (kt/yr) | Break-even, ICC renewed (EUR/t) | Break-even, curtailed 2030 (EUR/t) | **Required contracted contribution (EUR/t)** | Price needed over P1020 DP (EUR/t) | NPV10 at the gate: renewed / curtailed (EUR M) |
|---|---|---|---|---|---|
| 25 | 314 | 353 | **370** | 408 | +5.6 / +1.6 |
| 28 | 283 | 322 | **340** | 378 | +6.4 / +2.0 |
| 30 | 266 | 305 | **325** | 363 | +7.1 / +2.4 |
| 32 | 250 | 290 | **310** | 348 | +7.6 / +2.5 |
| 35 | 231 | 271 | **290** | 328 | +8.2 / +2.7 |
| 38 | 215 | 254 | **270** | 308 | +8.3 / +2.3 |
| 40 | 205 | 245 | **260** | 298 | +8.7 / +2.4 |

**NHT capex is released only if all five conditions hold:**
1. **Volume.** Signed OEM or Tier-1 SOP nominations of **≥25 kt/yr**.
   - Volume is read down to the nearest tabulated row: 33 kt uses the 32 kt row.
   - **Volume above 40 kt is counted as 40 kt.** The EUR 18M plant and the cash table are sized for at most 40 kt. Larger volume needs a new capex quote and a re-run.
2. **Contribution.** The contracted contribution, calculated on basis B from the signed price formula, is at least the required value in that row.
   - Example: 30 kt needs ≥EUR 325/t, i.e. a price of ≥P1020 DP + EUR 363/t.
   - That gives NPV +EUR 7.1M if ICC is renewed and +EUR 2.4M if the potlines are curtailed.
3. **Capex.** An installed quote of ≤EUR 19.8M including contingency.
4. **Metal ledger.**
   - S&OP confirms the 19.0 kt primary-equivalent draw in the ICC-renewed ledger.
   - The M9 plan confirms that 10.8 kt/yr of purchased P1020 can be remelted in the option-C casthouse.
5. **Remelt penalty.** The measured penalty is ≤EUR 115/t. If it is higher, the table is re-run at the measured value before the decision.

**Decision:**
- Today's price (P1020 + EUR 269) passes at no volume up to the 40 kt cap. Before any margin, it needs ≥43.3 kt in the curtailed case. **NHT is therefore WATCH.**
- **This gate supersedes the board paper's #5 trigger** ("OEM nomination of at least 20 kt/yr"). At 20 kt and today's price, NPV10 is −EUR 12.4M.
- The EUR 0.8M pre-gate qualification option continues in 2027: trial lots, Bühler and IDRA die trials, and the NHT-R chemistry screen.
- If the gate fails, only the EUR 0.8M is sunk.
- If the gate passes on the renewed ledger but not the curtailed one, NHT is deferred to the 31 Dec 2029 decision under the rule in Section 4.6.

### 6A.5 Customers and partners

| Role | Names |
|---|---|
| Target customers (RFQs by 31 Mar 2027) | Volvo Cars (Torslanda, Košice), VW Group (SSP cells), Tesla Berlin; Tier-1 megacasters |
| Die-machine OEMs, for trial castings | Bühler, IDRA |
| Science | ORNL RidgeAlloy as a reference; Leoben |
| Strategic logic | Rusal has owned Rheinfelden since 2021 ([Dry Cargo](https://www.drycargomag.com/rusal-completes-acquisition-of-aluminium-rheinfelden)), so OEMs will want a non-Russian EU source |

---

## 7. Building the capability

### 7.1 Organisation

The **Alloy Informatics & Design Centre** reports to the CTO and is led by a newly hired Head of Alloy Informatics.

| Role | FTE |
|---|---|
| Computational metallurgists (CALPHAD, precipitation) | 2–3 |
| ML / data scientists | 2–3 |
| Data engineers (digitising casthouse, rolling and extrusion history) | 1–2 |
| Lab technicians | 2–3 |
| Product / IP lead | 1 |
| **Total** | **6 (2027), 10 (2028), 12 (2029); EUR 0.9–1.8M/yr at about EUR 150k loaded per FTE** |

### 7.2 Data, our biggest asset

- Years of OES melt chemistry, process logs and test certificates. The hub's LIBS/XRF spectra are added if the hub reaches FID; otherwise lot certificates and inline chemistry on purchased scrap.
- One-off FAIR standardisation costs EUR 0.5–1M [est.]. It starts on day 1.
- The same data feeds:
  - the CFO's metal ledgers (Section 4.3);
  - the melt-by-melt metal balance that separates the robots' loss saving from A1's (Section 5.2).

### 7.3 Software

- Thermo-Calc with TCAL11/MOBAL. Benchmark: a TCAL9 perpetual licence cost EUR 10,440 in a public tender ([VSB](https://zakazky.vsb.cz/document_audit_71158/priloha-1-sw_thermocalc_tech_spec-doc)).
- In-house Python ML and Bayesian-optimisation stack, with Citrine or Alchemite (EUR 100–300k/yr) trialled for 12 months.
- Granta-type data management.
- Total EUR 0.4–0.5M/yr.

### 7.4 Laboratory, phased

| Phase | Content |
|---|---|
| 2027: buy access | MPIE Rapid Alloy Prototyping or Leoben casting trials; ARM-MIP access on negotiated IP terms; casthouse trial casts |
| 2028: build, gated | Multi-mould rapid casting (EUR 0.3–0.8M); lab rolling mill and extrusion/compression simulator (EUR 0.7–2M); robotic tensile testing (about EUR 0.35M, ZwickRoell roboTest P, price unconfirmed ([ZwickRoell](https://www.zwickroell.com/fileadmin/content/Files/SharePoint/user_upload/Brochures_EN/Flyer_Automated_Testing_Systems_EN.pdf))); automated metallography and SEM-EDS (EUR 0.3–0.8M); DSC, conductivity and corrosion rigs (EUR 0.2–0.4M). **Lab capex EUR 2.5–5M [est.]; budgeted at EUR 3.9M** |
| Gate to build (31 Dec 2027) | The 2027 programme needs ≥300 casts/yr, or external service demand ≥EUR 0.5M/yr, or a grant is awarded |

### 7.5 Build, buy or partner

| Component | Decision | Why |
|---|---|---|
| Data platform and trained property models (scrap to chemistry to properties) | **Build** | This is the moat; kept as a trade secret |
| CALPHAD databases | **Buy** (Thermo-Calc) | Industry standard |
| ML and Bayesian-optimisation platform | **Build** on open source; **trial-buy** Citrine/Alchemite for 12 months | Avoids lock-in |
| Charge optimiser | **Buy** (SMS/GHI), with our own property models integrated | Time to value; outcome-based contract paid on **charge-cost** savings only (Section 5.2) |
| Rapid prototyping and testing | **Partner in 2027, build in 2028** behind the gate | Prove the throughput need first |
| Fundamental science | **Partner** (Leoben, RWTH, MPIE, AIT, Brunel BCAST) | Grant leverage and talent |
| High-conductivity HPDC, robot-grade alloys | **Partner** (Alloyed, Phaseshift, Fehrmann) | WATCH items, small volumes |
| Crossover 5/7 | **License** (AMAG) | About 7-year incumbent lead |

### 7.6 Budget by year (capability only; alloy qualification sits in A, B and NHT)

| EUR M | 2027 | 2028 | 2029 | Total |
|---|---|---|---|---|
| Team (6, 10, 12 FTE) | 0.9 | 1.5 | 1.8 | 4.2 |
| Data digitisation (one-off) | 0.8 | 0.2 | — | 1.0 |
| Software and compute | 0.4 | 0.5 | 0.5 | 1.4 |
| External lab access and university partners | 0.6 | 0.6 | 0.5 | 1.7 |
| Lab capex | 0.4 | 2.5 | 1.0 | 3.9 |
| **Gross** | **3.1** | **5.3** | **3.8** | **12.2** |
| Horizon MAT-PROD-22 share, if awarded (Section 8.6) | — | −0.6 | −0.6 | −1.2 |
| **Net** | **3.1** | **4.7** | **3.2** | **11.0** |

- From 2030 the running cost is EUR 2.8M/yr (team 1.8 + software 0.5 + external 0.5).
- **The centre's NPV10 cost is −EUR 26.1M.** It is charged in full in the portfolio NPV. As a stress test it is also charged against Case A alone (NPV EUR 10.3M, IRR 15.9%; Section 4.4).
- Alloy-development services worth EUR 1–3M/yr from 2029 are upside and are not counted.

---

## 8. IP and commercial model

### 8.1 Model: own the chemistry window, sell the metal, license only outside the EU

- Western majors earn from alloy innovation mainly through **metal premiums**: Advanz, HSA6, CIRCAL, SOUL.
- A design house on its own earns little. QuesTek reported just over US$750k in fees and royalties ([NETL](https://www.netl.doe.gov/File%20Library/Events/2015/utsr/Wednesday/Saal.pdf)).

### 8.2 Patent landscape (CPC C22C21): families to clear and open claim space

**Status:**
- Kaiser US 2023/0416879 A1 is verified ([Justia](https://patents.justia.com/patent/20230416879)).
- **Publication numbers for Castasil-37, Magsimal-59, Trimal-37 and Alcoa C611 could not be retrieved.** Google Patents and Espacenet were refused by the egress proxy.
- We do not quote numbers from memory, because a wrong EP number in a Board paper is worse than none.
- **Owner:** IP counsel / R&D librarian, about 2 hours, by 6 Nov 2026.
- **FTO opinions:** General Counsel, by 15 Jan 2027. Three opinions at EUR 15–40k each.

| Field | Families we must clear (status unverified) | Freedom-to-operate inference [est.] | Open claim space we will file into [est.] |
|---|---|---|---|
| NHT HPDC | **Rheinfelden** Castasil-37 (AlSi9MnMoZr; priority about 2002–04) and Magsimal-59 (AlMg5Si2Mn; priority about mid-1990s); Castaduct-42/-18 (AlMg4Fe2; newer). **Trimet / Rheinfelden Alloys** Trimal-37 (priority 2015 or later). **Alcoa** C611 EZCast (priority about 2018–21). **Tesla** die-casting alloy applications (from 2021; US12378642 assignee unconfirmed). **China:** Xiaomi "Titan" (AI-designed), Lizhong, Huayu, Chalco | Castasil-37 and Magsimal-59 are probably expired (20-year term). Trimal-37 and C611 are probably in force until about 2035–41, so a design-around or licence is budgeted at EUR 0.2–0.5M [est.] | Scrap-based NHT with Fe 0.4–0.8% under a controlled Mn/Fe ratio. Process claims that tie the alloy window to sorted-scrap chemistry measured in line. Avoid the crowded AlSi7–11 / Mn 0.4–0.8 primary window |
| Al-Zr conductor | TAl/ZTAl/UTAl under IEC 62641 come from 1980s Japanese families and have expired. Live filings are likely from Rusal, State Grid / Far East Cable, NanoAl (Al-Zr-Er-Sc) and possibly Lamifil | Free to operate on the base chemistries | AlZr rod from recycled EC-grade feed; continuous-cast process windows; Al-Fe-Zr building wire |
| Fe-tolerant 6xxx | **Kaiser** US 2023/0416879 A1 (Fe and Mn ≤0.8% at >75–90% scrap; the closest blocker for Case A). **Novelis** high-recycled 6xxx sheet. **Constellium** recycled crash 6xxx. **Hydro** Fe-controlled 6xxx extrusion (CIRCAL is a brand, not an alloy claim) | The FTO opinion on Kaiser is the critical path for Case A | Combined Cu 0.2–0.5% and Zn 0.1–0.3% tolerance, with a homogenisation route that converts β-AlFeSi to α. Sorter-window-to-alloy-window control claims (the LIBS acceptance window set from the alloy's property window). The basic Fe/Mn metallurgy has extensive prior art |

**Queries for IP counsel:**
- **Google Patents / Espacenet:**
  - Assignee "Aluminium Rheinfelden", AlSi9Mn + Mo + Zr, non-heat-treatable HPDC (Castasil-37).
  - Assignee "Aluminium Rheinfelden", AlMg5Si2Mn (Magsimal-59).
  - Assignee "Rheinfelden Alloys" or "Trimet", NHT structural HPDC (Trimal-37).
  - Assignee "Alcoa", Al-Si-Mg-Mn HPDC without solution treatment (C611).
- **CPC searches:**
  - `cpc=C22C21/02 OR cpc=C22C21/04 and ta="die cast*" and ta="without heat treatment" and pd>=2015`
  - `cpc=C22C21/00 and ta=(zirconium and conductor) and pd>=2012`
  - `cpc=C22C21/08 and ta=(recycl* or scrap) and pa=(novelis or constellium or hydro or kaiser)`

### 8.3 IP layers

1. **Process and chemistry-control patents** in EP, US and CN (white space above): first filings by 30 Jun 2027.
2. **Trade secrets** on the sorting-to-melt correction models and training data.
3. **Trademark first,** as HSA6, CIRCAL and Castasil did.
4. **AA Teal Sheet / EN 573 registration** after 12 months of commercial supply. This helps purchasing departments but does not create a premium.
5. **Invention-disclosure process** from day 1, with every ML-designed candidate logged.

### 8.4 Pricing and premiums

| Product | Premium EUR/t | Source |
|---|---|---|
| A4 brand, building systems (Hueck, Aluprof, Reynaers) | 50–200 (base 100) | [est.]; Section 5.5 evidence |
| A4 brand, crash management (BMW, Benteler) | 100–300 (base 175) | [est.]; Volvo/BMW CO2 targets |
| Casthouse-side scrap down-shift (A2; a cost saving, not a premium), on contracted lower-rung tonnes only | 6–10 net LME points = 129–216 | [est.]; Section 5.2 ladder |
| Post-consumer substitution for primary (A3; a cost saving) | 6–13 net LME points = 129–280; booked 9 = 194 (gross 14.25 points less 5.3 of casthouse cost) | Fastmarkets MB-AL-0405, Argus, Recycling Europe; Section 5.2 |
| High-strength crash extrusion (HSA6 type) | 150–400 | [est.] |
| NHT structural HPDC: price over P1020 DP / contribution against the metal's alternative use | 269 today / 231 (P1020 basis), 190 (curtailed), 164 (billet basis). **Gate needs 298–408 over P1020 DP depending on volume** | [calc], Section 6A |
| Conductor rod: adder over P1020 | US$170–700 by year (mid-cycle 267), i.e. EUR 155/t over ingot at mid-cycle from liquid metal; **US$313/t floor needed if potlines close** | [est.], Sections 6.2, 6.6 |
| Al-Zr over EC rod | 300–800 | [est.] |
| Busbar / thermal extrusion over standard profiles | 300–600 incremental | [CTO est.] |
| Carbon differential alone | US$25–40/t (P1020); US$20–30/t (value-added products) | [Fastmarkets](https://fastmarkets.com/insights/low-carbon-aluminium-differentials-in-europe-widen-for-p1020-vaps) |

### 8.5 OEM joint development agreements and out-licensing

**JDAs:**
- Building: Hueck, then Aluprof.
- Automotive: BMW and Benteler.
- Data centres: one of Schneider, Vertiv, Siemens or ABB.
- Megacasting (only after the NHT gate): Volvo or VW.
- **IP split:** the OEM owns application-specific IP. **We keep the composition and process IP.**
- **Exclusivity:** the OEM gets 2–3 years of supply exclusivity in return for co-funding qualification.

**Out-licensing (non-EU only):**
- Template: Alcoa's C611 licensing ([Business Wire](https://www.businesswire.com/news/home/20220913005251/en/Alcoa-announces-innovations-in-alloy-development-and-deployment)).
- Royalty: 1–10% of net sales, with an automotive average of about 3.3% ([UpCounsel](https://www.upcounsel.com:443/patent-licensing-royalty-rates)).
- **Royalty base:** the licensee's net sales price of alloy ingot, EUR 2,700/t. EUR 60–140/t is therefore 2.2–5.2%, and 3.3% gives EUR 89/t.
- **Target:** EUR 1–3M/yr from 2030, which is 11–34 kt licensed at EUR 89/t. This is upside and is not in the portfolio.

**Toll manufacturing:** we act as a qualified manufacturing partner for OEM-owned alloys (e.g. [Apple](https://www.apple.com/newsroom/2023/04/apple-will-use-100-percent-recycled-cobalt-in-batteries-by-2025/)). This is opportunistic, at 5–20 kt per programme [est.].

### 8.6 EU funding

| Instrument | Amount for us | Status / timing | Owner | Booked |
|---|---|---|---|---|
| **Horizon CL4-2027-01-MAT-PROD-22** (Innovation Action) | **EUR 1.2M** (0.5–1.5) = about 25% of a EUR 7M project × 70% company rate. EUR 36M is the call total ([euacc.ai](https://www.euacc.ai/calls/HORIZON-CL4-2027-01-MAT-PROD-22), third-party). Per project EUR 5–8M [est.]. TRL 6–7 at end. ≥3 entities from 3 Member/Associated States | Deadline 2 Feb 2027 **[unverified on the official portal]**: [topic page](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl4-2027-01-mat-prod-22). Success rate 15–25% [est.]; expected value EUR 0.24M | Grants Office with the national NCP, **confirm by 30 Oct 2026** | Capability centre, if awarded |
| Horizon MAT-PROD-01 (RIA) | EUR 6–8M per project, up to 6 projects ([Ideal-ist](https://topictree.ideal-ist.eu/topic/7016), third-party [unverified]); our share EUR 0.5–1.5M [est.] | Same deadline [unverified] | Grants Office, 30 Oct 2026 | 0 (bid as partner) |
| **Innovation Fund small-scale (IF26)**: capex EUR 2.5–20M, up to 60% of relevant costs | **Case A casthouse adaptation: EUR 4.2M** (35% × 12). **NHT: EUR 6.3M** (35% × 18; maximum 10.8). The NHT bid is filed in April, but the grant is **accepted only if the NHT gate passes**. GHG case: A3 233 kt CO2/yr; NHT-R 15 kt × 50% × 15.5 = 116 kt/yr | Opens about Dec 2026, deadline about Apr 2027 [est.]. Expected value 20% × 10.5 = EUR 2.1M. Filed capex must stay below EUR 20M | Grants Office and Recycling Hub lead | Case A: committed if awarded. NHT: inside the option |
| IPCEI-CAM | National envelopes: past per-company awards EUR 10–100M [est.]; Wallonia call ([Wallonia](https://ecosysteme-economiecirculaire.wallonie.be/en/action-plan/ipcei-in-the-sector-of-advanced-circular-materials-for-clean-technologies-june-2026/)) | Aluminium coverage [unverified] | Government Affairs, ministry enquiry by 30 Nov 2026 | 0 |
| RFCS | Not eligible (coal and steel only, Council Decision 2008/376/EC) | — | — | 0 |
| DIGITAL-EMERGING-51/53 | Heavy competition (topic 51 drew 191 proposals) | Low priority | — | 0 |

**Grant totals:**
- Committed lines if all awarded: EUR 5.4M (Horizon 1.2 + IF Case A 4.2).
- Plus IF-NHT 6.3 only inside the NHT option. Even with that grant, NHT stays negative if the potlines close (−EUR 3.4M).
- Probability-weighted (committed): EUR 1.1M.
- **Decision basis: EUR 0.**

---

## 9. Risks and counter-moves

| # | Risk | Likelihood / impact | Counter-move |
|---|---|---|---|
| 1 | Qualification takes longer than planned (auto beyond 4 years) | High / High | Building extrusions (Hueck, Aluprof), the brand and B-ext come first (6–18 month qualification); OEM co-funded JDAs |
| 2 | Competitors get there first (Hydro, Constellium, Novelis, Speira) | High / Medium | Speed of the integrated data chain; standards seats; closed-loop scrap contracts; process patents filed by 30 Jun 2027 |
| 3 | **ICC not renewed; potlines curtailed or closed from 2030–31** (the board paper's central issue) | Medium–High / High for B-rod and NHT; medium for Case A (throughput); low for B-ext | Every line that depends on liquid metal is valued on both ledgers. B-rod and NHT gates sit after M9 and need NPV ≥ 0 on both, or wait for 31 Dec 2029. Case A is valued on the stranded casthouse (EUR 27.8M at C 130; 25.6 with contingency). B-ext is valued at EUR 12.1M. C ≥190 kt applies only in the funded option-C configuration (Section 4.6) |
| 4 | **Lower-rung scrap cannot be contracted in the tonnes booked** (new) | Medium / High for Case A | Value booked only on contracted tonnes. T2(c) needs ≥40 kt/yr of lower-rung grades + ≥15 kt/yr of A3 grades on ≥3-year terms. A2 tonnage is largely re-specification of existing suppliers. ≥3 MoU drafts by day 90. Below 55 kt by 31 Oct 2027, Case A is re-scoped (+EUR 6.7M) |
| 5 | **A3 net spread below the booked 9 points** (new) | Medium / Medium | T2(d)(ii) verifies ≥6 net points on quotes, MB-AL-0405/0426 history and a 2 × 50 t trial, and Case A is re-booked at the verified figure. At 6 points Case A is EUR 27.8M; at the joint A2/A3 floor with contingency, EUR 18.6M |
| 6 | **Hub misses FID or slips** | Medium / Low for Case A | Case A's value no longer depends on the hub: the same 55 kt of contracts books the same EUR 31.1M in either state. Without the hub, more tonnes can be booked only when contracted |
| 7 | **Hub and Case A compete for casthouse scrap capacity** | Low at 55–70 kt contracted / Medium above 72.5 kt | The internal threshold is 12.8–13.8 points at 55–70 kt, below the hub's 14-point gate. Above 72.5 kt, the test linked to tonnage applies at M12. A2 contracts above 40 kt carry a hub-FID volume-reduction clause |
| 8 | Casthouse-side down-shift spread compresses, or C is small | Medium / High for A2 | At 6 net points Case A gives NPV EUR 24.0M; at C = 100 kt, EUR 12.9M; with no A2, EUR 2.5M. T2 needs a verified ≥6 points and C ≥100 kt. EU restrictions on non-OECD scrap exports, now delayed ([Engineering News](https://www.engineeringnews.co.za/article/eu-aluminium-scrap-export-curbs-delayed-until-september-group-and-sources-say-2026-06-26)), should widen low-grade discounts when they apply |
| 9 | **A1 and the furnace robots claim the same metal loss** | Was High / Low | A1 restated to EUR 6.7/t; one owner per loss pool; A1 gate on charge cost only (≥EUR 3/t); yield credit only beyond the robots' measured saving |
| 10 | Named customers do not pay the A4 premium; Hydro CIRCAL holds Schüco | Medium / Medium | A4 = 0 still gives Case A NPV EUR 20.1M, IRR 25.1%; the case does not rely on Schüco; T2 needs priced LOIs |
| 11 | Rod adder lags billet; rod cannibalises billet | High / High for B-rod | B-rod WATCH; matched-basis gate; billet-linked adders (A ≥ S − US$46); switchable billet tranche |
| 12 | Spare primary smaller than 45 kt, or A3 does not free primary | Medium / High for B-rod | Ledger owned by the CFO. B-rod needs ≥27 kt left after NHT; at 25 kt in total B-rod is −EUR 18.1M, so it would not be built. If A3 cuts P1020 purchases instead, A3's own value rises (Section 4.2) |
| 13 | NHT volume or price short of the gate; Chinese NHT 15–20% cheaper ([CS.com.cn](https://www.cs.com.cn/ssgs/gsxw/202305/t20230531_6347491.html)) | High / Medium (only EUR 0.8M at risk) | NHT WATCH; capex only above the volume-specific gate on both ledgers; sell low-CO2, EU, non-Russian origin |
| 14 | Cu/Al falls below 3.5x | Medium / Medium for B-ext | Stress case of 12 kt × EUR 300 still gives IRR 28.1%; LME-indexed contracts |
| 15 | Innovation Fund threshold: NHT capex overruns EUR 20M | Medium / Medium | Filed scope capped at EUR 18M; contingency sits outside the filed scope |
| 16 | Data quality is poor or certificates are not linked to melts | Medium / High | Data lake in the first 90 days; KPI ≥80% linkage |
| 17 | Weak IP; the Kaiser application blocks 6xxx windows; Trimal-37 or C611 blocks NHT-P | High / Medium | Publication numbers by 6 Nov; FTO by 15 Jan 2027; process and control claims; trade secrets; design-around budget EUR 0.2–0.5M |
| 18 | Standards stay tight (EN 573/1706) | Medium / Medium | Bring qualified HRC chemistries into CEN TC 132; sell under customer specifications meanwhile |
| 19 | Talent scarcity | Medium / Medium | University PhD/postdoc pipeline; remote ML roles; visible Board sponsorship |
| 20 | Double-counting of scrap, metal or loss pools across this memo and the board paper, or booking tonnes no gate secures | Was Medium / now Low | Group-paper rule; contracted-tonnes rule; one CFO-owned scrap ledger and liquid-metal ledger; hub spread assigned to the hub; robot loss assigned to the robots; 20% haircut in Case A |
| 21 | AI hype drains budget | Low / Medium | NO-GO on generative crystal models; every model linked to a named product and customer |

---

## 10. 90-day action plan (26 Oct 2026 to 23 Jan 2027)

**Budget:** EUR 1.9M opex, released by the CEO now. Revision 5 moves EUR 10k from the CTO line to Market Intelligence for the added MB-AL-0405 and MB-AL-0282 series. The total is unchanged.

| # | Owner (role) | Deliverable by day 90 | Budget (EUR k) | KPI |
|---|---|---|---|---|
| 1 | **CTO** | Centre charter; Head of Alloy Informatics hired or offer accepted; 4 FTE seconded; monthly steering committee | 160 | Lead in seat; 4 FTE active |
| 2 | **Chief Digital Officer** | Data lake v0: OES, process and certificate data 2019–26 for the top 20 alloys, linked melt by melt; data dictionary shared with the hub; melt-by-melt metal balance for the robot-versus-A1 loss split | 300 | ≥80% of 2022–26 melts linked from chemistry to properties |
| 3 | **Head of Casthouse** | Charge-optimiser bake-off (SMS vs GHI vs in-house) with Speira reference calls; shadow mode on one furnace; outcome-based contract paid on charge cost. **Melt-loss baseline split by cause** (open item 28). **Existing scrap intake C by alloy** (with Casthouse Metallurgy, open item 22). **Solid-melt capacity by furnace and permitted solid melt** (with Casthouse Engineering and EHS, open item 34). **A3 trial plan for 2 × 50 t lots** (run by 31 Mar 2027, open item 32) | 200 | Modelled charge-cost saving ≥EUR 3/t; vendor selected; C confirmed by 13 Nov; melt capacity by 30 Nov |
| 4 | **Head of R&D Metallurgy** | Thermo-Calc installed; CALPHAD+ML screen of HRC 6063/6082 at Fe 0.4–0.8; 20–30 trial casts booked; NHT-R chemistry screen. **Wide-window specification for the hub's M3 LIBS trial.** Acceptance windows for the lower-rung and A3 contract grades | 250 | ≥3 candidate chemistries per family, each with a predicted property window; window spec delivered to the hub by 15 Dec; grade specs to Procurement by 15 Dec |
| 5 | **CSO + Head of Public Funding** | Day 5: MAT-PROD-22 and MAT-PROD-01 verified on the official portal. Day 90: MAT-PROD-22 proposal **complete**, signed off, all partner declarations in; submission by 30 Jan 2027. IF26 concept notes (Case A; NHT conditional). IPCEI ministry enquiry. **Hub FID test linked to tonnage, drafted for the board paper (replaces the withdrawn 16.5-point amendment)** | 200 | Portal check by 30 Oct; consortium ≥6 partners from ≥3 countries; proposal complete on 23 Jan; test tabled at the day-90 review |
| 6 | **Head of Sales, Extrusion & Rolled** | Commitments of the 8 named Case A targets verified (6 Nov); NDAs with Hueck and Aluprof (15 Dec), BMW and Benteler (15 Jan); JDA term sheets to Hueck, Aluprof and Reynaers | 100 | 8 rows verified; ≥4 NDAs; ≥2 term sheets with qualification co-funding and an indicative A4 premium |
| 7 | **Head of Casthouse Products (Primary)** | B-rod: cable-maker RFQs with adder indications **and post-2030 floor indications**; Properzi/Southwire quotes (by 15 Jan); billet-linked adder talks. NHT: trial-lot offers and RFQs to Volvo, VW and Tesla Berlin, quoting the volume-specific price table | 120 | Adder and floor indications from ≥3 cable makers; quotes in hand; ≥1 NHT trial lot at term-sheet stage |
| 8 | **CFO** | Board model mirrored into the finance repository (6 Nov). **Liquid-metal and scrap ledgers, both states, adopted with S&OP**, including A3's LME-or-P1020 basis. Normalised Cu US$9,500 signed off. **Remelt penalty from our remelt-furnace cost centre (Controlling, 15 Dec).** A1/A3 tonnage overlap (15 Dec). **Case A re-run on the A3 quotes and the A2 invoice spreads (15 Dec).** Hub capex phasing against its FID date checked with the board paper owner (6 Nov) | 100 | Ledgers signed by S&OP by 6 Nov; memo re-run by 15 Dec 2026 |
| 9 | **General Counsel / Head of IP** | Publication numbers for Castasil-37, Magsimal-59, Trimal-37 and C611 (6 Nov); three FTO opinions (15 Jan); disclosure and trade-secret policy. **Scrap-contract template:** ≥3-year term, % of LME indexation, grade certification, hub-FID volume-reduction clause | 170 | Numbers logged; FTO memos by 15 Jan 2027; ≥3 invention disclosures; template issued by 15 Dec |
| 10 | **Head of Sorting Hub project / Head of Recycling** | Sorter specification: LIBS/XRF data schema; Al-Li and Sc segregation channels; data-ownership clauses. **M3 LIBS trial run twice on the same Zorba lot, strict versus wide windows** (EUR 20–50k inside the hub's EUR 2.5M trial budget, not this plan) | 50 | Change approved within the hub budget; upgraded share measured at both window settings |
| 11 | **Head of Public Affairs / Standards** | Seats on CEN TC 132 and the EN 573 / EN 1706 working groups | 50 | Delegate nominated |
| 12 | **Head of Extrusion Operations** | B-ext: 1370/6101 busbar and manifold samples; account plans for Schneider, Vertiv, Siemens, ABB, Hitachi Energy | 100 | Samples to ≥1 OEM by 31 Dec 2026 |
| 13 | **Head of Market Intelligence** | Fastmarkets/CRU 2019–26 rod-adder and billet pull (13 Nov); one Fastmarkets low-carbon differential print. **Fastmarkets MB-AL-0404 / 0405 / 0426 / 0282 and Zorba series subscribed, and the ladder in Section 5.2 replaced with prints** (13 Nov). Bundesanzeiger and Slovak-register filings for 2022–23 remelt tonnages at Trimet and Slovalco (30 Nov). Ducker/CRU structural-casting study commissioned (EUR 20–40k) | 100 | Rod-adder series loaded by 13 Nov; scrap ladder printed by 13 Nov; analogue filings by 30 Nov; study kicked off by 30 Nov |
| 14 | **Head of Scrap Procurement** | 2025–26 purchase invoices by grade in points of LME (28 Oct, shared with the board paper's attachment 3). **≥3 MoU drafts of 20–30 kt/yr for lower-rung (mixed wrought / old rolled, taint/tabor) and A3 grades**, priced as % of LME, plus a re-specification plan for existing suppliers (open item 33). **≥2 firm quotes per A3 grade family** (15 Dec, open item 32) | 0 (inside the hub's M0–M6 work) | Purchased pool by grade loaded; ≥3 MoU drafts covering ≥55 kt/yr by 23 Jan; quotes by 15 Dec |
| 15 | **Head of Regulatory Affairs** | Post-2030 ICC timeline tracker (ETS-review proposal, DG COMP consultation, national notification), feeding the board paper's M9 plan and this memo's gates | 0 (inside the board paper's EUR 1.0M ICC campaign) | First tracker by 30 Nov 2026 |
| | **Total** | | **1,900** | **Day-90 review (23 Jan 2027).** Release **T1 (EUR 10.6M)**. Approve the trigger-conditional parts of the EUR 18.4M 2027 tranche (Section 4.5): T2 (3.5, now on contracted tonnes and both verified spreads), T3 (3.0) and the CFO contingency (1.3). **No NHT or B-rod capex.** Confirm the 30 Sep 2027 gate date for both options, after M9 |

**Check:** 160 + 300 + 200 + 250 + 200 + 100 + 120 + 100 + 170 + 50 + 50 + 100 + 100 + 0 + 0 = 1,900.

---

## 11. Evidence quality

### 11.1 Overall reliability

- **Access:** this revision could not open Fastmarkets, Argus, AlCircle, S&P Global, Recycling Europe, Speira or the Bezirksregierung pages directly (DNS failure or proxy 403). The revision 5 contract, price and curtailment figures come from search-engine extracts of the cited URLs.
- **Prices:**
  - Two post-consumer prints are now anchored: MB-AL-0404 at LME + EUR 48/t, and MB-AL-0405 at LME − EUR 278/t.
  - Argus taint/tabor levels for 2024 and the Recycling Europe Q4 2025 band are also sourced.
  - Still estimated: taint/tabor and old rolled 2026 levels, the premiums, the billet history and the matched rod adders.
- **Contracts:** one EU deal with volume and tenor is public (TSR–Novelis, about 25 kt/yr for 3 years). No EU contract discloses a price as % of LME.
- **Group-paper reconciliation:**
  - Hub figures reproduce the board paper exactly: −EUR 7.9M at 12 points, +EUR 11.2M at 14 points, EBITDA EUR 9.77M.
  - Robot metal loss is 0.3% × EUR 2,431 = EUR 7.29/t.
  - The ICC dates are the board paper's.
- **What still holds:**
  - The method:
    - matched pairs;
    - metal ledgers in two states;
    - contracted tonnes only;
    - decisions made with contingency and without grants;
    - group assets taken on the group's basis.
  - The break-evens:
    - Rod beats billet when A ≥ S − US$46.
    - B-rod needs 45.5 kt of spare primary, and a penalty of ≤EUR 108/t if curtailed.
    - NHT follows the volume-specific table.
    - The no-hub route equals the hub route at 55 kt contracted. The hub adds group value internally above 12.8–13.8 points at 55–70 kt.
  - The gate rules.
  - None of these depends on the unverified history, and the script re-runs on verified data.

### 11.2 Sourced vs estimated

| Category | Status | Examples |
|---|---|---|
| AI design-speed evidence | **Sourced** | MIT, Citrine, M54, GE, RidgeAlloy, Brunel, MPIE, AlloyBot, ARM-MIP |
| Charge-optimiser and robot evidence | **Sourced, qualitative for optimisers** | SMS, GHI, Speira rollout (no results); RiA 0.30% (quantified) |
| Competitor programmes | **Sourced** | Hydro CREATe, Nowa Sól, CirConAl, CIRCAL, Novelis 63%, AMAG, Speira SMS, Nexans–Hydro 17 kt/yr |
| Price basis | **Spot sourced; normalised estimated** | Spot Cu 14,400 / Al 2,940 (S&P Global, 15 Oct 2026); ECB FX; normalised Cu 9,500 [est.] |
| Scrap price ladder 2024–26 | **Partly sourced (search extracts)** | MB-AL-0404 and MB-AL-0405 levels (Fastmarkets webinar, Mar 2026); Argus taint/tabor 2024; Recycling Europe Q4 2025; Hydro extrusion-scrap %; German yard prices. MB-AL-0426 and MB-AL-0282 levels paywalled |
| A3 casthouse deductions (melt loss, energy, QA) | **Estimated, first principles** | 3.9–6.5 points; 2 × 50 t trial by 31 Mar 2027 |
| EU scrap supply contracts | **Sourced for volume and tenor (one EU deal); no pricing** | TSR–Novelis; Hydro–Sims (US); Hydro, Constellium, STEMIN volumes; S&P on tenor |
| Contractable tonnes without a hub | **Estimated** | 40–90 kt/yr, central 70 [est.] |
| Sorter window-width effect | **Estimated; no published curve** | TOMRA, Steinert and Hydro give purity and throughput only |
| ICC post-2030 timeline | **Current scheme sourced; timeline recalled and estimated** | OJ C 317/2020; EU Reporter Dec 2025; 25–40% probability [est.] |
| Curtailed-casthouse analogues and melt capex | **Sourced via search extracts; own arithmetic marked** | Rheinwerk permit and S4 furnace; Slovalco 2023 accounts; Aldel; Trimet Essen; 8 recycling-furnace capex points |
| Remelt penalty | **First-principles estimate** | EUR 70–160/t; Controlling to measure |
| Billet and rod premium history | **Estimated, unverified; no public rod series found** | Section 6.2; two AlCircle billet points and the SMM P1020A point are sourced |
| Metal ledgers | **Internal estimate** | Spare primary 45 kt (25–75); C 130 kt (100–190); S&OP and Casthouse Metallurgy to confirm |
| NHT demand | **Programme build-up from sourced anchors plus estimates** | Euroguss, Bühler, Castings SA, Light Metal Age, GII, Ducker (URLs from earlier rounds) |
| Case A customer commitments | **[unverified], recalled** | Section 5.5; verification due 6 Nov 2026 |
| Funding | **Third-party, unverified on the portal** | MAT-PROD-22 call total of EUR 36M and deadline; MAT-PROD-01 EUR 6–8M |
| Patents | **Families named; one publication verified** | Kaiser US 2023/0416879 A1 verified; four numbers pending (6 Nov) |
| Alloy premiums, tonnages, 2035 values | **Estimated / CTO reasoned** | Sections 3 and 8.4 |
| Capex (rod line, casthouse adaptation, NHT, B-ext, melter) | **CTO estimates** | Quotes are open items |

### 11.3 Open data items with owners and close dates

| # | Item | Why it matters | Owner | Due |
|---|---|---|---|---|
| 1 | Mirror `reports/appendix/alloy_board_model.py` into the finance model repository | Reproducibility | CFO | 6 Nov 2026 |
| 2 | Verified Fastmarkets Rotterdam 6063 billet DDP and P1020 annual averages, 2019–26 | Billet spread S | Treasury / Market Intelligence | 30 Oct 2026 |
| 3 | **EC/1370 rod-adder series 2019–26:** Fastmarkets/CRU pull; own billet invoices net of freight; cable-maker RFQ adder indications | Matched-basis B-rod scenarios; gate test 1 | Head of Market Intelligence (13 Nov 2026); Head of Sales Ops (6 Nov 2026); Head of Casthouse Products (15 Jan 2027) | 13 Nov 2026 / 15 Jan 2027 |
| 4 | **Net A2 down-shift spread** (current purchase grades against the contracted lower-rung grades), in points of LME, net of quality cost | A2; T2(d)(i) | CFO + Head of Scrap Procurement | 15 Dec 2026; contract-based at T2 |
| 5 | Rod-line quotes (Properzi, Southwire) plus building scope | B-rod gate test 4 | Head of Engineering / Procurement | 15 Jan 2027 |
| 6 | **Liquid-metal ledger inputs:** external ingot/sow/T-bar sales 2025–26 (30 kt est.), billet capacity utilisation, primary freed by A3, any external primary purchases. **Ruling on A3's LME or P1020 DP basis** | B-rod test 2; NHT draw; A3 upside (19–22 points) | Head of Casthouse / S&OP; ledger and ruling owned by the CFO | 6 Nov 2026 (inputs); 15 Dec 2026 (ruling) |
| 7 | Billet and rod conversion-cost deltas (EUR 115 / EUR 75 [est.]) | Rod-vs-billet rule (US$46) | Plant Controller | 13 Nov 2026 |
| 8 | Sign-off of normalised Cu US$9,500 and LMEselect 2026 averages | Cu/Al board basis | CFO / Metal Trading | 13 Nov 2026 |
| 9 | MAT-PROD-22 / MAT-PROD-01 topic texts on the official portal | Bid and per-project grant | Grants Office | 30 Oct 2026 |
| 10 | IF26 call dates and small-scale rules | Grants of EUR 4.2M and 6.3M | Grants Office | 15 Dec 2026 |
| 11 | IPCEI-CAM coverage of aluminium in our member state | Possible upside | Government Affairs | 30 Nov 2026 |
| 12 | Patent publication numbers (Castasil-37, Magsimal-59, Trimal-37, C611); FTO opinions incl. Tesla US12378642 assignee | IP strategy; NHT-P freedom | IP counsel (6 Nov 2026); General Counsel (15 Jan 2027) | 6 Nov 2026 / 15 Jan 2027 |
| 13 | Casthouse adaptation capex quote | Case A investment | Head of Casthouse | 31 Jan 2027 |
| 14 | Verification of the 8 named Case A commitments | Case A customers; A4 evidence | Head of Sales + Sustainability | 6 Nov 2026 |
| 15 | Priced LOIs for A4 (2 building + 1 automotive); Fastmarkets low-carbon differential print | A4 premium; T2 trigger | Head of Sales; Market Intelligence | 30 Jun 2027; 13 Nov 2026 |
| 16 | NHT demand: Ducker/CRU structural-casting tonnage; Bühler/IDRA/LK EU installed base; NHT RFQ price premium from Volvo, VW, Tesla Berlin | NHT market and gate | Market Intelligence (31 Jan 2027); Purchasing/CTO (15 Dec 2026); Head of Casthouse Products (31 Mar 2027) | as stated |
| 17 | NHT cost inputs (Si price, additions, conversion, remelt cost, billet margin) | NHT contribution EUR 231 | Controlling | 15 Dec 2026 |
| 18 | Installed Cu→Al system saving (20–40% [est.]) from busbar and transformer OEMs | B-ext pricing | Head of Extrusion Operations | 31 Jan 2027 |
| 19 | Linkage quality of historical chemistry-to-property data | Model feasibility | CDO | 23 Jan 2027 |
| 20 | Sc and Ce quotes from non-Chinese sources | Al-Sc and Al-Ce triggers | Procurement | 31 Mar 2027 |
| 21 | Robotic test-lab quotes (ZwickRoell and others) | 2028 lab gate | CTO | 30 Sep 2027 |
| 22 | **Casthouse existing scrap intake C by alloy** (130 kt est., range 100–190), and C for a scrap-fed casthouse under option C (≥190 est., funded configuration only) | A2 pool; T2(d)(iii); curtailed case | Head of Casthouse Metallurgy; option-C value from the M9 plan | 13 Nov 2026; Jul 2027 |
| 23 | **Purchased-scrap pool by grade in points of LME, 2025–26** (board paper attachment 3) | Ladder; A2 spread; proof that A2 contracts replace higher-grade tonnes | Head of Scrap Procurement | 28 Oct 2026 |
| 24 | **Upgraded share with strict versus wide windows** on the same Zorba lot (75% vs 90% est.) | Hub EUR 270 gate; R1 window value (EUR 19.2M of hub NPV) | Head of Recycling / Hub project (M3 LIBS trial, EUR 20–50k in the hub budget) | Jan 2027 |
| 25 | **Remelt and logistics penalty, purchased ingot against liquid metal** (EUR 115 est., range 70–160); stack-melter quote | B-rod test 6; NHT gate condition 5; B-ext curtailed case | Controlling (cost centre); Casthouse Engineering (quote) | 15 Dec 2026; 31 Jan 2027 |
| 26 | **Post-2030 ICC timeline** (25–40% est. probability of a final guideline by 31 Dec 2029); 80% aid-intensity check | Curtailment gates; M9 | Regulatory Affairs with European Aluminium; board paper legal opinion (day 45) | 30 Nov 2026 tracker; quarterly |
| 27 | A1/A3 tonnage overlap (6–15 kt of A1 sweetening against A3's 15 kt) | Inside the 20% haircut unless it exceeds EUR 3.64M | CFO / Controlling | 15 Dec 2026 |
| 28 | Baseline melt loss split by cause (hot metal, remelt, dross metal content), 2024–26 | Robot versus A1 loss ownership | Head of Casthouse | 15 Dec 2026 |
| 29 | Hub capex phasing (EUR 25M in 2027) against its Oct 2027 FID date in the board paper | Post-FID phasing improves hub NPV by EUR 2.2M; combined view | CFO with the board paper owner (CSO) | 6 Nov 2026 |
| 30 | Fastmarkets taint/tabor (MB-AL-0426) and Zorba series subscription | Replace the [est.] ladder rows | Market Intelligence / Treasury | 13 Nov 2026 |
| 31 | SMS/GHI site results (Speira) split into sweetening, additions and yield; RiA/EPIQ site data behind the 0.30% | A1 restatement range | Procurement (bake-off reference calls, NDA); COO (robot firm quote) | 30 Nov 2026; Jan 2027 |
| 32 | **A3 net substitution spread (new):** MB-AL-0404/0405/0426/0282 subscription; ≥2 firm quotes per A3 grade family; model re-run; 2 × 50 t casthouse trial on melt loss, energy and trim; contract-based confirmation | A3 booked at 9 net points (range 6–13); A1 sweetening; T2(d)(ii) | Market Intelligence (13 Nov 2026); Head of Scrap Procurement (15 Dec 2026); CFO (15 Dec 2026); Casthouse Manager (31 Mar 2027); Head of Scrap Procurement + CFO (at T2) | as stated |
| 33 | **Contracted scrap tonnes (new):** ≥3 MoU drafts of 20–30 kt/yr for lower-rung and A3 grades; re-specification plan for existing suppliers; signed ≥3-year contracts for ≥40 + 15 kt/yr | T2(c); Case A on contracted tonnes; hub test linked to tonnage | Head of Scrap Procurement; General Counsel (template) | 23 Jan 2027 (drafts); 30 Jun–31 Oct 2027 (signed) |
| 34 | **Solid-melt capacity (new):** current capacity and charge mix by furnace (t/h × hours); permitted solid melt under the emissions permit; OEM RFQ for a 60–110 kt two-chamber furnace; 2022–23 remelt tonnages at Trimet and Slovalco | Stranded versus option-C curtailment case; C ≥190 kt claim | Casthouse Engineering; EHS and Permitting; Capex Controlling; Market Intelligence | 30 Nov 2026 (capacity, permit, filings); 31 Mar 2027 (RFQ) |

---

## Appendix B. Board model

- **Script:** `/home/user/ALuminium-industry-buissnes-opprtunity/reports/appendix/alloy_board_model.py`. Python 3, no dependencies. Run with `python3 alloy_board_model.py`.
- **Output:** `/home/user/ALuminium-industry-buissnes-opprtunity/reports/appendix/alloy_board_model_output.txt`.
- **Audit copies** in the same folder: `alloy_board_model_rev4.py` / `alloy_board_model_output_rev4.txt` and `alloy_board_model_rev3.py` / `alloy_board_model_output_rev3.txt`.
  - The new output's first 420 lines are byte-identical to the revision 4 output, so every withdrawn revision 4 figure remains traceable.
- **What it prints, in order:**
  1. Revision 3 sections, unchanged. They are still used for B-ext, NHT (ICC-renewed runs), B-rod (matched table, ICC-renewed ledger, scenario grid, gate tests), the capability centre, the investment build-up and the option cash tables.
  2. **R4.1–R4.7** (revision 4): A1 against the robots, the hub on the board paper's model, Case A rev4, the combined view, the curtailment ledger, the NHT gate and the rev4 portfolio. R5 supersedes their Case A, combined and portfolio figures.
  3. **R5.1** A3 spread on the public post-consumer ladder (blend, gross, deductions, net).
  4. **R5.2** A1 re-priced with the A3 net spread.
  5. **R5.3** Case A booked on contracted tonnes:
     - audit reproduction of the CEO's EUR 42.1M re-run;
     - lever ramp and steady state;
     - runs;
     - the revision 4 → 5 bridge.
  6. **R5.4** the no-hub route on contracted tonnes:
     - Case A, P0, expected values, and internal and external thresholds for 40–115 kt;
     - tonnage break-evens;
     - security-of-supply premium;
     - the no-hub bridge.
  7. **R5.5** Case A + hub combined on the revision 5 basis, with the combined cash flow.
  8. **R5.6** curtailment by casthouse configuration (stranded on existing melt versus option C) and the melt-capex arithmetic.
  9. **R5.7** portfolio on the revision 5 basis, including every robustness row and 2031 EBITDA.
- **Change procedure:** every number in this memo is a line of that output. A change to any input is made in the script, re-run and then copied into the memo, never edited by hand.

---

**Decisions requested from the Executive Committee today:**
1. Approve the EUR 1.9M 90-day budget.
2. Endorse the GO / WATCH / NO-GO decisions in Section 4.1, including:
   - **Case A stays GO on the restated basis:** NPV EUR 31.1M (IRR 31.3%), booked on 55 kt/yr of contracted scrap and on published post-consumer prices. It claims no hub value and no uncontracted tonnes.
   - **NHT stays WATCH** behind the volume-specific gate on both ledgers. This **supersedes the board paper's 20 kt trigger**.
   - **B-rod stays WATCH** under the matched-basis, full-57 kt and curtailment tests. This supersedes and includes the board paper's #4 rod-line FID condition.
3. **Adopt the memo's two capital rules:**
   - Capex that depends on liquid metal must clear NPV10 ≥ 0 both with ICC renewed and with the potlines curtailed from 2030. Otherwise it waits for the 31 Dec 2029 decision. Both option gates are on 30 Sep 2027, after M9.
   - **Contracted-tonnes rule:** a scrap lever is booked only on the tonnes a gate secures by contract.
4. **Restate the robots/A1 boundary:** the furnace-robot case keeps EUR 7.3/t of metal loss; A1 is EUR 6.7/t.
5. Authorise the MAT-PROD-22 bid as lead or co-lead, with the proposal complete on 23 Jan 2027, and the two IF26 small-scale bids. The NHT grant is accepted only if the NHT gate passes.
6. **Committed envelope:** note EUR 54.1M gross (EUR 48.7M net if committed grants are awarded) for EUR 14.8M/yr EBITDA in 2031. Portfolio NPV10, with the capability centre fully charged, is:
   - EUR 26.6M (IRR 21.0%) on the decision basis;
   - EUR 36.2M if the hub is not built and the central 70 kt is contracted;
   - EUR 16.4M if the potlines are curtailed and the casthouse runs on its existing melt;
   - +EUR 2.2M after a failed T2.
7. **Day-90 tranche:** the 2027 tranche of EUR 18.4M comes to the day-90 review as a **gate-conditional** release:
   - T1 of EUR 10.6M at day 90.
   - T2 (3.5), at the latest by 31 Oct 2027. It is now conditional on:
     - **≥3-year contracts for ≥40 kt/yr of lower-rung grades and ≥15 kt/yr of A3 grades;**
     - **verified A2 and A3 spreads of ≥6 net points each.**
   - T3 (3.0) and the CFO-held contingency (1.3) only against their triggers.
   - **No NHT or B-rod capex.**
8. **Refer to the M12 hub FID (board paper):** the revision 4 crowd-out amendment (16.5 points) is withdrawn. The test linked to tonnage in Section 5.4A applies only if more than 72.5 kt/yr is contracted before M12; otherwise the hub's own 14-point gate stands.
9. **Board decisions later:**
   - The B-rod option (EUR 44.1M) and the NHT option (EUR 29.5M) come to the Board on 30 Sep 2027 as separate decisions after their gates.
   - Any solid-melt capex for a scrap-fed casthouse (EUR 36–110M) is an option-C decision in the board paper's M9 plan, not in this envelope.