---
name: contamination-threshold-check
description: "Flag water quality records that exceed contamination thresholds. Use when checking purity_score < 75, contamination_flag = 1, or identifying at-risk sites and records."
user-invocable: true
argument-hint: "Path to data file or DataFrame variable name"
---
# Contamination Threshold Check

Identify records that breach operational contamination thresholds.

## Thresholds
| Field | Condition | Severity |
|-------|-----------|----------|
| `purity_score` | < 75 | ⚠️ Warning |
| `purity_score` | < 50 | 🚨 Critical |
| `contamination_flag` | = 1 | 🚨 Critical |

## When to Use
- Before generating operational briefings
- When screening incoming data for safety issues
- When preparing site-risk rankings

## Procedure
1. Filter records matching any threshold condition
2. Group flagged records by `site_id` and `technician_id`
3. Compute flag rate per site (flagged records / total records)
4. Rank sites by flag rate descending
5. Identify any sites with consecutive threshold breaches (time-series pattern)

## Output
- Total flagged record count and percentage
- Per-site flag rates with severity classification
- List of consecutive-breach sites requiring immediate attention
