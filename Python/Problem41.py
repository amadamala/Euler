from math import sqrt
from time import *

def isprime(n):
	prime = True
	for i in range(3, int(sqrt(n)) + 1, 2):
		if n % i == 0:
			prime = False
			break
	if (n % 2 !=- 0 and prime and n > 2) or n == 2:
		return True
	else:
		return False

permutations = []
# Method to generate all permutations
def perm(s, prefix = ""):
	N = len(s)
	if N == 0:
		p = int(prefix)
		if p % 2 != 0:
			if isprime(p) and ispandigital(p):
				permutations.append(prefix)
	else:
		for i in range(N):
			perm((s[0:i] + s[i+1:N]), (prefix + s[i]))
			
def ispandigital(n):
	l = list(str(n))
	l.sort()
	for i in range(len(l)):
		if (i+1) != int(l[i]):
			return False
	return True

def main():
	t = clock()
	perm('1234567')
	print max(permutations)
	print "Time taken: %0.2f" %(clock() - t)
	
if __name__ == '__main__':
	main()