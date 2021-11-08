"""
539. Minimum Time Difference
Medium

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference
 between any two time-points in the list.


Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

"""
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        O(nlogn) - time
        O(n) - space
        """

        def getMin(s)->int:
            h,m = s.split(":")
            return int(h)*60+int(m)

        arr = sorted(map(getMin,timePoints))

        mini = float("inf")
        for i in range(1, len(arr)):
            mini = min(mini, arr[i]-arr[i-1])

        mini = min(mini, 24*60 - (arr[-1]-arr[0]))

        return mini


s = Solution()
times = [
    ["23:59","00:00"],
    ["23:59","00:00", "00:02"]
]

for time in times:
    print(s.findMinDifference(time))