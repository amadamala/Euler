"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
abundants = {}

"""
It can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
"""
UPPER_LIMIT = 28123

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
	for i in range(12, UPPER_LIMIT):
		for j in range(12, i/2):
			n1 = j
			n2 = i - j
			if isAbundant(n1) and isAbundant(n2):
				print i, n1, n2
				break;
		else:
			sum += i				
	print sum			

def main():
	# for i in range(12, UPPER_LIMIT/2):
	# 	if isAbundant(i):
	# 		abundants[i] = i
	# print abundants		
	sum_numbers_cannot_written_as_sum_of_2_abundants()

if __name__ == "__main__":
    main()
