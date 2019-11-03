import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())
#print(london_data.iloc[100:200])
print(len(london_data))

temp = london_data["TemperatureC"]
average_temp = np.mean(temp)
print("Average temperature is " +str(average_temp)+" C")
temperature_var = np.var(temp)
print("Variance temperature is " +str(temperature_var)+" C")
temperature_standard_deviation = np.std(temp)
print("Standard Deviation temperature is " +str(temperature_standard_deviation)+" C")

#Select Month Column for June
june = london_data.loc[london_data["month"]== 6]["TemperatureC"]

#Select Month Column for July
july = london_data.loc[london_data["month"]== 7]["TemperatureC"]

#Print average temp in june
print("Average temperature in june is " +str(np.mean(june))+" C")

#Print average temp in july
print("Average temperature in july is " +str(np.mean(july))+" C")

#Print standard deviation temp in june
print("Standrd deviation temperature in june is " +str(np.std(june))+" C")

#Print standard deviation temp in july
print("Standrd deviation temperature in july is " +str(np.std(july))+" C")

#Print mean and standard deviation for temps in each month
for i in range(1, 13):
  month = london_data.loc[london_data["month"]==i]["TemperatureC"]
  print("The mean temperature in month "+str(i) + " is "+str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i)+ " is "+ str(np.std(month)) + "\n")

print(london_data.head())
#Print mean and standard deviation for daily rain in each hour
for i in range(0, 24):
  hour = london_data.loc[london_data["hour"]==i]["dailyrainMM"]
  print("The mean daily rain in hour "+str(i) + " is "+str(np.mean(hour)))
  print("The standard deviation of daily rain in hour "+str(i)+ " is "+ str(np.std(hour)) + "\n")