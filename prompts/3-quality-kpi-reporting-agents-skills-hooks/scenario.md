# Prompt 3: Quality KPI Reporting Pipeline (Agents + Skills + Hooks)

## Troublesome scenario
Teams must publish recurring KPI reports under tight deadlines, but analysts still perform manual pre-flight checks and inconsistent narrative generation.

## How Copilot helps
Agent orchestration can split work (analysis, visualization, summary), skills can standardize KPI definitions, and hooks can enforce pre-report quality gates before publishing.

## Sample prompt
"Run the reporting pipeline for `../data/water_technicians_collections.csv`: analyze purity trends, produce KPI tables and charts, then generate a leadership summary only if hook checks pass."

## Agent customization
Use `pipeline-customization.yml` and the `hooks/pre_report_check.py` hook to automate report readiness.
