#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line: python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>

def rand_dna(lenseq, a, c, g, t): #setting parameters 
	seq = []
	for nt in range(lenseq):
		r = random.random()
		if r < a:		 	 seq.append('A')
		elif r < a + c: 	 seq.append('C')
		elif r < a + c + g:  seq.append ('G')
		else: 				 seq.append('T')
			
	return ''.join(seq)

#command line functions:
count = int(sys.argv[1])
min   = int(sys.argv[2])
max   = int(sys.argv[3])
a     = float(sys.argv[4])
c     = float(sys.argv[5])
g     = float(sys.argv[6])
t     = float(sys.argv[7])


#printing our sequence 

for v in range(count):
	l = random.randint(min, max)
	dna = rand_dna(l, a, c, g, t)
	print(f'>{v}')
	print(dna)
	
"""

"""
