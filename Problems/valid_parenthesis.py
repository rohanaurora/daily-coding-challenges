# Valid Parenthesis String

# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this
# string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
#
# Source - https://leetcode.com/problems/valid-parenthesis-string/solution/

class Solution:
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
            else:
                lo -= 1

            if c != ')':
                hi += 1
            else:
                hi -= 1

            if hi < 0:
                break

            lo = max(lo, 0)
        return lo == 0


s = Solution().checkValidString("(*")
print(s)

# Greedy Approach
# Time Complexity: O(N), where N is the length of the string.
#
# Space Complexity: O(1), the space used by our lo and hi pointers.