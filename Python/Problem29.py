#!/usr/bin/env python
# encoding: utf-8
"""
Problem29.py

Created by amadamala on 2011-05-12.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os

def distinct_terms(a, b):
	for i in range(a, b+1):
		for j in range(a, b + 1):
			print i, j

def main():
	a = 2
	b = 5
	distinct_terms(a, b)


if __name__ == '__main__':
	main()

