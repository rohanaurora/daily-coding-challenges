# Longest Happy String
#
# A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
#
# Given three integers a, b and c, return any string s, which satisfies following conditions:
#
# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences
# of the letter 'c'.
#
# s will only contain 'a', 'b' and 'c' letters.
# If there is no such string s return the empty string "".
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
#
# Source - https://leetcode.com/problems/longest-happy-string/

from collections import Counter

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        remaining = Counter({'a': a, 'b': b, 'c': c, })  # freq dict of remaining characters

        # In each loop we update remaining and recompute
        (fence, _), (wedge, _) = remaining.most_common(2)  # initial group
        while remaining[fence] > 0 and remaining[wedge] > 0:  # loop till no new groups could be formed
            # add first fence
            result.append(fence)
            remaining[fence] -= 1

            # (Optional) add second fence, if it wouldn't form triplet with first fence and last wedge
            if len(result) >= 2 and result[-2] == fence:
                pass
            elif remaining[fence] > 0:  # add second fence if any remaining
                result.append(fence)
                remaining[fence] -= 1

            # add wedge
            result.append(wedge)
            remaining[wedge] -= 1

            # recompute the fence and wedge char for next group
            (fence, _), (wedge, _) = remaining.most_common(2)

        # has remaining characters not consumed by loop, can append two maximum fences
        if remaining[fence] > 0:
            result.append(fence)
            remaining[fence] -= 1
            if remaining[fence] > 0:
                result.append(fence)

        return ''.join(result)

s = Solution().longestDiverseString(1,1,7)
print(s)

# O(a+b+c) time and space complexity