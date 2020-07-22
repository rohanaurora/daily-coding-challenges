# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
#
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# S consists of lowercase English letters only.
# 1 <= S.length <= 1000
# Source: https://leetcode.com/problems/remove-vowels-from-a-string

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if 1 <= len(S) <= 1000:
            return ''.join([v for v in S if v not in vowels])
        else:
            print("String not in bounds.")
            return


S = "leetcodeisacommunityforcoders"
z = Solution.removeVowels(S, S)
print(z)
