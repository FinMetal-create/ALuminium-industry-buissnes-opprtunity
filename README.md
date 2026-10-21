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
