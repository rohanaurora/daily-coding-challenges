# Detect Capital
# Source - https://leetcode.com/problems/detect-capital/

# 1. All letters in this word are capitals, like "USA".
# 2. All letters in this word are not capitals, like "leetcode".
# 3. Only the first letter in this word is capital, like "Google".
#

class Solution:
    def detectCapitalUse(self, word):
        if word == word.upper() or word == word.lower():
            return True
        elif (word == word.capitalize()):
            return True
        else:
            return False

    # return True if word.isupper() or word.islower() or word.istitle() else False


s = Solution().detectCapitalUse("FlaG")
print(s)