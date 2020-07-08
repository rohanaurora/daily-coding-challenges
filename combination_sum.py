# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.

# Input: candidates = [2,3,5], target = 8,
# Source - https://leetcode.com/problems/combination-sum/

class Solution:
        def combinationSum(self, nums, target):
            res = []
            nums.sort()

            def dfs(left, path, idx):
                if not left:
                    res.append(path[:])
                else:
                    for i, val in enumerate(nums[idx:]):
                        if val > left:
                            break
                        dfs(left - val, path + [val], idx + i)

            dfs(target, [], 0)
            return res

s = Solution().combinationSum([2,3,5], 8)
print(s)
