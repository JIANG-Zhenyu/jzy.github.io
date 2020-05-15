# -*- coding: utf-8 -*-
"""
Created on Fri May 15 09:06:05 2020

@author: Administrator
"""


seq = 'ATGCGACTACGATCGAGGGCCAT'
print(seq.translate(str.maketrans("AGCT","TCGA"))[::-1])