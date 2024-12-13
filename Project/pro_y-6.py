# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:16:12 2024

@author: hp
"""
#6)Is there a correlation between the number of subscribers and total video views for YouTube channels?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')

# Calculate the correlation between number of subscribers and total video views
correlation = df['subscribers'].corr(df['video views'])
print(f'Correlation between subscribers and total video views: {correlation}')

# Visualize the correlation using a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='subscribers', y='video views')
plt.title('Correlation between Subscribers and Total Video Views')
plt.xlabel('Number of Subscribers')
plt.ylabel('Total Video Views')
plt.show()
