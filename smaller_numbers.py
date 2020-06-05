# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array
#
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        dct = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dct:
                dct[n] = i
        return [dct[n] for n in nums]


# class Solution:
#     def smallerNumbersThanCurrent(self, num):
#         output = []
#         for i in num:
#             c = 0
#             for j in num:
#                 if j < i:
#                     c = c + 1
#             output.append(c)
#         return output

s = Solution()
z = s.smallerNumbersThanCurrent([8,1,2,2,3])
print(z)
