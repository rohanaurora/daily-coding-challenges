# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more
# than 25% of the time.
#
# Return that integer.
#
# Source - https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

class Solution:
    def findSpecialInteger(self, arr) -> int:
        res = len(arr) // 4
        count = 1
        prev = arr[0]
        for i in arr[1:]:
            if i == prev:
                count += 1
                if count > res:
                    return i
            else:
                count = 1
                prev = i
        return prev

arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
s = Solution().findSpecialInteger(arr)
print(s)