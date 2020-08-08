class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sam = []

        for i in range(len(mat)):
            sam.append((sum(mat[i]), i))
        sam.sort()
        res = []
        for i in range(k):
            res.append(sam[i][1])
        return res