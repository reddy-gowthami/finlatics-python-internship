# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:24:56 2024

@author: hp
"""

#7.How do the monthly earnings vary throughout different categories?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Calculate the average monthly earnings
df['avg_monthly_earnings'] = (df['lowest_monthly_earnings'] + df['highest_monthly_earnings']) / 2

# Visualize the variation of monthly earnings across different categories using a box plot
plt.figure(figsize=(14, 8))
sns.boxplot(data=df, x='category', y='avg_monthly_earnings')
plt.title('Variation of Monthly Earnings Across Different Categories')
plt.xlabel('Category')
plt.ylabel('Average Monthly Earnings')
plt.xticks(rotation=90)
plt.show()

# Alternatively, you can use a bar plot to show the mean average monthly earnings per category
plt.figure(figsize=(14, 8))
sns.barplot(data=df, x='category', y='avg_monthly_earnings', estimator=sum, ci=None)
plt.title('Total Monthly Earnings Across Different Categories')
plt.xlabel('Category')
plt.ylabel('Total Monthly Earnings')
plt.xticks(rotation=90)
plt.show()