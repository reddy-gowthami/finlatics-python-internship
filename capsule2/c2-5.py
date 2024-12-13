# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:35:48 2024

@author: hp
"""

c=int(input("enter no of roses u want:"))
d=int(input("enter the distance from your place:"))
cc=c*10
print(f"the cost of roses is {cc}")
dd=0
if d<5:
    print("delivery charge is 25")
    dd=25
elif d>=5 and d<=10:
    print("delivery charge is 50")
    dd=50
else:
    print("delivery charge is 75")
    dd=75
print(f"The total charge is {cc}+{dd}={cc+dd}")