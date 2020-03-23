# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 07:05:34 2020

@author: Administrator
"""

# the power of 2
# from the text, x < 2**13
# answer = "1750 is"
# So start the loop with i=13
# if x >= 2**i,
#    n=i, i=i-1, x=x-2**i
#    anewer = answer + "+2**"+ n
#else: i=i-1
# use while-loop
# print (str)

i = 13
x = 1750
answer = "1750 is"
n = 0
while i>=1:
    if x >= 2**i:
        n = i
        x = x - 2**i
        answer = answer + "+2**" + str(n)
        i=i-1
    else:
        i = i - 1


print (answer)
        