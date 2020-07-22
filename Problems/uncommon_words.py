# Uncommon Words from Two Sentences
#
# We are given two sentences A and B.  (A sentence is a string of space separated words. Each word consists only of
# lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Return a list of all uncommon words.
#
# You may return the list in any order.
#
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
#
# Source - https://leetcode.com/problems/uncommon-words-from-two-sentences/

import collections

# class Solution:
#     def uncommonFromSentences(self, A: str, B: str):
#         c = collections.Counter((A + " " + B).split())
#         return [i for i in c if c[i] == 1]


class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        la = A.split()
        lb = B.split()
        freq = {}
        output = []
        for word in la:
            freq[word] = freq.get(word, 0) + 1

        for word in lb:
            freq[word] = freq.get(word, 0) + 1

        return [k for k in freq if freq[k] == 1]

A = "apple apple"
B = "orange"
s = Solution().uncommonFromSentences(A, B)
print(s)