# Import required libraries for data analysis and visualization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create Box_plot_images directory if it doesn't exist
if not os.path.exists('Box_plot_images'):
    os.makedirs('Box_plot_images')

# Load the dataset and create route labels
base_df = pd.read_csv("matched_records_filteredLoc.csv")
base_df['route'] = base_df['source'] + " → " + base_df['destination']
# Create separate dataframe for rainy days
rainydays_df = base_df[base_df['rain']!=0]

# Calculate average and median prices for Lyft under different conditions
# North Station to Boston University route during rain
average_price_Lyft_northStnroute = base_df[(base_df['cab_type']== 'Lyft') & 
                                          (base_df['rain']!=0) & 
                                          (base_df['route']=='North Station → Boston University')]['price'].mean()
# Overall rainy day average
average_price_Lyft_rain = base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']!=0)]['price'].mean()
# Overall dry day average
average_price_Lyft_dry = base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']==0)]['price'].mean()
# Median prices for rainy and dry days
median_price_Lyft_rain = base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']!=0)]['price'].median()
median_price_Lyft_dry = base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']==0)]['price'].median()

# Calculate average and median prices for Uber under different conditions
# North Station to Boston University route during rain
average_price_Uber_northStnroute = base_df[(base_df['cab_type']== 'Uber') & 
                                        (base_df['rain']!=0) & 
                                        (base_df['route']=='North Station → Boston University')]['price'].mean()
# Overall rainy day average
average_price_Uber_rain = base_df[(base_df['cab_type']=='Uber') & (base_df['rain']!=0)]['price'].mean()
# Overall dry day average
average_price_Uber_dry = base_df[(base_df['cab_type']=='Uber') & (base_df['rain']==0)]['price'].mean()
# Median prices for rainy and dry days
median_price_Uber_rain = base_df[(base_df['cab_type']=='Uber') & (base_df['rain']!=0)]['price'].median()
median_price_Uber_dry = base_df[(base_df['cab_type']=='Uber') & (base_df['rain']==0)]['price'].median()

# Print summary statistics
print(f"Lyft - Ave Price (Rain) : {average_price_Lyft_rain}")
print(f"Lyft - Ave Price (Dry) : {average_price_Lyft_dry}")
print(f"Lyft - Median Price (Rain) : {median_price_Lyft_rain}")
print(f"Lyft - Median Price (Dry) : {median_price_Lyft_dry}")
print(f"Uber - Ave Price (Rain) : {average_price_Uber_rain}")
print(f"Uber - Ave Price (Dry) : {average_price_Uber_dry}")
print(f"Uber - Median Price (Rain) : {median_price_Uber_rain}")
print(f"Uber - Median Price (Dry) : {median_price_Uber_dry}")

# Create overlaid bar plots for price comparison
# First layer: Dry day prices (Black for Uber, Yellow for Lyft)
hue_colours = {"Uber":"#000000", "Lyft": "#FFFF00"}
sns.barplot(
    data=base_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=hue_colours,
    alpha=1,
    errorbar=None    
)

# Second layer: Rainy day prices (Gray for Uber, Orange for Lyft)
rain_colours = {"Uber":"#CCCCCC", "Lyft": "#F8450A"}
sns.barplot(
    data=rainydays_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=rain_colours,
    alpha=0.5,
    errorbar=None    
)

# Customize plot appearance
plt.title("Comparison of Uber and Lyft Average Price on Rainy vs Dry Days")
plt.xlabel("Route (Source → Destination)")
plt.ylabel("Average Price")
plt.legend(title="Cab Type")
plt.xticks(rotation=90, fontsize=6)  # Rotate and resize x-axis labels
plt.yticks(fontsize=6)  # Resize y-axis labels
plt.tight_layout()  # Adjust layout to prevent label overlap
# Save the figure instead of showing it
plt.savefig('Box_plot_images/overall_price_comparison.png', dpi=300, bbox_inches='tight')
plt.close()