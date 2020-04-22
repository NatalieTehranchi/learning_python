#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
codon= 3

for i in range (0,len(dna)-codon+1,3):
	print(i, dna[i: i+3])
	

"""
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
