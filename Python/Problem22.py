"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each 
name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.
What is the total of all the name scores in the file?
"""

import string
from time import *

def total_name_score():
	start = clock()
	hash = dict(zip([x for x in string.letters[26:]],range(1,27)))
	f = open('names.txt', 'r')
	words = sorted(f.read().replace('"','').split(','))
	sum = 0
	for pos in range(1, len(words) + 1):
		s = 0
		for c in list(words[pos - 1]): 
			s = s + hash[c]
		sum = sum + (s * pos)
	
	print "Sum = %d" %sum	
	print "Time taken = %.2f" % (clock()-start)
total_name_score()