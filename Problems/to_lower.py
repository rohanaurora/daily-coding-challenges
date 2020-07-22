# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution:
    def toLowerCase(self, str):
        res = []
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                res += chr(ord(char) + 32)
                # res += (chr(ord(char) | (1 << 5)))
            else:
                res += char

        return "".join(res)

s = Solution().toLowerCase("HELwwLO")
print(s)
