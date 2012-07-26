#!/usr/bin/python
#
# Project Euler (projecteuler.net) - Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

n = 2000000
a = 3
primes = [2]
while primes[-1] <= n:
  c = 0
  while 1 :
    d = primes[c]
    (q, r) = (a // d, a % d)
    if (r):
      if d <= q: c += 1
      else: primes.append(a); break
    else:break
  a += 1
print reduce(lambda x,y: x + y, primes[:-1] )
