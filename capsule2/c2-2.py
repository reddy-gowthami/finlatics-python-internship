# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:14:24 2024

@author: hp
"""
def count(word):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    c=0
    for char in word:
        if char in vowels:
            c=c+1
    return c
word=input("enter the word:")
r=count(word)
print(r)