facts = [1,2,6,24,120,720,5040,40320,362880,3628800]

def foo():
	N = 1000000
	for i in range(len(facts)-1, 0, -1):
		if facts[i] < N:
			print facts[i], (N/facts[i])
			N = N - ( (N / facts[i]) * facts[i])

def testBin():
	for i in range(16):
		print int2bin(i)
		
def int2bin(n, count=4):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])


foo()		
print testBin()
	
	
	
""" 
2(362880) + 6(40320) + 6(5040) + 2(720) + 5(120) + 1(24) + 2(6) + 2 (2) + 1 (0) 

   
0, 1, 2, 3, 4, 5, 6, 7, 8, 9  
-----------------------------
2 - 0, 1, 3, 4, 5, 6, 7, 8, 9  
7 - 0, 1, 3, 4, 5, 6, 8, 9
8 - 0, 1, 3, 4, 5, 6, 9
3 - 0, 1, 4, 5, 6, 9
9 - 0, 1, 4, 5, 6
1 - 0, 4, 5, 6
5 - 0, 4, 6
6 - 0, 4
                           
2783915640
"""	
