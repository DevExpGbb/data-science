---
name: narrative-synthesis
description: "Convert water quality metrics into concise operations guidance. Use when writing executive summaries, translating KPIs into plain-language recommendations, or producing briefing narratives."
user-invocable: true
argument-hint: "KPI table or metrics summary to narrate"
---
# Narrative Synthesis

Convert computed metrics into concise, actionable operations language.

## When to Use
- After KPI computation to produce briefing text
- When translating technical results for non-technical stakeholders
- When generating the recommendation paragraph in a water ops briefing

## Procedure
1. Accept KPI table and trend summary as input
2. Identify the top 2–3 most operationally significant signals
3. Frame each signal in terms of business/safety impact (not raw numbers)
4. Draft a recommendation paragraph: what to act on, by whom, by when
5. Apply plain-language rules:
   - Avoid jargon; replace metric names with plain equivalents
   - Lead with risk or opportunity, not methodology
   - Use active voice

## Output Format
**5 Bullet Points** (one per key signal, prioritized by severity):
- ⚠️ / 🚨 / ✅ [Site or dimension]: [finding in plain language]

**Recommendation Paragraph** (3–5 sentences):
Focus on highest-risk site first, then systemic patterns, then next action.

## Constraints
- DO NOT invent data not present in the input metrics
- Cite uncertainty when a metric is flagged as low-sample
