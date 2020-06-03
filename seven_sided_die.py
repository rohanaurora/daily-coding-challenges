# Seven-sided dice from five-sided dice
#
# Given an equal-probability generator of one of the integers 1 to 5 as dice5, create dice7 that generates a
# pseudo-random integer from 1 to 7 in equal probability using only dice5 as a source of random numbers,
# and check the distribution for at least one million calls using the function created in
# Simple Random Distribution Checker.
#
#
# Implementation suggestion: dice7 might call dice5 twice, re-call if four of the 25 combinations are given,
# otherwise split the other 21 combinations into 7 groups of three, and return the group index from the rolls.

from random import randint

def dice5():
    return randint(1, 5)

def dice7():
    r = dice5() + dice5() * 5 - 6
    if r < 21:
        return (r % 7) + 1
    else:
        return dice7()

s = dice7()
print(s)