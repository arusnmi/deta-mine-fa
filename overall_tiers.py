import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("matched_records_filteredLoc.csv")

# Create directory if it doesn't exist
output_dir = "overall_bargraph_merge"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Analyze distribution of service tiers for each cab company (Uber and Lyft)
for cabtype in ['Uber', 'Lyft']:
    # Filter data for current cab company
    cab_df = df[df['cab_type'] == cabtype].copy()
    # Create route labels by combining source and destination
    cab_df['route'] = cab_df['source'] + " → " + cab_df['destination']

    # Calculate ride frequency for each service tier on each route
    tier_counts = cab_df.groupby(['route', 'name']).size().unstack(fill_value=0)

    # Convert counts to percentages for better comparison
    tier_props = tier_counts.div(tier_counts.sum(axis=1), axis=0) * 100

    # Create stacked bar chart showing tier distribution
    ax = tier_props.plot(kind='bar', stacked=True, colormap='tab20')
    plt.title(f'Percentage Distribution of Tiers across Routes -- {cabtype}')
    plt.xlabel('Route')
    plt.ylabel('Percent of Rides')
    
    # Adjust text elements for better readability
    plt.xticks(rotation=90, fontsize=7)
    plt.yticks(fontsize=7)
    plt.tight_layout()

    # Add percentage labels on each segment of the stacked bars
    for i, route in enumerate(tier_props.index):
        y_offset = 0  # Track vertical position for label placement
        for tier in tier_props.columns:
            value = tier_props.loc[route, tier]
            if value > 0:  # Only add label if segment exists
                ax.text(
                    i,                              # x-position (bar index)
                    y_offset + value / 2,           # y-position (middle of segment)
                    f"{value:.1f}%",               # Format as percentage with 1 decimal
                    ha='center',                    # Center text horizontally
                    va='center',                    # Center text vertically
                    fontsize=6,                     # Small font size for clarity
                    fontweight='bold',              # Make text bold
                    color='black',                  # Black text for contrast
                    rotation=90                     # Rotate for better fit
                )
                y_offset += value  # Update position for next label

    # Configure and position the legend
    plt.legend(
        title='Tier',
        loc='upper center',
        bbox_to_anchor=(0.5, -0.9),  # Position below the plot
        fontsize=7,
        ncol=len(tier_props.columns)  # Spread tiers horizontally
    )

    # Save the figure
    plt.savefig(os.path.join(output_dir, f"{cabtype}_tier_distribution.png"))
    plt.close()