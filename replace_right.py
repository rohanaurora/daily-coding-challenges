# Replace Elements with Greatest Element on Right Side
#
# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1. After doing so, return the array.
#
# Source - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]


class Solution:
    def replaceElements(self, arr):
        maximum = -1
        res = [arr[-1]]
        i = len(arr) - 1

        while i > 0:
            if arr[i] > maximum:
                maximum = arr[i]

            res.append(maximum)
            i -= 1
        res.reverse()
        res[-1] = -1
        return res

        # res = -1
        # for i in range(len(arr) - 1, -1, -1):
        #     last = res
        #     res = max(res, arr[i])
        #     arr[i] = last
        # return arr

arr = [17,18,5,4,6,1]
s = Solution().replaceElements(arr)
print(s)