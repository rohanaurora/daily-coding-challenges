# Squares of a Sorted Array
#
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also
# in sorted non-decreasing order.
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, A):
        for i, j in enumerate(A):
            A[i] = j * j
        return sorted(A, reverse=False)

        # return sorted(i * i for i in A)

s = Solution().sortedSquares([-7,-3,2,3,11])
print(s)

