from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        res, ed, last_idx = 0, -1, defaultdict(lambda : -1)
        
        for i, it in enumerate(s):
            if last_idx[it] > ed: ed = last_idx[it]
            last_idx[it] = i
            res = max(res, i - ed)
        
        return res