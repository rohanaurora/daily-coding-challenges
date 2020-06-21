# Given an integer n and an integer start.
#
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
#
# Return the bitwise XOR of all elements of nums.
# https://leetcode.com/contest/weekly-contest-194/problems/xor-operation-in-an-array/

from functools import reduce

class Solution:
    def xorOperation(self, n, start):
        i = 0
        nums = [0] * n
        for i in range(len(nums)):
            nums[i] = start + 2 * i
        res = reduce(lambda x, y: x ^ y, nums)
        return res


s = Solution().xorOperation(10, 5)
print(s)
