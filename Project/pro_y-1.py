# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:44:26 2024

@author: hp
"""
#what are the top 10 you tube channels based on the no.of subscribers
import pandas as pd
df=pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
#sort the data acc to subscribers
sorted_df=df.sort_values(by='subscribers',ascending=False)
top_10_channels=sorted_df.head(10)
print(top_10_channels[['Youtuber','subscribers']])