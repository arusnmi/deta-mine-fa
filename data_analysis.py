import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


output_dir = 'histograms'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cab = pd.read_csv('cab_rides_cleaned.csv')

cab_companies = cab['name'].unique()

for company in cab_companies:
    cab_data = cab[cab['name'] == company]
    start = cab_data['source'].unique()
    end = cab_data['destination'].unique()
    for source in start:
        for destination in end:
            if source == destination:
                continue
                
            cab_data = cab[(cab['source'] == source) & (cab['destination'] == destination)]
            if len(cab_data) == 0:
                continue

            plt.figure(figsize=(12, 6))
            plt.hist(cab_data['price'], bins=30, alpha=0.7, label='Price')
            plt.title(f'Price Distribution for {company} from {source} to {destination}')
            plt.xlabel('Value') 
            plt.ylabel('Frequency')
            plt.legend()

            filename = f'{company}_{source}_{destination}.png'

            filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-', '.'))
            filepath = os.path.join(output_dir, filename)
            plt.savefig(filepath)
            plt.close()  


