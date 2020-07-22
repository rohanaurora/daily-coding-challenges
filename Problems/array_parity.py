# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all
# the odd elements of A. You may return any answer array that satisfies this condition.

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
    def sortArrayByParity(self, A):
        e = 0
        for i in range(len(A)):
            if A[i] & 1 == 0:
                A[i], A[e] = A[e], A[i]
                e += 1
        return A


input = [3,1,2,4]
s = Solution().sortArrayByParity(input)
print(s)

# Time complexity: O(n)
# Space complexity: O(1)