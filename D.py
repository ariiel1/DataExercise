import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime 
import calendar 

file = pd.read_csv(r"C:\Users\ariel\Desktop\BINUS\Assignments\I2P\Data\activity.csv")

def week(date): 
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    the_date = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    if calendar.day_name[the_date] in weekdays:
        return 'weekday'
    else:
        return 'weekend'
    
file["day"] = file["date"].apply(week)

interval = []
steps_weekday = []
steps_weekend = []

for data in file['interval'].unique():
    interval.append(data)
    steps_weekday.append(file.loc[(file['interval']==data) & (file['day']=='weekday'), 'steps'].dropna().mean())
    steps_weekend.append(file.loc[(file['interval']==data) & (file['day']=='weekend'), 'steps'].dropna().mean())

graphdata = pd.DataFrame({'Interval':interval, 'Weekday': steps_weekday,'Weekend':steps_weekend})

graphdata.plot.line(x="Interval")
plt.title('Average number of steps taken in 5-minute intervals')
plt.xlabel("Interval")
plt.ylabel('Steps')
plt.show()