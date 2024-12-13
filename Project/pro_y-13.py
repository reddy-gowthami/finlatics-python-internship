# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:31:55 2024

@author: hp
"""

#13.What is the average urban population percentage in countries with YouTube channels?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Select relevant columns for country and urban population percentage
urban_population_data = df[['Country', 'Urban_population']].drop_duplicates()

# Drop any rows with missing values
urban_population_data = urban_population_data.dropna()

# Calculate the average urban population percentage
average_urban_population = urban_population_data['Urban_population'].mean()

print(f'The average urban population percentage in countries with YouTube channels is {average_urban_population:.2f}%')