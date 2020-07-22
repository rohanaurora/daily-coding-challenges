# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#

class Solution:
    def runningSum(self, nums):
        x = 0
        res = []
        for i in nums:
            x += i
            res.append(x)
        return res

nums = [3,1,2,10,1]
s = Solution().runningSum(nums)
print(s)
