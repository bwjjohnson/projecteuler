#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with 
# British usage.

tc = 0
for n in range(1,1001):
    nc = 0
    ltd = n % 100
    if ltd == 10: nc = 3 # ten
    elif ltd == 11: nc = 6 # eleven
    elif ltd == 12: nc = 6 # twelve
    elif ltd == 13: nc = 8 # thirteen
    elif ltd == 14: nc = 8 # fourteen
    elif ltd == 15: nc = 7 # fifteen
    elif ltd == 16: nc = 7 # sixteen
    elif ltd == 17: nc = 9 # seventeen
    elif ltd == 18: nc = 8 # eighteen
    elif ltd == 19: nc = 8 # nineteen
    else:
        ones = n % 10
        if ones == 1: nc = 3 # one
        elif ones == 2: nc = 3 # two
        elif ones == 3: nc = 5 # three
        elif ones == 4: nc = 4 # four
        elif ones == 5: nc = 4 # five
        elif ones == 6: nc = 3 # six
        elif ones == 7: nc = 5 # seven
        elif ones == 8: nc = 5 # eight
        elif ones == 9: nc = 4 # nine
        tens = int((n-ones) % 100 / 10)
        if tens == 2: nc += 6 # twenty
        elif tens == 3: nc += 6 # thirty
        elif tens == 4: nc += 5 # forty
        elif tens == 5: nc += 5 # fifty
        elif tens == 6: nc += 5 # sixty
        elif tens == 7: nc += 7 # seventy
        elif tens == 8: nc += 6 # eighty
        elif tens == 9: nc += 6 # ninety
    hundreds = int((n-tens-ones) % 1000 / 100)
    if hundreds in range(1,10): 
        nc += 7 # hundred
        if ltd > 0: nc += 3 # and 
    if hundreds == 1: nc += 3 # one 
    elif hundreds == 2: nc += 3 # two
    elif hundreds == 3: nc += 5 # three
    elif hundreds == 4: nc += 4 # four
    elif hundreds == 5: nc += 4 # five
    elif hundreds == 6: nc += 3 # six
    elif hundreds == 7: nc += 5 # seven
    elif hundreds == 8: nc += 5 # eight
    elif hundreds == 9: nc += 4 # nine
    elif n == 1000: nc = 11 # one thousand
    tc += nc
print( tc )
