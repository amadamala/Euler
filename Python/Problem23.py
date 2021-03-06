"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
It can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
"""

"""

The upper bound for numbers that cannot be expressed as the sum of two numbers is actually
20161 not 28123 (as shown here). 
All even numbers greater than 48 can be written as the sum of two abundant numbers 
Minimum abundant not multiple of 2 or 3 = 5391411025
"""
from time import *
from collections import defaultdict

LIMIT = 20161
abundants = [None] * LIMIT

def d(n):
	for i in range(1, n + 1):
		j = 2
		while (i * j) < n:
			if abundants[i * j] is None:
				abundants[i * j] = i
			else:
				abundants[i * j] += i
			j += 1

def sum_numbers_cannot_written_as_sum_of_2_abundants():
	sum = LIMIT * (LIMIT + 1)  / 2
	for i in range(1, LIMIT + 1):
		# All even numbers greater than 48 can be written as the sum of two abundant numbers 
		if i > 48 and i % 2 == 0:
			sum = sum - i
		else:		
			for j in range(1, i/2 + 1): 
				n1 = j
				n2 = i - j
				if (n1 < abundants[n1]) and (n2 < abundants[n2]):
					sum = sum - i;
					break
	print sum	
# 4179871
def main():
	time_taken = clock()
	d(LIMIT)		
	sum_numbers_cannot_written_as_sum_of_2_abundants()
	# solution()
	print "Time taken = %.2f" % (clock() - time_taken)		

if __name__ == "__main__":
    main()