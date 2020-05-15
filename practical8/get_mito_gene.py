# -*- coding: utf-8 -*-
"""
Created on Fri May 15 09:13:06 2020

@author: Administrator
"""


import re
import os
os.chdir("C:\Users\Administrator\Desktop\.spyder-py3\material")
myfasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
all_seq=re.findall(r'(>.*?:Mito:.*[AGCT\n]+?)>',myfasta.read())
myfasta.close()
outfasta=open("mito_gene.fa","w")
for seq in all_seq:
    lines= list(seq.split('\n'))
    seq_head=lines[0]
    seq_def = ''.join(lines[1:]).replace('\n', '')
    head = '> ' + re.findall(r'Q[\d]*', seq_head)[0] + ' ' + str(len(seq_def))
    outfasta.write(head+'\n'+seq_def+'\n')
outfasta.close()