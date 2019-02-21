# importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# loading weather data frame

weather_data = pd.read_csv('Global_city_temp_list.csv')

# filling all the NA values with mean values
weather_data_edited = weather_data.fillna(weather_data.mean())

# getting the output for rolling average function

output = weather_data_edited.rolling(window = 100 , center = 'False' , on = 'city_avg_temp').mean()

# plotting the graphs

plt.bar(output['year'] ,output['global_avg_temp'])
plt.xlabel('years')
plt.ylabel('global avg temp')
plt.title('Global Average Temprature By Years')
plt.show()

