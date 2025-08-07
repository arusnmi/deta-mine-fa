import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



cab= pd.read_csv('cab_rides_cleaned.csv')
weather= pd.read_csv('weather_updated.csv')

def detect_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] < lower_bound) | (data[column] > upper_bound)]

different_districts = weather['location'].unique()

#tempture 
# relevent outlieres found in temperature
# for district_name in different_districts:
#     weathar_data= weather[weather['location'] == district_name]
#     outlieres_temp = detect_outliers(weathar_data, 'temp')

#     plt.figure(figsize=(12, 6))
#     plt.boxplot(weathar_data['temp'], vert=False)
#     plt.title(f'Temperature Outliers in {district_name}')
#     plt.xlabel('Temperature')
#     plt.show()


# Clouds 
# relevent outlieres found in clouds
# for district_name in different_districts:
#     weathar_data= weather[weather['location'] == district_name]
#     outlieres_temp = detect_outliers(weathar_data, 'clouds')

#     plt.figure(figsize=(12, 6))
#     plt.boxplot(weathar_data['clouds'], vert=False)
#     plt.title(f'clouds Outliers in {district_name}')
#     plt.xlabel('clouds')
#     plt.show()


# humidity 
# no outliers found in humidity
# for district_name in different_districts:
#     weathar_data= weather[weather['location'] == district_name]
#     outlieres_temp = detect_outliers(weathar_data, 'humidity')

#     plt.figure(figsize=(12, 6))
#     plt.boxplot(weathar_data['humidity'], vert=False)
#     plt.title(f'humidity Outliers in {district_name}')
#     plt.xlabel('humidity')
#     plt.show()


# rain=outliers
# for district_name in different_districts:
#     weathar_data= weather[weather['location'] == district_name]
#     outlieres_temp = detect_outliers(weathar_data, 'rain')

#     plt.figure(figsize=(12, 6))
#     plt.boxplot(weathar_data['rain'], vert=False)
#     plt.title(f'rain Outliers in {district_name}')
#     plt.xlabel('rain')
#     plt.show()

# wind
#notes: the graphs look identical but they are diffrent, not seen by the naked eye. 
# for district_name in different_districts:
#     weathar_data= weather[weather['location'] == district_name]
#     outlieres_temp = detect_outliers(weathar_data, 'wind')

#     plt.figure(figsize=(12, 6))
#     plt.boxplot(weathar_data['wind'], vert=False)
#     plt.title(f'wind Outliers in {district_name}')
#     plt.xlabel('wind')
#     plt.show()
    
#pressure
#notes: the graphs look identical but they are diffrent, not seen by the naked eye.
# for district_name in different_districts:
#     weathar_data= weather[weather['location'] == district_name]
#     outlieres_temp = detect_outliers(weathar_data, 'pressure')

#     plt.figure(figsize=(12, 6))
#     plt.boxplot(weathar_data['pressure'], vert=False)
#     plt.title(f'pressure Outliers in {district_name}')
#     plt.xlabel('pressure')
#     plt.show()
    

weather = weather[weather['rain'] <= 0.5]
weather.to_csv('weather_outless.csv', index=False)