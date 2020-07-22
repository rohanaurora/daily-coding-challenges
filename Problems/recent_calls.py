# Number of Recent Calls
#
# Write a class RecentCounter to count recent requests.
#
# It has only one method: ping(int t), where t represents some time in milliseconds.
#
# Return the number of pings that have been made from 3000 milliseconds ago until now.
#
# Any ping with time in [t - 3000, t] will count, including the current ping.
#
# It is guaranteed that every call to ping uses a strictly larger value of t than before.
#
# inputs = ["RecentCounter","ping","ping","ping","ping"]
# inputs = [[],[1],[100],[3001],[3002]]
# Output: [null,1,2,3,3]
#
# Source - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        # Remove any pings that took place more than 3000 milliseconds ago.
        while t - self.queue[0] > 3000:
            self.queue.popleft()
        return len(self.queue)

