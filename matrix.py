# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 13:45:42 2018

@author: bmpatel
"""

a, b=input().split()

a=int(a)
b=int(b)

output=1
for i in range(a):
    row=''
    for j in range(b):
        if(j==b-1):
            row=row+str(output)
        else:
            row=row+str(output)+' '              
        output=output+1
    if(i==a-1):
        print(row,end='')
    else:
        print(row)
