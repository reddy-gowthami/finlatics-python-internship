# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:12:56 2024

@author: hp
"""
#3.How many videos, on average, are uploaded by YouTube channels in each category?
import pandas as pd
df=pd.read_csv(r'C:\Users\hp\Desktop\G_csv.csv')
avg_uploads=df.groupby('category')['uploads'].mean().count()
print(avg_uploads)