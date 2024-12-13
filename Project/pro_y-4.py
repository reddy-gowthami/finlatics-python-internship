# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:31:19 2024

@author: hp
"""

#4.What are the top 5 countries with the highest number of YouTube channels?
import pandas as pd
df=pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
cc=df['Country'].value_counts()
highest=cc.head(5)
print(highest)