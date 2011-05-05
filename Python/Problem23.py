"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
abundants = []

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

def main():
	for i in range(12, UPPER_LIMIT+1):
		if isAbundant(i):
			abundants.append(i)
	print abundants		
	
if __name__ == "__main__":
    main()

