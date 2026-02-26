# Data Lifecycle Rules

## Folder Purpose
- `raw/` contains original source files exactly as received.
- `processed/` contains cleaned or transformed datasets derived from `raw/`.

## Non-Negotiable Rules
- Never modify files inside `raw/`.
- Every file in `processed/` must be reproducible from `raw/`.
- Scripts should only read from `raw/` and write to `processed/`.
- Keep file names meaningful and stage-specific.

## Naming Examples
- `raw/tourism_2024_source.csv`
- `processed/tourism_2024_cleaned_v1.csv`
- `processed/tourism_monthly_aggregated_v1.parquet`
