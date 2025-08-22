import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("matched_records_filteredLoc.csv")
df['route']=df['source'] + "→ " + df['destination']
routes=df['route'].unique()

for route in routes:
    route_df_norain = df[(df['route'] == route) & (df['rain'] == 0)]
    route_df_rain = df[(df['route'] == route) & (df['rain'] != 0)]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)  

    # Dry days barplot on left subplot
    sns.barplot(
        data=route_df_norain,
        x='cab_type',
        y='price',
        hue='cab_type',
        palette={"Uber": "black", "Lyft": "yellow"},
        alpha=1,
        errorbar=None,
        ax=axes[0]
    )
    axes[0].set_title('Dry Days')
    axes[0].set_xlabel('Cab Type')
    axes[0].set_ylabel('Average Price')

    # Rainy days barplot on right subplot
    sns.barplot(
        data=route_df_rain,
        x='cab_type',
        y='price',
        hue='cab_type',
        palette={"Uber": "blue", "Lyft": "red"},
        alpha=0.5,
        errorbar=None,
        ax=axes[1]
    )
    axes[1].set_title('Rainy Days')
    axes[1].set_xlabel('Cab Type')
    axes[1].set_ylabel('')  # No ylabel for right subplot; shared

    fig.suptitle(f'Price Comparison Rain vs Dry for Route: {route}', fontsize=14)

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for suptitle
    plt.show()


