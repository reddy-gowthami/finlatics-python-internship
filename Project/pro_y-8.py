# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:20:18 2024

@author: hp
"""

#8.What is the overall trend in subscribers gained in the last 30 days across all channels?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Ensure the 'created_date' column is in datetime format
df['created_date'] = pd.to_datetime(df['created_date'])

# Aggregate the data by the creation date and sum the subscribers gained in the last 30 days
trend_df = df.groupby('created_date')['subscribers_for_last_30_days'].sum().reset_index()

# Plot the trend
plt.figure(figsize=(14, 8))
sns.lineplot(data=trend_df, x='created_date', y='subscribers_for_last_30_days')
plt.title('Overall Trend in Subscribers Gained in the Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Total Subscribers Gained in Last 30 Days')
plt.xticks(rotation=45)
plt.show()