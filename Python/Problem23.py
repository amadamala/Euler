"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
It can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
"""

from time import *
from collections import defaultdict

LIMIT = 28123
abundants = [None] * LIMIT


# def isAbundant(n):
# 	sum = 0
# 	for i in range(1, n/2 + 1):
# 		if n % i == 0:
# 			sum += i
# 	# print n, sum		
# 	if sum > n :
# 		return True

def d(n):
	for i in range(1, n + 1):
		j = 2
		while (i * j) < n:
			if abundants[i * j] is None:
				abundants[i * j] = i
			else:
				abundants[i * j] += i
			j += 1
	# for i in range(len(abundants)):
	# 	print i, abundants[i]

def sum_numbers_cannot_written_as_sum_of_2_abundants():
	sum = (LIMIT * (LIMIT + 1) ) / 2

	for i in range(1, LIMIT + 1):
		for j in range(1, i/2 + 1):
			n1 = j
			n2 = i - j
			if (n1 < abundants[n1]) and (n2 < abundants[n2]):
				# print i, n1, n2
				sum = sum - i;
				break

	print sum			

def main():
	time_taken = clock()
	d(LIMIT)
	# time_taken = clock() - time_taken
	# print "Time taken = %.2f" % (clock() - time_taken)		
	# print abundants		
	sum_numbers_cannot_written_as_sum_of_2_abundants()
	print "Time taken = %.2f" % (clock() - time_taken)		

if __name__ == "__main__":
    main()