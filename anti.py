#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
comp = '' #comp for complement
anti = '' #holds reverse complex
for nt in dna:
	if   nt == 'A': comp = 'T' + comp
	elif nt == 'C': comp = 'G' + comp
	elif nt == 'G': comp = 'C' + comp
	else:           comp = 'A' + comp
print(comp)


"""
TTTTTTTTTTTCAGT
"""
