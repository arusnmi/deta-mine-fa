import pandas as pd


Cab=pd.read_csv('cab_rides.csv')

weather=pd.read_csv('weather.csv')

Cab.dropna(inplace=True)

Cab.to_csv('cab_rides_cleaned.csv', index=False)