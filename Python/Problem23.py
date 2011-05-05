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
	sum = 0
	for i in range(1, LIMIT):
		j = 12
		while j < (i/2 + 1):
			n1 = j
			n2 = i - j
			if (n1 in abundants) and (n2 in abundants):
				# print i, n1, n2
				break
			j += 1
		if j != i/2:
			# print i
			sum += i
	print sum			

def main():
	for i in range(12, (LIMIT/2 + 1)):
		if isAbundant(i):
			abundants[i] = i
	# print abundants		
	sum_numbers_cannot_written_as_sum_of_2_abundants()

if __name__ == "__main__":
    main()
