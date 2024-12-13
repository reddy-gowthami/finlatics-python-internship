# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:58:52 2024

@author: hp
"""

#16.How do the top 10 countries with the highest number of YouTube channels compare in terms of their total population?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Aggregate the number of YouTube channels per country
channels_per_country = df['Country'].value_counts().reset_index()
channels_per_country.columns = ['Country', 'num_channels']

# Identify the top 10 countries with the highest number of YouTube channels
top_10_countries = channels_per_country.head(10)

# Select relevant columns for merging
population_data = df[['Country', 'Population']].drop_duplicates()

# Merge the top 10 countries data with the population data
merged_data = pd.merge(top_10_countries, population_data, on='Country')

# Drop any rows with missing values
merged_data = merged_data.dropna()

# Display the merged data
print(merged_data.head())

# Visualize the comparison using a bar plot
plt.figure(figsize=(14, 8))
sns.barplot(data=merged_data, x='Country', y='Population')
plt.title('Population of the Top 10 Countries with the Highest Number of YouTube Channels')
plt.xlabel('Country')
plt.ylabel('Total Population')
plt.xticks(rotation=45)
plt.show()