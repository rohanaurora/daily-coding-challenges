# Given an integer array arr. You have to sort the integers in the array in ascending
# order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1'
# s you have to sort them in ascending order.
#
# Return the sorted array.

from collections import Counter
# class Solution:
#     def sortByBits(self, arr):
#         res = sorted(arr, key=lambda x: (bin(x).count('1'), x))
#         return res

class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (self.hamming_weight(x), x))

    @staticmethod
    # bitwise AND rightmost bit & right shift to check the next bit
    def hamming_weight(num: int) -> int:
        weight = 0

        while num:
            weight += num & 1
            num = num >> 1
        return weight

s = Solution().sortByBits([0,1,2,3,4,5,6,7,8])
print(s)