# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero. Given a lower and upper number bound,
# output a list of every possible self dividing number, including the bounds if possible.
# Source - https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left, right + 1):
            n = set(str(i))
            if '0' in n:
                continue
            s = True
            for div in n:
                if i % int(div) != 0:
                    s = False
                    break
            if s == True:
                res.append(i)

        return res


# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
s = Solution().selfDividingNumbers(1, 22)
print(s)