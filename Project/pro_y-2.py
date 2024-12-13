# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:04:34 2024

@author: hp
"""

#2.Which category has the highest average number of subscribers?
import pandas as pd
df=pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
avg_subscribers=df.groupby('category')['subscribers'].mean()
highest_avg_subscribers=avg_subscribers.sort_values(ascending=False).head(1)
print(highest_avg_subscribers)