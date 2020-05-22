#!/usr/bin/env python3

#A program that computes hydrophobicity in a window and creates file of values for plots
# Let the user choose the method (see below)
# https://en.wikipedia.org/wiki/Hydrophilicity_plot
# https://en.wikipedia.org/wiki/Hydrophobicity_scales

import argparse
import biotoolbox

parser = argparse.ArgumentParser(
	description='Testing hydrophobicity using desired method')
parser.add_argument('--input', required=True, type=str,
	metavar='<str>', help='file input')
parser.add_argument('--window', required=True, type=int,
	metavar='<int>', help='Window size')
parser.add_argument('--method', required=True, type=str,
	metavar='<str>', help='hydrophobicity method: kd, is, os, ios, cc ')
parser.add_argument('--switch', action='store_true',
	help='off reports values/on saves individual values for plots')
arg = parser.parse_args()

# dictionaries of options

kd_method  = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2}
       
is_method  = {'I': -0.31,'L':-0.56,'F':-1.13,'V':0.07,'M':-0.23,
       'P':0.45,'W':-1.85,'H':0.17,'T':0.14,'E': -0.01,
       'Q': 0.58,'C':-0.24,'Y':-0.94,'A': 0.17,'S':0.13,
       'N':0.42,'D':-0.07,'R':0.81,'K':0.99,'G':0.01}
       
os_method  = {'I':-1.12,'L':-1.25,'F':-1.71,'V':-0.46,'M':-0.67,
       'P':0.14,'W':-2.09,'H':0.11,'T':0.25,'E': 0.11,
       'Q': 0.77,'C':-0.02,'Y':-0.71,'A': 0.50,'S':0.46,
       'N':0.85,'D':0.43,'R':1.81,'K':2.80,'G':1.15}
       
cc_method  = {'I': -0.528,'A':-0.495,'F':-0.370,'L':-0.370,'M':-0.324,
       'P':-0.322,'V':-0.308,'W':-0.270,'C':0.081,'G':0.386,
       'T': 0.853,'S':0.936,'Y':1.677,'K': 2.101,'Q':2.176,
       'N':2.354,'E':3.173,'R':4.383,'D':9.573,'H':2.029}
       
ios_method = {'I': -0.81,'L':-0.69,'F':-0.58,'V':-0.53,'M':-0.44,
       'P':-0.31,'W':-0.24,'H':-0.06,'T':0.11,'E':0.12,
       'Q': 0.19,'C':0.22,'Y':0.23,'A': 0.33,'S':0.33,
       'N':0.43,'D':0.50,'R':1.00,'K':1.81,'G':1.14}
	
def hydrophobicity(protein, method):
	table = None
	if   method ==  'kd': table = kd_method
	elif method ==  'is': table = is_method
	elif method ==  'os': table = os_method
	elif method ==  'cc': table = cc_method
	elif method == 'ios': table = ios_method
	score = 0
	for aa in protein:
		if aa in table: 
			score += table[aa]
	return score/len(protein)

for name, protein in biotoolbox.read_fasta(arg.input):
	if arg.switch: 
		filename = name+'.csv' 
		with open(filename,'w') as fp:
			for i in range(len(protein)- arg.window+1):
				peptide = protein[i:i+arg.window]
				fp.write(f'{i+1},{hydrophobicity(peptide, arg.method)}\n')
	else:
		for i in range(len(protein)- arg.window+1):
			peptide = protein[i:i+arg.window]
			print(i+1, hydrophobicity(peptide, arg.method))

	
 
"""
python3 hydrophobicity.py --input proteins.fasta.gz --window 11 --method kd
"""
