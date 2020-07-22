# Remove All Adjacent Duplicates In String

# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and
# removing them.
# We repeatedly make duplicate removals on S until we no longer can. Return the final string after all such duplicate
# removals have been made.  It is guaranteed the answer is unique.
#
# Input: "abbaca"
# Output: "ca"
#
# Source - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S):
        res = []
        for i in S:
            if res and res[-1] == i:
                res.pop()
            else:
                res.append(i)
        return "".join(res)


input = "abbaca"
s = Solution().removeDuplicates(input)
print(input)
print(s)
