---
name: schema-check
description: "Validate expected columns and coercible dtypes in water quality datasets. Use when checking schema conformance, column presence, or type compatibility before analysis."
user-invocable: true
argument-hint: "Path to data file or DataFrame variable name"
---
# Schema Check

Validate that a water quality dataset conforms to the expected schema.

## When to Use
- Before any analysis pipeline runs
- When a schema mismatch error is reported
- When integrating a new data source

## Procedure
1. Load the dataset (CSV, parquet, or DataFrame)
2. Compare columns against the expected schema:
   - Required: `site_id`, `timestamp`, `purity_score`, `contamination_flag`, `technician_id`
   - Optional: `temperature`, `ph`, `turbidity`, `notes`
3. Check dtype coercibility (e.g., `purity_score` must be numeric, `timestamp` must be datetime-parseable)
4. Report any missing columns, extra columns, and type mismatches
5. Suggest corrective actions for each issue

## Output
- ✅ Pass / ❌ Fail per column
- Summary of dtype issues with suggested casts
- List of unexpected columns
