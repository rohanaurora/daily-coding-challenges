# High Five
# Given a list of scores of different students, return the average score of each student's top five scores
# in the order of each student's id.
#
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.
# The average score is calculated using integer division.

# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation:
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
#
# Source - https://leetcode.com/problems/high-five/

class Solution:
    def highFive(self, items):
        d = {}
        for i in items:
            try:
                d[i[0]].append(i[1])
            except:
                d[i[0]] = [i[1]]
        for i in d:
            d[i].sort()
            d[i] = d[i][::-1][:5]
        return [[i, sum(d[i]) // len(d[i])] for i in d]

x = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
s = Solution().highFive(x)
print(s)