#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 25
# A unit fraction contains 1 in the numerator. The decimal representation of 
# the unit fractions with denominators 2 to 10 are given:
# 
# 1/2    =     0.5
# 1/3    =     0.(3)
# 1/4    =     0.25
# 1/5    =     0.2
# 1/6    =     0.1(6)
# 1/7    =     0.(142857)
# 1/8    =     0.125
# 1/9    =     0.(1)
# 1/10    =     0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
# seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.

import sys

def isprime(n):
    n = abs(int(n))
    if n < 2: return False
    if n == 2: return True    
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

for n in range(1000,1,-1):
    if not isprime(n): continue
    lpow = 1
    done = False
    while not done:
        for mpow in range( lpow-1, 0, -1):
            if ( 10**lpow - 10**mpow ) % n == 0:
                if lpow - mpow == n - 1: print( n ); sys.exit(0)
                done = True; break
        lpow += 1
