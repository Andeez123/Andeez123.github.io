import numpy as np
import pandas as pd

df = pd.read_csv("cumulative-people-space.csv")
totals = pd.DataFrame(df.groupby(["Entity", "Code"])["Cumulative_number"].max().reset_index())
totals.rename(columns={"Cumulative_number": "Total_People"}, inplace=True)
totals = totals.sort_values(by="Total_People", ascending=False)
totals.to_csv("cumulated.csv", index=False)
