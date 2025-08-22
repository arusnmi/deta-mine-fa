import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

base_df=pd.read_csv("matched_records_filteredLoc.csv")
base_df['route'] = base_df['source'] + " → " + base_df['destination']
rainydays_df=base_df[base_df['rain']!=0]

average_price_Lyft_northStnroute=base_df[(base_df['cab_type']== 'Lyft') & (base_df['rain']!=0) & (base_df['route']=='North Station → Boston University')]['price'].mean()
average_price_Lyft_rain=base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']!=0)]['price'].mean()
average_price_Lyft_dry=base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']==0)]['price'].mean()
median_price_Lyft_rain=base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']!=0)]['price'].median()
median_price_Lyft_dry=base_df[(base_df['cab_type']=='Lyft') & (base_df['rain']==0)]['price'].median()
average_price_Uber_northStnroute=base_df[(base_df['cab_type']== 'Uber') & (base_df['rain']!=0) & (base_df['route']=='North Station → Boston University')]['price'].mean()
average_price_Uber_rain=base_df[(base_df['cab_type']=='Uber') & (base_df['rain']!=0)]['price'].mean()
average_price_Uber_dry=base_df[(base_df['cab_type']=='Uber') & (base_df['rain']==0)]['price'].mean()
median_price_Uber_rain=base_df[(base_df['cab_type']=='Uber') & (base_df['rain']!=0)]['price'].median()
median_price_Uber_dry=base_df[(base_df['cab_type']=='Uber') & (base_df['rain']==0)]['price'].median()
print(f"Lyft - Ave Price (Rain) : {average_price_Lyft_rain}")
print(f"Lyft - Ave Price (Dry) : {average_price_Lyft_dry}")
print(f"Lyft - Median Price (Rain) : {median_price_Lyft_rain}")
print(f"Lyft - Median Price (Dry) : {median_price_Lyft_dry}")
print(f"Uber - Ave Price (Rain) : {average_price_Uber_rain}")
print(f"Uber - Ave Price (Dry) : {average_price_Uber_dry}")
print(f"Uber - Median Price (Rain) : {median_price_Uber_rain}")
print(f"Uber - Median Price (Dry) : {median_price_Uber_dry}")

hue_colours={"Uber":"#000000", "Lyft": "#FFFF00"}
sns.barplot(
    data=base_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=hue_colours,
    alpha=1,
    errorbar=None    
)

rain_colours={"Uber":"#CCCCCC", "Lyft": "#F8450A"}
sns.barplot(
    data=rainydays_df,
    x='route',
    y='price',
    hue='cab_type',
    palette=rain_colours,
    alpha=0.5,
    errorbar=None    
)

plt.title("Comparison of Uber and Lyft Average Price on Rainy vs Dry Days")
plt.xlabel("Route (Source → Destination)")
plt.ylabel("Average Price")
plt.legend(title="Cab Type")
plt.xticks(rotation=90, fontsize=6)
plt.yticks(fontsize=6)
plt.tight_layout()
plt.show()