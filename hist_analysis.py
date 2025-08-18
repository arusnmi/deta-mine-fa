# Import required libraries for image processing and data analysis
import os
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def extract_histogram_data(image_path):
    """
    Extracts histogram data from an image file
    Args:
        image_path: Path to the image file
    Returns:
        Flattened histogram data array or None if image cannot be read
    """
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    # Convert image to grayscale for histogram analysis
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Calculate histogram with 256 bins
    hist = cv2.calcHist([gray], [0], None, [256], [0,256])
    return hist.flatten()

def analyze_districts():
    """
    Analyzes histogram data for all districts and cab types
    Returns:
        DataFrame containing analysis results
    """
    base_path = "histograms"
    results = []
    
    # Process each histogram image in the directory
    for filename in os.listdir(base_path):
        if filename.endswith('.png'):
            # Extract metadata from filename
            color, source, dest = filename.replace('.png','').split('_')
            
            # Get histogram data for the image
            hist_data = extract_histogram_data(os.path.join(base_path, filename))
            if hist_data is not None:
                # Calculate statistical metrics
                avg_intensity = np.mean(hist_data)
                peak_intensity = np.max(hist_data)
                
                # Store results
                results.append({
                    'cab_type': color,
                    'source': source,
                    'destination': dest,
                    'avg_usage': avg_intensity,
                    'peak_usage': peak_intensity
                })
    
    return pd.DataFrame(results)

def generate_district_analysis():
    """
    Generates analysis of cab usage patterns by district
    Returns:
        DataFrame containing most popular cab types by district
    """
    # Get raw analysis data
    df = analyze_districts()
    
    # Calculate average usage by district and cab type
    district_analysis = df.groupby(['source', 'cab_type'])['avg_usage'].mean().reset_index()
    
    # Determine the most popular cab type for each district
    popular_cabs = district_analysis.loc[district_analysis.groupby('source')['avg_usage'].idxmax()]
    
    return popular_cabs

if __name__ == "__main__":
    # Generate and display analysis results
    results = generate_district_analysis()
    print("\nMost Popular Cab Types by District:")
    print(results.to_string(index=False))
    
    # Create bar chart visualization
    plt.figure(figsize=(12, 6))
    districts = results['source'].unique()
    usage_values = results['avg_usage']
    
    # Plot and customize the visualization
    plt.bar(districts, usage_values)
    plt.xticks(rotation=45)
    plt.title('Cab Usage by District')
    plt.ylabel('Average Usage')
    plt.tight_layout()
    plt.savefig('district_analysis.png')