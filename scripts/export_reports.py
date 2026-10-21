"""Export a swarm workflow output JSON into Markdown reports under reports/."""
import json, os, sys

src, prefix = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "")
d = json.load(open(src))["result"]
os.makedirs("reports/research", exist_ok=True)

def cell(s):
    return str(s).replace("\n", " ").replace("|", "/")

for i, r in enumerate(d["reports"], 1):
    md = r["report_markdown"] + "\n\n### Key numbers\n\n| Metric | Value | Source |\n|---|---|---|\n"
    md += "\n".join(f"| {cell(k['metric'])} | {cell(k['value'])} | {cell(k['source'])} |" for k in r["key_numbers"])
    md += "\n\n### Scored opportunities\n\n| Opportunity | Score | Model | Capex | Time | Risk | Market |\n|---|---|---|---|---|---|---|\n"
    md += "\n".join(
        f"| **{cell(o['name'])}**: {cell(o['description'])} | {o['attractiveness_1_to_10']} | {cell(o['business_model'])} | "
        f"{o['capex_level']} | {cell(o['time_to_revenue'])} | {o['risk_level']} | {cell(o['demand_or_market_size'])} |"
        for o in r["opportunities"])
    open(f"reports/research/{i:02d}-{r['key']}.md", "w").write(md + "\n")

open(f"reports/{prefix}ceo-strategy-memo.md", "w").write(d["memo"])
if "initial_memo" in d:
    open("reports/ceo-strategy-memo-v1-initial.md", "w").write(d["initial_memo"])
if "review_history" in d:
    lines = [f"# CEO Review Log\n\n**Final status:** {'APPROVED' if d['approved'] else 'NOT APPROVED (round cap reached)'}\n"]
    for rv in d["review_history"]:
        lines.append(f"\n## Round {rv['round']}: {rv['verdict']} ({rv['score_1_to_10']}/10)\n\n**CEO feedback:** {rv['ceo_feedback']}\n\n**Failed criteria:**\n")
        lines += [f"- {c}" for c in rv["failed_criteria"]] or ["- none"]
        lines.append("\n**Gap tasks assigned:**\n")
        lines += [f"- {g['task']} (why: {g['why']})" for g in rv["gaps"]] or ["- none"]
    open("reports/ceo-review-log.md", "w").write("\n".join(lines) + "\n")
if d.get("gap_research"):
    os.makedirs("reports/gap-research", exist_ok=True)
    for j, g in enumerate(d["gap_research"], 1):
        open(f"reports/gap-research/r{g['round']}-{j:02d}.md", "w").write(f"# Gap task (round {g['round']})\n\n> {g['task']}\n\n{g['brief']}\n")
print("exported", len(d["reports"]), "reports")
