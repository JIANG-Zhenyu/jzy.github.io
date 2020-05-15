# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:26:16 2020

@author: Administrator
"""
#copy the gene lengths
#markers could use another string of numbers
#use L.sort() could easily get the extreme numbers at the front and the end of the list
#use del() couid remove the two numbers
#use print() and copy the code of boxplot from PPT

#gene_lengths=(9410,3944141,4442,105338,19149,76779,126550,36926,842,15981)
L = [9410,3944141,4442,105338,19149,76779,126550,36926,842,15981]
L.sort()
del(L[0])
del(L[8])

print(L)

import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(L,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
             )
plt.show()