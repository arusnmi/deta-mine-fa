import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def detect_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] < lower_bound) | (data[column] > upper_bound)]

cab= pd.read_csv('cab_rides_cleaned.csv')

start= cab['source'].unique()
end= cab['destination'].unique()
cab_companies = cab['cab_type'].unique()
# for source in start:
#     for destination in end:

#         if source == destination:
#             continue
            
#         product_ids = cab_data['product_id'].unique()
#         cab_data = cab[(cab['source'] == source) & (cab['destination'] == destination)]

#         if len(cab_data) == 0:
#             continue
            
#         outliers = detect_outliers(cab_data, 'distance')
        
#         plt.figure(figsize=(12, 6))
#         plt.boxplot(cab_data['distance'], vert=False)
#         plt.title(f'Distance Outliers from {source} to {destination}')
#         plt.xlabel('Distance')
#         plt.show()
#     product_ids = cab_data['product_id'].unique()
#     for product in product_ids:
#         product_data = cab_data[cab_data['product_id'] == product]

# Price+cab type+product ID

for company in cab_companies:
    cab_data = cab[cab['cab_type'] == company]
    
    # Group by product ID
    product_ids = cab_data['product_id'].unique()
    
    for product in product_ids:
        product_data = cab_data[cab_data['product_id'] == product]
        outliers = detect_outliers(product_data, 'price')
        
        plt.figure(figsize=(12, 6))
        plt.boxplot(product_data['price'], vert=False)
        plt.title(f'Price Outliers for {company} - Product ID: {product}')
        plt.xlabel('Price')
        plt.show()
        
        print(f"\nSummary for {company} - Product ID: {product}")
        print(f"Total rides: {len(product_data)}")
        print(f"Number of outliers: {len(outliers)}")
        print(f"Average price: ${product_data['price'].mean():.2f}")
        print("-" * 50)

weather= pd.read_csv('weather_updated.csv')
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