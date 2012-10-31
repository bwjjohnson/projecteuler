#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 18
# By starting at the top of the triangle below and moving to adjacent numbers 
# on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
# NOTE: As there are only 16384 routes, it is possible to solve this problem 
# by trying every route. However, Problem 67, is the same challenge with a 
# triangle containing one-hundred rows; it cannot be solved by brute force, 
# and requires a clever method! ;o)

with open( 'data/problem018.dat', 'r') as f:
    lines = f.readlines()
    lines.reverse()
    next = []
    for line in lines:
        cur = [int(i) for i in line.split()]
        if len(next) == len(cur):
            cur = [ cur[i] + next[i] for i in range(len(cur))] 
        next = []
        for i in range(len(cur)-1):
            next.append( cur[i] if cur[i] > cur[i+1] else cur[i+1] )
    print( cur[0] )
