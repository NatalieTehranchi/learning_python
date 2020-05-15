#!/usr/bin/env python3

import gzip
import sys
# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

def read_fasta(filename):
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

	
def kd(seq):
	sum = 0 
	for c in seq:
		if c == 'I': sum += 4.5
		elif c == 'V': sum += 4.2
		elif c == 'L': sum += 3.8
		elif c == 'F': sum += 2.8
		elif c == 'C': sum += 2.5
		elif c == 'M': sum += 1.9
		elif c == 'A': sum += 1.8
		elif c == 'G': sum += -0.4
		elif c == 'T': sum += -0.7
		elif c == 'S': sum += -0.8
		elif c == 'W': sum += -0.9
		elif c == 'Y': sum += -1.3
		elif c == 'P': sum += -1.6
		elif c == 'H': sum += -3.2
		elif c == 'E': sum += -3.5
		elif c == 'Q': sum += -3.5
		elif c == 'D': sum += -3.5
		elif c == 'N': sum += -3.5
		elif c == 'K': sum += -3.9
		elif c == 'R': sum += -4.5
	return sum/len(seq)
			
def hasHydrophobicHelix(seq, kd_val, length):
	for i in range(len(seq) -length+1): #don't want it to go past the window length
		peptideregion = seq[i:i+length]
		if kd(peptideregion) >= kd_val and 'P' not in peptideregion:
			return True
	return False

for name, seq in read_fasta('proteins.fasta.gz'):
	if  hasHydrophobicHelix(seq[0:30], 2.5, 8) and\
	hasHydrophobicHelix(seq[30:len(seq)], 2.0, 11): print(name)
"""
for the first 30 peptides need KD score to 8 aa within the 30
	KD function
how to restrict to first 30? 
after 30 aa: 11 aa KD score

Amino acids w/KD score > 2.5 = C?, F L V I
>2.0 = A M C F L V I 

Size exclusion? 
if c is c f l v i within 8 aa? in seq[i:i+30] 

if both are true, print the name

python3 transmembrane.py proteins.fasta.gz
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
