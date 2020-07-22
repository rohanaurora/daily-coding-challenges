# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray
# scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.
#
# If a cell has less than 8 surrounding cells, then use as many as you can.
#
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]

from itertools import product

class Solution:
    def imageSmoother(self, M):
        m = len(M)
        n = len(M[0])
        A = [[0] * n for i in range(m)]
        for i, j in product(range(m), range(n)):
            s = []
            for I, J in product(range(max(0, i - 1), min(i + 2, m)), range(max(0, j - 1), min(j + 2, n))):
                s.append(M[I][J])
            A[i][j] = int(sum(s) / len(s))
        return A


x =[[1, 1, 1], [1, 0, 1],[1, 1, 1]]

s = Solution().imageSmoother(x)
print(s)