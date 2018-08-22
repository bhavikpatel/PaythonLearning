# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 12:30:21 2018

@author: bmpatel
"""

with open("file1.txt") as myfile:
    print(myfile.read())
    myfile.write("I Edit File through paython program")
myfile.close()