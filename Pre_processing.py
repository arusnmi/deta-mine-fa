import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

Cab=pd.read_csv('cab_rides.csv')
Cab.dropna(inplace=True)
Cab.to_csv('cab_rides_cleaned.csv', index=False)

weather=pd.read_csv('weather.csv')

different_districts = weather['location'].unique()
for district_name in different_districts:
    district_data = weather[weather['location'] == district_name]
    disval= district_data['rain']
    med_val= disval.median()
    print (med_val)
    weather.loc[weather['location'] == district_name, 'rain'] = district_data['rain'].fillna(med_val)
    weather.to_csv('weather_updated.csv', index=False)


















