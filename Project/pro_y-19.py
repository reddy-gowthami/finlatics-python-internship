# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:04:52 2024

@author: hp
"""

#19.Are there any seasonal trends in the number of videos uploaded by YouTube channels?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Convert 'created_date' to datetime if it's not already
df['created_date'] = pd.to_datetime(df['created_date'])

# Extract month and year from the created_date
df['year'] = df['created_date'].dt.year
df['month'] = df['created_date'].dt.month

# Aggregate the number of videos uploaded by month and year
monthly_uploads = df.groupby(['year', 'month'])['uploads'].sum().reset_index()

# Create a 'date' column for better plotting
monthly_uploads['date'] = pd.to_datetime(monthly_uploads[['year', 'month']].assign(day=1))

# Plot the number of videos uploaded by month over time
plt.figure(figsize=(14, 8))
sns.lineplot(data=monthly_uploads, x='date', y='uploads')
plt.title('Monthly Number of Videos Uploaded by YouTube Channels')
plt.xlabel('Date')
plt.ylabel('Number of Videos Uploaded')
plt.xticks(rotation=45)
plt.show()