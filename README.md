# Aluminium Industry – Business Opportunity Swarm

A swarm of AI research agents that scans **future aluminium demand** and **how aluminium will be produced** (robotics, AI, green primary, recycling) for an EU aluminium company, and synthesises a CEO strategy memo.

## Swarm design

| # | Agent | Focus |
|---|-------|-------|
| 1 | robotics-demand | Humanoids, industrial robots, drones – kg Al/unit, tonnage 2030–2040 |
| 2 | mobility-demand | EVs, battery enclosures, gigacasting |
| 3 | energy-digital-demand | Solar, grids (Cu→Al), BESS, AI data centres |
| 4 | packaging-construction-defence | PPWR, renovation wave, aerospace, EU defence |
| 5 | robotics-automation-production | Potroom/casthouse robots, AI process control, robotic scrap sorting |
| 6 | green-primary-production | Inert anodes, HalZero, flexible smelting, power |
| 7 | recycling-circular | Scrap flows, upgrading, closed loops |
| 8 | policy-markets-advanced-mfg | CBAM, CRMA, China, AM powders, Al batteries |
| 9 | synthesis | CEO strategy memo with ranked opportunity portfolio |
| ∞ | **CEO review loop** | Results-driven CEO grades the memo against 8 hard success criteria. Every rejection spawns gap-research agents and a full rewrite — the swarm does not stop until the CEO approves (6-round runaway backstop, reported if hit). |

### Success criteria the CEO enforces
1. Every opportunity quantified (tonnes/EUR + year) with a cited source
2. Top 3 opportunities have a full business case: capex, revenue, EBITDA margin, payback/IRR, named partners, 12-month milestones
3. Robotics demand calculated explicitly (kg Al/unit × units) for 2030/2035, low/base/high
4. Robotics/AI in our own plants: EUR/t savings, capex, vendors, adopt vs co-develop vs sell decision
5. EU competitiveness: power price, CBAM EUR/t, Chinese overcapacity — and our response
6. 90-day plan with owners, deliverables, budget, KPIs
7. GO / NO-GO / WATCH per opportunity — no vague language
8. Internally consistent numbers

Script: [`.claude/workflows/aluminium-opportunity-swarm.js`](.claude/workflows/aluminium-opportunity-swarm.js) (Claude Code Workflow).

## Outputs

`reports/` – CEO memo and one report per specialist agent.

## Run outcome (21 Oct 2026)

**Score went from 5.5/10 to 8.9/10 over 6 rounds. Not yet approved.**

| Round | Verdict | Score | Criteria failed |
|---|---|---|---|
| 1 | Rejected | 5.5 | 8 |
| 2 | Rejected | 7.4 | 4 |
| 3 | Rejected | 8.1 | 3 |
| 4 | Rejected | 8.5 | 3 |
| 5 | Rejected | 8.8 | 3 |
| 6 | Rejected | 8.9 | 2 |

The swarm ran 49 agents in total. The CEO checked the arithmetic and it holds. The four small fixes from round 6 have been applied.

**What still blocks approval:** four facts that need normal corporate access. The research environment's network policy blocked EEX, Eurostat, EUR-Lex and the metal price services, so the agents could not fetch them.

| # | Missing item | Owner |
|---|---|---|
| 1 | EEX Phelix DE baseload settlements for Cal-28 to Cal-31 | Head of Energy |
| 2 | Whether a converter-foil anti-dumping expiry review was requested (duties lapse 9 Dec 2026) | General Counsel |
| 3 | Our scrap purchase prices by grade, and the Comext export unit value for HS 7602 | Procurement + Recycling |
| 4 | Comext tonnage for 2025 EU imports of Chinese semis | CSO analyst |

The CEO's position: approval without a rewrite once these are attached, unless Cal-31 settles at or below €64/MWh.

## Files

- `reports/ceo-strategy-memo.md`: final board paper (v6 plus the round-6 fixes)
- `reports/ceo-strategy-memo-v1-initial.md`: first draft
- `reports/ceo-review-log.md`: the CEO's verdict, feedback and gap tasks for every round
- `reports/research/`: the 8 specialist reports
- `reports/gap-research/`: 20 gap-closing briefs

## Alloy design swarm (25 Oct 2026)

Script: [`.claude/workflows/alloy-design-swarm.js`](.claude/workflows/alloy-design-swarm.js). 6 specialist agents, a CTO/CSO synthesis, then the CEO review loop. 28 agents in total.

**Score went from 6.6/10 to 8.9/10 over 5 rounds. Not yet approved.**

| Round | Score | Criteria failed |
|---|---|---|
| 1 | 6.6 | 8 |
| 2 | 8.2 | 4 |
| 3 | 8.5 | 3 |
| 4 | 8.8 | 2 |
| 5 | 8.9 | 3 |

**What still blocks approval:** the A2 lever (paying less for lower-grade scrap) uses a typed-in spread of 8 net points. The real figure depends on our own scrap purchase mix by grade, which is internal data. On the memo's own price ladder, 4–5 points is more likely, which would bring Case A to about EUR 17–20M of NPV instead of EUR 31M.

The strategy agents wrote [`reports/appendix/alloy_board_model.py`](reports/appendix/alloy_board_model.py), a model that uses only the Python standard library and prints every figure in the memo. Run `python3 reports/appendix/alloy_board_model.py` to reproduce them.

Outputs are in `reports/alloy-design/`.
