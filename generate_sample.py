"""
makes a SYNTHETIC weekly-sales dataset (walmart-style) so the analysis scripts
run without downloading anything.

NOT real data. the real "Walmart / retail analytics" datasets are on kaggle.
i generate fake rows with realistic patterns (bigger stores sell more, holidays
boost sales, nov/dec is higher) so the analysis + clustering actually show something.
"""
import csv
import math
import random
from datetime import date, timedelta

random.seed(7)

TYPE_BASE = {"A": 25000, "B": 16000, "C": 9000}       # avg dept sales by store type
TYPE_SIZE = {"A": (150000, 200000), "B": (90000, 140000), "C": (30000, 80000)}
DEPTS = [1, 2, 3, 4, 5]
DEPT_MULT = {1: 1.4, 2: 1.0, 3: 0.7, 4: 1.2, 5: 0.5}  # some depts sell more


def main(out="data/sample_sales.csv"):
    stores = {i: random.choice(["A", "B", "C"]) for i in range(1, 11)}
    store_size = {s: random.randint(*TYPE_SIZE[t]) for s, t in stores.items()}

    start = date(2025, 1, 3)
    weeks = [start + timedelta(weeks=w) for w in range(52)]
    # a few holiday weeks (super bowl, labour day, thanksgiving, christmas-ish)
    holidays = {weeks[i] for i in (5, 35, 46, 51)}

    rows = []
    for s, t in stores.items():
        unemployment = round(random.uniform(5, 9), 3)
        cpi = round(random.uniform(210, 225), 3)
        for wk in weeks:
            month = wk.month
            seasonal = 1.0 + (0.25 if month in (11, 12) else 0) + (0.1 if month in (6, 7) else 0)
            temp = round(50 + 25 * math.sin((wk.timetuple().tm_yday / 365) * 2 * math.pi - 1.3)
                         + random.gauss(0, 5), 1)
            fuel = round(random.uniform(2.6, 3.9), 3)
            is_hol = wk in holidays
            for d in DEPTS:
                base = TYPE_BASE[t] * DEPT_MULT[d] * seasonal
                if is_hol:
                    base *= 1.3
                sales = round(max(0.0, base * random.uniform(0.85, 1.15)), 2)
                rows.append([s, d, wk.isoformat(), sales, int(is_hol),
                             temp, fuel, cpi, unemployment, t, store_size[s]])

    fields = ["Store", "Dept", "Date", "Weekly_Sales", "IsHoliday",
              "Temperature", "Fuel_Price", "CPI", "Unemployment", "Type", "Size"]
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(fields)
        w.writerows(rows)
    print(f"wrote {len(rows)} rows ({len(stores)} stores x {len(DEPTS)} depts x {len(weeks)} weeks) -> {out}")


if __name__ == "__main__":
    main()
