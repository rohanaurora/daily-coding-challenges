# Given an array of characters, compress it in-place. The length after compression must always be smaller than or
# equal to the original array. Every element of the array should be a character (not int) of length 1.
#
# After you are done modifying the input array in-place, return the new length of the array.
# Source - https://leetcode.com/problems/string-compression/

from collections import Counter
class Solution:
    def compress(self, chars) -> int:
        res = []
        x = Counter(chars)
        for i in x.keys():
            res.append(i)
            res.append(str(x.get(i)))
        if len(res) == 2:
            res.pop(-1)
        chars[:] = list(res)

s = Solution().compress(["a","a","b","b","c","c","c"])
print(s)
