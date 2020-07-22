# Split a String in Balanced Strings
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s split it in the maximum amount of balanced strings.
#
# Return the maximum amount of splitted balanced strings.
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
#

class Solution:
    def balancedStringSplit(self, s):
        res = c = 0
        for i in s:
            print(i)
            if i == "L":
                c += 1
            else:
                c += -1
            if c == 0:
                res += 1
        return res

# from itertools import accumulate
#
# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         return list(accumulate(1 if c == "R" else -1 for c in s)).count(0)

s = Solution().balancedStringSplit("LLLRLRRR")
print(s)