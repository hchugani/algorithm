"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
 6 units of rain water (blue section) are being trapped.
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        O(N): time
        O(1) : space
        """
        ans = 0
        left, right = 0 , len(height)-1
        left_max, right_max = 0, 0

        while left < right:
            if height[left]<height[right]:
                if height[left]>left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left+=1
            else:
                if height[right]>right_max:
                    right_max = height[right]
                else:
                    ans+= right_max - height[right]
                right-=1

        return ans

s = Solution()
inputs = [
    [0,1,0,2,1,0,1,3,2,1,2,1]
]

for arr in inputs:
    print(s.trap(arr))