export const meta = {
  name: 'aluminium-opportunity-swarm',
  description: 'Swarm of research agents scanning future aluminium demand and next-gen production (robotics, AI, green) for an EU aluminium CEO, then a strategy synthesis',
  phases: [
    { title: 'Research', detail: '8 specialist agents: 4 demand-side, 4 supply/production-side' },
    { title: 'Synthesis', detail: 'Chief strategy agent ranks opportunities into a CEO memo' },
  ],
}

const TODAY = '2026-10-21'
const CONTEXT = `You are part of a research swarm working for the CEO of a mid-to-large EU aluminium company (primary smelting, casthouse, rolling/extrusion, and recycling exposure). Today is ${TODAY}. The CEO is looking for NEW BUSINESS OPPORTUNITIES for 2026-2040.
Use WebSearch (load it with ToolSearch "select:WebSearch,WebFetch" first) and WebFetch heavily. Prefer recent (2024-2026) sources: IAI, European Aluminium, CRU, Wood Mackenzie, IEA, BloombergNEF, McKinsey, company reports (Hydro, Novelis, Constellium, Speira, Alcoa, Rio Tinto, ELYSIS, Tesla, Figure, Boston Dynamics, Unitree etc.), EU Commission. Quantify everything you can (tonnes, CAGR, EUR, kg Al per unit). Cite sources with URLs inline. Flag clearly where numbers are estimates or yours. Be concrete and commercially minded — what could an EU aluminium company actually build, buy, partner on, or sell?
Your report_markdown should be a thorough, well-structured Markdown section (roughly 1200-2000 words) with headings, a key numbers table, and a "So what for our company" section.`

const AGENTS = [
  { key: 'robotics-demand', title: 'Robotics, Humanoids & Drones as Aluminium Demand',
    focus: `Demand for aluminium from robotics: humanoid robots (Tesla Optimus, Figure, Agility, Unitree, 1X, UBTech, etc.), industrial/collaborative robots, AMRs/warehouse robots, drones/eVTOL, exoskeletons. Estimate kg of aluminium per unit (frames, actuator housings, motor housings, heat sinks, gearboxes), alloy/product forms (high-strength extrusions, die/thixo castings, forgings, precision machined billet, 3D-printed Al), unit forecasts 2030/2035/2040 and resulting tonnage. Compare competing materials (magnesium, CFRP, engineering plastics). Identify supply-chain niches an EU aluminium producer could own (e.g. robot-grade extrusion profiles, actuator housings, thermal management parts).` },
  { key: 'mobility-demand', title: 'EVs, Automotive Lightweighting & Gigacasting',
    focus: `Aluminium demand from EVs and mobility: kg Al per BEV vs ICE, battery enclosures/trays, crash management, body-in-white, gigacasting/megacasting (Tesla, Volvo, Toyota, Chinese OEMs, EU OEMs adoption), new casting alloys (non-heat-treatable, high-recycled-content), e-motor housings, rail and trucks, e-buses. EU EV market outlook and the impact of Chinese competition. Opportunities: low-carbon alloy supply for gigacasting, closed-loop scrap with OEMs, battery enclosure extrusions.` },
  { key: 'energy-digital-demand', title: 'Energy Transition, Grids & Data Centres',
    focus: `Aluminium demand from the energy transition and digital infrastructure: solar PV frames & mounting, wind, grid expansion (overhead conductors, cables — Al substituting copper given copper scarcity), transformers, battery storage (BESS enclosures, battery foil), heat pumps, hydrogen equipment, and AI data centres (cooling, server racks, liquid cooling cold plates, power infrastructure). EU grid action plan numbers. Copper-to-aluminium substitution as a theme. Quantify tonnages.` },
  { key: 'packaging-construction-defence', title: 'Packaging, Construction, Aerospace & Defence',
    focus: `Aluminium demand from packaging (cans, PPWR EU packaging regulation, plastic substitution), building & construction (renovation wave, facades, low-carbon building products), aerospace (narrowbody ramp-up, Al-Li alloys), space/satellites, and the EU defence spending surge (ReArm Europe / SAFE: armoured vehicles, ammunition, drones, shipbuilding, aerospace plate). Which segments offer premium margins and security-of-supply arguments for EU producers?` },
  { key: 'robotics-automation-production', title: 'Robotics, AI & Automation in Aluminium Production',
    focus: `How aluminium will be PRODUCED with robotics, automation and AI: autonomous potroom robots (anode changing, crust breaking, tapping — e.g. ECL/Fives/REEL/Hydro), robotic casthouse operations (skimming, dross handling, sampling), AI process control for smelters (pot control, energy flexibility), digital twins, machine vision for quality, autonomous cranes/vehicles, robotic scrap sorting (LIBS, XRF, AI vision — e.g. AMP, Greyparrot, TOMRA, Steinert, Hydro's sorting), lights-out extrusion and finishing lines, predictive maintenance. Include vendors, deployed examples, productivity/safety/cost gains. Opportunities: adopt, co-develop, or SELL automation/AI as a business line.` },
  { key: 'green-primary-production', title: 'Green Primary Production Technologies',
    focus: `Next-generation primary aluminium production: inert anodes (ELYSIS, Rusal), Hydro HalZero, carbon capture for smelters, hydrogen/electric calcination for alumina (e.g. Alcoa/Rio refinery electrification, mechanical vapour recompression), flexible smelting / demand response (EnPot, Hydro), renewable PPAs and nuclear/SMR for smelters, technology readiness and timelines, capex, and cost per tonne. EU smelter closures and restart economics with current power prices. Opportunities: licensing, pilots, joint ventures, premium low-carbon brands (Hydro CIRCAL/REDUXA, Alcoa EcoLum etc.).` },
  { key: 'recycling-circular', title: 'Recycling, Scrap & Circular Business Models',
    focus: `Recycling and circularity: EU scrap volumes and growth, scrap leakage/exports from the EU (and debate about export restrictions), post-consumer scrap upgrading, sorting tech, remelt and refining of mixed scrap, dross processing, end-of-life EV and battery aluminium, building demolition scrap, closed-loop agreements with OEMs, digital material passports. Economics (margin per tonne of recycled vs primary), carbon advantage (~0.5 vs ~16 t CO2/t). Opportunities: new recycling plants, scrap trading/collection platforms, alloy-to-alloy recycling.` },
  { key: 'policy-markets-advanced-mfg', title: 'EU Policy, Markets & Advanced Manufacturing',
    focus: `(1) EU policy and market context: CBAM definitive phase from 2026 and its effect on aluminium imports, EU ETS, Critical Raw Materials Act (aluminium/bauxite as strategic), Clean Industrial Deal, Industrial Accelerator Act / "Made in Europe" low-carbon product requirements, US tariffs (Section 232), energy prices, Chinese overcapacity and the 45 Mt cap, LME/Midwest/Rotterdam premiums, green premiums. (2) Advanced manufacturing: aluminium additive manufacturing powders and wire (WAAM), high-performance/scandium alloys, aluminium-air & aluminium-ion batteries, aluminium as hydrogen/energy carrier, aluminium foam, nano-structured alloys. Which of these are real commercial opportunities by 2030-2040?` },
]

const OPP_SCHEMA = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    description: { type: 'string' },
    demand_or_market_size: { type: 'string', description: 'Quantified where possible, with year' },
    business_model: { type: 'string', description: 'build / buy / partner / license / sell service etc.' },
    capex_level: { type: 'string', enum: ['low', 'medium', 'high', 'very high'] },
    time_to_revenue: { type: 'string', description: 'e.g. 1-2 years, 3-5 years, 5-10 years' },
    risk_level: { type: 'string', enum: ['low', 'medium', 'high'] },
    attractiveness_1_to_10: { type: 'number' },
    key_sources: { type: 'array', items: { type: 'string' } },
  },
  required: ['name', 'description', 'demand_or_market_size', 'business_model', 'capex_level', 'time_to_revenue', 'risk_level', 'attractiveness_1_to_10'],
}

const REPORT_SCHEMA = {
  type: 'object',
  properties: {
    report_markdown: { type: 'string' },
    key_numbers: { type: 'array', items: { type: 'object', properties: { metric: { type: 'string' }, value: { type: 'string' }, source: { type: 'string' } }, required: ['metric', 'value', 'source'] } },
    opportunities: { type: 'array', items: OPP_SCHEMA, minItems: 3 },
  },
  required: ['report_markdown', 'key_numbers', 'opportunities'],
}

phase('Research')
const results = await parallel(AGENTS.map(a => () =>
  agent(`${CONTEXT}\n\nYOUR SPECIALIST AREA: ${a.title}\n${a.focus}\n\nReturn: report_markdown (start with "## ${a.title}"), key_numbers, and 3-6 concrete business opportunities scored for an EU aluminium company.`,
    { label: `research:${a.key}`, phase: 'Research', schema: REPORT_SCHEMA })
    .then(r => r ? { ...a, ...r } : null)
))
const ok = results.filter(Boolean)
const failed = AGENTS.filter(a => !ok.find(r => r.key === a.key)).map(a => a.key)
if (failed.length) log(`Research agents with no result: ${failed.join(', ')}`)

phase('Synthesis')
const digest = ok.map(r => `### ${r.title}\nKEY NUMBERS:\n${r.key_numbers.map(k => `- ${k.metric}: ${k.value} (${k.source})`).join('\n')}\nOPPORTUNITIES:\n${r.opportunities.map(o => `- ${o.name} [score ${o.attractiveness_1_to_10}, capex ${o.capex_level}, risk ${o.risk_level}, ${o.time_to_revenue}, model: ${o.business_model}] — ${o.description} | Market: ${o.demand_or_market_size}`).join('\n')}\n\nFULL REPORT:\n${r.report_markdown}`).join('\n\n---\n\n')

const memo = await agent(`You are the Chief Strategy Officer of a mid-to-large EU aluminium company (primary, casthouse, rolling/extrusion, recycling). Today is ${TODAY}. A swarm of ${ok.length} specialist research agents produced the reports below on future aluminium demand and future production methods (incl. robotics/AI).

Write the CEO STRATEGY MEMO in Markdown. Structure:
# Aluminium 2040: New Business Opportunities — CEO Strategy Memo
1. Executive summary (8-10 bullets, the big picture in numbers: global & EU demand outlook 2030/2040, where growth comes from)
2. Demand map — a table of demand segments with tonnage today vs 2030/2035, CAGR, EU relevance, margin potential
3. How aluminium will be produced in 2040 — robotics, AI, green primary, recycling: what changes and what it means for cost & competitiveness
4. Ranked opportunity portfolio — a table of the top 10-12 opportunities (deduplicate across reports) with: score, business model, capex, time-to-revenue, risk, and a one-line rationale. Group into horizons: H1 quick wins (0-2y), H2 build (2-5y), H3 bets (5-10y+)
5. Deep dives on the top 3 opportunities (what to do, partners/targets, rough investment, KPIs)
6. Robotics special focus: (a) robotics as a demand market, (b) robotics in our own plants — a combined play
7. Key risks & counter-moves (energy prices, Chinese overcapacity, CBAM leakage, scrap export, tech failure)
8. 90-day action plan for the executive team
9. Where the research disagrees or is uncertain (be honest about weak numbers)
Be decisive and specific; cite the most important numbers with their sources. Don't invent sources — only use those in the reports.

RESEARCH REPORTS:
${digest}`, { label: 'synthesis:ceo-memo', phase: 'Synthesis', effort: 'high' })

return { memo, reports: ok.map(r => ({ key: r.key, title: r.title, report_markdown: r.report_markdown, key_numbers: r.key_numbers, opportunities: r.opportunities })), failed }
