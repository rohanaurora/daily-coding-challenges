# Count and Say
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
# You can do so recursively, in other words from the previous member read off the digits, counting the number of
# digits in groups of the same digit.
#
# Note: Each term of the sequence of integers will be represented as a string.

class Solution:
    def countAndSay(self, n: int) -> str:
        output = '1'

        for i in range(2, n + 1):
            res = ''
            cur = output[0]
            count = 1
            for x in output[1:]:
                if x == cur:
                    count += 1
                else:
                    res += str(count) + cur
                    count = 1
                    cur = x

            res += str(count) + cur
            output = ''.join(res)

        return output

s = Solution().countAndSay(3)
print(s)
