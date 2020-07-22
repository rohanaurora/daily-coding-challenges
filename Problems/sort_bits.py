# Given an integer array arr. You have to sort the integers in the array in ascending
# order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1'
# s you have to sort them in ascending order.
#
# Return the sorted array.

# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]

# class Solution:
#     def sortByBits(self, arr):
#         res = sorted(arr, key=lambda x: (bin(x).count('1'), x))
#         return res

class Solution:
    def sortByBits(self, arr):
        res = sorted(arr, key=lambda x: (self.hamming_weight(x), x))
        return res

    @staticmethod
    def hamming_weight(n: int) -> int:
        c = 0
        while n:
            c += 1      # c += n & 1
            n &= n - 1  # n >>= 1
            print(n)
        return c


s = Solution().sortByBits([0,1,2,3,4,5,6,7,8])
print(s)