# Increasing Decreasing String
#
# Given a string s. You should re-order the string using the following algorithm:
#
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and
# append it to the result.
#
# Return the result string after sorting s with this algorithm.
# Source - https://leetcode.com/problems/increasing-decreasing-string/

# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"

import collections

class Solution:
    def sortString(self, s):
        o = sorted([m, n] for m, n in collections.Counter(s).items())   # [['a', 4], ['b', 4], ['c', 4]]
        res = []
        while len(res) < len(s):
            for i in range(len(o)):
                if o[i][1]:
                    res.append(o[i][0])
                    o[i][1] -= 1
            for i in range(len(o)):
                if o[~i][1]:
                    res.append(o[~i][0])
                    o[~i][1] -= 1
        return ''.join(res)


input = "aaaabbbbcccc"
s = Solution().sortString(input)
print(s)