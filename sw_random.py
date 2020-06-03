#!/usr/bin/env python3

import argparse
import biotoolbox
import random

parser = argparse.ArgumentParser(
	description='Program generates random sequences and calculates Smith Waterman score')
# required arguments

parser.add_argument('--l', required=True, type=int,
	metavar='<int>', help='length of sequences generated')
parser.add_argument('--runs', required=True, type=int,
	metavar='<int>', help='number of sequences created')
#options
#sw values:
parser.add_argument('--m', required=False, type=int, default= 1,
	metavar='<int>', help='match score in sw algorithm [%(default)i]')
parser.add_argument('--n', required=False, type=int, default= -1,
	metavar='<int>', help='mismatch score in sw algorithm [%(default)i]')
parser.add_argument('--gap', required=False, type=int, default= -1,
	metavar='<int>', help='gap score in sw algorithm [%(default)i]')

#random sequence options
parser.add_argument('--a', required=False, type=int, default= 1,
	metavar='<int>', help='weight of A [%(default)i]')
parser.add_argument('--c', required=False, type=int, default= 1,
	metavar='<int>', help='weight of C [%(default)i]')
parser.add_argument('--g', required=False, type=int, default= 1,
	metavar='<int>', help='weight of G [%(default)i]')
parser.add_argument('--t', required=False, type=int, default= 1,
	metavar='<int>', help='weight of T [%(default)i]')
	
arg = parser.parse_args()

def random_seq(length, a, c, g, t): #lowercase = weights
	comp = 'A'* a + 'C'* c + 'G'* g + 'T'* t
	dna = []
	for i in range(length):
		dna.append(random.choice(comp))
	return ''.join(dna)

scores = []
for i in range(arg.runs):
	s1 = random_seq(arg.l, arg.a, arg.c, arg.g, arg.t)
	s2 = random_seq(arg.l, arg.a, arg.c, arg.g, arg.t)
	score, a1, a2 = biotoolbox.sw(s1, s2, arg.m, arg.n, arg.gap)
	scores.append(score)
for s in scores:
	print(s)
	
"""
for histogram shape use command line:
python3 sw_random.py --l X --runs Y | sort -n | uniq -c 
"""

