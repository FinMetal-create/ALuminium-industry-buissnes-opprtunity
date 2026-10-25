# Alloy Design in the Age of AI — Strategy Memo

**To:** CEO, Executive Committee, Board Technology & Strategy Committee
**From:** CTO and Chief Strategy Officer
**Date:** 25 October 2026
**Planning basis:** LME EUR 2,155/t (US$2,500/t), so 1 LME point = EUR 21.55/t. Cu/Al ratio 4.9x on the board basis.
**Evidence convention:** linked figures come from the six research reports. **[est.]** marks an estimate made in those reports. **[CTO est.]** marks an assumption added in this memo, and every one of these is listed as an open item in Section 11.

---

## 1. Executive summary

1. **AI shortens alloy design. It does not shorten qualification.** Composition screening falls from 2–4 years to 3–12 months. MIT evaluated 40 compositions where conventional design would run more than 1 million simulations ([MIT](https://news.mit.edu/index%2Ephp/2025/printable-aluminum-alloy-sets-strength-records-may-enable-lighter-aircraft-parts-1007)). ORNL's RidgeAlloy went from concept to a full-scale HPDC part in 15 months ([ASM](https://www.asminternational.org/?p=1161707)). Customer qualification is unchanged: 2–4 years in automotive and 5–15 years in aerospace ([NASA](https://ntrs.nasa.gov/api/citations/20110013659/downloads/20110013659.pdf)). An automotive alloy now takes about 3–5 years in total, against 10–20 classically [est.]. **We start customer programmes now.**
2. **Our advantage is integration, not algorithms.** Smelter, casthouse, rolling, extrusion and a 100 kt/yr AI sorting hub can share one data chain: sorter spectra, then melt chemistry, then certified properties. Hydro (CREATe, US$2.5M over 5 years) ([Recycling Today](https://www.recyclingtoday.com/news/hydro-university-of-michigan-partnership)) and Constellium (CirConAl, GBP 10M) ([APC](https://www.apcuk.co.uk/impact/funded-projects/constellium-circular-and-constant-aluminium-circonal/)) are building this through universities. We build it in-house and keep it proprietary.
3. **Business case A (scrap-tolerant alloys plus AI casthouse blending) is GO.** Base case is **about EUR 30M/yr EBITDA by 2030**, range EUR 18–45M. Investment is EUR 25–35M over 2027–30 before grants, with payback during 2029. The largest lever is a one-grade scrap down-shift on 100 kt of intake, worth **EUR 17–26M/yr** (EUR 172–259/t) [est.].
4. **Quick win in 6–12 months: an AI charge optimiser.** Value is EUR 5–15/t on 300 kt, or EUR 1.5–4.5M/yr [est.], with payback under a year. Speira is already rolling out SMS Metallics Optimizer at three sites ([Foundry Planet](https://www.foundry-planet.com/d/digital-solution-enhances-efficiency-reduces-costs-and-promotes-sustainable-circular-economy/)).
5. **Business case B (conductor rod plus data-centre electrical and thermal extrusions) is GO, subject to an investment-decision gate.** Base case is **about EUR 27M/yr by 2030** on EUR 35–55M capex. The Cu/Al ratio of 4.6–4.9x is far above the 3.5–4.0x switching threshold ([AlCircle](https://www.alcircle.com/news/rising-copper-prices-accelerate-shift-towards-aluminium-wiring-in-automotive-industry-120125)). Each tonne of aluminium deployed saves the customer about EUR 19,000 of copper [est.]. The gate is two cable-maker offtake LOIs and a validated rod-line quote.
6. **Non-heat-treatable (NHT) structural casting alloy is GO.** EU demand is 250–400 kt/yr by 2030 [est.]. At an EUR 300–700/t premium, 40 kt/yr is worth **EUR 12–28M/yr** [est.]. Rusal has owned Rheinfelden since 2021 ([Dry Cargo](https://www.drycargomag.com/rusal-completes-acquisition-of-aluminium-rheinfelden)), so OEMs will want a non-Russian EU source. The window is the next 12–18 months while Volvo Košice and other programmes fix their specifications.
7. **Capability:** an alloy-informatics team of 8–12 FTE, costing **EUR 8–14M over 3 years** [est.], with 30–50% grant co-funding. In 2027 we buy software and lab access. We build our own rapid-prototyping lab only in 2028, behind a gate.
8. **Commercial model: own the chemistry window, sell the metal, license only abroad.** Branded-alloy premium is EUR 50–350/t [est.]. Non-EU licences earn about EUR 60–140/t in royalties [est.]. IP protection rests on process and chemistry-control patents plus trade secrets, because composition patents on 6xxx are easy to design around.
9. **Funding deadline:** Horizon CL4-2027-01-MAT-PROD-22 (EUR 36M) **closes 2 February 2027** ([EU call](https://www.euacc.ai/calls/HORIZON-CL4-2027-01-MAT-PROD-22)), about 100 days from today. We submit. We also file IPCEI-CAM expressions of interest.
10. **Portfolio total:** about **EUR 70M/yr base EBITDA uplift by 2031** from A, B and NHT combined after overlap haircuts [CTO est.], for EUR 80–125M investment before grants. **NO-GO:** our own Al-Li production, a greenfield battery-foil mill, a greenfield AM atomiser, high-entropy alloys, and generative-crystal-model R&D. **WATCH:** 5/7 crossover sheet (AMAG leads by about 7 years), scandium, and twin-roll casting.

---

## 2. How AI changes alloy development

### 2.1 Proven, promising and hype

| Status | Technique / claim | Evidence | Decision relevance for us |
|---|---|---|---|
| **Proven** | CALPHAD + ML surrogates + Bayesian optimisation for composition search | MIT: 40 compositions instead of >1M simulations; 50% stronger than design without ML ([MIT](https://news.mit.edu/index%2Ephp/2025/printable-aluminum-alloy-sets-strength-records-may-enable-lighter-aircraft-parts-1007)). Citrine/HRL: 11.5M combinations narrowed to 100 candidates, commercial about 2 years after publication ([Citrine](https://CITRINE.IO/wp-content/uploads/2021/04/Case-Study-HRL-AM-powder-development.pdf)). PatSnap: 800,000 compositions and 36 experiments for +12.6% modulus ([PatSnap](https://www.patsnap.com/resources/blog/articles/ai-accelerated-alloy-design-landscape-2026/)), from the summary only | **Core tool.** Applies directly to designing for scrap windows |
| **Proven** | ICME shortens the whole programme | QuesTek M54: about 6 years against 15–20 typical ([NIST](https://www.nist.gov/document/materialsinnovationcasestudyquestek090616pdf)). GE: 15 to 9 years ([NIST/MGI](https://www.nist.gov/node/1507161)) | Sets realistic expectations: roughly halves the time, not 100x |
| **Proven** | ML rationalisation of an alloy portfolio | Brunel: 42 6xxx grades reduced to 10 "optimal alloys" using 292 datasets ([Springer](https://link.springer.com/article/10.1007/s40831-025-01112-4)) | Low cost. Enlarges scrap pools |
| **Proven** | Scrap-tolerant alloy design | ORNL RidgeAlloy: more than 2M calculations, 15 months to a full-scale part ([ASM](https://www.asminternational.org/?p=1161707)). ML-guided Sc addition to recycled Al validated at +4.37% UTS ([BIT](https://pure.bit.edu.cn/zh/publications/design-of-high-strength-and-ductile-recycled-al-alloys-by-machine/)). JMI 2024: >190 W/m·K and >220 MPa thermal alloy ([JMI](https://www.oaepublish.com/articles/jmi.2024.21)) | **Our main use case** |
| **Proven, scaling** | High-throughput and self-driving labs | MPIE: 50 conditions in about 5 days ([MPIE](https://www.mpie.de/4151172/combinatorial-metallurgy-and-processing)). AlloyBot: >100 compositions/week ([TMS](https://www.programmaster.org/PM/PM.nsf/ApprovedAbstracts/C51BFD5FCD57FCD785258CBB00102E33)). Texas A&M ARM-MIP: US$24.9M, 50 rising to more than 200 alloys/month, with industry access on negotiated IP terms ([TAMU](https://stories.tamu.edu/news/2026/08/05/texas-am-to-build-self-driving-laboratory-for-metals-open-to-researchers-nationwide/)) | Buy access first, build later |
| **Promising** | LLM multi-agent design assistants | EGA at ICSOBA 2025 ([ICSOBA](https://icsoba.org/assets/files/publications/2025/Papers/CH08%20-%20Physics-Aware%20Multi-Agent%20AI%20Framework%20for%20Property%20Prediction%20and%20Design%20of%20Aluminium%20Alloys.pdf)). AlloyGPT ([ASM](https://asm.confex.com/asm/imat2025/webprogram/Paper63852.html)). MIT PNAS 2025 ([DSpace](https://dspace.mit.edu/handle/1721.1/163619)) | They orchestrate tools; they are not autonomous designers. Pilot only |
| **Hype for us** | Generative crystal models (MatterGen, GNoME) | Some "discoveries" are disordered versions of known compounds ([HU Berlin](https://edoc.hu-berlin.de/18452/38430)). Our properties come from microstructure and processing | Not relevant before about 2028. No spend |
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

**Conclusion:** AI is worth about 1–3 years and 50–60% of development cost per alloy. It does not change the qualification clock. Our plans therefore treat qualification as the critical path, and every alloy programme has a named customer before lab work starts.

### 2.3 What competitors are doing

- **Hydro:** CREATe with U-Michigan on Fe-tolerant extrusion alloys, plus SFI FAST (2026–33) on post-consumer scrap in safety-critical parts ([NAV](https://arbeidsplassen.nav.no/stillinger/stilling/2ba31115-971a-4398-ae69-87b76c53d954)).
- **Constellium:** AI work with 3ALP and MIT on Fe/Mn in 6xxx; CirConAl crash systems from >90% post-consumer scrap ([Constellium](https://constellium.com/news/showcase-aluminum-solutions-collaborative-research-project-circonal-cenex2025)); R&D of about US$50M and about 300 staff ([Constellium](https://www.constellium.com/innovation)).
- **Novelis:** hiring for AI alloy discovery ([Novelis](https://careers-novelis.icims.com/jobs/47609/ai-%26-advanced-modeling-co-op/job)).
- **Speira:** SMS Metallics Optimizer.
- **EGA:** LLM framework.

There is no public AI conductor-alloy programme at Hydro, Novelis or Constellium (Report 4), so that space is open for a first mover.

---

## 3. Alloy opportunity map

Tonnage columns show EU demand unless marked global. Figures marked (x) are CTO extrapolations to 2035, because the reports give no 2035 figure.

| Alloy family | End market | Tonnage 2030 | Tonnage 2035 | Premium EUR/t over standard | Qualification time | Our right to win |
|---|---|---|---|---|---|---|
| Scrap-tolerant HRC 6xxx extrusion billet (Fe 0.4–0.8, Mn/Cr) | Building, automotive extrusions | EU 6xxx billet 3–4 Mt/yr [est.]; our target 40–60 kt | 60–100 kt ours (x) | 50–200 + spread capture 172–259 [est.] | ~1 yr building; 2–4 yrs auto [est.] | **High.** The sorting hub and casthouse data chain is hard to copy |
| HRC 5xxx/6xxx sheet | Auto body, building | Part of 50–150 kt ours [est.] | 100–150 kt (x) | 50–200 [est.] | 2–4 yrs | **Medium-high.** Novelis is ahead at 63% average recycled content and up to 85% in auto ([Novelis](https://investors.novelis.com/news-events/press-releases/detail/1415/novelis-wins-award-for-100-recycled-end-of-life-vehicle-scrap-product)) |
| Certified ≥75% post-consumer brand | Auto, building, foundry | 50 kt ours | 80–120 kt (x) | 50–200 [est.]; low-carbon P1020 differential only $25–40/t ([Fastmarkets](https://fastmarkets.com/insights/low-carbon-aluminium-differentials-in-europe-widen-for-p1020-vaps)) | 12–18 months | **Medium.** Competes with Hydro CIRCAL (1.9 kg CO2e/kg) |
| NHT structural HPDC (AlSi10MnMg / AlMg5Si2Mn class) | Giga- and megacasting | 250–400 kt [est.]; global 1.5–2.5 Mt | 400–600 kt (x) | 300–700 over AlSi9Cu3, plus 50–150 low-CO2 [est.]; or 150–350 over AlSi10Mg [est.] | 2–4 yrs after alloy ready | **Medium-high.** Low-Fe primary, non-Russian origin; die-casters with 5–7% margins cannot fund alloy R&D ([AlCircle](https://www.alcircle.com/news/giga-casting-the-aluminium-shot-escaping-the-cost-trap-via-rheocasting-ridgealloy-and-tier-1-consolidation-120137)) |
| EC 1370 / 8xxx / 6101-6201 conductor rod | Grid, LV/MV cable, data-centre connection | EU 0.6–0.9 Mt [est.]; 8xxx and LV/MV 150–300 kt [est.] | +4–6%/yr, so 0.75–1.2 Mt (x) | EC 200–400; 6xxx 300–600; 8xxx 250–450; green 100–250 [est.] | 6–12 months with cable makers | **High.** Hot metal from the smelter, as at Midal and Karmøy; EU cable makers import rod |
| Heat-resistant Al-Zr (TAL/ZTAL), later Al-Zr-Er/Sc-lean | HTLS reconductoring | 20–50 kt [est.] | 40–80 kt (x) | 300–800 over EC rod [est.] | 24–48 months (IEC 62641/62004 plus TSO pilots) | **Medium.** Needs the rod line first |
| Busbar and high-thermal-conductivity extrusions | Data centres, BESS, switchgear | EU addressable 40–80 kt [est.] | 60–120 kt (x) | Conversion 1,500–3,000 [est.] | 6–12 months OEM | **Medium-high.** Existing extrusion presses |
| High-conductivity thin-wall HPDC (≥45% IACS, ≥150 MPa) | E-motor, inverter and robot housings | 30–80 kt [est.] | 50–120 kt (x) | 500–1,000 [est.] | 24–48 months | **Medium-low.** Tesla holds patents at 46–55% IACS; Alcoa AT237 is about 41% IACS |
| Robot-grade 6xxx/7xxx bar, plate, extrusion | Humanoids, cobots, drones | 50–200 kt semis globally [est.] | CRU moderate case 10 Mt by 2050 ([CRU](https://www.crugroup.com/en/communities/thought-leadership/2025/the-next-commodity-battleground-humanoid-robots/)) | 800–2,000 [est.] | 12–30 months | **Medium.** Mg is cheaper per tonne; our pitch is EU supply security |
| 5/7 crossover AlMgZn(Cu) sheet | Auto structural, rail | 10–30 kt [est.] | 20–50 kt (x) | Value-added, not quantified | 3–5 yrs | **Low.** AMAG CrossAlloy.57 leads by about 7 years ([AMAG](https://www.amag-al4u.com/produkte/crossalloy/automotive)) |
| Al-Ce / ACMZ high-temperature cast | E-drive, turbo, H2 | 5–20 kt by 2032 [est.] | 10–25 kt (x) | 300–800 over A356 [est.] | 2–4 yrs | **Low-medium.** Would be licensed in from ORNL/Eck |
| Al-Sc / Al-Sc-Zr master alloy | Defence, AM | ~855 t/yr Al-2Sc globally ([Valuates](https://reports.valuates.com/market-reports/QYRE-Auto-34R6611/global-aluminium-scandium)) | Doubles if Syerston ramps (x) | US$60–75/kg conversion | 1.5–3 yrs | **Low.** Oxide supply is the constraint |
| AM powder / WAAM wire | Aero, motorsport, defence | 1–3 kt globally [est.] | 2–6 kt (x) | EUR 70–125/kg | 2–4 yrs industrial; 4–7 yrs aero | **Low.** Licensing or tolling only |
| Battery foil stock / can sheet | Li-ion, Na-ion, BESS | Foil 100–300 kt [est.] | Uncertain | Foil stock 600–1,500 conversion [est.] | 12–24 months | **Low.** China added about 1.27 Mt of foil capacity ([AlCircle](https://www.alcircle.com/news/growing-demand-for-aluminium-battery-foil-prompts-china-to-commission-17-new-capacities-98896)) |
| Al-Li | Aerospace | Market US$2.3–2.8bn | n/a | 1.5–2.5x 7xxx plate [est.] | 5–10+ yrs | **None.** Incumbents locked in |

---

## 4. Ranked portfolio

Score is out of 10. It weights value (30%), right to win (25%), time to revenue (20%), risk (15%) and capital intensity (10%), starting from the specialist reports' scores and adjusted by us.

| # | Opportunity | Decision | Capex / dev spend 2027–30 | Time to revenue | Risk | Score | Gate (next go/no-go) |
|---|---|---|---|---|---|---|---|
| 1 | **AI charge optimiser and property-window specification** (scrap-to-spec digital thread) | **GO** | EUR 2–3M [CTO est.] | 6–12 months | Low | **9.1** | 3-month shadow run on one furnace shows ≥EUR 5/t saving (by Q2 2027) |
| 2 | **Scrap-tolerant "house" 6xxx extrusion and HRC sheet family** fed by the hub | **GO** | EUR 18–30M incl. casthouse adaptation and qualification [CTO est.] | 12–24 months building; 2–4 yrs auto | Medium | **8.8** | ML-designed Fe 0.5–0.8 variants meet the EN 755 property window in lab (Q4 2027), plus one signed building-systems JDA |
| 3 | **Low-carbon EU NHT structural HPDC alloy** (ingot and liquid metal) | **GO** | EUR 10–20M [CTO est.] | 12–24 months first lots; 2–4 yrs serial | Medium | **8.2** | Trial-lot agreement with one OEM casting shop or Tier-1 megacaster (Volvo Košice/Torslanda cluster) by Q3 2027 |
| 4 | **EU low-carbon conductor rod platform** (EC/8xxx/6101), with scrap-tolerant 8xxx/6xxx chemistry | **GO, investment-decision gated** | EUR 25–40M rod line [CTO est.] + EUR 1–3M alloy development | 18–30 months | Low-medium | **8.0** | Two cable-maker LOIs totalling ≥40 kt/yr indexed offtake, a firm line quote, and margin above the billet alternative. Investment decision Q2 2027 |
| 5 | **Data-centre busbar and thermal extrusions** (1370/6101; high-thermal-conductivity 6xxx/1xxx; manifolds) | **GO** | EUR 5–10M [CTO est.] | 9–18 months | Medium | **7.5** | One framework contract or qualification order from Schneider, Vertiv, Siemens or ABB by Q4 2027 |
| 6 | **Portfolio rationalisation and closed-loop scrap contracts** (incl. gigacasting returns take-back) | **GO** | < EUR 1M | 12–36 months | Low | **7.3** | SKU count cut ≥30% without customer loss; first take-back contract by Q4 2027 |
| 7 | **Al-Zr HTLS rod, then ML Al-Zr-Er / Sc-lean conductor and extrusion alloys** | **WATCH → GO** once rod line is approved | EUR 1–3M R&D (grant-funded) | 24–48 months | Medium | **6.8** | Rod-line investment approved, plus one TSO pilot partner |
| 8 | **High-conductivity HPDC and robot-grade 6xxx/7xxx** via start-up partnership (Alloyed, Phaseshift, Fehrmann) | **WATCH** | < EUR 1M per year | 24–48 months | High | **6.0** | Partner shows ≥45% IACS at ≥150 MPa in trial castings; motor OEM signs a co-development deal |
| 9 | **5/7 crossover sheet by licence** (AMAG/Leoben) | **WATCH** | Licence fee plus mill trials (not quantified) | 3–5 yrs | High | **5.5** | AMAG open to licence or JV on acceptable terms (exploratory talks in 2027) |
| 10 | **Greenfield battery-foil mill, own Al-Li, greenfield AM atomiser, twin-roll line, HEAs** | **NO-GO** (supply foil stock and Al-Li/Sc scrap segregation only; review twin-roll in 2029) | 0 | n/a | High | ≤5.0 | Re-open only if the EU foil market tightens or a partner funds a twin-roll pilot |

**Low-cost options that stay alive:**
- Al-Li and Sc scrap segregation channels at the hub (Report 5, score 5), added to the sorter specification now at almost no cost.
- Al-Sc master alloy, kept as WATCH until Sunrise Syerston delivers in 1H 2028 ([ASX](https://announcements.asx.com.au/asxpdf/20260810/pdf/072l1673ycxhhl.pdf)).

---

## 5. Business case A: scrap-tolerant alloys and AI casthouse blending

### 5.1 Logic

Sorting alone does not create value if our alloy specifications still force us to dilute the sorted scrap with primary metal. Value comes from three steps together:
1. Sorted scrap with a known composition distribution, from the hub's LIBS/XRF data.
2. Alloys designed for that distribution: Fe 0.4–0.8 with Mn/Cr to convert β-AlFeSi to the α-phase, which has industrial evidence ([AIT](https://publications.ait.ac.at/en/publications/tolerance-of-almgsi-wrought-alloys-for-high-fe-contents-the-role-/); Kaiser patent application, Fe and Mn up to 0.8% at >75–90% scrap ([Justia](https://patents.justia.com/patent/20230416879))).
3. A charge optimiser that aims each melt at the cheapest compliant mix, with products specified by property window rather than tight composition window.

### 5.2 Value levers, steady state 2030

| Lever | Mechanism | EUR/t | Volume | EUR M/yr, range | EUR M/yr, base |
|---|---|---|---|---|---|
| A1 AI charge optimisation | Aim closer to spec limits; 2–5 pp less sweetening; 0.2–0.5 pp better yield | 5–15 per t of output | 300 kt | 1.5–4.5 [est.] | 3.0 |
| A2 One-grade scrap down-shift | Wider Fe/Cu/Zn windows let us buy one grade lower (8–12 pts) | 172–259 | 100 kt of intake | 17–26 [est.] | 20.0 |
| A3 Higher recycled content | Post-consumer scrap at about 80% LME replaces primary | ~431 | 15 kt in base (30 kt high case) | 6–13 (up to 25) [est.] | 6.0 |
| A4 Certified ≥75% post-consumer brand | Green and recycled premium, DNV/ASI verified, EPD < 2 kg CO2e/kg | 50–200 | 50 kt | 2.5–10 [est.] | 5.0 |
| A5 Portfolio rationalisation | Fewer alloy changes, larger segregated pools, less downgrading | — | Group-wide | 2–5 [est.] | 3.0 |
| **Gross** | | | | **29–58** | **37** |
| Overlap haircut (A1/A2/A3 share the same scrap tonnes) | | | | −20% [CTO est.] | −7 |
| **Net, 2030** | | | | **18–45** | **≈30** |

The net range matches Report 2's combined realistic range of EUR 20–45M/yr.

**CO2:** A3 at 30 kt avoids about 465 kt CO2/yr, since each tonne of primary displaced avoids about 15.5 t.

### 5.3 Investment and opex, 2027–30 [CTO est. unless noted]

| Item | EUR M |
|---|---|
| Charge optimiser: SMS Metallics Optimizer, GHI ALEA or in-house build, plus integration and inline chemistry | 2–3 |
| Casthouse adaptation for lower-grade scrap: melt treatment, Mn/Cr master-alloy dosing, furnace capacity for contaminated scrap (Speira is adding such furnaces, per Report 2) | 8–15 |
| Development of 3 alloys (HRC 6060/6063, 6082, 5xxx/6xxx sheet), AI-enabled | 4–6 (lower end of EUR 4–12M per alloy, since these are variants of existing grades) |
| Customer qualification for 2–3 alloy-OEM pairs | 3–9 (EUR 1–5M per pair [est.]) |
| Certification (DNV/ASI, EPD) | 0.3–0.5 |
| **Total investment** | **≈18–33, base EUR 28M** |
| Grant share on the R&D portion (30–50%) | −3 to −6 |
| Incremental opex: share of informatics team, licences, certification audits | 2–3 per year |

Excluded: the capex of the 100 kt hub itself, which is already planned.

### 5.4 Cash profile and payback, base case [CTO est.]

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Investment (EUR M) | −9 | −10 | −6 | −3 |
| Net EBITDA uplift (EUR M) | +2 (A1) | +8 (A1, A5, building HRC on 30 kt) | +18 (hub at full rate, A4 launched) | +30 |
| Cumulative (EUR M) | −7 | −9 | +3 | +30 |

- **Payback:** charge optimiser under 1 year; whole case during 2029, about 2.5–3 years after start.
- **Indicative NPV:** EUR 30M/yr over 10 years at 8%, less investment, gives roughly EUR 150M [CTO est.].

### 5.5 Partners

| Role | Partners |
|---|---|
| Science | Montanuniversität Leoben (Pogatscher group, "dirty alloys" ([TU Wien PDF](https://repositum.tuwien.at/bitstream/20.500.12708/158251/1/Raabe-2022-Progress%20in%20Materials%20Science-vor.pdf))); AIT (Fe-tolerance work); RWTH; MPIE (RAP). Avoid exclusive ties with NTNU/SINTEF, which are close to Hydro |
| Software and vendors | Thermo-Calc (TCAL11/MOBAL); SMS group or GHI; Citrine or Intellegens on trial |
| Customers | One building-systems extruder or OEM (fast: about 1-year qualification); 1–2 auto OEMs or Tier-1s for crash and structural extrusions |
| Standards | CEN TC 132, EN 573 / EN 1706 revision, which already aims to raise allowable impurity levels ([BSI](https://standardsdevelopment.bsigroup.com/projects/9026-13536)) |
| Consortia | Tie in with Horizon CLEANMAT (EUR 7.33M) and RecAL (EUR 10.6M) ([CORDIS](https://cordis.europa.eu/project/id/101294748/de)) |

### 5.6 Milestones

| When | Milestone |
|---|---|
| Q1 2027 | Data lake v1 (OES, process logs, certificates 2019–26); optimiser vendor chosen |
| Q2 2027 | Optimiser shadow mode on one furnace; MAT-PROD-22 submitted (2 Feb) |
| Q3 2027 | First ML-designed HRC 6063/6082 variants cast (rapid casting via MPIE or partner lab) |
| Q4 2027 | Lab properties pass; building-systems trial extrusions |
| 2028 | Optimiser live on all furnaces; hub data feeds the model; first commercial HRC billet sales |
| 2029 | Auto qualification complete; AA Teal Sheet filed after 12 months of commercial supply ([AA form](https://www.aluminum.org/sites/default/files/2021-11/TEMPLATEWROUGHTALLOYREGISTRATIONFORM20180.docx)); ≥75% post-consumer brand launched |
| 2030 | Full 100 kt hub output absorbed into house alloys |

---

## 6. Business case B: electrical conductor and thermal-management alloys

### 6.1 Logic

- **Copper substitution.** At Cu/Al of 4.6–4.9x, 1 t of aluminium replaces about 2.0 t of copper at equal current. That saves the customer about EUR 19,000 of copper metal per tonne of aluminium [est.], and about 25–45% at cable level [est.]. Prysmian is already at about 40% aluminium by weight ([AlCircle](https://www.alcircle.com/news/rising-copper-prices-accelerate-shift-towards-aluminium-wiring-in-automotive-industry-120125)).
- **Demand.** EU grid investment of EUR 584bn ([EC](https://energy.ec.europa.eu/publications/eu-action-plan-grids_en)). Data-centre aluminium demand of 0.6–0.9 Mt/yr at peak inside the asset, 55% of it cooling, with 3–4x that across the whole system ([Wood Mackenzie](https://www.woodmac.com/press-releases/wood-mackenzie-data-centre-metals-demand-isnt-an-asset-story.-its-a-grid-story)).
- **Our edge.** Hot metal from the smelter is the cheapest route to low-Ti/V EC rod after boron treatment. EU cable makers import from Midal, India and Norway (Hydro Karmøy supplies about 70 kt/yr ([Hydro](https://hydro.com/en/aluminium/products/casthouse-products/wire-rod-for-cable-and-wire-solutions/))).
- **Where AI helps.** We use AI for scrap-tolerant conductor chemistry: a model of conductivity as a function of scrap mix, boron treatment and ageing that guarantees 61% IACS at 30–50% recycled content. That beats Midal's 15–30% MiRecAL benchmark ([EPD](https://www.environdec.com/library/epd28974)).

### 6.2 Value levers, steady state 2030

| Lever | Volume | EUR/t | EUR M/yr, range | EUR M/yr, base |
|---|---|---|---|---|
| B1 Conductor rod (35 kt EC 1370, 15 kt 8xxx, 10 kt 6101/6201) | 60 kt | Gross premium over P1020 200–600; net margin assumed at 50% of premium after conversion [CTO est.] | 6–18 | 10 |
| B2 Scrap in 8xxx/6xxx conductor melts (40% of 25 kt = 10 kt scrap replacing primary) | 10 kt | 172–431 | 1.7–4.3 | 3 |
| B3 Green premium on ≥30% recycled conductor rod | 25 kt | 100–250 [est.] | 2.5–6.3 | 4 |
| B4 Al-Zr TAL/ZTAL HTLS rod (from 2029) | 5–10 kt | 300–800 over EC [est.] | 1.5–8 | 3.5 |
| B5 Data-centre busbar and thermal extrusions; incremental margin over standard profiles of 300–600/t [CTO est.] on conversion of 1,500–3,000/t [est.] | 20 kt | 300–600 | 6–12 | 8 |
| **Total 2030** | | | **≈12–45** | **≈27** |

**Customer value created:** 60 kt of conductor aluminium displaces about 120 kt of copper, worth about EUR 1.1bn at the board basis. That supports long-term LME-indexed offtakes with a fixed premium.

### 6.3 Investment and opex [CTO est.]

| Item | EUR M |
|---|---|
| Continuous rod line (Properzi type) fed with hot metal, plus boron treatment and degassing; build takes 12–18 months (Report 4) | 25–40 (**not sourced; open item 1**) |
| Alloy development and conductivity models: 8xxx/6xxx scrap-tolerant, then Al-Zr-Er | 1–3 per family [est.] |
| Type testing: EN 50182/50183, IEC 62641/62004 | 0.3–1 per family [est.] |
| Busbar and thermal extrusion: dies, fabrication and finishing cell, coolant-compatible surface treatment | 5–10 |
| **Total** | **≈35–55** |
| Incremental opex | Rod-line crew and maintenance, folded into the net-margin assumption; DC application engineers 0.5M/yr |

**Payback:** first rod in H2 2028; cable-maker qualification takes 6–12 months; volume from 2029. Payback is about 3–4 years from the investment decision, or 2–2.5 years after start-up. B5 starts earlier, in 2027–28, on existing presses.

**Key economic test, open item 2:** hot metal sent to rod is not sent to billet. The North German 6063 billet premium swung from about $500/t (Dec 2025) to $1,175–1,250/t (May 2026) ([AlCircle](https://www.alcircle.com/news/european-aluminium-premium-reaches-a-record-472-t-in-march-is-it-a-build-up-from-last-year-or-the-hormuz-crisis-117803)). The rod line must beat the billet alternative across the cycle, not only at the current peak. This is the first condition of the investment decision.

### 6.4 Partners

| Segment | Partners |
|---|---|
| Cable makers (offtake) | Nexans, Prysmian, NKT, Lamifil (holds an Al-Zr patent; potential co-developer), Tratos, De Angeli |
| HTLS | CTC Global ACCC licensees (50,000+ km installed ([CTC](https://ctcglobal.com/?p=266860))); one EU TSO for a pilot line |
| Data centres | Schneider, Vertiv, Siemens, ABB, plus EU busway makers |
| Science | Alloyed/BCAST (heat-conducting scrap-based alloy, ([The Engineer](https://www.theengineer.co.uk/content/news/525k-to-accelerate-ai-alloy-design))); TECNALIA MetalIA; Leoben/RWTH for Al-Zr-Er |
| Equipment | Properzi-type rod-line vendor (quote needed) |

### 6.5 Milestones

| When | Milestone |
|---|---|
| Q1 2027 | Cable-maker market sounding; LOIs targeted; rod-line budget quote; billet-vs-rod margin model |
| Q2 2027 | Investment decision on the rod line (gate: ≥40 kt/yr LOIs, IRR above hurdle at mid-cycle billet premium); first busbar qualification samples to a DC OEM |
| Q4 2027 | Conductivity-vs-scrap-mix ML model validated on lab casts at ≥61% IACS with ≥30% scrap |
| H2 2028 | Rod line commissioned; cable-maker qualification |
| 2029 | Commercial rod at 40 kt; Al-Zr type tests begin; DC extrusions at 15 kt |
| 2030 | 60 kt rod, 20 kt DC extrusions, first HTLS pilot line |

**Sensitivity:** if Cu/Al falls below 4.0x, B5 and the 8xxx substitution demand soften. EC rod for overhead lines is almost entirely aluminium already, so B1 holds. In a Cu/Al 3.8x stress case, EBITDA is about EUR 17M/yr [CTO est.].

---

## 7. Building the capability

### 7.1 Organisation

The **Alloy Informatics & Design Centre** reports to the CTO and is led by a newly hired Head of Alloy Informatics.

| Role | FTE | Notes |
|---|---|---|
| Computational metallurgists (CALPHAD, precipitation) | 2–3 | |
| ML / data scientists | 2–3 | |
| Data engineers | 1–2 | Digitise casthouse, rolling and extrusion history |
| Lab technicians | 2–3 | |
| Product / IP lead | 1 | |
| **Total** | **8–12 FTE, EUR 1.2–1.8M/yr [est.]** | |

### 7.2 Data, our biggest asset

- Years of OES melt chemistry, process logs and test certificates, plus the hub's LIBS/XRF spectra from commissioning.
- One-off FAIR standardisation costs EUR 0.5–1M [est.]. Data standardisation is the bottleneck named in the 2026 reviews, so it starts on day 1.

### 7.3 Software

- Thermo-Calc with TCAL11/MOBAL. Benchmark: a TCAL9 perpetual licence cost EUR 10,440 in a public tender ([VSB](https://zakazky.vsb.cz/document_audit_71158/priloha-1-sw_thermocalc_tech_spec-doc)).
- Bayesian optimisation and ML stack: in-house Python as the default, with Citrine or Alchemite (EUR 100–300k/yr) trialled for 12 months.
- Granta-type data management.
- Total software spend EUR 0.3–0.6M/yr [est.].

### 7.4 Laboratory (Materials Acceleration Platform), phased

| Phase | Content |
|---|---|
| 2027: buy access | MPIE Rapid Alloy Prototyping or Leoben casting trials; ARM-MIP access on negotiated IP terms; casthouse trial casts |
| 2028: build, gated | Multi-mould rapid casting (EUR 0.3–0.8M); lab rolling mill and extrusion/compression simulator (EUR 0.7–2M); robotic tensile testing (about EUR 0.35M, ZwickRoell roboTest P with 300 specimens unattended, price unconfirmed ([ZwickRoell](https://www.zwickroell.com/fileadmin/content/Files/SharePoint/user_upload/Brochures_EN/Flyer_Automated_Testing_Systems_EN.pdf))); automated metallography and SEM-EDS (EUR 0.3–0.8M); DSC, conductivity and corrosion rigs (EUR 0.2–0.4M). **Lab capex EUR 2.5–5M [est.]** |
| Gate to build | 2027 programme needs at least 300 casts/yr, or external service demand of at least EUR 0.5M/yr, or the grant is awarded |

### 7.5 Build, buy or partner

| Component | Decision | Why |
|---|---|---|
| Data platform and trained property models (scrap to chemistry to properties) | **Build, own it** | This is the moat. Keep it as a trade secret |
| CALPHAD databases | **Buy** (Thermo-Calc) | Industry standard |
| ML and Bayesian-optimisation platform | **Build** on open source; **trial-buy** Citrine/Alchemite | Avoid lock-in; SaaS speeds up year 1 |
| Charge optimiser | **Buy** (SMS/GHI) and integrate our own property models | Time to value; vendors publish no EUR/t, so contract on outcomes |
| Rapid prototyping and testing | **Partner in 2027, build in 2028** | Prove throughput need first |
| Fundamental science | **Partner** (Leoben, RWTH, MPIE, AIT, Brunel BCAST) | Grant leverage and talent pipeline |
| Niche specialty alloys (high-conductivity HPDC, AM) | **Partner or license** (Alloyed, Phaseshift, Fehrmann; Aheadd/Addalloy-type licences) | High risk, small volumes |
| Crossover 5/7 | **License** (AMAG) | About 7-year incumbent lead |

### 7.6 Budget by year (capability only; alloy qualification sits in A and B)

| EUR M | 2027 | 2028 | 2029 | 3-yr total |
|---|---|---|---|---|
| Team (6, then 10, then 12 FTE) | 0.9 | 1.5 | 1.8 | 4.2 |
| Data digitisation (one-off) | 0.8 | 0.2 | — | 1.0 |
| Software and compute | 0.4 | 0.5 | 0.5 | 1.4 |
| External lab access and university partners | 0.6 | 0.6 | 0.5 | 1.7 |
| Lab capex | 0.4 | 2.5 | 1.0 | 3.9 |
| **Gross** | **3.1** | **5.3** | **3.8** | **12.2** (within EUR 8–14M [est.]) |
| Grants (30–50%) | −0.5 | −2.0 | −1.5 | −4.0 |
| **Net** | **2.6** | **3.3** | **2.3** | **≈8.2** |

**From 2029: alloy-development services** to casters, extruders and OEMs, at EUR 1–3M/yr [est.]. Die-casters with 5–7% margins cannot fund this work themselves.

---

## 8. IP and commercial model

### 8.1 Model: own the chemistry window, sell the metal, license only abroad

Western majors earn from alloy innovation mainly through **metal premiums**: Advanz, HSA6, CIRCAL, SOUL. The value of a design house on its own is small; QuesTek reported only more than $750k in fees and royalties ([NETL](https://www.netl.doe.gov/File%20Library/Events/2015/utsr/Wednesday/Saal.pdf)).

### 8.2 IP layers

1. **Process and chemistry-control patents** in EP, US and CN: melt correction from sorted-scrap data, homogenisation windows, AI-controlled chemistry. Composition-window patents on 6xxx are weak because they are easy to design around (Report 6).
2. **Trade secrets** on the sorting-to-melt correction models and training data.
3. **Trademark first.** HSA6, CIRCAL and Castasil all sold under a trademark before registration.
4. **AA Teal Sheet / EN 573 registration** after 12 months of commercial supply, with a 30-day SCATR review. EN pick-up takes 2–4 years [est.]. Registration helps purchasing departments but does not create a premium.
5. **Invention disclosure process** from day 1, with every ML-designed candidate logged.

### 8.3 Pricing and premiums

| Product | Premium EUR/t | Source |
|---|---|---|
| Branded scrap-tolerant / high-recycled 6xxx billet or sheet | 50–200 | [est.] |
| High-strength crash extrusion (HSA6 type) | 150–400 | [est.] |
| Proprietary structural HPDC vs AlSi10Mg | 150–350 | [est.] |
| Conductor rod vs P1020 | 200–600 | [est.] |
| Al-Zr vs EC rod | 300–800 | [est.] |
| Carbon differential alone | $25–40/t only | Fastmarkets |

The carbon differential alone is too thin to build a case on. It must be bundled with recycled content and performance.

### 8.4 OEM joint development agreements

- Two or three JDAs: automotive or building extrusion, a Tier-1 megacaster, and a cable maker.
- The OEM owns application-specific IP. **We keep the composition and process IP.**
- The OEM gets **2–3 years of supply exclusivity** in return for co-funding qualification.
- The premium lasts for the platform's life, about 6–8 years.

### 8.5 Out-licensing

- Non-EU licensing follows the Alcoa C611 to CSMet template ([Business Wire](https://www.businesswire.com/news/home/20220913005251/en/Alcoa-announces-innovations-in-alloy-development-and-deployment)).
- Royalty is 1–10% of net sales, with an automotive average of about 3.3% ([UpCounsel](https://www.upcounsel.com:443/patent-licensing-royalty-rates)), so about EUR 60–140/t [est.].
- Target EUR 1–3M/yr from 2030.

### 8.6 Toll manufacturing for OEM-owned alloys

We act as qualified manufacturing partner for alloys the OEM owns, in the style of Apple's 100% recycled alloy ([Apple](https://www.apple.com/newsroom/2023/04/apple-will-use-100-percent-recycled-cobalt-in-batteries-by-2025/)). Opportunistic, at 5–20 kt per programme [est.].

### 8.7 EU funding to tap

| Instrument | Size / timing | Use |
|---|---|---|
| Horizon CL4-2027-01-MAT-PROD-22 (IAM4EU + Processes4Planet) | EUR 36M; **deadline 2 Feb 2027** | Scrap-to-property digital thread and AI alloy design. **Lead or co-lead** |
| MAT-PROD-23 (AI acceleration of materials discovery) | 2026–27 work programme | Informatics platform |
| MAT-PROD-01 (Made in Europe) | EUR 6–8M per project, up to 6 projects ([Ideal-ist](https://topictree.ideal-ist.eu/topic/7016)) | NHT structural alloy or conductor |
| DIGITAL-EMERGING-51/53 | Topic 51 drew 191 proposals, so heavy competition | Charge optimiser and AI in process industries; low priority |
| IPCEI-CAM | National calls open (Slovenia, Wallonia ([Wallonia](https://ecosysteme-economiecirculaire.wallonie.be/en/action-plan/ipcei-in-the-sector-of-advanced-circular-materials-for-clean-technologies-june-2026/))) | First industrial deployment: casthouse scale-up of scrap-based alloys, possibly the rod line |
| Advanced Materials Act; Horizon partnership 2028–34 (aims to cut time-to-market from 10–20 to 5–10 years ([FFG](https://www.ffg.at/sites/default/files/downloads/The-Future-of-Advanced-Materials-Research-and-Innovation-in-Europe.pdf))) | 2027+ | Position early |

**Grant stack target:** EUR 5–25M against a EUR 15–40M R&D and deployment programme [est.].

---

## 9. Risks and counter-moves

| # | Risk | Likelihood / impact | Counter-move |
|---|---|---|---|
| 1 | **Qualification takes longer than planned** (auto beyond 4 years) | High / High | Building extrusions and conductor rod come first (6–12 month qualification). OEM co-funded JDAs. Use the 18–20 month material-qualification path where possible (low confidence) |
| 2 | **Competitors get there first** (Hydro CREATe/FAST, Constellium CirConAl, Novelis, Speira SMS) | High / Medium | Speed of the integrated data chain. Seats on standards committees. Lock in customers with closed-loop scrap contracts. File process patents in 2027 |
| 3 | **Scrap spread compresses** (EU export levy of 15% is repeatedly delayed ([AlCircle](https://www.alcircle.com/news/eu-proposes-15-tax-on-aluminium-scrap-exports-to-secure-recycled-metal-supply-120114)); domestic competition for scrap) | Medium / High for A2 | An export levy would widen the spread in our favour. Test the case at 5 points (EUR 108/t), which gives A2 of about EUR 11M. The property-window charge optimiser keeps its value whatever the spread |
| 4 | **Chinese NHT alloy 15–20% cheaper** ([CS.com.cn](https://www.cs.com.cn/ssgs/gsxw/202305/t20230531_6347491.html)) | Medium / High for NHT | Sell low-CO2, EU origin, CBAM exposure, liquid-metal logistics and non-Russian ownership. Avoid commodity AlSi9Cu3 |
| 5 | **Cu/Al ratio falls below 4.0x** | Medium / Medium for B | Rod line is mainly for overhead lines, which are aluminium anyway. Index offtakes to LME. Stress case gives about EUR 17M/yr |
| 6 | **Rod line cannibalises billet premium** | Medium / High | Investment decision gated on through-cycle margin. Keep casthouse flexibility |
| 7 | **Data quality is poor or certificates are not linked to melts** | Medium / High | Data lake in the first 90 days. KPI of ≥80% linkage. FAIR budget of EUR 0.5–1M |
| 8 | **Weak IP** (composition easy to design around) | High / Medium | Process and control patents plus trade secrets. Value sits in the data chain, which cannot be copied without a sorting hub |
| 9 | **Standards stay tight** (EN 573/1706) | Medium / Medium | Bring qualified HRC chemistries into the committee. Sell under customer material specifications in the meantime |
| 10 | **Talent** (computational metallurgists and ML staff are scarce) | Medium / Medium | Hire through university partnerships (PhD/postdoc pipeline); remote ML roles; give the centre visible board sponsorship |
| 11 | **Double-counting across business cases** | Medium / Medium | 20% overlap haircut in A. A single scrap-tonnage ledger owned by the CFO |
| 12 | **AI hype drains budget** | Low / Medium | No spend on generative crystal models or autonomous LLM labs. Every model must link to a named product and customer |
| 13 | **Mg substitution in robotics; PEEK/CFRP** | Medium / Low | Robotics stays WATCH. Pitch Mg critical-raw-material risk and recyclability |

---

## 10. 90-day action plan (26 Oct 2026 to 23 Jan 2027)

**Budget:** EUR 1.9M opex, released by the CEO now.

| # | Owner (role) | Deliverable by day 90 | Budget (EUR k) | KPI |
|---|---|---|---|---|
| 1 | **CTO** | Charter for the Alloy Informatics & Design Centre; Head of Alloy Informatics hired or offer accepted; 4 FTE seconded internally; steering committee set up (monthly) | 250 | Lead in seat; 4 FTE active |
| 2 | **Chief Digital Officer / Head of Data** | Data lake v0: OES, process and certificate data 2019–26 for top 20 alloys, linked melt by melt; data dictionary shared with the hub sensor team | 300 | ≥80% of melts 2022–26 linked from chemistry to properties |
| 3 | **Head of Casthouse** | Charge-optimiser bake-off (SMS Metallics Optimizer vs GHI ALEA vs in-house prototype); shadow mode started on one furnace; outcome-based contract terms | 200 | Modelled saving of at least EUR 5/t; vendor selected |
| 4 | **Head of R&D Metallurgy** | Thermo-Calc TCAL11/MOBAL installed; first CALPHAD+ML screen of HRC 6063/6082 at Fe 0.4–0.8 with Mn/Cr; 20–30 trial casts booked (MPIE/Leoben/in-house) | 250 | ≥3 candidate chemistries, each with a predicted property window |
| 5 | **CSO + Head of Public Funding** | MAT-PROD-22 consortium signed (Leoben/RWTH/MPIE, plus one OEM and one sorter vendor); proposal at final draft (submit by 2 Feb 2027); IPCEI-CAM expression of interest filed in our member state | 150 | Consortium of ≥6 partners; proposal 90% complete |
| 6 | **Head of Sales, Extrusion & Rolled** | Three JDA term sheets: one building-systems customer, one auto OEM or Tier-1, one megacaster (Volvo Košice/Torslanda cluster) | 100 | ≥2 term sheets signed, with qualification co-funding agreed |
| 7 | **Head of Casthouse Products (Primary)** | Conductor market test: meetings with 6 cable makers; LOIs targeted; budget quote for a Properzi-type line; NHT structural alloy trial-lot offer | 150 | ≥1 LOI in hand, ≥2 more in negotiation; quote received |
| 8 | **CFO** | Integrated model for A, B and NHT with a single scrap-tonnage ledger; billet-vs-rod through-cycle analysis; Fastmarkets MB-AL-0426 Taint/Tabor subscription | 100 | Investment-decision pack template ready for Q2 2027 |
| 9 | **General Counsel / Head of IP** | Freedom-to-operate and patent landscape (C22C21 in WIPO/Espacenet, incl. Kaiser, Tesla, Alcoa, Rheinfelden, CN filers); invention-disclosure and trade-secret policy | 200 | FTO memo; ≥3 invention disclosures logged |
| 10 | **Head of Sorting Hub project** | Sorter specification updated: LIBS/XRF data schema feeding the casthouse model; Al-Li and Sc segregation channels; data-ownership clauses in vendor contracts | 50 | Specification change approved within the hub budget |
| 11 | **Head of Public Affairs / Standards** | Seats on CEN TC 132 and the EN 573 / EN 1706 revision working groups; contact with European Aluminium | 50 | Delegate nominated |
| 12 | **Head of Extrusion Operations** | Data-centre product scan: 1370/6101 busbar and manifold samples; target-account plan for Schneider, Vertiv, Siemens and ABB | 100 | Samples to ≥1 OEM |
| | **Total** | | **1,900** | **Day-90 executive review**: approve the 2027 budget (capability EUR 3.1M; case A EUR 9M) and set the investment-decision timetable for the rod line and NHT |

---

## 11. Evidence quality

### 11.1 Overall reliability

- **Method caveat.** All six reports note that direct fetches of most publisher, university and price-reporting sites failed. Most figures therefore come from search-indexed abstracts and press releases, not full documents.
- **Price data.** Fastmarkets scrap, rod and low-carbon assessments are largely paywalled. No proprietary-alloy price list is public.
- **Consequence.** Every premium in this memo is an estimate.

### 11.2 Sourced vs estimated

| Category | Status | Examples |
|---|---|---|
| AI design-speed evidence | **Sourced** (primary or press release) | MIT 40 vs >1M; Citrine 11.5M to 100; M54 about 6 yrs; GE 15 to 9; RidgeAlloy 15 months; Brunel 42 to 10; MPIE, AlloyBot, ARM-MIP throughput |
| Competitor programmes | **Sourced** | Hydro CREATe US$2.5M; CirConAl GBP 10M; CIRCAL 1.9 kg CO2e/kg; Novelis 63%; AMAG CrossAlloy properties; Speira SMS rollout |
| Market and macro | **Sourced, with some vendor reports of low reliability** | EU scrap exports 1.27 Mt; wire rod 8.32 Mt; EUR 584bn grids; WoodMac 0.6–0.9 Mt; Cu US$14,540/t; billet premium swings |
| Funding calls | **Sourced** | MAT-PROD-22 EUR 36M / 2 Feb 2027; MAT-PROD-01 EUR 6–8M |
| Alloy premiums EUR/t (all families) | **Estimated** | Cost build-ups and analyst ranges |
| Tonnages (NHT EU 250–400 kt, conductor rod 0.6–0.9 Mt, DC extrusions 40–80 kt, foil 100–300 kt) | **Estimated**, bottom-up | Press count × utilisation; capacity × intensity |
| 2035 tonnages | **CTO extrapolation**, unsourced | Section 3, marked (x) |
| Value scenarios (A2 EUR 17–26M; A1 EUR 1.5–4.5M; combined EUR 20–45M) | **Estimated** on the board grade-spread basis | Charge-optimiser vendors publish no EUR/t |
| Qualification times (auto 2–4 yrs; 18–20 months) | **Low confidence** | Source is an Alibaba blog summary |
| Capex for rod line, casthouse adaptation, NHT line, DC fabrication | **CTO estimates, not in the reports** | Must be quoted |
| Unconfirmed | ZwickRoell price about EUR 350k; China gigapress count (LinkedIn); PatSnap full report | |

### 11.3 Open data items with owners

| # | Item | Why it matters | Owner | Due |
|---|---|---|---|---|
| 1 | Rod-line capex and conversion cost (Properzi-type quote) | Case B investment decision | Head of Casthouse Products | Q1 2027 |
| 2 | Through-cycle billet premium vs rod margin | Cannibalisation test | CFO | Q1 2027 |
| 3 | Actual scrap grade prices (Fastmarkets Taint/Tabor MB-AL-0426; hub feed price curve) | A2 and A3 value | CFO + Head of Scrap Procurement | Day 60 |
| 4 | Linkage quality of our own historical chemistry-to-property data | Feasibility of the models | CDO | Day 90 |
| 5 | Casthouse adaptation capex for lower-grade scrap (furnace, melt treatment) | Case A investment | Head of Casthouse | Q1 2027 |
| 6 | Validated OEM qualification timelines and costs (direct OEM interviews) | Critical path | Head of Sales Extrusion & Rolled | Q1 2027 |
| 7 | Customer willingness to pay for recycled content and CIRCAL-equivalent pricing | A4 and B3 premiums | CSO | Q1 2027 |
| 8 | NHT alloy demand by EU programme (Volvo, Hyundai/Toyota suppliers, Tier-1s) | NHT sizing | CSO | Q1 2027 |
| 9 | Patent landscape and FTO (WIPO/Espacenet C22C21; Tesla US12378642 assignee unconfirmed) | IP strategy | General Counsel | Day 90 |
| 10 | EN 573 / CEN registration timing | Commercial path | Head of Standards | Q1 2027 |
| 11 | Overlap between A1, A2 and A3 on the same scrap tonnes | Avoid double-counting | CFO | Day 90 |
| 12 | Er/Yb cost and availability for Sc-lean alloys; EU CRMA strategic-project list | WATCH items 7 and Sc | Head of R&D Metallurgy | Q2 2027 |
| 13 | Robotic test-lab equipment quotes (ZwickRoell and others) | 2028 lab gate | CTO | Q3 2027 |
| 14 | Cu/Al stress case and data-centre aluminium share (CRU full report) | Case B sensitivity | CSO | Q1 2027 |

---

**Decisions requested from the Executive Committee today:**
1. Approve the EUR 1.9M 90-day budget.
2. Endorse the GO/WATCH/NO-GO portfolio in Section 4.
3. Authorise the MAT-PROD-22 bid as lead or co-lead.
4. Mandate investment-decision packs for the rod line and the NHT alloy line by Q2 2027.