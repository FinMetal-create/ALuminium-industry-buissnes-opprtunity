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

Script: [`.claude/workflows/aluminium-opportunity-swarm.js`](.claude/workflows/aluminium-opportunity-swarm.js) (Claude Code Workflow).

## Outputs

`reports/` – CEO memo and one report per specialist agent.
