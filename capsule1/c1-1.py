# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:56:05 2024

@author: hp
"""

name=input("Please enter your name:")
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
print(f"orginal values are:{n1},{n2}")
n1,n2=n2,n1
print(f"swapped values are:{n1},{n2}")