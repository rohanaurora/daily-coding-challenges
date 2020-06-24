# Most Common Word
#
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not
# case sensitive.  The answer is in lowercase.
#
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"

from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        str = " ".join(re.split('\W+', paragraph.lower()))
        str_list = str.split(" ")
        x = Counter(str_list)
        for word in banned:
            if word.lower() in x:
                del x[word]
        v, k = max((v, k) for k, v in x.items())
        return k


input = "Bob hit a ball, the hit BALL flew far after it was hit."
s = Solution().mostCommonWord(input,"hit")
print(s)
