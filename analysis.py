"""
basic EDA on the weekly sales data - the kind of questions a retail analyst asks.

usage:
    python analysis.py                 # uses data/sample_sales.csv
    python analysis.py --data real.csv
"""
import argparse

import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/sample_sales.csv")
    args = ap.parse_args()

    df = pd.read_csv(args.data, parse_dates=["Date"])
    print(f"[*] {len(df)} rows, {df['Store'].nunique()} stores, {df['Dept'].nunique()} depts\n")

    total = df["Weekly_Sales"].sum()
    print(f"total sales:        {total:,.0f}")
    print(f"avg weekly sales:   {df['Weekly_Sales'].mean():,.0f}")

    # holiday weeks tend to sell more - by how much?
    hol = df.groupby("IsHoliday")["Weekly_Sales"].mean()
    lift = (hol[1] / hol[0] - 1) * 100
    print(f"\navg sales  non-holiday: {hol[0]:,.0f}")
    print(f"avg sales  holiday:     {hol[1]:,.0f}  (+{lift:.1f}%)")

    print("\ntop 5 stores by total sales:")
    top_stores = df.groupby("Store")["Weekly_Sales"].sum().sort_values(ascending=False).head()
    for store, s in top_stores.items():
        print(f"  store {store:<3} {s:,.0f}")

    print("\nsales by department:")
    by_dept = df.groupby("Dept")["Weekly_Sales"].sum().sort_values(ascending=False)
    for dept, s in by_dept.items():
        print(f"  dept {dept:<3} {s:,.0f}")

    print("\nsales by month:")
    monthly = df.groupby(df["Date"].dt.month)["Weekly_Sales"].sum()
    for m, s in monthly.items():
        bar = "#" * int(s / monthly.max() * 30)
        print(f"  {m:>2}  {bar} {s:,.0f}")


if __name__ == "__main__":
    main()
