# Write a function that, given:
#
# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.
#
# Example: for amount=4 (4¢) and denominations=[1,2,3](1¢, 2¢ and 3¢), your program would output 4—the number of
# ways to make 4¢ with those denominations:
#
# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢
# Source: https://www.interviewcake.com/question/python3/coin

# TODO
def get_permutation(amount, denominations):

    for coin in denominations:

        for higher_amount in range(coin, amount + 1):
            r = higher_amount - coin
            print(f"For {r}")

    return 0


output = get_permutation(4, [1, 2, 3])
print(output)
