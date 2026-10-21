## Robotics, Humanoids & Drones as Aluminium Demand

*Research swarm, robotics specialist. As of 21 Oct 2026. Method note: direct page fetches were blocked by the network proxy in this session, so the figures below come from web-search extracts of the cited pages. Anything marked **[est.]** is my own estimate or model and not a published figure.*

### 1. Executive summary

- **Humanoids are the only robotics segment that matters for tonnage.** Industrial robots, cobots, AMRs, exoskeletons, drones and eVTOL together are probably **<100 kt Al/yr** through 2030 **[est.]**. Humanoids could reach **~0.15 Mt by 2035 and ~0.7 Mt (range 0.2–1.8 Mt) of net aluminium content by 2040** **[est.]**. CRU's long-run case is **~10 Mt/yr by 2050** ([CRU](https://www.crugroup.com/en/communities/thought-leadership/2025/the-next-commodity-battleground-humanoid-robots/)).
- **Robotics is about value, not volume.** Even in the bull case it is around 1% of global aluminium demand by 2040. But robot parts are precision-machined housings, high-strength tubes and thermal parts that sell for **€20–80/kg finished** **[est.]**, against roughly €2.5–3.5/kg for ingot. The money is in becoming a **component and semi-finished supplier to actuator makers**, not in selling more metal.
- **Aluminium is the default structural material today.** CRU puts it at **17–25 kg per humanoid**, the biggest single material by weight. Steel dominates gearboxes and screws. Magnesium, CFRP and PEEK compete at the edges. The EU sources **~97% of its magnesium from China** ([Argus](https://www.argusmedia.com/ja/news-and-insights/latest-market-news/2431861-market-weighs-up-eu-s-magnesium-sourcing-targets)), so supply security works for an EU aluminium supplier.
- **2025 was the year humanoids proved demand was real but small.** About **13–18k humanoids were sold globally**, ~90% by Chinese firms ([Interesting Engineering / Omdia, IDC](https://interestingengineering.com/research/the-humanoid-robot-reality-check)). Unitree shipped **>5,500** and AgiBot **5,168**. Tesla's Optimus output is still minimal.

### 2. Aluminium content per unit

| Robot class | Typical mass | Al content (net, in product) | Main Al product forms | Source / basis |
|---|---|---|---|---|
| Humanoid (Optimus / Figure 03 class) | ~60 kg (Figure 03 ≈ 61 kg) | **17–25 kg** structural (CRU). **20–30 kg** incl. actuator/motor housings, battery enclosure, heat sinks **[est.]** | 6061/7075 machined billet and plate, HPDC and semi-solid castings, high-strength extruded tubes, forgings | [CRU](https://www.crugroup.com/en/communities/thought-leadership/2025/the-next-commodity-battleground-humanoid-robots/), [nextpit](https://www.nextpit.de/news/figure-03-wie-humanoide-roboter-bald-die-hausarbeit-uebernehmen) |
| Small humanoid (Unitree G1 class) | ~35 kg | 8–15 kg **[est.]** | Die castings, CNC parts | [est.] |
| Cobot (UR10e class) | 33.5 kg incl. cable | 12–20 kg **[est.]** (aluminium tube and cast joint housings) | Extruded tube, castings, machined housings | [UR datasheet](https://www.universal-robots.com/media/1826690/01_2023_collective_data_sheet.pdf) |
| Industrial 6-axis robot | 50 kg – 1.5 t | 20–80 kg avg **[est.]**. Cast iron for heavily loaded housings, cast Al for dynamic arm parts | Sand/gravity castings, machined parts | [KUKA via Red Dot](https://red-dot.org/project/kr-270-r2700-ultra-29875) |
| AMR / warehouse robot | 50–500 kg | 10–40 kg **[est.]** | Extruded chassis, sheet, castings | [est.] |
| AS/RS grid and shuttle systems | per site | tens to hundreds of tonnes per site **[est.]** | Structural extrusions | [est.], needs verification |
| Exoskeleton | 3–15 kg | 1–5 kg **[est.]** | Tubes, forgings, machined parts | [est.] |
| FPV / small military drone | 0.5–3 kg | 0.05–0.3 kg (motor bells, mounts). Frames are mostly CFRP **[est.]** | 7075 machined parts | [est.] |
| eVTOL | 1.5–3 t | 100–300 kg **[est.]**. Airframes are CFRP-dominated | 2xxx/7xxx plate, forgings | [Stratview/CW](https://www.compositesworld.com/news/stratview-research-launches-2025-report-on-evtol-dynamics) |

**Buy-to-fly matters.** Much of a humanoid's aluminium is CNC-machined from billet or plate. Humanoid-supply-chain analyses note that Tesla supplier Xusheng machines Optimus joint housings ([humanoid.guide](https://humanoid.guide/?p=18163)). Semi-finished demand is therefore **1.5–3× net content** **[est.]**, which means a large flow of clean, alloy-segregated machining chips to recycle.

**Where the aluminium sits in a humanoid [est., based on CRU, IDTechEx, Goodfellow]:**
- Torso and pelvis structure: 6061 / 7xxx machined or cast, ~6–9 kg.
- Limb links and tubes: high-strength extrusions or forgings, ~5–8 kg.
- Rotary and linear actuator housings plus motor housings: ~28–40 actuators per robot, ~0.1–0.3 kg each, ~4–8 kg in total.
- Battery enclosure and thermal plates: ~2–4 kg.
- Hands and fine parts: small amounts.

Actuators make up **~56% of humanoid BOM cost**. Steel dominates the gear and screw internals, with aluminium in the housings ([Morgan Stanley via gondola](https://gondola.cc/posts/69265942-benzinga-youtube); [IDTechEx actuators](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)). Agility's Digit already markets "aerospace-grade aluminium" arms ([ALCircle](https://www.alcircle.com/news/agility-robotics-showcases-digit-featuring-aerospace-grade-aluminium-at-promat-2023-97720)). Korea's Samkee was selected in June 2026 to develop an **aluminium die-cast upper-body frame** for a humanoid ([ALCircle](https://www.alcircle.com/news/samkee-chosen-to-develop-lightweight-humanoid-robot-aluminium-die-casting-to-play-a-key-role-120046)). That points to a shift from machined billet towards near-net casting as volumes grow.

### 3. Unit forecasts

**Humanoids (annual production):**
- **2025 actual:** ~13–18k units (Omdia/IDC). Unitree >5,500, AgiBot 5,168, Figure and Agility ~150 each ([humanoid.guide](https://humanoid.guide/humanoid-deployments-in-2026-favor-figure-and-agility/)).
- **Goldman Sachs (Sep 2026 update):**
  - 2026: 75k units (up from 51k).
  - 2030: **890k** (up from 256k).
  - 2035: **6.5M**, a ~$138bn market (up from 1.4M and $38bn).
  - Sources: [247wallst](https://247wallst.com/investing/2026/09/14/goldman-sachs-just-supercharged-its-humanoid-robot-prediction-5x-to-6-5-million-by-2035/), [humanoid.guide](https://humanoid.guide/?p=18115).
- **Morgan Stanley:** installed base ~24M by 2036, **~134–138M by 2040** and **~1bn by 2050**, with a 6-year replacement cycle and >90% industrial/commercial use ([OODA Loop](https://oodaloop.com/briefs/technology/humanoid-robots-seen-as-5-trillion-global-opportunity-at-morgan-stanley/)). MS also expects BOM cost to fall ~11%/yr ([Shenzhen Daily](https://www.newsgd.com/m/node_a21acd2229/94f15140ad.shtml)).
- **CRU:** up to **100M produced by 2040** and 400M in 2050 (aggressive case).
- **Tesla:** a Fremont line with **1M/yr design capacity** and a 10M/yr Giga Texas aspiration. Musk himself called the 2026 ramp "impossible to predict" ([Electrek](https://electrek.co/2026/04/22/tesla-optimus-production/)).

**Other segments:**
- **Industrial robots:** 542k installed in 2024, operational stock 4.66M. China 54%, Europe 16% ([IFR](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years)).
- **Cobots:** ~57k shipped in 2025, rising to ~129k by 2030, about +17%/yr ([SCXchange / Interact](https://www.thescxchange.com/editorial/featured/cobot-shipments-to-rise-more-than-17-by-2030-china-maintains-market-dominance)).
- **Mobile robots:** revenue just under $5bn (2024) rising to $14bn (2030), 19% CAGR ([MMH / Interact Analysis](https://www.mmh.com/article/interact-analysis-cuts-mobile-robot-growth-forecast)).
- **Exoskeletons:** 50k units (2024) rising to 195k (2030) ([ABI](https://www.abiresearch.com/news-resources/chart-data/exoskeleton-market-forecast-size-outlook)).
- **Drones:**
  - Ukraine produced ~2.5–4M drones in 2025, and its capacity is now >8M FPV/yr ([Kyiv Post](https://www.kyivpost.com/amp/post/46892), [RNBO](https://rnbo.gov.ua/en/Diialnist/7370.html)).
  - EU industry has signed up to a goal of **>100k drone and C-UAS systems/yr by 2027** ([ESD](https://euro-sd.com/2026/03/news/industry-news/50150/the-drone-industry-sends-a-clear-message/)).
  - The "drone wall" (European Drone Defence Initiative) is expected to be complete by end-2027, with ~€6bn ([Euronews](https://www.euronews.com/my-europe/2025/10/15/eu-plans-functional-drone-wall-against-russia-by-end-of-2027-leak-shows)).
  - EU producers supply <30% of the military drones used ([Rabobank](https://www.rabobank.com/knowledge/d011511599-european-drone-investments-mapping-the-value-chain)).
- **eVTOL:** fleet of 12k by 2035 and 45k by 2040 (Bain, via search). The eVTOL aluminium alloy market is ~$112M (2024), rising to $270M (2031) ([Intel MR](https://www.intelmarketresearch.com/materials-and-chemicals/4768/evtol-aluminum-alloy-material-2025-2032-100)).

### 4. Tonnage model [est.]

**Humanoid scenarios (annual production × net Al per unit):**

| Year | Low | Base | High |
|---|---|---|---|
| 2030 | 0.3M × 22 kg ≈ **7 kt** | 0.9M (GS) × 22 kg ≈ **20 kt** | 3M × 22 kg ≈ **66 kt** |
| 2035 | 2M × 21 kg ≈ **42 kt** | 6.5M (GS) × 22 kg ≈ **143 kt** | 20M × 20 kg ≈ **400 kt** |
| 2040 | 10M × 18 kg ≈ **180 kt** | 35M × 20 kg ≈ **700 kt** (MS installed base ÷ 6-yr cycle + growth) | 100M (CRU) × 18 kg ≈ **1.8 Mt** |

In the low and high cases, the falling kg per unit reflects lightweighting and magnesium or plastic substitution. Semi-finished demand is about 1.5× these figures because of machining losses. A Chinese trade source's claim of **100–125 kt by 2030** ([Aluminium China](https://www.aluminiumchina.com/en-gb/news-center/industry-news/2025/4/5.html)) would need about 4–5M units. I treat it as a bull-case number.

**Non-humanoid robotics:**
- **2030:** about **40–70 kt** in total:
  - industrial robots ~25–40 kt
  - AMRs ~10–25 kt
  - cobots ~2 kt
  - exoskeletons <1 kt
  - drones ~1–2 kt
  - eVTOL <1 kt
- **2040:** perhaps **80–150 kt**.

**Total robotics aluminium (net content):**

| Year | Base | Range |
|---|---|---|
| 2030 | ~70 kt | 50–140 kt |
| 2035 | ~230 kt | 100–500 kt |
| 2040 | ~0.8 Mt | 0.3–2.0 Mt |

**Value pool:** at €25–40/kg for finished robot-grade components, the base case is worth **€5–8bn/yr by 2035** and **€20–30bn/yr by 2040** in aluminium-component revenue **[est.]**.

### 5. Competing materials

| Material | Density (g/cm³) | Where it wins | Threat to Al | Notes |
|---|---|---|---|---|
| **Aluminium (6061/7075, A356, high-conductivity casting alloys)** | 2.7 | Frames, housings, heat sinks, tubes | — | Cheap, machinable, recyclable, conducts heat (motor heat removal is a key humanoid limit) |
| **Magnesium (AZ91, AM60, thixomolded)** | 1.74 | Weight-critical skeletons. AgiBot/Zhiyuan uses a Mg skeleton ([SMM](https://news.metal.com/en/newscontent/104033658-zhiyuan-robotics-uses-magnesium-alloy-for-lightweight-strong-skeleton-in-new-humanoid-robot)). A Mg-housed industrial robot weighed 34.6% less than its Al version ([IMA](https://www.intlmag.org/page/showcase2025-commercial-cast)) | **Medium–high in China** | China ≈ 89% of world Mg output ([EC](https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/second-depth-review-strategic-areas-europes-interests_en)), EU 95–97% import dependence. Corrosion. Big supply risk for EU/US OEMs |
| **CFRP** | ~1.6 | Premium limbs, drone frames, eVTOL airframes | Medium (drones, eVTOL: high) | Slow cycle times, cost, poor recyclability, little use in heat-dissipating housings |
| **PEEK / engineering plastics** | ~1.3 | Covers, brackets, gears in hands | Low–medium | Kingfa's own chairman calls most humanoid PEEK uses "hype" ([Gasgoo](https://autonews.gasgoo.com/articles/news/kingfa-techs-yu-fei-pours-cold-water-most-current-peek-applications-in-humanoid-robotics-are-hype-2100425756185628673)) |
| **Steel** | 7.8 | Gears, planetary roller screws, bearings | Complementary | Dominant inside actuators (IDTechEx) |
| **Titanium** | 4.4 | High-stress nodes | Low | Cost |

**Net view [est.]:** aluminium keeps **55–70% of structural metal mass** in Western humanoids through 2035. Chinese OEMs move faster to magnesium. Aluminium's strongest defence is **thermal function plus stiffness per euro**, so parts that combine structure and heat sinking are the most defensible.

### 6. Where the EU stands

- **China owns volume.** It makes ~90% of today's humanoids, over half of industrial robot installs and most cobot shipments. Its aluminium and magnesium supply chains (Xusheng, Tuopu, Sanhua) are already integrated with Tesla and the domestic OEMs.
- **The EU has an emerging demand cluster.** Schaeffler is a humanoid actuator supplier (up to 250 Nm). It is partnered with Neura Robotics, plans to deploy a "mid-four-digit" number of humanoids by 2035, and holds a minority stake in Agility ([Logistik Heute](https://logistik-heute.de/en/news/physical-ai-schaeffler-and-neura-robotics-collaborate-humanoid-robots-233371.html), [heise](https://heise.de/-11068017)). Other EU names: 1X (Norway), Humanoid (UK), Wandercraft (France), KUKA, ABB, Universal Robots, Harmonic Drive SE, Maxon. Defence drone makers include Helsing (HX-2), Quantum Systems and Stark.
- **The EU has policy tailwinds.** These include the CRMA magnesium-diversification push, defence sovereignty (the Readiness 2030 drone programmes), CBAM, and OEM Scope-3 targets that favour low-CO₂ EU metal.

### 7. So what for our company

1. **Don't build tonnage capacity for robotics.** Even the base case (~0.8 Mt by 2040) is spread across global supply chains, and most of it will be in China. Robotics is not a reason to restart a potline.
2. **Do build a "robot-grade" product line on existing extrusion, casthouse and rolling assets.** The products:
   - tight-tolerance high-strength tubes and profiles
   - 7xxx/6xxx machining billet and plate with certified low porosity
   - high-thermal-conductivity casting alloys
   - all with a low-CO₂ passport
   
   This is a high-margin niche that our quality systems already support.
3. **Move downstream through one acquisition.** Buy an EU precision casting and machining SME (HPDC plus semi-solid plus 5-axis CNC). The aim is to become a Tier-2 supplier of actuator and motor housings to Schaeffler, Harmonic Drive, Maxon, Bosch Rexroth and the European humanoid OEMs.
4. **Turn buy-to-fly into an advantage.** Offer closed-loop chip take-back to robot and drone machining shops, so their swarf goes back to our casthouse as low-CO₂ input.
5. **Position for defence.** Qualify 7xxx plate and forgings for drone and C-UAS makers that need non-Chinese supply.
6. **Sell against magnesium dependency.** Our pitch to OEMs: "EU-sourced, recyclable aluminium versus 97% China-sourced magnesium."
7. **Gate investments on milestones.** Scale only if global humanoid output exceeds 250k units/yr by 2028 and a Western OEM signs a multi-year housing contract. Until then, keep capex in the tens of millions of euros.

### Key numbers

| Metric | Value | Source |
|---|---|---|
| Aluminium per humanoid robot (structural) | 17-25 kg (20-30 kg incl. actuator/motor housings, battery, heat sinks - own estimate) | CRU 2025 https://www.crugroup.com/en/communities/thought-leadership/2025/the-next-commodity-battleground-humanoid-robots/ |
| CRU humanoid aluminium demand, 2050 (moderate scenario, 400M units/yr) | ~10 Mt/yr Al (plus 2.4 Mt Cu); up to 100M units produced by 2040 | CRU 2025 https://www.crugroup.com/en/communities/thought-leadership/2025/the-next-commodity-battleground-humanoid-robots/ |
| Global humanoid sales 2025 | 13,000-18,000 units, ~90% Chinese; Unitree >5,500, AgiBot 5,168 | Omdia/IDC via https://interestingengineering.com/research/the-humanoid-robot-reality-check |
| Goldman Sachs humanoid shipments forecast (Sep 2026) | 75k (2026), 890k (2030), 6.5M (2035); ~$138bn market 2035 | https://247wallst.com/investing/2026/09/14/goldman-sachs-just-supercharged-its-humanoid-robot-prediction-5x-to-6-5-million-by-2035/ |
| Morgan Stanley humanoid installed base | ~24M (2036), ~134-138M (2040), ~1bn (2050); 6-yr replacement cycle | https://oodaloop.com/briefs/technology/humanoid-robots-seen-as-5-trillion-global-opportunity-at-morgan-stanley/ |
| Humanoid aluminium demand (own model, base case) | ~20 kt (2030), ~143 kt (2035), ~700 kt (2040); range 0.18-1.8 Mt in 2040 | Own estimate based on GS/MS/CRU units x 18-22 kg |
| Total robotics aluminium demand (own model, base) | ~70 kt (2030), ~230 kt (2035), ~0.8 Mt (2040) | Own estimate |
| Robot-grade Al component value pool (own estimate) | EUR 5-8bn/yr (2035), EUR 20-30bn/yr (2040) at EUR 25-40/kg finished | Own estimate |
| Actuators share of humanoid BOM cost | ~56% | Morgan Stanley Humanoid 100 via https://gondola.cc/posts/69265942-benzinga-youtube |
| Industrial robot installations 2024 | 542,000 units (China 54%, Europe 16%); operational stock 4.66M | IFR World Robotics 2025 https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years |
| Cobot shipments | ~57k (2025) to ~129k (2030), ~17% CAGR | Interact Analysis via https://www.thescxchange.com/editorial/featured/cobot-shipments-to-rise-more-than-17-by-2030-china-maintains-market-dominance |
| Mobile robot market revenue | <$5bn (2024) to $14bn (2030), 19% CAGR | Interact Analysis via https://www.mmh.com/article/interact-analysis-cuts-mobile-robot-growth-forecast |
| Exoskeleton shipments | 50k (2024) to 195k (2030) | ABI Research https://www.abiresearch.com/news-resources/chart-data/exoskeleton-market-forecast-size-outlook |
| EU drone industry production goal | >100,000 drone/C-UAS systems per year by 2027; drone wall ~EUR 6bn, complete end-2027 | https://euro-sd.com/2026/03/news/industry-news/50150/the-drone-industry-sends-a-clear-message/ ; https://www.euronews.com/my-europe/2025/10/15/eu-plans-functional-drone-wall-against-russia-by-end-of-2027-leak-shows |
| Ukraine drone production | ~2.5-4M drones in 2025; capacity >8M FPV/yr in 2026 | https://www.kyivpost.com/amp/post/46892 ; https://rnbo.gov.ua/en/Diialnist/7370.html |
| EU magnesium import dependence on China | ~95-97% (China ~89% of world Mg output) | Argus https://www.argusmedia.com/ja/news-and-insights/latest-market-news/2431861-market-weighs-up-eu-s-magnesium-sourcing-targets ; EC in-depth review |
| eVTOL aluminium alloy market | $112M (2024) to $270M (2031) | https://www.intelmarketresearch.com/materials-and-chemicals/4768/evtol-aluminum-alloy-material-2025-2032-100 |
| Figure 03 / UR10e mass | ~61 kg humanoid; 33.5 kg cobot | https://www.nextpit.de/news/figure-03-wie-humanoide-roboter-bald-die-hausarbeit-uebernehmen ; https://www.universal-robots.com/media/1826690/01_2023_collective_data_sheet.pdf |

### Scored opportunities

| Opportunity | Score | Model | Capex | Time | Risk | Market |
|---|---|---|---|---|---|---|
| **Robot-grade precision extrusions, tubes and machining billet/plate**: Launch a certified 'robot-grade' product family on existing extrusion and rolling assets: tight-tolerance 6xxx/7xxx hollow limb tubes, actuator-housing profiles cut to near-net length, low-porosity 6061/7075 machining billet and plate, all with a low-CO2 product passport. Customers: humanoid OEMs (Neura, 1X, Humanoid, Agility via Schaeffler), cobot/industrial robot makers (UR, KUKA, ABB), AMR chassis makers and AS/RS integrators. Sold at a premium to standard profiles. | 8 | Build (product line on existing assets) + co-development agreements with OEMs/actuator makers | low | 1-2 years | low | Robotics Al ~70 kt (2030) to ~230 kt (2035) and ~0.8 Mt (2040) net content, base case [own est.]; semi-finished demand ~1.5x net because of machining. A 10-15% share of the Western portion means ~10-40 kt/yr of high-margin semis by 2035. |
| **Tier-2 actuator and motor housing supplier (acquire EU precision casting + CNC SME)**: Acquire an EU precision HPDC / semi-solid casting and 5-axis machining company and turn it into a specialist supplier of rotary/linear actuator housings, motor housings, gearbox covers and torso castings. Target customers: Schaeffler (humanoid actuators up to 250 Nm; Neura partnership, Agility stake), Harmonic Drive SE, Maxon, Bosch Rexroth and EU humanoid OEMs. The shift from machined billet to near-net die casting as volumes grow (e.g. Samkee's humanoid frame contract) favours a casthouse-integrated player. | 7.5 | Buy (bolt-on M&A, EUR 30-150M EV) + partner (long-term agreements with actuator Tier-1s) | medium | 1-3 years | medium | 28-40 actuators per humanoid, ~4-8 kg Al housings per robot [est.]; at GS 6.5M units (2035) that is ~25-50 kt of housings globally, ~EUR 1-2.5bn/yr at EUR 30-50/kg finished [own est.]. Actuators are ~56% of humanoid BOM cost (Morgan Stanley). |
| **Thermal-management aluminium for robots (high-conductivity alloys, heat sinks, cold plates)**: Develop and license high-thermal-conductivity, high-strength casting and extrusion alloys, and make skived/extruded heat sinks and cold plates for actuator drives, robot battery packs and onboard AI compute. Motor heat is a key limit on humanoid performance, and parts that combine structure with heat removal are where aluminium beats magnesium, CFRP and PEEK. The same products serve power electronics and data centres, which spreads the risk. | 7 | Build (alloy R&D + product line) + license alloys to casters/die-casters | low | 2-3 years | medium | ~2-5 kg thermal-function Al per humanoid [est.]; ~15-30 kt in 2035 base case from humanoids alone, plus overlap with power-electronics and data-centre cooling markets that are far larger [own est.] |
| **Closed-loop machining-chip recycling + low-CO2 'robot passport' metal**: Robot and drone parts are heavily machined (buy-to-fly 1.5-3x), producing large volumes of clean, alloy-segregated swarf. Offer EU machining shops and robot OEMs a chip take-back service (collection, de-oiling, remelt in our casthouse), with certified CO2 values and traceability for the OEMs' Scope-3 reporting and for CBAM, and a contrast with China-sourced magnesium (EU ~97% import dependence). | 7 | Build service + sell premium low-carbon billet; partner with machining shops | low | 1-2 years | low | Machining scrap is ~0.5-2x net Al content: ~10-40 kt/yr (2030) to ~100-300 kt/yr (2035) of robotics-related swarf across all segments [own est.]; also applies to aerospace/defence machining |
| **Sovereign aluminium for EU defence drones and counter-UAS**: Qualify 7xxx/2xxx plate, extrusions and forgings plus machined kits for European drone, loitering-munition and counter-drone interceptor makers (Helsing, Quantum Systems, Stark, MBDA/Rheinmetall programmes). The selling point is a non-Chinese, defence-qualified, surge-capable supply chain. Most small-drone frames are CFRP, so focus on motor bells and mounts, launchers, ground stations, C-UAS turrets and larger airframes. | 6 | Sell semis/kits + framework supply contracts; possibly partner with a defence machining house | low | 1-2 years | medium | EU industry goal >100k drone/C-UAS systems per year by 2027; drone wall ~EUR 6bn; EU makers currently supply <30% of the drones used. Al tonnage is small (low single-digit kt/yr) but margins and strategic value are high [own est.] |
| **Aluminium additive manufacturing (Al-Sc / high-strength powder) for topology-optimised robot and eVTOL parts**: Produce high-strength aluminium AM powders (Al-Sc, Al-Mg-Zr) and/or run a print service for topology-optimised humanoid hip/knee brackets, drone and eVTOL fittings, and robot grippers. This is a niche today. It is an option on future lightweighting that counters magnesium/CFRP substitution. | 4.5 | Partner / minority stake in an AM specialist; license powder alloys | medium | 3-5 years | high | Sub-kt today; eVTOL aluminium alloy market $112M (2024) to $270M (2031); robotics AM share uncertain [own est. <5 kt/yr by 2035] |
