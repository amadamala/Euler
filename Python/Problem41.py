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

# def perm(s):
# 	perm1('', s)
def perm(prefix , s):
	N = len(s)
	if N == 0:
		if int(prefix) % 2 != 0:
			if isprime(int(prefix)) and ispandigital(int(prefix)):
				print prefix
	else:
		for i in range(N):
			perm((prefix + s[i]), (s[0:i] + s[i+1:N]))
               # perm1(prefix + s.charAt(i), s.substring(0, i) + s.substring(i+1, N));
				
def foo(n):
	for i in range(n):
		if isprime(i) and ispandigital(i):
			print i

def ispandigital(n):
	l = list(str(n))
	l.sort()
	for i in range(len(l)):
		if (i+1) != int(l[i]):
			return False
	# print n
	return True

def main():
	t = clock()
	foo(10000)
	print "Time taken: %0.2f" %(clock() - t)
	
	t = clock()
	perm("", '1234567')
	print "Time taken: %0.2f" %(clock() - t)
	
if __name__ == '__main__':
	main()