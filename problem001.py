#!/usr/bin/python
#
# Project Euler (projecteuler.net) - Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

max = 1000
sum = 0
threes = 3
fives = 5
while ( threes < max ):
    print threes
    sum += threes
    print "sum = ", sum
    threes += 3
while ( fives < max ):
    print fives
    if ( fives % 3 != 0 ):
        sum += fives
        print "sum = ", sum
    fives += 5
print sum

