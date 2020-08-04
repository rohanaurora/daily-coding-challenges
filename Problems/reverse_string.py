# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
# extra memory. You may assume all the characters consist of printable ascii characters.

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Source - https://leetcode.com/articles/reverse-string/

# Recursion
# Space complexity : O(N) to keep the recursion stack.
# Time complexity : O(N) time to perform N/2 swaps.

class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        print(s)


input = ["h", "e", "l", "l", "o"]
s = Solution().reverseString(input)


# 2 pointers solution, swap from left and right. left = right for middle
# class Solution:
#     def reverseString(self, s):
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left, right = left + 1, right - 1

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         for i in range(len(s)//2):s[i],s[-i-1]=s[-i-1],s[i]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1