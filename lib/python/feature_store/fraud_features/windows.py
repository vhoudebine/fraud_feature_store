import pandas as pd

def LaggedSum(df, id_col, order_col, agg_col):
	lagged_sum = df.sort_values(by=order_col).groupby(id_col)[agg_col].transform(pd.Series.cumsum)
	return lagged_sum