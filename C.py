import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime 
import calendar 

file = pd.read_csv("activity.csv")

print("Total number of NA in old dataset:")
print(pd.isnull(file).sum())

new_file = file.fillna(0)
print("Total number of NA in new dataset:")
print(pd.isnull(new_file).sum())

days = []
steps = []
for data in new_file["date"].unique():
    days.append(data)
    steps.append(new_file.loc[new_file["date"]==data, "steps"].dropna().sum())
    
graphdata = pd.DataFrame({"Days":days, "Steps":steps})

graph = graphdata.plot.bar(x="Days", y="Steps", width=0.5, color="r") 
plt.title("Total Number of Steps Taken per Day")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.show()

print(f"Mean: {graphdata.mean().item()}")
print(f"Median: {graphdata.median().item()}")