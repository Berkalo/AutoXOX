import pandas as pd
import numpy as np

df = pd.read_csv("2000000_sampl_unique.csv",
                 sep =',',
                 names =["p1-1","p1-2","p1-3","p1-4","p1-5",
                  "p2-1","p2-2","p2-3","p2-4","p2-5",
                  "L1","L2","L3","L4",
                  "Win_Mov_T",
                  "Winner",])


df = df.iloc[1:]
print(df.head(4))
print(df.describe())
print(df.info)

df["Winner"] = df["Winner"].astype("category")

print(df.head(4))
print(df.describe())
print(df.info)
