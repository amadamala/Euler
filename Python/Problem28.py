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

def spiral_sum(N):
	s = 1 + sum(x for x in list(4 * (2 * i+ 1)**2  - 12 * i  for i in range(1, (N + 1)/2) ))
	print "One liner ::", s
	
def spiral_sum_readable(N):
	s = 1;   # for spiral 1, 1 is the only element 
	for i in range(1, (N + 1)/2):
		s = s + 4 * (2 * i + 1)**2 - 12 * i 
	print "Readable solution:: ", s

N = 1001	
spiral_sum(N)
spiral_sum_readable(N)
