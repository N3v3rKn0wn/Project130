import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Unnamed: 0"]
del df["Unnamed: 6"]
del df["Star_name.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Luminosity"]

df.to_csv('project_results.csv')
