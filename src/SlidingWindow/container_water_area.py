"""
11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two
lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        O(N) Time
        O(1) space
        """

        # Brute force O(N*N), find area between all possible combinations
        # area = min(a[r],a[l])*(r-l)
        a = height
        l = 0
        r = len(height)-1
        max_area = 0

        while l < r :
            area = min(a[r],a[l])*(r-l)
            max_area = max(max_area, area)
            if a[l]<=a[r]:
                l+=1
            else:
                r-=1
        return max_area

s = Solution()

heights = [
    [1,8,6,2,5,4,8,3,7],
    [1,1],
    [4,3,2,1,4]
]

for height in heights:
    print(s.maxArea(height))

