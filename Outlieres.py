# Import required libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define function to detect outliers using IQR method
def detect_outliers(data, column):
    # Calculate Q1, Q3 and IQR
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    # Calculate bounds for outlier detection
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Return data points outside the bounds
    return data[(data[column] < lower_bound) | (data[column] > upper_bound)]

# Read the cleaned cab rides data
cab = pd.read_csv('cab_rides_cleaned.csv')

# Get unique values for source, destination and cab types
start = cab['source'].unique()
end = cab['destination'].unique()
cab_companies = cab['cab_type'].unique()

# Analyze distance outliers for each source-destination pair
for source in start:
    for destination in end:
        # Skip if source and destination are same
        if source == destination:
            continue
            
        product_ids = cab_data['product_id'].unique()
        cab_data = cab[(cab['source'] == source) & (cab['destination'] == destination)]

        # Skip if no data exists for this route
        if len(cab_data) == 0:
            continue
            
        # Detect and visualize distance outliers
        outliers = detect_outliers(cab_data, 'distance')
        plt.figure(figsize=(12, 6))
        plt.boxplot(cab_data['distance'], vert=False)
        plt.title(f'Distance Outliers from {source} to {destination}')
        plt.xlabel('Distance')
        plt.show()

# Analyze price outliers for each cab company and product ID
for company in cab_companies:
    cab_data = cab[cab['cab_type'] == company]
    product_ids = cab_data['product_id'].unique()
    
    for product in product_ids:
        # Filter data for current product
        product_data = cab_data[cab_data['product_id'] == product]
        outliers = detect_outliers(product_data, 'price')
        
        # Create boxplot for price distribution
        plt.figure(figsize=(12, 6))
        plt.boxplot(product_data['price'], vert=False)
        plt.title(f'Price Outliers for {company} - Product ID: {product}')
        plt.xlabel('Price')
        plt.show()
        
        # Print summary statistics
        print(f"\nSummary for {company} - Product ID: {product}")
        print(f"Total rides: {len(product_data)}")
        print(f"Number of outliers: {len(outliers)}")
        print(f"Average price: ${product_data['price'].mean():.2f}")
        print("-" * 50)

# Read and analyze weather data
weather = pd.read_csv('weather_updated.csv')
different_districts = weather['location'].unique()

# Analyze temperature outliers by district
for district_name in different_districts:
    weathar_data = weather[weather['location'] == district_name]
    outlieres_temp = detect_outliers(weathar_data, 'temp')
    plt.figure(figsize=(12, 6))
    plt.boxplot(weathar_data['temp'], vert=False)
    plt.title(f'Temperature Outliers in {district_name}')
    plt.xlabel('Temperature')
    plt.show()

# Analyze cloud cover outliers by district
for district_name in different_districts:
    weathar_data = weather[weather['location'] == district_name]
    outlieres_temp = detect_outliers(weathar_data, 'clouds')
    plt.figure(figsize=(12, 6))
    plt.boxplot(weathar_data['clouds'], vert=False)
    plt.title(f'clouds Outliers in {district_name}')
    plt.xlabel('clouds')
    plt.show()

# Analyze humidity outliers by district
for district_name in different_districts:
    weathar_data = weather[weather['location'] == district_name]
    outlieres_temp = detect_outliers(weathar_data, 'humidity')
    plt.figure(figsize=(12, 6))
    plt.boxplot(weathar_data['humidity'], vert=False)
    plt.title(f'humidity Outliers in {district_name}')
    plt.xlabel('humidity')
    plt.show()

# Analyze rainfall outliers by district
for district_name in different_districts:
    weathar_data = weather[weather['location'] == district_name]
    outlieres_temp = detect_outliers(weathar_data, 'rain')
    plt.figure(figsize=(12, 6))
    plt.boxplot(weathar_data['rain'], vert=False)
    plt.title(f'rain Outliers in {district_name}')
    plt.xlabel('rain')
    plt.show()

# Analyze wind speed outliers by district
# Note: Subtle differences exist between districts
for district_name in different_districts:
    weathar_data = weather[weather['location'] == district_name]
    outlieres_temp = detect_outliers(weathar_data, 'wind')
    plt.figure(figsize=(12, 6))
    plt.boxplot(weathar_data['wind'], vert=False)
    plt.title(f'wind Outliers in {district_name}')
    plt.xlabel('wind')
    plt.show()

# Analyze pressure outliers by district
# Note: Subtle differences exist between districts
for district_name in different_districts:
    weathar_data = weather[weather['location'] == district_name]
    outlieres_temp = detect_outliers(weathar_data, 'pressure')
    plt.figure(figsize=(12, 6))
    plt.boxplot(weathar_data['pressure'], vert=False)
    plt.title(f'pressure Outliers in {district_name}')
    plt.xlabel('pressure')
    plt.show()

# Remove extreme rainfall values (> 0.5) and save cleaned data
weather = weather[weather['rain'] <= 0.5]
weather.to_csv('weather_outless.csv', index=False)