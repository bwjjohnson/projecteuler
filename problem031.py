#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are 
# eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can £2 be made using any number of coins?

c = [1,2,5,10,20,50,100,200]
def count( n, m ):
    if n == 0: return 1
    if n < 0: return 0
    if m < 0 and n >= 1: return 0
    return count( n, m - 1 ) + count( n - c[m], m )
print( count(200,len(c)-1) )
