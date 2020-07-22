# Find N Unique Integers Sum up to Zero
#
# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

import random


class Solution:
    def sumZero(self, n):
        res = []

        if n % 2 != 0:
            res.append(0)

        digits = n // 2
        for i in range(1, digits + 1):
            res.append(i)
            res.append(-1 * i)

        return res


s = Solution().sumZero(5)
print(s)
print(sum(s))
