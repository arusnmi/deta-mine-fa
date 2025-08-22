# Import required libraries for data manipulation, machine learning, and preprocessing
import pandas as pd  # For data manipulation and analysis
import numpy as np   # For numerical operations
from sklearn.linear_model import LinearRegression    # For regression modeling
from sklearn.impute import SimpleImputer            # For handling missing values
from sklearn.preprocessing import LabelEncoder       # For encoding categorical variables

# SECTION 1: Process Cab Rides Data
# Read the raw cab rides dataset from CSV file
Cab=pd.read_csv('cab_rides.csv')

# Display summary of missing values in each column of the cab dataset
non= Cab.isna().sum()
print(non)

# Clean the cab rides data by removing rows with any missing values
# inplace=True modifies the original dataframe
Cab.dropna(inplace=True)

# Export the cleaned cab rides data to a new CSV file
# index=False prevents writing row numbers as a separate column
Cab.to_csv('cab_rides_cleaned.csv', index=False)

# SECTION 2: Process Weather Data
# Read the weather dataset from CSV file
weather=pd.read_csv('weather.csv')

# fillall not vals
weather.fillna(0, inplace=True)




    
# Save the updated weather data with filled missing values to a new CSV file
# index=False prevents writing row numbers as a separate column
weather.to_csv('weather_updated.csv', index=False)


















