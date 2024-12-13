# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:53:49 2024

@author: hp
"""

#10.What is the distribution of channel creation dates? Is there any trend over time?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Convert 'created_date' to datetime format
df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')

# Drop rows where 'created_date' is NaT (not a time)
df_clean = df.dropna(subset=['created_date'])

# Check the number of remaining rows after cleaning
print("\nNumber of rows after cleaning:", df_clean.shape[0])

# Extract year and month from 'created_date'
df_clean['year'] = df_clean['created_date'].dt.year
df_clean['month'] = df_clean['created_date'].dt.month

# Check the range of years
min_year = df_clean['year'].min()
max_year = df_clean['year'].max()
print(f"\nYear range: {min_year} - {max_year}")

# Plot the distribution of channel creation dates
plt.figure(figsize=(14, 7))

# Plot the number of channels created per year using basic matplotlib functions
plt.subplot(1, 2, 1)
if not df_clean.empty:
    plt.hist(df_clean['year'], bins=range(min_year, max_year + 2), color='blue', edgecolor='black')
    plt.title('Distribution of Channel Creation Dates')
    plt.xlabel('Year')
    plt.ylabel('Number of Channels Created')
    plt.xticks(range(min_year, max_year + 1), rotation=45)
    plt.grid(True)
else:
    plt.text(0.5, 0.5, 'No data available for plotting', horizontalalignment='center', verticalalignment='center', fontsize=12, color='red')

# Plotting the trend over time
plt.subplot(1, 2, 2)
if not df_clean.empty:
    df_grouped = df_clean.groupby(['year', 'month']).size().reset_index(name='channel_count')
    df_grouped['date'] = pd.to_datetime(df_grouped[['year', 'month']].assign(day=1))
    plt.plot(df_grouped['date'], df_grouped['channel_count'], marker='o')
    plt.title('Trend of Channel Creation Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Channels Created')
    plt.xticks(rotation=45)
    plt.grid(True)
else:
    plt.text(0.5, 0.5, 'No data available for plotting', horizontalalignment='center', verticalalignment='center', fontsize=12, color='red')

plt.tight_layout()
plt.show()

