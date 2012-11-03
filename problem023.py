#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 23
# A perfect number is a number for which the sum of its proper divisors is 
# exactly equal to the number. For example, the sum of the proper divisors of 
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less 
# than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24. By 
# mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit 
# cannot be reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two abundant numbers 
# is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

import math
def d(n):
    pd = set([1])
    for d in range(2, int(math.ceil(math.sqrt(n)))+1):
        if n % d == 0: 
            pd.add( d ); pd.add( int(n / d) )
    return sum(pd)
ab = []
ul = 28123
for n in range(12,ul): 
    if d(n) > n : ab.append( n )
ch = set(range(25,ul))
for n in ab:
    for m in ab:
        try: ch.remove( n + m )
        except KeyError: pass
print( sum(range(24)) + sum(ch) )
