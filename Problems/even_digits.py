# Given an array nums of integers, return how many of them contain an even number of digits.
#
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.

class Solution:
    def findNumbers(self, nums):
        ctr = 0
        for e in nums:
            ctr += 1 if len(str(e)) % 2 == 0 else 0
        return ctr
        # return sum([1 for i in map(str, nums) if len(i) % 2 == 0])

s = Solution().findNumbers([12,345,2,6,7896])
print(s)
