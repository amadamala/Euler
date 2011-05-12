#!/usr/bin/env python
# encoding: utf-8
"""
Problem30.py

Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.


Created by amadamala on 2011-05-12.˝
Copyright (c) 2011 __amadamala__. All rights reserved.
"""

import sys
import os


def main():
	n = 5 * (9 ** 5)
	total = 0
	for i in range(2, n): # 1 is not considered as per rools
		s = 0
		for j in str(i):
			s += int(j) ** 5
		if i == s :
			total += s	
	print total		

if __name__ == '__main__':
	main()

