# Number of Steps to Reduce a Number to Zero
# Given a non-negative integer num, return the number of steps to reduce it to zero.
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
#
# Source - https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num):
        steps = 0
        while num != 0: num = (num // 2) if (num % 2 == 0) else (num - 1); steps += 1
        return steps

s = Solution()
steps = s.numberOfSteps(14)
print(steps)