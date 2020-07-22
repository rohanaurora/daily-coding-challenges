# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
#
# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value,
# that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
#
# Source - https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums):
        m1, m2 = 0, 0
        for n in nums:
            if n > m1:
                m2 = m1
                m1 = n
            else:
                m2 = max(n, m2)
        return (m1 - 1) * (m2 - 1)

# Alternative Solution
#
# class Solution:
#     def maxProduct(self, nums):
#         nums.sort()
#         return (nums[-1]-1) * (nums[-2]-1)

s = Solution().maxProduct([1, 5, 4, 5])
print(s)

# Time: O(n)
# Space: O(1)