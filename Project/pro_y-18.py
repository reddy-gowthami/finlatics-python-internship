# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 18:58:41 2024

@author: hp
"""

#18.How does the distribution of video views for the last 30 days vary across different channel types?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Select relevant columns for channel type and video views for the last 30 days
views_last_30_days_data = df[['channel_type', 'video_views_for_the_last_30_days']]

# Drop any rows with missing values
views_last_30_days_data = views_last_30_days_data.dropna()

# Optionally, visualize the distribution using a violin plot for more detailed insight
plt.figure(figsize=(12, 8))
sns.violinplot(data=views_last_30_days_data, x='channel_type', y='video_views_for_the_last_30_days')
plt.title('Distribution of Video Views for the Last 30 Days Across Different Channel Types')
plt.xlabel('Channel Type')
plt.ylabel('Video Views for the Last 30 Days')
plt.xticks(rotation=45)
plt.show()