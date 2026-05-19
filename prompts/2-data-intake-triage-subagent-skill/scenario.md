# Prompt 2: Data Intake Triage (Custom Subagent + Skills)

## Troublesome scenario
Incoming field files are inconsistent (types, nulls, and unexpected values). Analysts lose time building repetitive cleaning code and validation checks.

## How Copilot helps
A dedicated subagent can own data intake triage while reusable skills apply standard checks for schema, missingness, and contamination thresholds.

## Sample prompt
"Use the Data Intake Auditor subagent and schema-check skill to inspect `../data/water_technicians_collections.csv`, generate cleaning code, and return a cleaned dataframe plus a quality checklist."

## Agent customization
Use `subagent-and-skills.yml` to define a specialized subagent with reusable cleaning skills.
