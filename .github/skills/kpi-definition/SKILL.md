---
name: kpi-definition
description: "Standardize water purity, alert-rate, and site-risk metrics. Use when defining KPI calculations, ensuring metric consistency across reports, or setting up a new KPI pipeline."
user-invocable: true
---
# KPI Definition

Standardized definitions and computation procedures for water operations KPIs.

## Core KPIs

### Purity Score (Site Average)
- **Formula**: `mean(purity_score)` per `site_id` over reporting period
- **Benchmark**: ≥ 85 = Good, 75–84 = Acceptable, < 75 = At Risk

### Alert Rate
- **Formula**: `count(contamination_flag = 1) / count(*)`  per site per period
- **Benchmark**: < 5% = Normal, 5–15% = Elevated, > 15% = Critical

### Site Risk Score
- **Formula**: `(1 - purity_score/100) * 0.6 + alert_rate * 0.4`
- **Benchmark**: < 0.15 = Low, 0.15–0.30 = Medium, > 0.30 = High

## When to Use
- Before computing KPIs to confirm formula alignment
- When onboarding a new reporting period or data source
- To resolve discrepancies between reports

## Procedure
1. Confirm reporting period and `site_id` scope
2. Apply formulas above using validated data
3. Attach benchmark classification to each metric
4. Flag any KPIs computed from < 10 records (insufficient sample)
