# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 09:40:22 2018

@author: bmpatel
"""

lst_numb=[]
for i in range(0,50):
    lst_numb.insert(i,i+1)

a, b = input().split()

a=int(a)
b=int(b)

lst_numb=lst_numb[a:b]

for data in lst_numb:
    print(data)