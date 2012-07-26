#!/usr/bin/python
#
# Project Euler (projecteuler.net) - Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
# the 6th prime is 13.
# What is the 10 001st prime number?

import math

n = 10001
a = 3
result = [2]
num = 2
while num <= n:
  cont = 0
  while 1 :
    divisor = result[cont]
    (quotient, remainder) = divmod(a,divisor)
    if (remainder):
      if divisor <= quotient :
        cont += 1 
      else:
        result.append(a)
        num += 1
        break
    else:
      break
  a += 1
print result[n-1]
