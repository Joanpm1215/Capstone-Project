import pandas as pd
import numpy as np

df_traffic = pd.read_csv("Data-Collisions.csv")
df_traffic100 = df_traffic.head(100)

# print(df_traffic.columns)
print(df_traffic["SEVERITYCODE"].value_counts())


# print(df_traffic["ROADCOND"].isnull().sum())



