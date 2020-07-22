# Create Target Array in the Given Order
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
#
# It is guaranteed that the insertion operations will be valid.

# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
#
# Source - https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums, index):
        output = []
        for x, y in enumerate(nums):
            output.insert(index[x], y)
        return output

# Alternative solution using zip()
# class Solution:
#     def createTargetArray(self, nums, index):
#         output = []
#         for i, j in zip(nums, index):
#             output.insert(j, i)
#         return output

s = Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1])
print(s)
