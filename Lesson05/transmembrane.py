#!/usr/bin/env python3

import argparse
import biotoolbox
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

parser = argparse.ArgumentParser(
	description='Predicts transmembrane proteins.')
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='protein file')
	
parser.add_argument('--win1', required=False, type=int, default=8,
	metavar='<int>', help='length of signal peptide [%(default)i]' )
parser.add_argument('--win2', required=False, type=int, default=11,
	metavar='<int>', help='length of hydrophobic region [%(default)i]')
parser.add_argument('--kd1', required=False, type=float, default=2.5,
	metavar='<float>', help='kd value for signal peptide [%(default)f]')
parser.add_argument('--kd2', required=False, type=float, default=2.0,
	metavar='<float>', help='kd value for hydrophobic region [%(default)f]')

arg = parser.parse_args()


for name, seq in biotoolbox.read_fasta(arg.file):
	if biotoolbox. hasHydrophobicHelix(seq[0:30], arg.kd1, arg.win2)\
	and biotoolbox. hasHydrophobicHelix(seq[30:len(seq)], arg.kd2, arg.win2): 
		print(name)
		

"""
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
