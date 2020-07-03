# Generate a String With Characters That Have Odd Counts
#
# Input: n = 4
# Output: "pppz"
# Source - https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

# class Solution:
#     def generateTheString(self, n: int):
#         if n % 2 != 0:
#             return 'a' * n
#         else:
#             return "a" * (n - 1) + 'b'

class Solution:
    def generateTheString(self, n: int):
        return 'a' + 'ba'[n & 1] * (n - 1)


s = Solution().generateTheString(40)
print(s)
