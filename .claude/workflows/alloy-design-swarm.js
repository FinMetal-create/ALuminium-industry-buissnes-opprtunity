export const meta = {
  name: 'alloy-design-swarm',
  description: 'Swarm researching AI-driven aluminium alloy design (scrap-tolerant, casting, conductor/thermal, advanced alloys, IP) for an EU aluminium CEO, synthesised into a strategy refined by a CEO review loop',
  phases: [
    { title: 'Research', detail: '6 specialist agents on alloy design themes' },
    { title: 'Synthesis', detail: 'CTO/CSO writes alloy design strategy with business cases' },
    { title: 'CEO Review', detail: 'Results-driven CEO grades against hard criteria' },
    { title: 'Gap Research', detail: 'Agents close each gap the CEO flags' },
    { title: 'Revise', detail: 'Strategy rewritten; loop back to CEO review' },
  ],
}

const TODAY = '2026-10-25'
const CONTEXT = `You are part of a research swarm for the CEO of a mid-to-large EU aluminium company: a ~300 kt/yr primary smelter with casthouse, rolling mill, extrusion, and a planned 100 kt/yr AI scrap-sorting hub. Planning basis from the company's board paper: LME normalised US$2,500/t = EUR 2,155/t; recycled metal ~0.5 t CO2/t vs ~16 t for primary; EU exported a record 1.27 Mt of scrap in 2025; scrap grade spreads of 8-20 points of LME. Today is ${TODAY}.
TOPIC: ALLOY DESIGN in the age of AI — how new aluminium alloys (and AI/ML-driven alloy development) create business opportunities.
Use WebSearch and WebFetch (load with ToolSearch "select:WebSearch,WebFetch"). Prefer 2023-2026 sources: journals (Acta Materialia, Nature, npj Computational Materials), conference papers (TMS Light Metals, ICAA), company releases (Hydro, Novelis, Constellium, Alcoa, Speira, AMAG, Rheinfelden, Tesla, Rio Tinto, Elementum 3D, HRL, Equispheres), Aluminum Association registrations, patent databases (Google Patents, Espacenet), EU programmes. Quantify: market sizes, tonnages, price premiums (EUR/t), development time and cost, qualification time. Cite URLs inline. Mark estimates [est.]. If a source is blocked, say so and give a reasoned estimate with a range — never invent a source.
report_markdown: thorough Markdown section (1200-2000 words) with headings, a key numbers table, named players/alloys, and a "So what for our company" section.`

const AGENTS = [
  { key: 'ai-alloy-informatics', title: 'AI & Materials Informatics for Alloy Design',
    focus: `State of the art in AI/ML-driven alloy design: CALPHAD + ML surrogates, Bayesian optimisation/active learning, generative models, physics-informed ML, LLM agents for materials, autonomous/self-driving labs and high-throughput testing (robotic sample prep, rapid casting, automated tensile testing). Vendors and tools: Thermo-Calc, Citrine Informatics, QuesTek (ICME), Materials Design, Intellegens (Alchemite), Polymerize, Ansys Granta, MatterGen/GNoME relevance to metals. Documented aluminium examples (alloys discovered or optimised by ML; industry programmes at Novelis, Hydro, Constellium, Alcoa, Speira; academic groups like Max Planck Düsseldorf, NTNU/SINTEF, Leoben, RWTH). Evidence on time and cost reduction vs. classic alloy development. What team, data, software and lab capex a company needs to build this capability.` },
  { key: 'scrap-tolerant-alloys', title: 'Scrap-Tolerant, High-Recycled-Content & Crossover Alloys',
    focus: `Alloys designed to absorb post-consumer scrap: tolerance of Fe, Cu, Zn, Si, Mn, Cr impurities; Fe-intermetallic modification (Mn, Cr, Sr, Ca, rapid solidification); crossover alloys (AlMgZn(Cu), e.g. AMAG/Montanuniversität Leoben), "universal"/unified alloys and the push to reduce the number of wrought alloys; high-recycled-content products (Hydro CIRCAL, Novelis high-recycled-content sheet, Constellium, Speira, Apple/automotive specs); EN/AA specification barriers. AI-driven casthouse scrap blending and real-time charge optimisation (vendors, deployed cases, savings in EUR/t). Quantify the economic value of impurity tolerance: how much cheaper scrap (points of LME) a given tolerance unlocks, and the resulting EUR/t and EUR m/yr value for a 300 kt producer.` },
  { key: 'structural-casting-robotics-alloys', title: 'Structural Casting, Gigacasting & Robot-Grade Alloys',
    focus: `Non-heat-treatable HPDC structural alloys for giga/mega-casting (Alcoa C611 EZCast, Rheinfelden Castasil/Castaduct/Magsimal, Tesla's patented alloy, Chinese alloys from LK/Lizhong/Wencan suppliers, Hydro, Speira, Trimet), recycled-content versions, ductility/crash requirements, ingot premiums vs. standard foundry alloy. Robot-grade alloys: high-strength 6xxx/7xxx extrusion and machining billet/plate for humanoids/cobots/drones, thin-wall high-conductivity casting alloys for motor and actuator housings, competition with magnesium, PEEK, CFRP. Tonnages, premiums, OEM qualification timelines, and where AI-designed alloys could win.` },
  { key: 'electrical-thermal-alloys', title: 'Electrical Conductor, Battery & Thermal Management Alloys',
    focus: `Alloys for electrification and AI data centres: overhead conductors (1350, 6201 AAAC, heat-resistant Al-Zr TAL/ZTAL for HTLS, ACCC cores), 8xxx (8030/8176) building wire and cables replacing copper, busbars, transformer windings, high-conductivity casting alloys for e-motor rotors, battery foil (1xxx/8xxx) and cell cans, high-thermal-conductivity alloys for liquid-cooling cold plates, heat sinks and immersion cooling in data centres. Cu->Al substitution economics at a Cu/Al price ratio of ~4.9x. Market sizes in tonnes and premiums over P1020 (EUR/t), EU players (Nexans, Prysmian, NKT, Lamifil, Midal, Gränges, Speira, Hydro). Where AI-optimised alloys (strength-conductivity trade-off) create an edge.` },
  { key: 'advanced-alloys', title: 'Advanced Alloys: AM, Scandium, Al-Li, Al-Ce & Nano-Modified',
    focus: `Additive manufacturing alloys (AlSi10Mg, Scalmalloy, A20X, Al-Zr/Al-Ce, HRL/Elementum 3D 7A77 nano-functionalised, Constellium Aheadd, Equispheres, 6K), powder and WAAM wire markets; scandium (supply ~30-40 t/yr Sc2O3, China export controls Apr 2025, Rio Tinto, Sc recovery from bauxite residue/red mud projects in EU e.g. SCALE/ScaVanger), Sc-lean substitutes (Zr, Er, Yb) and ML searches for them; Al-Li (Constellium Airware, Arconic, Novelis), Al-Ce alloys (ORNL/Eck), high-temperature Al alloys, nano-modified and metal-matrix composites, high-entropy alloys relevance. Market sizes, prices EUR/kg, margins, and which are investable for an EU producer by 2030-2035.` },
  { key: 'ip-qualification-business', title: 'Alloy IP, Qualification & Business Models',
    focus: `How companies make money from alloy innovation: alloy patent landscape for aluminium 2015-2026 (who files most: Novelis, Arconic/Howmet, Alcoa, Constellium, Hydro, Chinese players; Tesla), Aluminum Association teal-sheet registration, EN standards, licensing models and royalty levels, proprietary alloy price premiums (EUR/t), qualification timelines and costs by sector (automotive PPAP, aerospace AMS/OEM, defence, electrical utilities, consumer electronics like Apple's recycled alloys), joint development agreements with OEMs. EU funding for alloy/AI materials work: Horizon Europe, Processes4Planet, Made in Europe, Clean Industrial Deal, IPCEI, national programmes. Recommend a business model for an EU producer with a casthouse.` },
]

const OPP_SCHEMA = {
  type: 'object',
  properties: {
    name: { type: 'string' }, description: { type: 'string' },
    demand_or_market_size: { type: 'string' }, business_model: { type: 'string' },
    capex_level: { type: 'string', enum: ['low', 'medium', 'high', 'very high'] },
    time_to_revenue: { type: 'string' }, risk_level: { type: 'string', enum: ['low', 'medium', 'high'] },
    attractiveness_1_to_10: { type: 'number' }, key_sources: { type: 'array', items: { type: 'string' } },
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
  agent(`${CONTEXT}\n\nYOUR SPECIALIST AREA: ${a.title}\n${a.focus}\n\nReturn: report_markdown (start with "## ${a.title}"), key_numbers, and 3-6 concrete opportunities scored for our company.`,
    { label: `research:${a.key}`, phase: 'Research', schema: REPORT_SCHEMA })
    .then(r => r ? { ...a, ...r } : null)))
const ok = results.filter(Boolean)
const failed = AGENTS.filter(a => !ok.find(r => r.key === a.key)).map(a => a.key)
if (failed.length) log(`Research agents with no result: ${failed.join(', ')}`)

phase('Synthesis')
const digest = ok.map(r => `### ${r.title}\nKEY NUMBERS:\n${r.key_numbers.map(k => `- ${k.metric}: ${k.value} (${k.source})`).join('\n')}\nOPPORTUNITIES:\n${r.opportunities.map(o => `- ${o.name} [score ${o.attractiveness_1_to_10}, capex ${o.capex_level}, risk ${o.risk_level}, ${o.time_to_revenue}, ${o.business_model}] — ${o.description} | Market: ${o.demand_or_market_size}`).join('\n')}\n\nFULL REPORT:\n${r.report_markdown}`).join('\n\n---\n\n')

const memo = await agent(`You are the CTO and Chief Strategy Officer of a mid-to-large EU aluminium company (300 kt smelter, casthouse, rolling, extrusion, planned 100 kt AI scrap hub). Today is ${TODAY}. ${ok.length} specialist research agents produced the reports below on alloy design in the age of AI.

Write the ALLOY DESIGN STRATEGY memo in Markdown:
# Alloy Design in the Age of AI — Strategy Memo
1. Executive summary (8-10 bullets with numbers)
2. How AI changes alloy development (what is proven vs hype; time/cost evidence)
3. Alloy opportunity map — table: alloy family, end market, tonnage 2030/2035, premium EUR/t over standard, qualification time, our right to win
4. Ranked portfolio (8-10 opportunities) with GO / NO-GO / WATCH, capex, time-to-revenue, risk, score, gate
5. Business case A: scrap-tolerant alloys + AI casthouse blending (EUR/t value, EUR m/yr, capex/opex, payback, partners, milestones)
6. Business case B: electrical conductor & thermal-management alloys (Cu->Al substitution, data centres, grid) — same depth
7. Building the capability: alloy-informatics team, data, software, autonomous lab, partners, budget by year, build vs buy vs partner
8. IP & commercial model: patents, licensing, ingot premiums, OEM joint development, EU funding to tap
9. Risks & counter-moves
10. 90-day action plan (owners by role, deliverables, budget, KPIs)
11. Evidence quality: what is sourced vs estimated, open data items with owners
Be decisive; cite sources from the reports only.

RESEARCH REPORTS:
${digest}`, { label: 'synthesis:alloy-strategy', phase: 'Synthesis', effort: 'high' })

const CRITERIA = `SUCCESS CRITERIA (all must be met for APPROVED):
1. Every portfolio opportunity has a quantified market (tonnes or EUR, with year) and a cited source, or a clearly-labelled reasoned estimate with range.
2. Business cases A and B each give: EUR/t value mechanism, EUR m/yr at maturity, capex and opex, payback/IRR, named partners/customers/vendors, and 12-month milestones. The arithmetic must be shown and reproducible.
3. The AI claim is evidence-based: documented aluminium cases of ML-designed or ML-optimised alloys, and an honest view of what AI does NOT shorten (qualification).
4. The capability build has a year-by-year budget, headcount, software/lab capex, and an explicit build vs buy vs partner decision.
5. The IP/commercial model names target patents/white space, licensing terms or premium assumptions, and at least two concrete EU funding instruments with amounts.
6. Clear GO / NO-GO / WATCH per opportunity, no vague language.
7. 90-day plan has owners (by role), deliverables, budget and KPIs.
8. Numbers are internally consistent. Data that cannot be obtained from public sources is acceptable ONLY if labelled, bounded with a range, and assigned an internal owner and date to close it.`

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['APPROVED', 'REJECTED'] },
    score_1_to_10: { type: 'number' },
    failed_criteria: { type: 'array', items: { type: 'string' } },
    gaps: { type: 'array', items: { type: 'object', properties: { task: { type: 'string' }, why: { type: 'string' } }, required: ['task', 'why'] } },
    ceo_feedback: { type: 'string' },
  },
  required: ['verdict', 'score_1_to_10', 'failed_criteria', 'gaps', 'ceo_feedback'],
}

const MAX_ROUNDS = 4
const GAPS_PER_ROUND = 3
let current = memo
let approved = false
const reviewHistory = []
const gapResearch = []
for (let round = 1; round <= MAX_ROUNDS; round++) {
  phase('CEO Review')
  const review = await agent(`You are the CEO of a mid-to-large EU aluminium company. You are extremely results-driven: the team cannot stop until this alloy strategy is investable and board-ready. Today is ${TODAY}.
Grade strictly against the criteria. Any criterion not fully met => REJECTED. Score honestly (9+ only if board-ready tomorrow). List up to ${GAPS_PER_ROUND} concrete, web-researchable tasks that would close the gaps, most important first. Do not re-request data the memo has already shown to be unobtainable publicly if it is labelled, bounded and owned per criterion 8.

${CRITERIA}

PREVIOUS ROUNDS: ${reviewHistory.length ? JSON.stringify(reviewHistory.map(r => ({ round: r.round, score: r.score_1_to_10, failed: r.failed_criteria }))) : 'none'}

ALLOY STRATEGY MEMO (round ${round}):
${current}`, { label: `ceo-review:r${round}`, phase: 'CEO Review', schema: REVIEW_SCHEMA, effort: 'high' })
  if (!review) { log(`Round ${round}: review agent failed`); continue }
  reviewHistory.push({ round, ...review })
  log(`Round ${round}: ${review.verdict} — ${review.score_1_to_10}/10, ${review.failed_criteria.length} criteria failed`)
  if (review.verdict === 'APPROVED') { approved = true; break }
  if (round === MAX_ROUNDS) break

  const gaps = review.gaps.slice(0, GAPS_PER_ROUND)
  if (review.gaps.length > GAPS_PER_ROUND) log(`Round ${round}: ${review.gaps.length - GAPS_PER_ROUND} lower-priority gaps deferred`)
  const fills = (await parallel(gaps.map((g, i) => () =>
    agent(`${CONTEXT}\n\nThe CEO REJECTED the alloy strategy memo and needs this gap closed:\nTASK: ${g.task}\nWHY: ${g.why}\n\nResearch thoroughly. Return a focused Markdown brief (500-1000 words) with quantified findings, explicit calculations, assumptions and source URLs. If data does not exist publicly, give a reasoned estimate with range and say which internal function could close it.`,
      { label: `gap-research:r${round}-${i + 1}`, phase: 'Gap Research' })
      .then(t => t ? { round, task: g.task, brief: t } : null)))).filter(Boolean)
  gapResearch.push(...fills)

  phase('Revise')
  const revised = await agent(`You are the CTO/CSO. The CEO rejected your alloy strategy memo (score ${review.score_1_to_10}/10).
CEO FEEDBACK: ${review.ceo_feedback}
FAILED CRITERIA: ${review.failed_criteria.join(' | ')}

${CRITERIA}

NEW GAP RESEARCH:
${fills.map(f => `### ${f.task}\n${f.brief}`).join('\n\n')}

Rewrite the FULL memo (same structure), fix every failed criterion, integrate new research with sources. Output only the complete revised Markdown memo.

CURRENT MEMO:
${current}`, { label: `revise:r${round}`, phase: 'Revise', effort: 'high' })
  if (revised) current = revised
}
if (!approved) log(`Stopped after ${MAX_ROUNDS} rounds without CEO approval — final memo is the best version so far`)

return { memo: current, initial_memo: memo, approved, review_history: reviewHistory, gap_research: gapResearch, failed,
  reports: ok.map(r => ({ key: r.key, title: r.title, report_markdown: r.report_markdown, key_numbers: r.key_numbers, opportunities: r.opportunities })) }
