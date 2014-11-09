#!/usr/bin/python
###########################################################################
# filename      : split_n_rename.py
# date written  : 20/02/2013
# written by    : THChew (teonghan@gmail.com)
# description   : split fasta and rename
# last update   : 20/02/2013    - version 0.1
###########################################################################
# split length function
# original author: Abu Zahed Jony
def split_by_length(s,block_size):
    w=[]
    n=len(s)
    for i in range(0,n,block_size):
        w.append(s[i:i+block_size])
    return w

import sys
from Bio import SeqIO
import re
if len(sys.argv)!=int(3):
    print "Invalid argument"
    print "Usage: python split_n_rename.py fasta name"

else:
    fasta=str(sys.argv[1])
    name='>'+str(sys.argv[2])
    out=fasta+'.out'
    counter=1
    f=open(out,"w")
    for seq_record in SeqIO.parse(fasta, "fasta"):
        sequence=seq_record.seq
        sequence=sequence.tomutable()
        sequence_string=sequence.data
        pattern="[N]+"
        for match in re.finditer(pattern,sequence_string):
            s=match.start()
            e=match.end()
            sequence[s:e]='-'
        sequence=str(sequence)
        sequence=sequence.split('-')
        print(sequence)
        for item in sequence:
            write_str=split_by_length(item,80)
            f.write(name+str(counter)+'\n')
            for i in write_str:
                f.write(i+'\n')
            counter=counter+1
    f.close()
