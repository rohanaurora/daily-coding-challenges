# Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute,
# you will create a folder with the name names[i]. Since two files cannot have the same name, if you enter a folder
# name which is previously used, the system will have a suffix addition to its name in the form of (k), where, k is
# the smallest positive integer such that the obtained name remains unique. Return an array of strings of length n
# where ans[i] is the actual name the system will assign to the ith folder when you create it.
#
# Source - https://leetcode.com/problems/making-file-names-unique/
#
# Input: names = ["gta","gta(1)","gta","avalon"]
# Output: ["gta","gta(1)","gta(2)","avalon"]

import re
from collections import Counter
class Solution:
    def getFolderNames(self, names):
        res = {}
        ans = []
        for s in names:
            if s in res:
                i = res[s]
                while s + '(' + str(i) + ')' in res:
                    i += 1
                new = s + '(' + str(i) + ')'
                ans.append(new)
                res[new] = 1
                res[s] = i
            else:
                ans.append(s)
                res[s] = 1
        return ans


names = ["kaido","kaido(1)","kaido","kaido(1)"]
s = Solution().getFolderNames(names)
print(s)

