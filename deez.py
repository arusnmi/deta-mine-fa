import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("matched_records_filteredLoc.csv")

# Get all Uber and Lyft combos
for cabtype in ['Uber', 'Lyft']:
    cab_df = df[df['cab_type'] == cabtype].copy()
    cab_df['route'] = cab_df['source'] + " → " + cab_df['destination']

    # Count number of rides per route and per name (tier)
    tier_counts = cab_df.groupby(['route', 'name']).size().unstack(fill_value=0)

    # Find percent of each tier for each route
    tier_props = tier_counts.div(tier_counts.sum(axis=1), axis=0) * 100  # percentage

    # Create the bar plot (each bar is a route, and each segment is a tier as percent)
    ax = tier_props.plot(kind='bar', stacked=True, colormap='tab20')
    plt.title(f'Percentage Distribution of Tiers across Routes -- {cabtype}')
    plt.xlabel('Route')
    plt.ylabel('Percent of Rides')
    plt.xticks(rotation=90, fontsize=7)
    plt.yticks(fontsize=7)
    plt.tight_layout()

    # Add percentage values on the top of each tier (on top of each bar segment)
    for i, route in enumerate(tier_props.index):
        y_offset = 0
        for tier in tier_props.columns:
            value = tier_props.loc[route, tier]
            if value > 0:
                ax.text(
                    i, y_offset + value / 2,        # position: x (bar), y (middle of segment)
                    f"{value:.1f}%",                # formatted percent
                    ha='center', va='center', fontsize=6, fontweight='bold', color='black', rotation=90
                )
                y_offset += value

    plt.legend(
    title='Tier',
    loc='upper center',
    bbox_to_anchor=(0.5, -0.9),  # 0.5 centers, negative y puts below x-axis
    fontsize=7,
    ncol=len(tier_props.columns)   # spread legend into as many columns as there are tiers
)

    plt.show()