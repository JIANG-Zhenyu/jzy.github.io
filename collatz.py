# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 07:00:39 2020

@author: Administrator
"""

# Suppose n is 25
# According to the  definition of the Collatz sequence:
# use while-loop
# if n % 2 = 0, n=n/2,  anewer = answer + "-"+ n
# else: n= 3*n + 1, anewer = answer + "-"+ n
# print (answer)

n = 25
answer = "25"
while n > 1:
    if n%2 == 0:
        n= n/2
        anewer = answer + "-" + str(n)
    else:
        n= 3*n + 1
        anewer = answer + "-" + str(n)

print(answer)