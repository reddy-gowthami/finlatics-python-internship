# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:48:40 2024

@author: hp
"""

#15.What is the correlation between the number of subscribers and the population of a country?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Aggregate the total number of subscribers per country
subscribers_per_country = df.groupby('Country')['subscribers'].sum().reset_index()
subscribers_per_country.columns = ['Country', 'total_subscribers']

# Select relevant columns for merging
population_data = df[['Country', 'Population']].drop_duplicates()

# Merge the aggregated data with the population data
merged_data = pd.merge(subscribers_per_country, population_data, on='Country')

# Drop any rows with missing values
merged_data = merged_data.dropna()

# Display the merged data
print(merged_data.head())

# Calculate the correlation between the number of subscribers and the population
correlation = merged_data['total_subscribers'].corr(merged_data['Population'])
print(f'Correlation between the number of subscribers and the population: {correlation}')