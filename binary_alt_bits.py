# Given a positive integer, check whether it has alternating bits: namely,
# if two adjacent bits will always have different values.

# https://leetcode.com/problems/binary-number-with-alternating-bits/

# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101

import re
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = str(bin(n)[2:])
        return '00' not in x and '11' not in x

        # return all(int(b[i]) + int(b[i + 1]) == 1 for i in range(len(b) - 1))


s = Solution().hasAlternatingBits(4)
print(s)

# More solutions = https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/657141/3-ways-From-naive-to-more-fine-tuned-solutions