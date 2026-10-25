## AI & Materials Informatics for Alloy Design

*Research date 2026-10-25. Method note: WebFetch could not resolve most publisher and university domains during this run (DNS errors on brunel.ac.uk, wisc.edu, foundrymag.com, desy.de, patsnap.com, euroguss.de). The facts below come from search-indexed abstracts, press releases and trade reports, each with its URL. Anything marked [est.] is my own reasoned estimate, not a sourced figure.*

### 1. Executive view

AI has made the **composition-design phase** of alloy development much shorter. It has not made **qualification** much shorter, and qualification is where most of the time and money goes. The 10–20-year lab-to-market baseline is still the norm in aluminium ([U-Michigan/MGI](https://msewww.engin.umich.edu/?p=3343)). The best ICME cases reach about 6 years for a flight-critical alloy: QuesTek's Ferrium M54 against the usual 15–20 years ([NIST case study](https://www.nist.gov/document/materialsinnovationcasestudyquestek090616pdf)). GE cut its engine-alloy cycle from 15 to 9 years ([NIST/MGI](https://www.nist.gov/node/1507161)).

For a European smelter-to-semis group, the main value of AI is not inventing exotic alloys. It is **designing and certifying alloys that accept more, and dirtier, scrap while meeting the same customer specs**, and then running the casthouse with properties predicted from that scrap. This connects directly to our 100 kt/yr sorting hub and to the 8–20-point LME scrap spread, which is about EUR 172–431/t at the EUR 2,155/t planning price.

### 2. State of the art, by technique

**CALPHAD + ML surrogates (ICME).** Thermodynamic databases are the physics backbone. Thermo-Calc's TCAL11 covers all industrial wrought alloys from 1xxx to 7xxx ([Thermo-Calc](https://thermocalc.com/products/databases/aluminum-based-alloys/)). The usual workflow runs millions of CALPHAD/precipitation simulations, trains a fast surrogate on them, and then searches composition space. MIT's 2025 printable high-temperature Al alloy needed only **40 evaluated compositions instead of more than 1 million simulations**. It came out 5x stronger than a cast counterpart, **50% stronger than alloys designed by conventional simulation without ML**, and stable to 400 °C ([MIT News](https://news.mit.edu/index%2Ephp/2025/printable-aluminum-alloy-sets-strength-records-may-enable-lighter-aircraft-parts-1007)).

**Bayesian optimisation and active learning.** Multi-objective BO (qEHVI) has been shown to find Al-alloy Pareto fronts within a small experimental budget ([arXiv 2401.06106](https://arxiv.org/html/2401.06106v2)). Active-learning loops typically converge in about 6 iterations; that HEA benchmark is cited in the same search set. Tree-based models and other ML models have produced experimentally validated 7xxx alloys: YS 712 MPa with 19% elongation in J. Alloys Compd. 2022, and about 952 MPa UTS in Communications Materials 2021 ([paperity](https://paperity.org/p/273621093/accelerated-discovery-of-high-strength-aluminum-alloys-by-machine-learning)). A PatSnap 2026 landscape teaser cites a **12.6% modulus gain over a commercial aerospace alloy, found among 800,000 compositions with 36 experiments** ([PatSnap](https://www.patsnap.com/resources/blog/articles/ai-accelerated-alloy-design-landscape-2026/)). I could only read the summary, not the full report.

**Recycling-oriented ML (the most relevant work for us).**
- **Brunel (Tiwari, Mendis, Eskin), J. Sustainable Metallurgy 2025.** Clustering and optimisation on 292 datasets **reduced 42 grades of 6xxx to 10 "optimal alloys"** across T5/T6/T7 tempers, explicitly to ease scrap sorting ([Springer](https://link.springer.com/article/10.1007/s40831-025-01112-4)).
- **Li et al. 2025 (Elsevier).** Random-forest models of recycled Al with Fe-rich intermetallics; an ML-guided 0.10 wt% Sc addition was validated experimentally (+4.37% UTS) ([BIT](https://pure.bit.edu.cn/zh/publications/design-of-high-strength-and-ductile-recycled-al-alloys-by-machine/)).
- **Michigan Tech thesis 2025.** Multi-objective BO combined with Thermo-Calc to design castable Al-Mg-Fe-Si-Cu-Zn alloys; the alloys were cast and tested ([MTU](https://digitalcommons.mtu.edu/etdr/2012)).
- **Journal of Materials Informatics 2024.** XGBoost/SVM design of Al-2.64Si-0.43Mg with **thermal conductivity above 190 W/m·K and UTS above 220 MPa**, validated experimentally. This is relevant to e-drive housings and heat sinks ([JMI](https://www.oaepublish.com/articles/jmi.2024.21)).
- **Central South University patent CN122024897A (2026).** Combines solidification simulation with ML to predict Fe-phase types in reclaimed Al ([patent](https://www.goveda.com/patent/CN-122024897-A)).

**LLM agents.** EGA, a primary producer like us, presented a **physics-aware multi-agent LLM framework for Al-alloy property prediction and design** at ICSOBA 2025 ([ICSOBA](https://icsoba.org/assets/files/publications/2025/Papers/CH08%20-%20Physics-Aware%20Multi-Agent%20AI%20Framework%20for%20Property%20Prediction%20and%20Design%20of%20Aluminium%20Alloys.pdf)). AlloyGPT, trained on CALPHAD-derived data for printable high-temperature Al alloys, appeared at IMAT 2025 ([ASM](https://asm.confex.com/asm/imat2025/webprogram/Paper63852.html)). MIT's multi-agent GNN+LLM system was published in PNAS in 2025 ([DSpace@MIT](https://dspace.mit.edu/handle/1721.1/163619)). Today these are research assistants that orchestrate tools. They are not autonomous designers.

**Generative crystal models (MatterGen, GNoME).** These have little direct relevance to commercial Al alloys. Our alloy properties come from microstructure, precipitation and processing, not from discovering new crystal structures. Critics show that MatterGen "discoveries" can be disordered versions of known compounds that were already in its training data ([HU Berlin](https://edoc.hu-berlin.de/18452/38430)). These models are useful at most for screening intermetallic or dispersoid phases.

**Self-driving labs and high-throughput testing.**
- **Texas A&M ARM-MIP.** US$24.9M over 6 years for the first national robotic metals lab. Targets are **50 alloys/month in year 1, rising to more than 200/month by year 6**. Industry can buy access under negotiated IP terms ([TAMU](https://stories.tamu.edu/news/2026/08/05/texas-am-to-build-self-driving-laboratory-for-metals-open-to-researchers-nationwide/)).
- **UW-Madison AlloyBot.** Automated arc-melting of **more than 100 compositions/week**, with a claimed "100x faster" development ([TMS abstract](https://www.programmaster.org/PM/PM.nsf/ApprovedAbstracts/C51BFD5FCD57FCD785258CBB00102E33)).
- **MPI Düsseldorf Rapid Alloy Prototyping.** **50 material conditions (5 alloys x 10 treatments) in about 5 days**, taking idea-to-result from months down to days ([MPIE](https://www.mpie.de/4151172/combinatorial-metallurgy-and-processing)).
- **ZwickRoell roboTest P.** Up to **300 tensile specimens tested unattended**. A vendor flyer chart suggests about EUR 350k per system, but I could not read the exact figure ([ZwickRoell](https://www.zwickroell.com/fileadmin/content/Files/SharePoint/user_upload/Brochures_EN/Flyer_Automated_Testing_Systems_EN.pdf)).

### 3. Vendors and players

| Player | Offer | Al evidence |
|---|---|---|
| Thermo-Calc | CALPHAD, TCAL11/MOBAL8, Prisma | Industry standard. A TCAL9 perpetual licence cost **EUR 10,440** in a Czech tender ([VSB](https://zakazky.vsb.cz/document_audit_71158/priloha-1-sw_thermocalc_tech_spec-doc)) |
| Citrine Informatics | AI platform (US$16M Series C in 2023) | HRL 7A77 nano-functionalised powder: searched **11.5M combinations, narrowed to 100 candidates**, commercial about 2 years after publication; vendor claims R&D in 1/2 to 1/5 of the usual time ([Citrine](https://CITRINE.IO/wp-content/uploads/2021/04/Case-Study-HRL-AM-powder-development.pdf)) |
| HRL Laboratories | Alloy IP | 7A77.50 / 7A77.60L: **first AM alloys registered with the Aluminum Association** ([AM Chronicle](https://amchronicle.com/news/hrl-laboratories-receives-aluminum-association-registration-for-am-alloys/?amp=1)) |
| Intellegens (Alchemite) | ML for sparse data | Ni alloy case (not Al): vendor claims **about 15 years and US$10M saved**, working from data as sparse as 0.05% ([Metal AM](https://www.metal-am.com/machine-learning-algorithm-designs-new-alloy-for-metal-additive-manufacturing-2/)) |
| QuesTek | ICME design services | 18 alloy patents; Navy SBIR for 7xxx AM Al ([Navy SBIR](https://navysbir.com/15_1/24.htm)) |
| Alloyed (ex-OxMet, UK) | ABD platform | £37M Series B (2025); £525k EPSRC project with Brunel BCAST for **scrap-based automotive Al** ([The Engineer](https://www.theengineer.co.uk/content/news/525k-to-accelerate-ai-alloy-design)) |
| Fehrmann MaterialsX (Hamburg) | MatGPT | Claims Al-alloy development in "days or weeks"; works with DESY on Multi-Digi-Mat ([Euroguss](https://euroguss.de/en/exhibitors/fehrmann-materials-x-2233786/matgpttm-2265714)) |
| Phaseshift (Toronto) | RAD platform | US$3M seed; claims "100x faster"; licenses the alloys it designs ([BetaKit](https://betakit.com/phaseshift-technologies-raises-4-1-million-cad-to-fuse-material-discovery-with-ai/)) |
| Ansys Granta, Polymerize, Materials Design | Data management, ML, atomistics | Generic tools; I found no documented Al case [gap] |

**Aluminium majors.** Market-wide, materials informatics is still a small software market: about US$170M in 2025, US$410M by 2030 ([MarketsandMarkets](https://prnewswire.co.uk/news-releases/material-informatics-market-worth-410-4-million-in-2030---exclusive-report-by-marketsandmarkets-302389751.html)). Company activity:
- **Constellium.** Uses AI with Grenoble (3ALP lab) and MIT on how Fe/Mn impurities affect the crash and forming performance of 6xxx. It also leads the £10M CirConAl project, which makes parts with more than 90% recycled content ([Constellium](https://constellium.com/about-us/stories/advancing-materials-science-with-partnerships)).
- **Hydro.** US$2.5M over 5 years for CREATe at U-Michigan, including **AI computational alloy design for Fe-tolerant extrusion alloys** ([Recycling Today](https://www.recyclingtoday.com/news/hydro-university-of-michigan-partnership)). Hydro also owns the RACE project with SINTEF/NTNU/Benteler, and there is the new **SFI FAST (2026–2033)** centre on post-consumer scrap in safety-critical parts ([NAV](https://arbeidsplassen.nav.no/stillinger/stilling/2ba31115-971a-4398-ae69-87b76c53d954)).
- **Novelis.** Is hiring for physics-based and data-driven models aimed at high-recycled-content alloys ([Novelis careers](https://careers-novelis.icims.com/jobs/51015/aluminum-modeling-engineer-co-op/job)).
- **Speira, Alcoa.** I found no public AI alloy programme.
- **AMAG with Leoben.** Commercialised the CrossAlloy crossover family, which may tolerate more impurities. This is classical metallurgy, but a natural target for ML ([Leoben](https://pure.unileoben.ac.at/en/publications/on-the-potential-of-aluminum-crossover-alloys/)).
- **Tesla.** Its in-house non-heat-treated casting alloy (YS ≥130 MPa as-cast) shows OEMs now design their own alloys. I found no evidence that ML was used ([Foundry-Planet](https://www.foundry-planet.com/d/tesla-s-aluminum-alloys-patent-hints-at-ultra-tough-evs-that-are-cheaper-to-produce/)).

**EU programmes.** The Group of Chief Scientific Advisors' April 2026 opinion calls for AI, digital twins and self-driving labs ([SAM](https://scientificadvice.eu/news/ai-could-unlock-the-next-generation-of-advanced-materials-key-takeaways-from-the-webinar/)). A proposed 2028–34 Horizon partnership aims to cut time-to-market from 10–20 years to 5–10 ([FFG](https://www.ffg.at/sites/default/files/downloads/The-Future-of-Advanced-Materials-Research-and-Innovation-in-Europe.pdf)). Running scrap projects include RecAL (EUR 10.6M, 19 partners, AI sorting) and CLEANMAT (EUR 7.33M, a digital thread from sorting to alloy qualification) ([CORDIS](https://cordis.europa.eu/project/id/101294748/de)). The Advanced Materials Act is still at the consultation stage.

### 4. Time and cost evidence

| Phase | Classic | AI/ICME-enabled | Source / basis |
|---|---|---|---|
| Composition screening | 2–4 yrs, 100s of casts | 3–12 months, 30–100 casts | MIT 40 vs 1M; PatSnap 36 experiments; [est.] |
| Lab validation | 1–2 yrs | 3–6 months with RAP or robotic testing | MPIE 50 conditions in 5 days |
| Plant scale-up | 1–3 yrs | 1–2 yrs (ML process windows) | [est.] |
| Customer qualification | Auto 2–4 yrs; aero 5–10+ yrs | Little change | M54 about 6 yrs total; [est.] |
| **Total** | **10–20 yrs** | **Auto 3–5 yrs; aero 6–8 yrs** | MGI, NIST; [est.] |
| Programme cost, one new wrought alloy | EUR 10–30M [est.] | EUR 4–12M [est.] | Intellegens US$10M saved (vendor claim) |

### 5. What it takes to build the capability [est.]

- **Team (8–12 FTE, about EUR 1.2–1.8M/yr):** 2–3 computational metallurgists (CALPHAD/precipitation), 2–3 ML/data scientists, 1–2 data engineers to digitise casthouse, rolling and extrusion history, 2–3 lab technicians, and 1 product/IP lead.
- **Data:** Our biggest asset. Years of melt chemistry (OES), process logs and test certificates. Standardising them (FAIR) is the bottleneck named in the 2026 reviews. One-off cost EUR 0.5–1M.
- **Software (EUR 0.3–0.6M/yr):** Thermo-Calc suite plus TCAL/MOBAL (tens of k€ per seat), an informatics platform (Citrine or Alchemite, EUR 100–300k/yr) or an in-house Python/BO stack, Granta-type data management, and cloud compute.
- **Lab capex (EUR 2.5–5M):** Multi-mould rapid casting (EUR 0.3–0.8M), lab rolling mill and extrusion/hot-compression simulator (EUR 0.7–2M), robotic tensile testing (about EUR 0.35M), automated metallography/SEM-EDS (EUR 0.3–0.8M), DSC, conductivity and corrosion rigs (EUR 0.2–0.4M).
- **Total 3-year programme: EUR 8–14M.** A 30–50% grant share is realistic through Horizon Europe, Austrian/German national programmes, or IPCEI-type schemes.

### 6. Key numbers

| Metric | Value |
|---|---|
| Classic alloy lab-to-market | 10–20 yrs |
| MIT ML design: candidates evaluated | 40 (vs >1M simulations) |
| Brunel ML rationalisation of 6xxx | 42 grades to 10 |
| Citrine/HRL search space | 11.5M combinations to 100 candidates |
| Texas A&M SDL throughput | 50 rising to 200+ alloys/month |
| MPIE Rapid Alloy Prototyping | 50 conditions in about 5 days |
| Materials informatics market | US$170M (2025) to US$410M (2030) |
| Scrap spread at planning price | EUR 172–431/t |
| In-house capability, 3-yr cost | EUR 8–14M [est.] |

### 7. So what for our company

1. **Our edge is integration, not algorithms.** Few players in Europe own smelter, casthouse, rolling, extrusion *and* a 100 kt AI sorting hub. Sorter spectra, melt chemistry and final properties can all feed one model, making a closed **scrap-to-property digital thread**. Hydro and Constellium are building this through universities. We should do it in-house, with Leoben/RWTH/NTNU/MPI as partners.
2. **The quickest money is in the casthouse.** ML property models let us **specify alloys by property window rather than tight composition window**, and optimise the charge mix for the cheapest scrap that still meets the properties. Each extra point of LME captured on 100 kt is worth about EUR 2.2M/yr. Each tonne of primary displaced avoids about 15.5 t CO2.
3. **New alloys should be "scrap-native" 6xxx/5xxx/crossover families** (Fe/Cu/Zn-tolerant) for automotive and building extrusions and sheet, registered with the Aluminum Association and co-qualified with 1–2 OEMs. Qualification time is still the bottleneck, so start customer programmes now.
4. **Avoid hype.** Generative crystal models (MatterGen/GNoME) and autonomous LLM designers are not decision-relevant for our products before about 2028. Buy SaaS and test capacity (for example ARM-MIP access) before committing to a full self-driving lab.
5. **Protect IP and data.** Patent the composition-and-process windows. Keep the trained models and the data proprietary.

### Key numbers

| Metric | Value | Source |
|---|---|---|
| Classic alloy development & deployment time | 10-20 years | https://msewww.engin.umich.edu/?p=3343 ; https://www.nist.gov/node/1507161 |
| Best-in-class ICME alloy to flight qualification (QuesTek M54) | ~6 years vs 15-20 typical | https://www.nist.gov/document/materialsinnovationcasestudyquestek090616pdf |
| GE engine alloy cycle with computational methods | 15 to 9 years | https://www.nist.gov/node/1507161 |
| MIT ML-designed printable Al alloy: compositions evaluated | 40 (vs >1 million simulations); 50% stronger than non-ML design; stable to 400 C | https://news.mit.edu/index%2Ephp/2025/printable-aluminum-alloy-sets-strength-records-may-enable-lighter-aircraft-parts-1007 |
| Brunel ML rationalisation of 6xxx alloys for recycling | 42 grades reduced to 10 optimal alloys (292 datasets) | https://link.springer.com/article/10.1007/s40831-025-01112-4 |
| Citrine/HRL 7A77 search space | 11.5M combinations to 100 candidates; commercial ~2 yrs after publication | https://CITRINE.IO/wp-content/uploads/2021/04/Case-Study-HRL-AM-powder-development.pdf |
| PatSnap-cited AI alloy benchmark | 800,000 compositions searched with 36 experiments; +12.6% modulus | https://www.patsnap.com/resources/blog/articles/ai-accelerated-alloy-design-landscape-2026/ |
| Texas A&M ARM-MIP self-driving metals lab | US$24.9M/6 yrs; 50 alloys/month yr1 to >200/month yr6 | https://stories.tamu.edu/news/2026/08/05/texas-am-to-build-self-driving-laboratory-for-metals-open-to-researchers-nationwide/ |
| MPIE Rapid Alloy Prototyping throughput | 50 material conditions in ~5 days | https://www.mpie.de/4151172/combinatorial-metallurgy-and-processing |
| UW-Madison AlloyBot synthesis throughput | >100 compositions/week | https://www.programmaster.org/PM/PM.nsf/ApprovedAbstracts/C51BFD5FCD57FCD785258CBB00102E33 |
| Robotic tensile testing capacity (ZwickRoell roboTest P) | Up to 300 specimens unattended; ~EUR 350k system (chart, unconfirmed) | https://www.zwickroell.com/fileadmin/content/Files/SharePoint/user_upload/Brochures_EN/Flyer_Automated_Testing_Systems_EN.pdf |
| Thermo-Calc TCAL9 perpetual licence (public tender) | EUR 10,440 | https://zakazky.vsb.cz/document_audit_71158/priloha-1-sw_thermocalc_tech_spec-doc |
| Materials informatics software market | US$170M (2025) to US$410M (2030), 19.2% CAGR | https://prnewswire.co.uk/news-releases/material-informatics-market-worth-410-4-million-in-2030---exclusive-report-by-marketsandmarkets-302389751.html |
| Hydro-U-Michigan CREATe (incl. AI alloy design, Fe tolerance) | US$2.5M over 5 years | https://www.recyclingtoday.com/news/hydro-university-of-michigan-partnership |
| Constellium CirConAl recycled-content alloy project | GBP 10M; >90% recycled content parts | https://www.apcuk.co.uk/impact/funded-projects/constellium-circular-and-constant-aluminium-circonal/ |
| Alloyed (ex-OxMet) Series B / EPSRC scrap-based Al project | GBP 37M / GBP 525k | https://3dprintingindustry.com/news/alloyed-raises-37m-in-new-funding-for-metal-alloy-development-237275/ |
| Horizon Europe CLEANMAT / RecAL scrap-to-alloy projects | EUR 7.33M / EUR 10.6M | https://cordis.europa.eu/project/id/101294748/de ; https://leitat.org/blog/recal-project-a-circular-future-for-european-aluminium/ |
| Scrap grade spread at planning LME EUR 2,155/t | EUR 172-431/t (8-20 points) | Company board paper (calculation) |
| In-house AI alloy design capability, 3-yr total cost | EUR 8-14M incl. EUR 2.5-5M lab capex [est.] | Own estimate from vendor/tender data above |
| AI-enabled automotive alloy time to market | 3-5 yrs vs 8-12 classic [est.] | Own estimate; qualification remains bottleneck |

### Scored opportunities

| Opportunity | Score | Model | Capex | Time | Risk | Market |
|---|---|---|---|---|---|---|
| **ML property-based charge optimiser (scrap-to-spec digital thread)**: Train ML property models on our casthouse OES chemistry, process logs and test certificates, plus sorting-hub sensor data. Specify products by property window rather than tight composition window, and optimise each melt's charge mix for the cheapest scrap that still meets the properties. This is materials informatics applied directly in production, with no new alloy and no customer requalification for in-spec products. | 9 | Internal margin uplift (scrap spread capture, lower primary/hardener use), plus a low-carbon product premium. | low | 6-18 months | low | Covers ~100 kt/yr hub output plus scrap used across casthouse. Each extra LME point captured on 100 kt is about EUR 2.2M/yr; 3-5 points is EUR 6-11M/yr [est.]. Each tonne of primary displaced avoids ~15.5 t CO2. |
| **AI-designed scrap-native (Fe/Cu-tolerant) 6xxx/5xxx/crossover alloy family**: Use CALPHAD+ML surrogates and Bayesian optimisation to design 2-4 new extrusion and sheet alloys that keep crash, forming and corrosion performance at higher Fe/Cu/Zn levels from post-consumer scrap. Register them with the Aluminum Association and co-qualify with 1-2 automotive or building OEMs. Hydro (CREATe) and Constellium (3ALP/CirConAl) are doing the same, so speed matters. | 8.5 | Proprietary alloys sold as semis, at a premium or with lower input cost. Patent the composition and process windows and license them to partners. | medium | 3-5 years (OEM qualification is the bottleneck) | medium | EU automotive and building extrusions/sheet are multi-Mt markets. For us, 50-150 kt/yr of product using lower-grade scrap [est.]. Value is the spread capture (EUR 100-300/t) plus a low-carbon premium [est.]. |
| **Alloy portfolio rationalisation and closed-loop OEM scrap contracts**: Apply the Brunel-style clustering/optimisation method (42 to 10 grades) to our own and our customers' alloy portfolios. Propose a reduced set of unified, recycling-friendly grades and back them with take-back contracts for production scrap that keep the alloys in closed loops. | 7.5 | Technical service bundled with supply contracts; shared savings with OEMs. | low | 1-3 years | medium | Fewer grades means fewer casthouse alloy changes and less downgrading. Fewer sorting classes at the hub raise sort yields; estimated EUR 2-6M/yr savings [est.] plus customer lock-in. |
| **In-house Materials Acceleration Platform (rapid casting + robotic testing + ML), grant co-funded**: Build a team of 8-12 FTE with a Thermo-Calc and informatics stack, multi-mould rapid casting, a lab rolling mill and extrusion simulator, robotic tensile testing and automated metallography, modelled on MPIE Rapid Alloy Prototyping and Texas A&M ARM-MIP. Partner with Leoben, RWTH, NTNU or MPI, and seek Horizon Europe and national funding. Sell spare capacity as an alloy-development service. | 7 | Internal R&D capability plus a contract alloy-development service for casters, extruders and OEMs, with 30-50% grant co-funding. | medium | 2-3 years (internal benefit earlier) | medium | Cuts screening cycles from years to months. Materials informatics market grows from US$170M to US$410M by 2030. Service revenue EUR 1-3M/yr possible [est.]. |
| **Specialty AI-designed alloys via start-up partnerships (high-conductivity, non-heat-treat casting, AM)**: Co-develop or license niche alloys with AI-alloy start-ups (Alloyed, Fehrmann MaterialsX, Phaseshift), with our casthouse supplying low-carbon base metal and master alloys. Targets include high-thermal-conductivity Al-Si-Mg for e-drive housings and heat sinks (JMI 2024: >190 W/m.K, >220 MPa), non-heat-treated gigacasting alloys, and high-temperature AM alloys. | 6 | Joint venture or licensing; low-carbon feedstock supply; royalty share. | low | 2-4 years | high | Niche volumes of 1-20 kt/yr [est.], but premiums of EUR 300-1,500/t over standard foundry alloy for specialty grades [est.]. AM powder is far higher, but volumes are small. |
