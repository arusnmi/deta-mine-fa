# Import required libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create a directory to store histogram plots
output_dir = 'histograms'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the cleaned cab ride data
cab = pd.read_csv('cab_rides_cleaned.csv')

# Get unique cab companies from the dataset
cab_companies = cab['name'].unique()

# Analyze price distribution for each company and route
for company in cab_companies:
    # Filter data for current cab company
    cab_data = cab[cab['name'] == company]
    # Get unique source and destination locations
    start = cab_data['source'].unique()
    end = cab_data['destination'].unique()
    
    # Iterate through each source-destination pair
    for source in start:
        for destination in end:
            # Skip if source and destination are the same
            if source == destination:
                continue
            
            # Filter data for current route
            cab_data = cab[(cab['source'] == source) & (cab['destination'] == destination)]
            # Skip if no data exists for this route
            if len(cab_data) == 0:
                continue

            # Create histogram for price distribution
            plt.figure(figsize=(12, 6))
            plt.hist(cab_data['price'], bins=30, alpha=0.7, label='Price')
            plt.title(f'Price Distribution for {company} from {source} to {destination}')
            plt.xlabel('Value') 
            plt.ylabel('Frequency')
            plt.legend()

            # Generate filename for the plot
            filename = f'{company}_{source}_{destination}.png'
            # Clean filename to remove invalid characters
            filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-', '.'))
            # Create full file path
            filepath = os.path.join(output_dir, filename)
            # Save and close the plot
            plt.savefig(filepath)
            plt.close()


