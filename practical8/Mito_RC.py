# -*- coding: utf-8 -*-
"""
Created on Fri May 15 09:23:22 2020

@author: Administrator
"""


import re
import os
os.chdir("C:\Users\Administrator\Desktop\.spyder-py3\material")
myfasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
M_seq=re.findall(r'(>.*?:Mito:.*[AGCT\n]+?)>',myfasta.read())
myfasta.close()
out_seq=[]
outfasta=open(input("Type the name of new FASTA here:>"),"w")
for seq in M_seq:
    lines= list(seq.split('\n'))
    seq_head=lines[0]
    seq_def = ''.join(lines[1:]).replace('\n', '').translate(str.maketrans("AGCT","TCGA"))[::-1]
    head='> '+re.findall(r'Q[\d]*',seq_head)[0]+' '+str(len(seq_def))
    outfasta.write(head+'\n'+seq_def+'\n')
outfasta.close()