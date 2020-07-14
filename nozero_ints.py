# Convert Integer to the Sum of Two No-Zero Integers
#
# Source - https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n):
        for a in range(n):
            if '0' not in f'{a}{n - a}':
                return [a, n - a]


s = Solution().getNoZeroIntegers(11)
print(s)
