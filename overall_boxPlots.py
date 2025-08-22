# Import required libraries for data visualization and analysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load and prepare the dataset
base_df = pd.read_csv("matched_records_filteredLoc.csv")
# Create route labels by combining source and destination
base_df['route'] = base_df['source'] + " → " + base_df['destination']
# Create separate dataframe for rainy day analysis
rainydays_df = base_df[base_df['rain']!=0]

# Define color scheme for dry day visualization
# Black for Uber, Yellow for Lyft
hue_colours = {"Uber":"#000000", "Lyft": "#FFFF00"}

# Create boxplot for dry day price comparison
sns.boxplot(
    data=base_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=hue_colours    
)

# Customize dry day plot appearance
plt.title("Comparison of Uber and Lyft on Dry Days")
plt.xlabel("Route (Source → Destination)")
plt.ylabel("Price Range")
plt.legend(title="Cab Type")
plt.xticks(rotation=90, fontsize=6)  # Rotate and resize x-axis labels
plt.yticks(fontsize=6)  # Resize y-axis labels
plt.tight_layout()  # Adjust layout to prevent label overlap
plt.show()

# Define color scheme for rainy day visualization
# Blue for Uber, Red for Lyft
rain_colours = {"Uber":"#2441B4", "Lyft": "#F8450A"}

# Create boxplot for rainy day price comparison
sns.boxplot(
    data=rainydays_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=rain_colours    
)

# Customize rainy day plot appearance
plt.title("Comparison of Uber and Lyft on Rainy Days")
plt.xlabel("Route (Source → Destination)")
plt.ylabel("Price Range")
plt.legend(title="Cab Type")
plt.xticks(rotation=90, fontsize=6)  # Rotate and resize x-axis labels
plt.yticks(fontsize=6)  # Resize y-axis labels
plt.tight_layout()  # Adjust layout to prevent label overlap
plt.show()