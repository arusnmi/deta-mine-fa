import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

base_df=pd.read_csv("matched_records_filteredLoc.csv")
base_df['route'] = base_df['source'] + " → " + base_df['destination']
rainydays_df=base_df[base_df['rain']!=0]

hue_colours={"Uber":"#000000", "Lyft": "#FFFF00"}
sns.boxplot(
    data=base_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=hue_colours    
)

plt.title("Comparison of Uber and Lyft on Dry Days")
plt.xlabel("Route (Source → Destination)")
plt.ylabel("Price Range")
plt.legend(title="Cab Type")
plt.xticks(rotation=90, fontsize=6)
plt.yticks(fontsize=6)
plt.tight_layout()
plt.show()

rain_colours={"Uber":"#2441B4", "Lyft": "#F8450A"}
sns.boxplot(
    data=rainydays_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=rain_colours    
)

plt.title("Comparison of Uber and Lyft on Rainy Days")
plt.xlabel("Route (Source → Destination)")
plt.ylabel("Price Range")
plt.legend(title="Cab Type")
plt.xticks(rotation=90, fontsize=6)
plt.yticks(fontsize=6)
plt.tight_layout()
plt.show()