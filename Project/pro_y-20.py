# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:14:07 2024

@author: hp
"""

#20.What is the average number of subscribers gained per month since the creation of YouTube channels till now?
import pandas as pd
from datetime import datetime
df = pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
# Convert 'created_date' to datetime format
df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')

# Get the current date
current_date = datetime.now()

# Calculate the number of months between the creation date and now
df['months_since_creation'] = (current_date.year - df['created_date'].dt.year) * 12 + (current_date.month - df['created_date'].dt.month)

# Drop rows where 'months_since_creation' is less than or equal to 0 (which should be rare)
df = df[df['months_since_creation'] > 0]

# Calculate the total number of subscribers gained and total months for each channel
df['total_subscribers'] = df['subscribers']

# Aggregate data to find the total number of subscribers and total months
total_data = df.groupby('Country').agg({'total_subscribers': 'sum', 'months_since_creation': 'sum'}).reset_index()

# Calculate the average number of subscribers gained per month
total_data['average_subscribers_per_month'] = total_data['total_subscribers'] / total_data['months_since_creation']

# Print the resulting data
print(total_data[['Country', 'average_subscribers_per_month']].head())

# Calculate the overall average number of subscribers gained per month
overall_average = total_data['average_subscribers_per_month'].mean()
print(f'The overall average number of subscribers gained per month since the creation of YouTube channels is {overall_average:.2f}')