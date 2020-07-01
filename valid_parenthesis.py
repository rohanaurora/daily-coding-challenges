class Solution:
    def checkValidString(self, s):
        res = []
        for i in s:
            if i == "(" or i == ")" or i == "*":
                res.append(i)
        x = res
        print(x)
        return True

s = Solution().checkValidString("(*)")
print(s)
