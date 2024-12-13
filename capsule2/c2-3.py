# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:19:05 2024

@author: hp
"""

list=[]
for i in range(6):
    list.append(input("enter a name:"))
for n in list:
    if n.lower().startswith('a') or n.upper().startswith('A'):
        print(f"{n}")