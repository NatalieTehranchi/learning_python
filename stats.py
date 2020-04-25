#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

numbers = []
for line in fileinput.input():
	if line.startswith('#'): continue 
	numbers.append(float(line))

#count
count = len(numbers)

#max and min
numbers.sort()
min = numbers[0]
max = numbers[-1]

#mean
sum = sum(numbers)
mean = sum/count

#standard deviation
x = 0 
for n in numbers:
	x += ((n - mean)**2)
stdev = (sqrt(x/count))

#median
m = (count+1)/2
mup= (int(m))
mdown= (int(m - 1))
median = (numbers[mup] + numbers[mdown])/2


print(f'Count:{count}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mean: {mean}')
print(f'Std. dev: {stdev:.5}')
print(f'Median: {median}')



"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""



