#!/usr/bin/env python
# encoding: utf-8
"""
Problem30.py

Created by amadamala on 2011-05-12.
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

