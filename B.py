import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime 
import calendar 

file = pd.read_csv("activity.csv")

interval = []
steps = []

for data in file["interval"].unique():
    interval.append(data)
    steps.append(file.loc[file["interval"]==data, "steps"].dropna().mean())

graphdata = pd.DataFrame({"Interval":interval, "Steps":steps})

graphdata.plot.line(x="Interval", y="Steps", figsize=(10,10))
plt.xlabel("Interval")
plt.ylabel("Steps")
plt.show()

print(f"Interval with the most steps is {interval[steps.index(max(steps))]}")