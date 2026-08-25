"""Module 6: Data Transformation.

Part A: Core task — average of five quality scores + conditional status.
Part B: Pipeline — clean raw exported scores, group by billing_code,
        compute average_score (0-100 scale) and status per billing code.
"""

import re
from pathlib import Path

import pandas as pd

MODULE_DIR = Path(__file__).parent
RAW_CSV = MODULE_DIR / "Exported TS Data Query Result Tue Aug 25 2026 12_50_14 GMT+0000 (Greenwich Mean Time) - Sheet1.csv"
SUMMARY_CSV = MODULE_DIR / "summary.csv"

THRESHOLD = 95.0
UNKNOWN_CODE = "unknown"
JOB_ID_PATTERN = re.compile(
    r"^(?=[A-Za-z0-9-]+$)(?=.*[a-z])(?=.*[A-Z])[A-Za-z0-9-]{13,16}$"
)


def classify(avg: float) -> str:
    return "Meeting Expectations" if avg > THRESHOLD else "Needs Improvement"


def part_a_core_task() -> None:
    scores = [85, 87, 90, 94, 88]
    avg = sum(scores) / len(scores)
    result = "Meeting Expectations" if avg > THRESHOLD else "Needs Improvement"
    print(f"Average: {avg} - {result}")


def looks_like_job_id(value: str) -> bool:
    return bool(JOB_ID_PATTERN.fullmatch(value))


def part_b_pipeline() -> pd.DataFrame:
    df = pd.read_csv(RAW_CSV)
    df.columns = [c.strip().lower() for c in df.columns]

    for col in ("job_id", "billing_code"):
        df[col] = df[col].astype(str).str.strip()

    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    before = len(df)
    df = df.dropna(subset=["score", "job_id", "billing_code"])
    dropped = before - len(df)

    mask = df["billing_code"].apply(looks_like_job_id)
    unknown_count = int(mask.sum())
    df.loc[mask, "billing_code"] = UNKNOWN_CODE

    df["score_100"] = df["score"] * 100.0

    summary = (
        df.groupby("billing_code")["score_100"]
        .agg(average_score="mean", review_count="count")
        .reset_index()
    )
    summary["average_score"] = summary["average_score"].round(2)
    summary["status"] = summary["average_score"].apply(classify)
    summary = summary.sort_values("average_score", ascending=False)

    summary.to_csv(SUMMARY_CSV, index=False)

    overall_avg = round(df["score_100"].mean(), 2)
    print("\n--- Pipeline summary ---")
    print(f"Rows read:            {before}")
    print(f"Rows dropped (bad):   {dropped}")
    print(f"Rows relabeled:       {unknown_count} -> '{UNKNOWN_CODE}'")
    print(f"Billing codes:        {summary['billing_code'].nunique()}")
    print(f"Overall average_score: {overall_avg} - {classify(overall_avg)}")
    print(f"Meeting Expectations: {(summary['status'] == 'Meeting Expectations').sum()} codes")
    print(f"Needs Improvement:    {(summary['status'] == 'Needs Improvement').sum()} codes")
    print(f"Wrote: {SUMMARY_CSV}")
    return summary


if __name__ == "__main__":
    print("=== Part A: Core Task ===")
    part_a_core_task()
    part_b_pipeline()
