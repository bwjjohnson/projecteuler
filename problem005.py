#!/usr/bin/python
#
# Project Euler (projecteuler.net) - Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 
# 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

import sys

n = 20
x = 9699690 # 2*3*5*7*11*13*17*19 = product of primes < 20 
while 1:
  newx = False
  for d in range(n,1,-1):
    if x % d != 0:
      rem = ( x % d * 1.0 ) / d
      m = 1
      while 1:
        if m * rem == int( m * rem ):
          break
        m += 1
      x *= m
      newx = True
      break
  if not newx: print x; break

