# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  '
# 'Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so
# "a" is considered a different type of stone from "A".

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
# Input: J = "z", S = "ZZ"
# Output: 0

class Solution:
    def numJewelsInStones(self, J, S):
        j = set(J)
        count = 0
        for i in S:
            count += 1 if i in j else 0
        return count

        # Solution 2
        # res = map(S.count, J)
        # return sum(res)

        # Solution 3
        # return sum(s in J for s in S)

s = Solution().numJewelsInStones("aA", "aAAbbbb")
print(s)
