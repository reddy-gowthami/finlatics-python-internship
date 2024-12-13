# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:17:23 2024

@author: hp
"""

#11.Is there a relationship between gross tertiary education enrollment and the number of YouTube channels in a country?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Aggregate the number of YouTube channels per country
channels_per_country = df['Country'].value_counts().reset_index()
channels_per_country.columns = ['Country', 'num_channels']

# Display the aggregated data
print(channels_per_country.head())

# Select relevant columns for merging
education_data = df[['Country', 'Gross tertiary education enrollment (%)']].drop_duplicates()

# Merge the aggregated data with the gross tertiary education enrollment data
merged_data = pd.merge(channels_per_country, education_data, on='Country')

# Drop any rows with missing values
merged_data = merged_data.dropna()

# Display the merged data
print(merged_data.head())

# Calculate the correlation between gross tertiary education enrollment and the number of channels
correlation = merged_data['num_channels'].corr(merged_data['Gross tertiary education enrollment (%)'])
print(f'Correlation between number of YouTube channels and gross tertiary education enrollment: {correlation}')

# Visualize the relationship using a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_data, x='Gross tertiary education enrollment (%)', y='num_channels')
plt.title('Relationship between Gross Tertiary Education Enrollment and Number of YouTube Channels')
plt.xlabel('Gross Tertiary Education Enrollment (%)')
plt.ylabel('Number of YouTube Channels')
plt.show()