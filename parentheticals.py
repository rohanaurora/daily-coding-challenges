# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
#
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
# finds the corresponding closing parenthesis.
#
# Example: if the example string above is input with the number 10 (position of the first parenthesis),
# the output should be 79 (position of the last parenthesis).
#
# Source - https://www.interviewcake.com/question/python3/matching-parens

class Solution:
    def parentheticals(self, s, num):
        res = 0

        for i in range(num + 1, len(s)):
            char = s[i]
            if char == '(':
                res += 1
            elif char == ')':
                if res == 0:
                    return i
                else:
                    res -= 1

input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print(input)
s = Solution().parentheticals(input, 7)
print(s)

# O(n) time complexity
# O(1) space complexity