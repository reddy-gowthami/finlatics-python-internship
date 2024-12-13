# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 00:26:08 2024

@author: hp
"""

import pandas as pd
data={
      "Employee_name":["gowthami","anu","gopal","ram","sree"],
      "Income":[100000,200000,100000,500000,30000]}
df=pd.DataFrame(data,index=['a','b','c','d','e'])
print(df)