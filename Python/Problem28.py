# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def solution(N):
	s = 1 + sum(x for x in list(4 * (2 * i+ 1)**2  - 12 * i  for i in range(1, (N + 1)/2) ))
	return s
def sol(N):
	sum = 1;   # for spiral 1, 1 is the only element 
	for i in range(1, (N + 1)/2):
		sum = sum + 4 * (2 * i + 1)**2 - 12 * i 
	print sum
	
print solution(1001)
print sol(1001)