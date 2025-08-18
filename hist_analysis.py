import os
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def extract_histogram_data(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Get histogram data
    hist = cv2.calcHist([gray], [0], None, [256], [0,256])
    return hist.flatten()

def analyze_districts():
    base_path = "histograms"
    results = []
    
    for filename in os.listdir(base_path):
        if filename.endswith('.png'):
            # Parse filename components
            color, source, dest = filename.replace('.png','').split('_')
            
            # Get histogram data
            hist_data = extract_histogram_data(os.path.join(base_path, filename))
            if hist_data is not None:
                # Calculate metrics
                avg_intensity = np.mean(hist_data)
                peak_intensity = np.max(hist_data)
                
                results.append({
                    'cab_type': color,
                    'source': source,
                    'destination': dest,
                    'avg_usage': avg_intensity,
                    'peak_usage': peak_intensity
                })
    
    return pd.DataFrame(results)

def generate_district_analysis():
    df = analyze_districts()
    
    # Group by districts and cab types
    district_analysis = df.groupby(['source', 'cab_type'])['avg_usage'].mean().reset_index()
    
    # Find most popular cab type for each district
    popular_cabs = district_analysis.loc[district_analysis.groupby('source')['avg_usage'].idxmax()]
    
    return popular_cabs

if __name__ == "__main__":
    results = generate_district_analysis()
    print("\nMost Popular Cab Types by District:")
    print(results.to_string(index=False))
    
    # Create visualization
    plt.figure(figsize=(12, 6))
    districts = results['source'].unique()
    usage_values = results['avg_usage']
    
    plt.bar(districts, usage_values)
    plt.xticks(rotation=45)
    plt.title('Cab Usage by District')
    plt.ylabel('Average Usage')
    plt.tight_layout()
    plt.savefig('district_analysis.png')