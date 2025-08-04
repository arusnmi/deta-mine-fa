import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

Cab=pd.read_csv('cab_rides.csv')
Cab.dropna(inplace=True)
Cab.to_csv('cab_rides_cleaned.csv', index=False)

weather=pd.read_csv('weather.csv')


le = LabelEncoder()
weather['location_encoded'] = le.fit_transform(weather['location'])


features = ['time_stamp', 'humidity', 'wind', 'temp', 'location_encoded', 'clouds', 'pressure'
]

X = weather[features]
y = weather['rain']

imputer = SimpleImputer(strategy='mean')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)


rain_not_null = weather['rain'].notna()
model = LinearRegression()
model.fit(X_imputed[rain_not_null], y[rain_not_null])

rain_is_null = weather['rain'].isna()
weather.loc[rain_is_null, 'rain'] = model.predict(X_imputed[rain_is_null])

weather.to_csv('weather_cleaned.csv', index=False)