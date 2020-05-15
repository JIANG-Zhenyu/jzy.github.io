# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:25:52 2020

@author: Administrator
"""
# markers could change the words in "DNA" string to test.
# start with a=t=c=g=0
# for i in DNA:if i =="A"
# a = a+1
# as same as t,c,g
# then copy the code of pie chart in the PPT 


DNA = "ATCGATCGATCGATCGA"
nucle= {'A':0, 'T':0, 'C':0 ,'G':0}
for i in DNA:
    if i =="A":
       nucle['A'] += 1
    elif i =='T':
       nucle['T'] += 1
    elif i =='C':
       nucle['C'] += 1
    elif i =='G':
       nucle['G'] += 1

print('The DNA string(',DNA,')has',nucle['A'], 'A',nucle['T'], 'T',nucle['C'], 'C',nucle['G'], 'G',)
    
import matplotlib.pyplot as plt
labels = ['A' ,'T','C','G']
sizes = [nucle['A'],nucle['T'],nucle['C'],nucle['G']]
explode = (0,0.1,0,0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False,
          startangle=90)
plt.axis ('equal')
plt.show()


