# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:38:42 2024
@author: hp
"""

#9.Are there any outliers in terms of yearly earnings from YouTube channels?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Calculate the average yearly earnings
df['avg_yearly_earnings'] = (df['lowest_yearly_earnings'] + df['highest_yearly_earnings']) / 2
# Visualize the average yearly earnings using a box plot to identify outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='avg_yearly_earnings')
plt.title('Box Plot of Average Yearly Earnings')
plt.ylabel('Average Yearly Earnings')
plt.show()
# Identify the outliers
Q1 = df['avg_yearly_earnings'].quantile(0.25)
Q3 = df['avg_yearly_earnings'].quantile(0.75)
IQR = Q3 - Q1
# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# Filter out the outliers
outliers = df[(df['avg_yearly_earnings'] < lower_bound) | (df['avg_yearly_earnings'] > upper_bound)]
print("Outliers in terms of average yearly earnings:")
print(outliers[['Youtuber', 'avg_yearly_earnings']])