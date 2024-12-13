# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:28:18 2024

@author: hp
"""

def square(num):
    print(num**2)
def cube(num):
    print(num**3)
list=[]
for i in range(10):
    list.append(int(input("enter a number:")))
for n in list:
    if n%2==0:
        square(n)
    else:
        cube(n)