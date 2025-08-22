# Import required libraries for data visualization and analysis
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the matched records CSV file containing cab ride data
df=pd.read_csv("matched_records_filteredLoc.csv")

# Create a new column 'route' by combining source and destination with an arrow
df['route']=df['source'] + "→ " + df['destination']
# Get unique routes for analysis
routes=df['route'].unique()

# Iterate through each unique route to create comparative visualizations
for route in routes:
    # Split data into rainy and non-rainy days for the current route
    route_df_norain = df[(df['route'] == route) & (df['rain'] == 0)]
    route_df_rain = df[(df['route'] == route) & (df['rain'] != 0)]

    # Create a figure with two subplots side by side, sharing y-axis scale
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)  

    # Left subplot: Price comparison for dry days
    sns.barplot(
        data=route_df_norain,
        x='cab_type',
        y='price',
        hue='cab_type',
        palette={"Uber": "black", "Lyft": "yellow"},  # Color scheme for dry days
        alpha=1,
        errorbar=None,
        ax=axes[0]
    )
    axes[0].set_title('Dry Days')
    axes[0].set_xlabel('Cab Type')
    axes[0].set_ylabel('Average Price')

    # Right subplot: Price comparison for rainy days
    sns.barplot(
        data=route_df_rain,
        x='cab_type',
        y='price',
        hue='cab_type',
        palette={"Uber": "blue", "Lyft": "red"},  # Different color scheme for rainy days
        alpha=0.5,
        errorbar=None,
        ax=axes[1]
    )
    axes[1].set_title('Rainy Days')
    axes[1].set_xlabel('Cab Type')
    axes[1].set_ylabel('')  # Remove ylabel since it's shared with left subplot

    # Add main title for the entire figure
    fig.suptitle(f'Price Comparison Rain vs Dry for Route: {route}', fontsize=14)

    # Adjust layout to prevent overlap and display the plot
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


