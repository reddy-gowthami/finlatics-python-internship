# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:07:37 2024

@author: hp
"""

n=int(input("enter the year:"))
if (n%4==0 and n%100!=0)or n%400==0:
    print(f"{n} is a leap year.")
else:
    print(f"{n} is not a leap year.")