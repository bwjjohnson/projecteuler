#!/usr/bin/python
#
# Project Euler (projecteuler.net) - Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import sys

def is_palindrome(s):
  return all(s[i] == s[-(i + 1)] for i in range(len(s)//2))

for x in range(997799,100001,-1):
  if is_palindrome(str(x)):
    for d in range(999,100,-1):
      (q, r) = (x // d, x % d)
      if r == 0 and q >= 100 and q <= 999:
        print d, "*", q, " = ", x
        sys.exit()

