# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 06:54:06 2020

@author: Administrator
"""
#4.1
a = 123
b = 123123
c = b / 7
d = c / 11
e = d / 13

if a == e:
    print ("a is equal to e")
if a > e:
    print ("a is larger than e")
if a < e:
    print ("a is smaller than e")
    
# Because 7*11*13=1001

#4.2
X = True
Y = False
if X == True and Y == False:
    Z = True
elif X == False and Y == True:
    Z = True
else:
    Z = False
    
W = (X!=Y)
print("W is", W, "and Z is", Z)
print("Is W same as Z ?", W == Z)
