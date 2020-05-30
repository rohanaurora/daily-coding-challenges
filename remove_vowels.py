# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
#
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# S consists of lowercase English letters only.
# 1 <= S.length <= 1000
# Source: https://leetcode.com/problems/remove-vowels-from-a-string

class Solution:
    def removeVowels(self, S: str) -> str:
        s_list = list(S)
        if 1 <= len(s_list) <= 1000:
            for c in s_list:
                if c == 'a' or c == 'e' or c == "i" or c == 'o' or c == 'u':
                    s_list.remove(c)
                output = "".join(s_list)
                return output
        else:
            print("String not in bounds.")



S = "leetcodeisacommunityforcoders"
z = Solution.removeVowels(S, S)
print(z)