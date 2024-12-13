# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:36:21 2024

@author: hp
"""

#14.Are there any patterns in the distribution of YouTube channels based on latitude and longitude coordinates?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Select relevant columns for latitude and longitude
location_data = df[['Latitude', 'Longitude']].drop_duplicates()

# Drop any rows with missing values
location_data = location_data.dropna()

# Visualize the distribution using a scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=location_data, x='Longitude', y='Latitude', alpha=0.5)
plt.title('Distribution of YouTube Channels Based on Latitude and Longitude')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Visualize the distribution using a hexbin plot (heatmap-like visualization)
plt.figure(figsize=(12, 8))
plt.hexbin(location_data['Longitude'], location_data['Latitude'], gridsize=50, cmap='coolwarm', bins='log')
plt.title('Hexbin Plot of YouTube Channels Based on Latitude and Longitude')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='log10(Number of Channels)')
plt.show()
