# Output Artifacts Rules

## Folder Purpose
- `figures/` stores plots and charts.
- `reports/` stores summaries, tables, and exported documentation.
- `models/` stores trained model artifacts.

## Non-Negotiable Rules
- Do not store outputs inside `data/raw/` or `data/processed/`.
- Use descriptive names so outputs are easy to review.
- Treat outputs as derived artifacts that can be regenerated.

## Naming Examples
- `figures/visitor_trend_2024.png`
- `reports/tourism_summary_q1_2026.pdf`
- `models/linear_regression_visitors_v1.pkl`
