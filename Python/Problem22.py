"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each 
name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.
What is the total of all the name scores in the file?
"""

""" open file and read file"""
BASE = 64 			# subtracting BASE from Ascii of char gives its position
f = open('names.txt', 'r+')
input = f.read()

def total_name_score():
	s = input.replace('"','').split(',')
	s.sort()
	
	sum = 0
	for pos in range(1, len(s)+1)
		s = 0;
		# find the sum of characters order
		for j in list(item):
			s = s + ord(j) - BASE
		sum = sum + (s * pos)
	print sum	
total_name_score()		