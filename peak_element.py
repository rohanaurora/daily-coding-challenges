# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Source - https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, num):
        l = 0
        r = len(num)-1
        while l < r:
            mid = (l+r)//2
            if num[mid] < num[mid+1]:
                l = mid+1
            elif num[mid] > num[mid+1]:
                r = mid
        return r


nums = [1,2,3,1]
print(f"Input: {nums}")
s = Solution().findPeakElement(nums)
print(s)