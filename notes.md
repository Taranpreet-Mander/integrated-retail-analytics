# notes

## what this is

retail analytics practice. two sides: descriptive analytics (whats happening in
the sales data) and clustering (grouping stores). picked it because retail data
has holidays, seasonality and economic features which make for interesting EDA.

## what i learned

- pandas groupby + agg is the workhorse for this. holiday lift was just a
  groupby("IsHoliday").mean() and comparing the two.
- for clustering you have to StandardScaler first, otherwise "Size" (hundreds of
  thousands) totally dominates "unemployment" (single digits) and the clusters
  are basically just sorting by size.
- i build one row per store (aggregating the weekly rows) before clustering -
  you cluster the stores, not every weekly record.
- KMeans needs you to pick k. i just used 3 (big/medium/small-ish). should really
  use the elbow method to choose it properly - noted as a todo.

## honest notes

- sample data is SYNTHETIC (generate_sample.py). real walmart data is messier and
  has more columns (markdowns, multiple years). numbers here are illustrative.
- the two "big store" clusters (0 and 2) are kind of similar - with k=3 it split
  them partly on unemployment. with better k selection this'd be cleaner.

## todo
- demand forecasting (predict next weeks sales)
- elbow/silhouette for choosing k
- markdown impact analysis
- charts in a notebook
