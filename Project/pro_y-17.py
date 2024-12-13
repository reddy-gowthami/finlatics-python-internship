# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 18:52:00 2024

@author: hp
"""

#17)Is there a correlation between the number of subscribers gained in the last 30 days and the unemployment rate in a country?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Aggregate the total number of subscribers gained in the last 30 days per country
subscribers_last_30_days_per_country = df.groupby('Country')['subscribers_for_last_30_days'].sum().reset_index()
subscribers_last_30_days_per_country.columns = ['Country', 'total_subscribers_last_30_days']

# Select relevant columns for merging
unemployment_data = df[['Country', 'Unemployment rate']].drop_duplicates()

# Merge the aggregated data with the unemployment rate data
merged_data = pd.merge(subscribers_last_30_days_per_country, unemployment_data, on='Country')

# Drop any rows with missing values
merged_data = merged_data.dropna()

# Display the merged data
print(merged_data.head())

# Calculate the correlation between the number of subscribers gained in the last 30 days and the unemployment rate
correlation = merged_data['total_subscribers_last_30_days'].corr(merged_data['Unemployment rate'])
print(f'Correlation between the number of subscribers gained in the last 30 days and the unemployment rate: {correlation}')