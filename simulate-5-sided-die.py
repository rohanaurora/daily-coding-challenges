# You have a function rand7() that generates a random integer from 1 to 7.
# Use it to write a function rand5() that generates a random integer from 1 to 5.

import random


def rand7():
    r = random.randint(1, 7)
    return r


def rand5():
    max_number = 5
    result = max_number + 1
    while result >= 5:
        result = rand7()
        print(f"Randomized number is {result}")
    return result


z = rand5()
print(z)

# Complexity - Worst-case O(∞) time (keep re-rolling forever) and O(1) space.
