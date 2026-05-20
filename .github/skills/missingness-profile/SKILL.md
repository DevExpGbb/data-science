---
name: missingness-profile
description: "Report null percentages and recommended imputations for water quality data. Use when profiling missing data, deciding imputation strategy, or assessing data completeness."
user-invocable: true
argument-hint: "Path to data file or DataFrame variable name"
---
# Missingness Profile

Profile null/missing values and recommend imputation strategies.

## When to Use
- Before model training or KPI computation
- When missing data percentage is unknown
- When deciding between imputation strategies

## Procedure
1. Compute per-column null counts and percentages
2. Classify missingness severity:
   - **Low** (< 5%): safe to impute with median/mode
   - **Medium** (5–20%): impute with care; flag in output
   - **High** (> 20%): warn; consider dropping column or using forward-fill for time series
3. Recommend imputation method per column based on dtype and missingness pattern
4. Check for systematic missingness patterns (e.g., always null for a specific `site_id`)

## Output
| Column | Null % | Severity | Recommended Action |
|--------|--------|----------|--------------------|
| ...    | ...    | ...      | ...                |

Plus a summary of any systematic patterns found.
