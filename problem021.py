#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 20
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and 
# each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 
# 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

import math

def d(n):
    pd = set([1])
    for d in range(2, int(math.ceil(math.sqrt(n)))+1):
        if n % d == 0:
            pd.add( d )
            pd.add( int(n / d) )
    return sum(pd)
dv = [0]
for n in range(1,10000): dv.append( d(n) )
an = set()
for d in range( 1, len(dv) ):
    if ( dv[d] < len(dv) 
         and d != dv[d]
         and d == dv[dv[d]] ):
        an.add( d )
        an.add( dv[d] )
print( sum(an) )
