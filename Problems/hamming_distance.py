# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Input: x = 1, y = 4
# Output: 2
# Source - https://leetcode.com/problems/hamming-distance/


# Brian Kernighan's Algorithm
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        n = x ^ y
        while n:
            res += 1
            n &= n - 1
        return res

s = Solution().hammingDistance(1, 4)
print(s)
