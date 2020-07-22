# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the
# ith kid has.
#
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the
# greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
#
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
#
# 2 <= candies.length <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50
#
# Source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        highest = max(candies)
        output_list = []
        for i in candies:
            total = i + extraCandies
            if total >= highest:
                output_list.append(True)
            else:
                output_list.append(False)
        return output_list


s = Solution()
candies = [4, 2, 1, 1, 2]
output = s.kidsWithCandies(candies, 1)
print(f"{candies}\n{output}")
