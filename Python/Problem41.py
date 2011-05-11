from math import sqrt
def isprime(n):
	prime = True
	for i in range(3, sqrt(n) + 1, 2):
		if n % i == 0:
			prime = False
			break
	if (n % 2 !=- 0 and prime and n > 2) or n == 2:
		return True
	else:
		return False			

def foo():
	for i in range(2, 100000):
		if isprime(i):
			ispandigital(i)
			
def ispandigital(n):
	l = list(str(n)).sort()
	for i in range(l):
		if i != l(i):
			return False	
	print n		
	return True		
foo()