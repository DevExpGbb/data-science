import csv
from pathlib import Path


def main() -> int:
    csv_path = Path("data/water_technicians_collections.csv")
    if not csv_path.exists():
        print(f"Pre-report check failed: missing data file at {csv_path}")
        return 1

    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("Pre-report check failed: no data rows found")
        return 1

    required = {
        "collection_id",
        "site_id",
        "technician_id",
        "purity_score",
        "contamination_flag",
    }

    missing_columns = sorted(required - set(rows[0].keys()))
    if missing_columns:
        print(f"Pre-report check failed: missing columns {missing_columns}")
        return 1

    if any(not row.get("collection_id") or not row.get("site_id") for row in rows):
        print("Pre-report check failed: key identifiers contain null values")
        return 1

    print("Pre-report check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
