"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
a = []

def proper_divisors(n):
	print n
	for i in range(1, n/2 + 1):
		if n % i == 0:
			a.append(i)
	print a

proper_divisors(10)		