from time import *
from collections import defaultdict
"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
abundants = defaultdict(int)

"""
It can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
"""
LIMIT = 28123

def isAbundant(n):
	sum = 0
	for i in range(1, n/2 + 1):
		if n % i == 0:
			sum += i
	if sum > n :
		return True
	# print sum

def sum_numbers_cannot_written_as_sum_of_2_abundants():
	sum = (LIMIT * (LIMIT + 1) ) / 2

	for i in range(1, LIMIT + 1):
		for j in range(1, i/2 + 1):
			n1 = j
			n2 = i - j
			if (n1 in abundants) and (n2 in abundants):
				# print i, n1, n2
				sum = sum - i;
				break

	print sum			

def main():
	time_taken = clock()
	
	for i in range(12, LIMIT):
		if isAbundant(i):
			abundants[i] = i
	# print abundants		
	sum_numbers_cannot_written_as_sum_of_2_abundants()
	print "Time taken = %.2f" % (clock() - time_taken)
	
if __name__ == "__main__":
    main()