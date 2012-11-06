#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction 
# a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?

n = 1001
i = ans = 1
l = 2
while l < n**2:
    l += i # down
    ans += l
    i += 1
    l += i # left
    ans += l
    l += i # up
    ans += l
    i += 1
    l += i # right
    ans += l - 1
print( ans )
