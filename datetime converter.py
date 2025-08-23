import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('matched_records_filteredLoc.csv')

# Convert datetime column using pandas datetime
df['datetime'] = pd.to_datetime(df['datetime'], format='%d-%m-%Y %H:%M:%S')

# Create a new column with time as decimal hours
df['time_decimal'] = df['datetime'].dt.hour + df['datetime'].dt.minute/60.0

# Save the updated DataFrame to CSV
df.to_csv('matched_records_filtered_with_time.csv', index=False)

# Print to verify some values
print(df[['datetime', 'time_decimal']].head())


