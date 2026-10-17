"""
segment the stores into groups using KMeans, so you could treat similar stores
the same way (stocking, staffing, promotions). this is the "store optimization"
part of retail analytics.

usage:
    python cluster_stores.py            # uses data/sample_sales.csv
    python cluster_stores.py -k 4       # choose number of clusters
"""
import argparse

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/sample_sales.csv")
    ap.add_argument("-k", "--clusters", type=int, default=3)
    args = ap.parse_args()

    df = pd.read_csv(args.data)

    # build one row PER STORE with the features we want to cluster on
    per_store = df.groupby("Store").agg(
        avg_weekly_sales=("Weekly_Sales", "mean"),
        total_sales=("Weekly_Sales", "sum"),
        size=("Size", "first"),
        unemployment=("Unemployment", "first"),
    ).reset_index()

    features = ["avg_weekly_sales", "size", "unemployment"]
    X = StandardScaler().fit_transform(per_store[features])   # scale so big numbers dont dominate

    km = KMeans(n_clusters=args.clusters, random_state=42, n_init=10)
    per_store["cluster"] = km.fit_predict(X)

    print(f"[*] clustered {len(per_store)} stores into {args.clusters} groups\n")
    for c in sorted(per_store["cluster"].unique()):
        grp = per_store[per_store["cluster"] == c]
        print(f"cluster {c}: stores {list(grp['Store'])}")
        print(f"   avg weekly sales ~ {grp['avg_weekly_sales'].mean():,.0f}, "
              f"avg size ~ {grp['size'].mean():,.0f}")

    print("\nper-store detail:")
    print(per_store.sort_values("cluster").to_string(index=False))


if __name__ == "__main__":
    main()
