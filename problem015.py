#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 15
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without 
# backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

# The approach for this algorithm is to use dynamic programming such that the
# solution is computed from the summation of each of its subproblems starting
# with a 1x1 grid and working up to a NxN grid
d = 20 # The dimension of the grid
n = 1  # The current row to compute
g = list(range(2,d+2)) # pre-compute the first row of route counts
# iterate through the rows calculating the route counts from the summation
# of the previous rows route counts
while n < d:  
    # the first value of the next row is twice because along the diagonal the 
    # number of routes is the same when either route is taken
    h = [g[1]*2] 
    for x in g[2:]:
        # compute the next highest route count from the sum of the
        # two subproblems that compose the current problem
        h.append( h[-1] + x )
    # replace the last list with current one
    g = h
    n += 1
# at the end g should be a list with only one value being the summation
# of all of the subproblems that compose it
print( g[0] )
