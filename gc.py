#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc_count= 0 

for c in dna:
	if c == 'G' or c == 'C':
		gc_count += 1
print('%.2f' % (gc_count/len(dna)))
print('{:.2f}'.format(gc_count/len(dna)))
print(f'{gc_count/len(dna):.2f}')

"""
0.42
0.42
0.42
"""