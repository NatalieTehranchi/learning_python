#!/usr/bin/env python3

import gzip
import sys

# Write a program that finds peptidies within protein sequences
# Command line:
#	python3 pepsearch.py IAN

def read_fasta(filename): #creating our function 
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else: 
		fp = open(filename)
	
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()
	
protein_file = sys.argv[1] #the file
pattern = sys.argv[2] #what we're looking for 'IAN'

for name, seq in read_fasta(protein_file): #using our function here
	if pattern in seq:
		print(seq)
"""
python3 pepsearch.py proteins.fasta.gz IAN | wc -w
	43
"""
