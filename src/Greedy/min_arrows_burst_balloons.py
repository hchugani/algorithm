from typing import List

"""
452. Minimum Number of Arrows to Burst Balloons
Medium

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons 
are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose 
horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the 
balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along t
he x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There
 is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, 
 bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        O(NlogN) time
        """

        points = sorted(points,key=lambda x : x[0])

        x = y = 0
        count = 0


        for i in range(len(points)):
            if i==0:
                x,y = points[i]
                count+=1
                continue

            # find intersection points x, y
            if points[i][0]<=y:
                x = max(x, points[i][0])
                y = min(y, points[i][1])
            else:
                x,y = points[i]
                count+=1

        return count

s = Solution()

inputs = [
    [[10,16],[2,8],[1,6],[7,12]],
    [[1,2],[3,4],[5,6],[7,8]],
    [[1,2],[2,3],[3,4],[4,5]],
    [[1,8],[2,6],[7,12]]
]

for points in inputs:
    print(s.findMinArrowShots(points))