# Analyze User Website Visit Pattern
#
# We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].
# A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
# (The websites in a 3-sequence are not necessarily distinct.) Find the 3-sequence visited by the largest number of
# users. If there is more than one solution, return the lexicographically smallest such 3-sequence.
#
# Source - https://leetcode.com/problems/analyze-user-website-visit-pattern/
#
# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
#                   timestamp = [1,2,3,4,5,6,7,8,9,10],
#                    website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation:
# The tuples in this example are:
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
# The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
# The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
# The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
# The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.


from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username, timestamp, website):

        z = zip(timestamp, username, website)  #=> [(3, 'joe', 'career'),....]
        sorted_z = sorted(z)

        mapping = defaultdict(list)
        for t, u, w in sorted_z:  #=> {joe: [home, about, career]}
            mapping[u].append(w)

        # use a dict for counting
        counter_dict = defaultdict(int)

        for website_list in mapping.values():
            combs = set(combinations(website_list, 3))  #=> size of combination is set to 3
            for comb in combs:
                counter_dict[comb] += 1  #=> Tuple as key, counter as value,  e.g. ('home', 'about', 'career') : 2

        # sort descending by value, then lexicographically
        sorted_counter_dict = sorted(counter_dict, key=lambda x: (-counter_dict[x], x))
        return sorted_counter_dict[0]


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

s = Solution().mostVisitedPattern(username, timestamp, website)
print(s)
