#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n  n/2 (n is even)
# n  3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following 
# sequence:
#
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
# 

d = {'1':1}
def chain( n ):
    if str(n) in d:
        return d[str(n)]
    if n%2 == 0:
        d[str(n)] = chain(int(n/2)) + 1
    else:
        d[str(n)] = chain(3*n+1) + 1
    return d[str(n)]
cur = 999999
ans = 1
while cur > 1:
    z = chain(cur)
    if ans < z: 
        ans = z
        last = cur
    cur -= 1
print( last )
