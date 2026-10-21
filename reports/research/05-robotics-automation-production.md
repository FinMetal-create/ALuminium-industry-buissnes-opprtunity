## Robotics, AI & Automation in Aluminium Production

*Research swarm: production technology. As of 21 Oct 2026. Numbers marked [E] are my own estimates or calculations. Vendor and company claims are labelled as such.*

### 1. Executive summary

Automation in aluminium is no longer a single technology bet. It is a set of separate, proven use cases, each with its own payback. In order of economic value for an EU integrated producer:

1. **AI and sensor-based scrap sorting.** This is the largest new revenue pool. The EU exported a record **1.26 Mt of aluminium scrap in 2024** ([European Aluminium via Fastmarkets](https://www.fastmarkets.com/insights/eu-moves-to-restrict-aluminium-scrap-exports)), and the Commission is moving to restrict up to **~950 kt** of it ([AlCircle](https://www.alcircle.com/news/eu-aluminium-scrap-export-measure-delayed-as-commission-shifts-from-duty-to-non-oecd-restrictions-121153)). Sorting is what turns that scrap into low-carbon wrought alloy.
2. **AI process control and energy flexibility in the potroom.** Power is roughly 35% of smelter cost. **A 1% cut in power use is worth about USD 4–5 M a year at a 1 Mt smelter** ([AlCircle case study](https://www.alcircle.com/blog/case-study-improving-aluminium-smelter-efficiency-with-explainable-ai-and-digital-twins)). Flexible potlines can also earn money in volatile EU power markets.
3. **Robotics for hazardous potroom and casthouse tasks** (anode change, skimming, tapping, furnace cleaning). The case rests mainly on safety, labour and consistency. It is now commercial but has not yet scaled.
4. **Downstream automation** (extrusion, rolling, finishing): machine vision, robotic handling and predictive maintenance. These are mature technologies, applied incrementally.

The clearest proof that this pays is **EGA**: more than **80 AI/Industry 4.0 use cases**, a reported **USD 100–123 M of financial impact**, **+12% throughput and +18% labour productivity** ([WAM 2026](https://www.wam.ae/en/article/c11afzq-ega-wins-%E2%80%98ai-vision-and-strategy-award%E2%80%99-2026); [AlCircle](https://www.alcircle.com/blog/case-study-ega-leading-the-aluminium-industry-with-ai-powered-transformation)). There is also a precedent for automation as a business line: Hydro's subsidiary **Hycast** sells casthouse technology to third parties, for example a **NOK 200 M contract with China's Innovation Group** and **EUR 9.7 M with Alu Iberica** ([AlCircle](https://alcircle.com/news/hydro-signs-nok-200-million-contract-with-innovation-group-for-casthouse-technology-66386); [Aluminium Today](https://aluminiumtoday.com/news/hycast-wins-contract-to-deliver-state-of-the-art-technology-to-spanish-aluminium-company-alu-iberica)).

---

### 2. Potroom robotics: anode change, crust breaking, cranes

**Status.** In most smelters, anodes are still changed with a manually operated pot tending machine (PTM). Rio Tinto notes that **several hundred anodes are changed every day in each smelter** ([ICSOBA 2022, Rio Tinto](https://icsoba.org/assets/files/publications/2022/Papers/AL10%20-%20Aluminium%20Electrolysis%20Cells-%20Anode%20Changing%20Automation%20Challenges.pdf)). The work is hot, exposed to fluoride and strong magnetic fields, and is one of the most dangerous jobs on the site.

**Vendors and deployments**
- **AlumatIQ** (Mosjøen, Norway; SINTEF-backed) makes a robot cell that covers the whole anode-change sequence: hood handling, crust breaking, anode change and covering. The company's own claims are that a change drops from **25 to 15 minutes per anode** and from **three operators to one**, and that consistent execution avoids placement errors which today take **24–72 h** to show up in pot control ([SINTEF](https://sintef.no/en/projects/2020/alumatiqanodeskifterobot); CEO interview cited via [Mining Technology](https://www.mining-technology.com/features/robot-smelting-automation-reshaping-aluminium-production/)). These figures are unverified.
- **Fives ECL** offers PTM automation and an "Embedded Service Robot" for hood handling ([ICSOBA 2015](https://icsoba.org/assets/files/publications/2015/Papers/AL09%20-%20Embedded%20service%20robot%20-%20towards%20an%20automated%20efficient%20and%20green%20smelter.pdf)), and the SMARTCrane monitoring system ([Springer](https://link.springer.com/chapter/10.1007/978-3-031-50308-5_73)). Fives supplied **14 new multi-functional cranes to EGA Jebel Ali** (full fleet by early 2025). EGA's roadmap goes from remote operation in a central control room to full autonomy ([Gulf Industry](https://gulfindustryonline.com/Article/18164/EGA_makes_major_move_towards_full_crane_automation)).
- **REEL** (brands Alesa, NKM Noell, Möller) sells potroom cranes with supervisory software that automates crane sequences and zone access ([REEL 2025 brochure](https://www.reelinternational.com/wp-content/uploads/2025/09/Brochure-REEL-Aluminium-EN-2025.pdf)).
- **Qatalum** (a Hydro joint venture) automated cover handling across **704 pots** ([Qatalum](https://www.qatalum.com/Media/News/Pages/Qatalum,-only-smelter-in-the-world-to-use-automated-Cover-Handlers.aspx)). **Rio Tinto** has robotic anode-yoke repair at Tiwai Point and ran machine-vision PTM pilots at AP60 Jonquière.
- **Autonomous logistics.** ECA Group (now Exail) demonstrated an AGV for heavy smelter loads with Rio Tinto ([Exail](https://www.exail.com/news/eca-group-successfully-demonstrates-automated-guided-vehicle-agv-system-for-aluminium-smelters)).

**Economics [E].** Take a 200 kt/y EU smelter with about 300 pots and ~235 anode changes a day. At the vendor's stated figures, labour drops from about 290 to about 60 person-hours a day. That is roughly **50–55 FTE, or about EUR 3.5–4.5 M a year** at EUR 70–80k fully loaded cost per FTE. The estimate excludes the value of fewer anode-placement errors and less fluoride exposure.

**Strategic caveat.** **ELYSIS started its first commercial-size 450 kA inert-anode cell at Alma in Nov 2025** ([Mining Weekly](https://www.miningweekly.com/article/major-step-forward-for-emissions-free-aluminium-smelting-2025-11-14)). If inert anodes scale, anode changing largely disappears. For EU brownfield potlines, however, carbon anodes are likely to stay in use until the late 2030s [E]. Robotic anode change is therefore a **10–15-year asset**, not a permanent franchise. It should be bought or co-developed, not built from scratch.

---

### 3. AI process control, digital twins and energy flexibility

- **Energy baseline.** Real smelters use **13.5–15.0 kWh/kg** of aluminium ([AlCircle](https://www.alcircle.com/blog/case-study-improving-aluminium-smelter-efficiency-with-explainable-ai-and-digital-twins)). Hydro's Karmøy pilot reached **12.27 kWh/kg**, with HAL4e Ultra cells at a potential **11.8** ([Hydro](https://hydro.com/en/media/news/2020/hydro-karmoy-technology-pilot-successfully-verified)). That gap shows how much value good control can unlock.
- **AI results reported**
  - One AI anode-effect and digital-twin deployment (smelter not named) saved **137 kWh/t of energy** and cut anode-effect frequency by **32.5%** over six months ([AlCircle](https://www.alcircle.com/news/ai-in-aluminium-smelters-is-your-smelters-digital-twin-about-to-fail-120266)).
  - An explainable-AI case reported **ROI in 2.5 months** (same source family).
  - Alba expanded its AI pot-line work with **ARRAY Innovation** in Nov 2025, covering bath temperature, energy and pot life ([AlCircle](https://www.alcircle.com/press-release/alba-expands-collaboration-with-array-innovation-to-include-advanced-data-modelling-and-ai-on-pot-lines-for-enhanced-efficiency-and-safety-116061)).
  - Hindalco presented AI anode-effect prediction at ICSOBA 2025 ([ICSOBA](https://icsoba.org/assets/files/publications/2025/Papers/AL52%20-%20AI-Driven%20Anode%20Effect%20Prediction%20in%20Hindalco%20Renukoot%20Smelter.pdf)).
  - RUSAL is putting machine vision into 5 smelters (about RUB 1.6 bn). Billet quality assessment fell from **4 h to 15 min** ([AlCircle](https://www.alcircle.com/news/rusal-implements-artificial-intelligence-at-aluminium-smelters-110877)).
- **What the 137 kWh/t saving means for us [E].** At a 200 kt smelter that is about **27 GWh a year, or ~EUR 1.6 M a year at EUR 60/MWh**. It also lowers PFC emissions, which reduces ETS and CBAM-related exposure.
- **Energy flexibility (the "virtual battery").**
  - **TRIMET Essen** converted 120 cells to modulate load by **±25% for up to 48 h**, about **1,120 MWh** of virtual storage, using EnPot shell heat exchangers ([Light Metal Age](https://www.lightmetalage.com/news/industry-news/smelting/trimet-starts-trial-operation-of-its-virtual-battery/)). EnPot claims **±20–30%** modulation ([ICSOBA 2022](https://icsoba.org/assets/files/publications/2022/Shorts/ST03S%20-%20Decarbonisation%20of%20Aluminium%20Production%20by%20Demand%20Side%20Response.pdf)).
  - **ACER expects Europe to need 2.4x today's flexibility by 2030** ([European Aluminium DSR paper, May 2025](https://european-aluminium.eu/wp-content/uploads/2025/05/2025-05-27-European-Aluminium-Position-Paper-on-Demand-Side-Response.pdf)).
  - The natural next step is AI that optimises bath heat balance against intraday and day-ahead prices ([ICSOBA 2025 AL68](https://icsoba.org/assets/files/publications/2025/Papers/AL68%20-%20Electricity%20Market%20Driven%20Optimisation%20of%20Aluminium%20Smelting%20Operations.pdf)). Talum (Slovenia) and the University of Maribor have already modelled solar-surplus absorption ([MDPI 2024](https://www.mdpi.com/2076-3417/14/22/10108/html)).

---

### 4. Casthouse robotics

- **Skimming, stirring and furnace cleaning.**
  - Vision- and force-controlled battery robots from **Dynamic Concept with EPIQ Machinery** ([ICSOBA 2022](https://icsoba.org/assets/files/publications/2022/Papers/AL13%20-%20Automation%20of%20Furnace%20Tending-%20ARFT%20Technology.pdf); [AlCircle](https://www.alcircle.com/press-release/dynamic-concept-and-epiq-machinery-enter-into-a-partnership-to-promote-an-advanced-robotic-solution-for-aluminium-casthouses-83271)).
  - **RiA** rail-mounted charge and skim machines, now using AI and camera-based remote operation ([ICSOBA 2023](https://icsoba.org/assets/files/publications/2023/Papers/CH06%20-%20Safe,%20Autonomous,%20and%20Energy%20Efficient%20Furnace%20Tending,%20Minimizing%20Waste.pdf)).
  - Hydro's Cassopolis (US) recycling casthouse includes an **AI-aided dross-skimming robot** ([GIFA](https://www.gifa.com/en/Media_News/News/Company_News/Hydro_8216_s_new_casthouse_in_Cassopolis,_Michigan)).
- **Casting automation.** **Hycast** sells automated casting lines designed to keep operators away from molten metal, and is developing an under-table camera system ([AlCircle interview](https://www.alcircle.com/news/interview/we-have-a-new-product-which-we-will-launch-later-this-year-its-a-camera-system-which-runs-underneath-the-casting-table-ola-furu-august-riise-from-hyca-95128)).
- **Value [E].** Consistent skimming lowers dross and metal loss. A 0.2–0.5 percentage-point melt-loss reduction on 300 kt/y of remelt is **600–1,500 t of metal a year, or EUR 1.4–3.5 M**. Most of the safety value (molten-metal incidents) is not counted in that figure.

---

### 5. Robotic scrap sorting (LIBS, XRF/XRT, AI vision)

This is the most commercially important area, because it decides whether EU low-carbon wrought products can be made from post-consumer scrap.

| Vendor / player | Technology | Performance (source) |
|---|---|---|
| TOMRA AUTOSORT PULSE | Dynamic LIBS, 4 lasers | >95% purity on 5xxx/6xxx. **4–7 t/h** in real operation at Gerhard Lang, against a 15 t/h nameplate ([TOMRA](https://tomra.com/waste-metal-recycling/products/machines/autosort-pulse); [AlCircle](https://www.alcircle.com/blog/recycling-technologies-driving-europes-aluminium-circularity-and-lowering-primary-metal-dependence)) |
| Steinert PLASMAX | LIBS plus XRT pre-sort | >95% purity; **3–6 t/h** reported, up to 11 t/h claimed ([Steinert](https://steinertglobal.com/sorting-systems/sensor-sorting/libs-sorting-systems/steinert-plasmax-libs/); [Hub-4](https://hub-4.com/news/a-new-benchmark-for-sorting-aluminium-alloys)) |
| Hydro HySort | In-house LIBS | Nowa Sól (PL) added 2 HySort units in 2025 at a 120 kt/y sorting hub ([Hydro](https://integration.hydro.com/en/global/about-hydro/hydro-worldwide/europe/poland/nowa-sol/hydro-aluminium-nowa-sol/)). US JV Alusort with PADNOS: Hydro invested USD 4 M for its 50%, up to 20 kt/y ([Light Metal Age](https://www.lightmetalage.com/news/industry-news/recycling-remelt/hydro-and-padnos-to-pioneer-new-scrap-sorting-technologies-for-the-u-s-market/)) |
| Sortera (Novelis-backed) | XRF plus AI vision | Markle, IN: about **220 M lb (~100 kt)/y**; USD 30.5 M Series C in 2023 ([SP-Edge](https://sp-edge.com/companies/1720921)) |
| Constellium | LIBS-sorted automotive scrap | >95% purity; processed at Neuf-Brisach ([TipRanks/The Fly](https://www.tipranks.com/news/the-fly/constellium-sorts-automotive-aluminum-scrap-with-libs-technology)) |
| AMP Robotics / Greyparrot | AI vision and robotic picking | AMP raised a USD 91 M Series D in Dec 2024. Greyparrot received Bollegraaf's AI unit plus about USD 12.8 M; Bollegraaf says ~40% of waste sorting is still manual ([letsrecycle](https://www.letsrecycle.com/news/greyparrot-and-bollegraaf-agree-10-1m-strategic-partnership)) |

**Volumes.** Post-consumer aluminium scrap in Europe is projected to rise from **3.6 Mt (2019) to 8.6 Mt (2050)** ([Circular Aluminium Action Plan](https://www.resourcemedia.eco/article/european-circular-aluminium-action-plan-launched)). Meanwhile, about **15% of EU recycling capacity is offline for lack of feedstock** ([Kitco/Reuters, Nov 2025](https://www.kitco.com/news/off-the-wire/2025-11-18/eu-plans-curb-exports-aluminum-scrap)).

**Economics [E]**
- A 50 kt/y sorting line needs about 8 t/h of effective throughput, or **2–3 LIBS units plus XRT, eddy-current and shredding pre-processing**. Total capex is roughly **EUR 10–20 M**.
- Sorted wrought fractions can earn an estimated **EUR 150–400/t** over mixed shredded or Twitch. A historical reference point is the ~€100/t spread between castings scrap and taint/tabor ([Argus](https://www.argusmedia.com/en/news-and-insights/latest-market-news/1803797-twitch-oversupply-weighs-on-aluminium-scrap-in-europe)). The larger gain comes from **replacing purchased primary metal or slab** in our own rolling and extrusion. On that basis I estimate the line pays back in about 3–5 years.

---

### 6. Lights-out extrusion, rolling and finishing

- **Extrusion.** SMS **HybrEx** (servo-hybrid press) claims **up to 55% less energy and up to 20% more productivity**; Hydro took a 25 MN unit in 2025 ([AlCircle](https://www.alcircle.com/news/germany-aluminium-extrusion-technology-advances-with-gunther-wensing-h-h-herrmann-hieber-kind-co-discover-the-key-technologies-121233)). Robotic sawing and stacking is available from IMA Schelling and Mössner, and automatic marking and strapping is spreading. Inline AI vision for speed tears and surface defects is offered by Matroid and CYRUS ([Wevolver](https://www.wevolver.com/article/transforming-aluminum-extrusion-matroids-advanced-computer-vision-solutions-for-enhanced-quality-control-and-industry-efficiency)).
- **Predictive maintenance.** Commonly quoted ranges are **30–50% less downtime** (McKinsey, as cited by others) and **8–12% lower maintenance cost than preventive maintenance** (US DOE) ([Zerynth summary](https://zerynth.com/blog/predictive-maintenance-and-data-analysis-for-metal-production-plants/)). Hydro's EU CogniTwin project built a digital twin of a smelter gas treatment centre ([Tekna](https://tekna.no/en/professional-areas/it-and-telecommunications/it-blog/digital-twin-solutions--example-of-application-in-process-industry)).
- **Humanoids.** These are still at pilot stage. Figure 02 loaded **90,000 parts over 1,250 h in an 11-month BMW pilot** ([Automate](https://www.automateshow.com/blog/humanoid-robots-in-manufacturing-the-state-of-industrial-humanoid-robots-in-2026)). I found no deployment in aluminium. The realistic window for packing, inspection and logistics tasks in finishing halls is 2029 or later [E].
- **Context.** EU-27 robot density is **231 per 10,000 employees** (Germany 449) ([IFR 2026](https://ifr.org/ifr-press-releases/robot-density-surges-in-europe-asia-and-americas)). Aluminium Deutschland reports labour shortages alongside cost-driven job cuts ([AlCircle](https://www.alcircle.com/news/aluminium-deutschland-remains-cautiously-optimistic-amidst-high-energy-prices-and-labour-shortages-107924)), so automation is a cost and competitiveness lever, not only a response to staff scarcity.
- **Funding.** The EU **Apply AI Strategy** includes AI-robotics funding paths from Q4 2025 and an **EUR 18 M Horizon call for AI robotics in manufacturing** ([Futurium](https://futurium.ec.europa.eu/en/node/17584)).

---

### 7. Key numbers

| Metric | Value | Source |
|---|---|---|
| EGA AI/Industry 4.0 impact | USD 100–123 M; 80+ use cases; +12% throughput, +18% labour productivity | WAM 2026, AlCircle |
| Smelter energy, real operations | 13.5–15.0 kWh/kg | AlCircle |
| Value of 1% power saving, 1 Mt smelter | USD 4–5 M/y | AlCircle |
| AI anode-effect / digital-twin result | -137 kWh/t; -32.5% anode effects | AlCircle |
| Robotic anode change (vendor claim) | 25 to 15 min; 3 to 1 operators | AlumatIQ |
| TRIMET virtual battery | ±25% for 48 h; ~1,120 MWh | Light Metal Age |
| EU scrap exports 2024 | 1.26 Mt (record) | European Aluminium |
| LIBS sorting, real throughput | 3–7 t/h per unit; >95% purity | TOMRA, Steinert |
| EU post-consumer scrap | 3.6 Mt (2019) to 8.6 Mt (2050) | CAAP |
| HybrEx extrusion press | up to -55% energy, +20% productivity | SMS via AlCircle |
| EU-27 robot density | 231 per 10k employees | IFR |

---

### 8. So what for our company

1. **Build an AI-sorting scrap hub (first priority).** Pair LIBS/XRT lines (TOMRA or Steinert) with our own AI layer on scrap chemistry, and feed the output directly into our casthouse. EU scrap export restrictions will push more scrap back onto the EU market, so **closed-loop sorting capacity built in 2026–2028 has a first-mover advantage**. Partner with one or two large scrap dealers or shredders in a JV, following the Hydro/PADNOS Alusort model.
2. **Run a potroom "AI + flex" programme.** Adopt AI pot control (ARRAY-type or in-house), retrofit EnPot-style heat exchangers, and sell flexibility to TSOs. Indicative value is EUR 3–8 M/y per 200 kt smelter [E], with low capex.
3. **Co-develop robotics, do not build it.** Take a minority stake or a development partnership with AlumatIQ (potroom) and Dynamic Concept or RiA (casthouse) and serve as their EU reference site. Negotiate a royalty share when they sell to third parties.
4. **Treat automation as a business line.** Following the Hycast model, package proven solutions (sorting recipes, alloy digital twin, flex optimiser) as a technology and service unit for other EU casthouses and remelters. This is optional; a credible offer needs 2–3 years of proven use in our own plants first.
5. **Hedge the inert-anode risk.** Size anode-robotics investments for payback within 5 years [E]. Keep an ELYSIS licensing watch.

### Key numbers

| Metric | Value | Source |
|---|---|---|
| EGA financial impact from AI/Industry 4.0 use cases | USD 100-123 M from 80+ use cases; +12% throughput, +18% labour productivity | https://www.wam.ae/en/article/c11afzq-ega-wins-%E2%80%98ai-vision-and-strategy-award%E2%80%99-2026 ; https://www.alcircle.com/blog/case-study-ega-leading-the-aluminium-industry-with-ai-powered-transformation |
| Real smelter energy consumption | 13.5-15.0 kWh/kg Al (Hydro Karmøy pilot: 12.27; HAL4e Ultra potential 11.8) | https://www.alcircle.com/blog/case-study-improving-aluminium-smelter-efficiency-with-explainable-ai-and-digital-twins ; https://hydro.com/en/media/news/2020/hydro-karmoy-technology-pilot-successfully-verified |
| Value of 1% power reduction at a 1 Mt smelter | USD 4-5 M per year (power is ~35% of cost) | https://www.alcircle.com/blog/case-study-improving-aluminium-smelter-efficiency-with-explainable-ai-and-digital-twins |
| AI anode-effect / digital twin result (smelter not named) | -137 kWh/t energy; -32.5% anode-effect frequency over 6 months | https://www.alcircle.com/news/ai-in-aluminium-smelters-is-your-smelters-digital-twin-about-to-fail-120266 |
| Robotic anode change performance (vendor claim) | 25 to 15 min per anode; 3 to 1 operators | AlumatIQ CEO via https://www.mining-technology.com/features/robot-smelting-automation-reshaping-aluminium-production/ ; https://sintef.no/en/projects/2020/alumatiqanodeskifterobot |
| Labour saving from robotic anode change, 200 kt smelter | ~50-55 FTE, ~EUR 3.5-4.5 M/y (own estimate) | Own estimate based on AlumatIQ claims |
| TRIMET Essen virtual battery | ±25% load for up to 48 h; ~1,120 MWh storage equivalent; 120 cells | https://www.lightmetalage.com/news/industry-news/smelting/trimet-starts-trial-operation-of-its-virtual-battery/ |
| EnPot modulation capability | ±20% (up to ±30% with process changes) | https://icsoba.org/assets/files/publications/2022/Shorts/ST03S%20-%20Decarbonisation%20of%20Aluminium%20Production%20by%20Demand%20Side%20Response.pdf |
| EU flexibility need by 2030 (ACER) | 2.4x current flexibility resources | https://european-aluminium.eu/wp-content/uploads/2025/05/2025-05-27-European-Aluminium-Position-Paper-on-Demand-Side-Response.pdf |
| EU aluminium scrap exports 2024 | 1.26 Mt (record, +50% vs 5 years earlier); up to ~950 kt targeted by restrictions | https://www.fastmarkets.com/insights/eu-moves-to-restrict-aluminium-scrap-exports ; https://www.alcircle.com/news/eu-aluminium-scrap-export-measure-delayed-as-commission-shifts-from-duty-to-non-oecd-restrictions-121153 |
| LIBS alloy sorter real-world throughput and purity | 3-7 t/h per unit; >95% purity on 5xxx/6xxx | https://tomra.com/waste-metal-recycling/products/machines/autosort-pulse ; https://hub-4.com/news/a-new-benchmark-for-sorting-aluminium-alloys |
| Hydro Nowa Sól sorting hub | 120 kt/y sorting capacity; 2 HySort LIBS units added in 2025 | https://integration.hydro.com/en/global/about-hydro/hydro-worldwide/europe/poland/nowa-sol/hydro-aluminium-nowa-sol/ |
| Sortera (Novelis-backed) AI/XRF sorting capacity | ~220 M lb (~100 kt) per year at Markle, IN | https://sp-edge.com/companies/1720921 |
| European post-consumer Al scrap availability | 3.6 Mt (2019) to 8.6 Mt (2050) | https://www.resourcemedia.eco/article/european-circular-aluminium-action-plan-launched |
| SMS HybrEx extrusion press | Up to -55% energy, up to +20% productivity | https://www.alcircle.com/news/germany-aluminium-extrusion-technology-advances-with-gunther-wensing-h-h-herrmann-hieber-kind-co-discover-the-key-technologies-121233 |
| RUSAL machine vision billet QA | Assessment time 4 h to 15 min; ~RUB 1.6 bn across 5 smelters | https://www.alcircle.com/news/rusal-implements-artificial-intelligence-at-aluminium-smelters-110877 |
| Predictive maintenance benefit | 30-50% less downtime; 8-12% cost saving vs preventive | https://zerynth.com/blog/predictive-maintenance-and-data-analysis-for-metal-production-plants/ (citing McKinsey, US DOE) |
| EU-27 robot density | 231 robots per 10,000 employees (Germany 449) | https://ifr.org/ifr-press-releases/robot-density-surges-in-europe-asia-and-americas |
| Hycast external casthouse technology contracts | NOK 200 M (Innovation Group, China); EUR 9.7 M (Alu Iberica) | https://alcircle.com/news/hydro-signs-nok-200-million-contract-with-innovation-group-for-casthouse-technology-66386 ; https://aluminiumtoday.com/news/hycast-wins-contract-to-deliver-state-of-the-art-technology-to-spanish-aluminium-company-alu-iberica |
| ELYSIS inert anode milestone | First commercial-size 450 kA cell started at Alma, Nov 2025 | https://www.miningweekly.com/article/major-step-forward-for-emissions-free-aluminium-smelting-2025-11-14 |

### Scored opportunities

| Opportunity | Score | Model | Capex | Time | Risk | Market |
|---|---|---|---|---|---|---|
| **AI-enabled alloy sorting and scrap upgrading hub (closed loop into own casthouse)**: Build one or more 50-100 kt/y sorting hubs combining shredding, eddy current, XRT and LIBS (TOMRA/Steinert or licensed tech) plus our own AI scrap-chemistry and blending layer, feeding sorted 5xxx/6xxx fractions directly into our casthouse for low-carbon wrought products. Run as a JV with large EU scrap dealers or shredders (Hydro/PADNOS Alusort model). Timed to benefit from EU scrap export restrictions that will put more scrap back onto the EU market. | 9 | Build + JV/partner (with scrap dealers and sorting OEMs); captive offtake plus sale of sorted fractions | medium | 1-2 years | medium | EU scrap exports 1.26 Mt in 2024 (up to ~950 kt targeted by restrictions); EU post-consumer scrap 3.6 Mt (2019) rising to 8.6 Mt (2050); ~15% of EU recycling capacity idle for lack of feedstock (2025) |
| **Potroom 'AI + Flex': AI pot control and monetised energy flexibility**: Deploy AI/explainable-AI pot control (bath temperature, AlF3 feeding, anode-effect prediction) and digital twins across potlines. Retrofit EnPot-type shell heat exchangers to modulate load by ±20-25%, and use an AI optimiser to schedule power use against day-ahead and intraday prices and sell balancing and demand-response services to TSOs. | 8 | Adopt (buy software/retrofit, partner with ARRAY Innovation/EnPot-type vendors), sell flexibility services | low | 1-2 years | low | Indicative EUR 3-8 M/y per 200 kt smelter (own estimate): ~1% energy saving (~EUR 1.6 M/y) plus flexibility revenue; ACER expects 2.4x EU flexibility need by 2030; TRIMET Essen ~1,120 MWh virtual storage |
| **Co-development and minority stake in potroom and casthouse robotics**: Become the EU reference site for robotic anode change (AlumatIQ), PTM/crane remote and autonomous operation (Fives, REEL) and robotic furnace skimming and cleaning (Dynamic Concept/EPIQ, RiA). Take a minority equity stake or development agreement with royalties on third-party sales. Payback must stay within ~5 years because inert anodes (ELYSIS) could eliminate anode changing from the late 2030s. | 7 | Partner / co-develop / minority investment (venture-style) plus adoption | medium | 3-5 years | medium | Own estimate: ~50-55 FTE / EUR 3.5-4.5 M/y labour saving per 200 kt smelter from anode-change robotics; 0.2-0.5 pp melt-loss reduction in casthouse = EUR 1.4-3.5 M/y per 300 kt remelt; global addressable base ~200 smelters |
| **Lights-out extrusion and finishing cells with machine vision and predictive maintenance**: Upgrade extrusion plants with servo-hybrid presses (e.g. SMS HybrEx), robotic sawing, stacking and strapping, AGVs, inline AI surface-defect vision and plant-wide predictive maintenance, aiming at unmanned night shifts. Target the highest-cost EU sites first. | 7 | Adopt / build with OEM partners (SMS, IMA Schelling, Mössner, vision start-ups) | medium | 1-2 years | low | HybrEx: up to -55% energy, +20% productivity (vendor); predictive maintenance 30-50% less downtime, 8-12% lower maintenance cost; EU-27 robot density 231/10k employees |
| **Spin-out industrial AI and automation technology business (Hycast-style)**: Once solutions are proven in our own plants (sorting recipes, alloy-blending digital twin, flex optimiser, casthouse vision), package them as a technology and service unit sold to EU remelters, casthouses and smelters, and to fast-growing Middle East and Asian producers. Model: Hydro's Hycast, which sells casting technology externally, with China its biggest market. EU Apply AI and Horizon robotics calls can co-fund development. | 6 | Sell service / license software and technology packages | low | 3-5 years | medium | Precedent contracts: Hycast NOK 200 M (Innovation Group) and EUR 9.7 M (Alu Iberica); EGA's own AI programme USD 100-123 M impact shows willingness to pay; EUR 18 M Horizon AI-robotics manufacturing call |
| **General-purpose and humanoid robot pilot programme for finishing and logistics**: Run a low-cost watching brief and pilot of humanoid and mobile manipulators (Figure, Unitree, Agility and similar) for packing, inspection and intralogistics in finishing halls. The aim is to learn early and own task data, not to earn near-term returns. | 4 | Partner / pilot (adopt later) | low | 5-10 years | high | Figure 02 at BMW: 90,000 parts over 1,250 h in an 11-month pilot; no aluminium deployments found as of 2026; realistic scale-up 2029+ (own estimate) |
