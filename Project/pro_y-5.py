# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:03:58 2024

@author: hp
"""

#5.What is the distribution of channel types across different categories?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
# Make sure to adjust the path to where your dataset is stored
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Create a crosstab to see the distribution of channel types across different categories
channel_type_distribution = pd.crosstab(df['category'], df['channel_type'])

# Plot the distribution using a heatmap for better visualization
plt.figure(figsize=(12, 8))
sns.heatmap(channel_type_distribution, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Distribution of Channel Types Across Different Categories')
plt.xlabel('Channel Type')
plt.ylabel('Category')
plt.show()
