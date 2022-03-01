"""
1353. Maximum Number of Events That Can Be Attended
Medium


You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and
ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.



Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
"""
from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        O(NlogN): Time
        O(N): Space
        :param events:
        :return:
        """

        events.sort(key=lambda x : x[0])
        max_days = max(j for i, j in events)
        active = []

        i = 0
        ans = 0
        for cur_day in range(1, max_days+1):
            while i < len(events) and events[i][0]==cur_day:
                heapq.heappush(active, events[i][1])
                i+=1

            while active and active[0]<cur_day:
                heapq.heappop(active)

            if active:
                heapq.heappop(active)
                ans+=1
        return ans

s = Solution()
print(s.maxEvents([[1,2],[2,3],[3,4],[1,2]]))