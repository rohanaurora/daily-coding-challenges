# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all
# strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4
# times, you need to include that character three times in the final answer. You may return the answer in any order.

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]

class Solution:
    def commonChars(self, A):
        main = list(A[0])
        A = list(map(list, A))
        res = []
        for c in main:
            for i in range(1, len(A)):
                s = A[i]
                if c not in s:
                    break
                else:
                    s.remove(c)
            else:
               res.append(c)
        return res


s = Solution().commonChars(["bella","label","roller"])
print(s)

