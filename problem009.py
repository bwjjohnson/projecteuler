#!/usr/bin/python
#
# Project Euler (projecteuler.net) - Problem 9
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
import sys

target = 1000
a = 1
b = 2
c = math.sqrt(a*a + b*b)
while a + b + c < target:
  while a + (b-1) + c < target:
    c = math.sqrt(a*a + b*b)
    if int(c) == c and (a + b + c) == target:
      print int(a * b * c)
      sys.exit()
    b += 1
  a += 1
  b = a + 1
  c = math.sqrt(a*a + b*b)
