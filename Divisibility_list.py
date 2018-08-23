# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 09:40:22 2018

@author: bmpatel
"""

lst_numb=[]
for i in range(0,50):
    lst_numb.insert(i,i+1)

a = input()

a=int(a)

count=0
for data in lst_numb:
    if data!=0:
        if data%a==0:
            count=count+1
print(count-1)