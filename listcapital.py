# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:31:42 2023

@author: Ashwin Suresh
"""
#Q2

names = ["Shankaran","Jonathan","James","Justin","Magnus"]

snames = []


for i in names:
    x = i[:4].upper()
    snames.append(x)
    
for i in snames:
    print(i)    