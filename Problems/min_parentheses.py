# Minimum Remove to Make Valid Parentheses
#
# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
# parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s):
        open_par = []
        s = list(s)

        for i, char in enumerate(s):
            if char == '(':
                open_par.append(i)
            elif char == ')':
                if open_par:
                    open_par.pop()
                else:
                    s[i] = ""

        while open_par:
            s[open_par.pop()] = ""

        return "".join(s)

i = "(a(b(c)d)"
s = Solution().minRemoveToMakeValid(i)
print(s)

# Using a Stack and String Builder

# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         index = set()
#         stack = []
#         res = []
#         for i, j in enumerate(s):
#             if j not in "()":
#                 continue
#             if j == "(":
#                 stack.append(i)
#             elif not stack:
#                 index.add(i)
#             else:
#                 stack.pop()
#         index = index.union(set(stack))
#
#         for x, y in enumerate(s):
#             if x not in index:
#                 res.append(y)
#         return "".join(res)