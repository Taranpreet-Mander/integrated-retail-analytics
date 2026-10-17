# Integrated Retail Analytics

a data analytics project on retail (walmart-style) weekly sales data. two parts:

1. **analysis** - answer the questions a retail analyst would ask: how big is the holiday boost? which stores/departments sell most? whats the seasonal trend?
2. **store segmentation** - use KMeans clustering to group similar stores, so you could optimise stocking/staffing/promotions per group instead of per store.

did this to practice pandas (groupby, aggregation) and unsupervised learning (clustering).

## the data

based on the classic **Walmart retail / store sales** datasets on Kaggle (weekly sales per store + department, with holiday flags and economic indicators like CPI, fuel price, unemployment).

> ⚠️ the committed `data/sample_sales.csv` is **synthetic** - i wrote `generate_sample.py` to make realistic fake data (bigger stores sell more, holidays boost sales, nov/dec peaks) so everything runs with no download. real data will look different. point the scripts at a real csv with `--data`.

## how to run

```bash
pip install -r requirements.txt
python generate_sample.py      # make the synthetic sample
python analysis.py             # EDA summary
python cluster_stores.py       # segment stores (KMeans)
```

## part 1 - analysis (sample output)

```
total sales:        47,164,860
avg weekly sales:   18,140

avg sales  non-holiday: 17,627
avg sales  holiday:     24,295  (+37.8%)

top stores: 5, 8, 6, 2 ...
top depts:  1, 4, 2, 3, 5
```

key findings on the sample:
- **holidays give a ~38% sales lift** - big deal for inventory planning
- **sales peak in Nov/Dec** (seasonal), with a smaller summer bump
- a handful of large stores drive most of the revenue

## part 2 - store clustering (sample output)

```
cluster 0: stores [2, 5]           avg weekly sales ~ 25,944, size ~ 169,444
cluster 1: stores [1,3,4,7,9,10]   avg weekly sales ~ 12,929, size ~ 71,575
cluster 2: stores [6, 8]           avg weekly sales ~ 25,969, size ~ 166,498
```

clustered stores on avg weekly sales, size, and local unemployment (scaled first with StandardScaler). it cleanly separates the big high-revenue stores from the smaller ones - which is exactly the kind of segmentation you'd use to decide where to push promotions.

## what i'd improve

- [ ] actual demand forecasting (predict next week's sales) - maybe a time-series model or regression
- [ ] markdown/promotion impact analysis (the real dataset has markdown columns)
- [ ] pick the number of clusters properly (elbow method / silhouette) instead of just k=3
- [ ] a notebook with real charts instead of ascii bars
- [ ] anomaly detection for weird sales spikes/drops

## stack
python, pandas, scikit-learn

MIT license.
