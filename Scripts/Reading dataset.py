import pandas as pd
import numpy as np

df_traffic = pd.read_csv("../data/Data-Collisions.csv")
x = len(df_traffic.columns)
pd.set_option("display.max_columns", x)
df_traffic100 = df_traffic.head(100)
print(df_traffic100.head())
print(x)




