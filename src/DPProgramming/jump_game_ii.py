"""
45. Jump Game II
Medium


Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps
 to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

from typing import List
from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        O(N) both
        :param nums:
        :return:
        """

        @lru_cache(maxsize=None)
        def jump(ind):
            if ind == len(nums)-1:
                return 0

            if ind>=len(nums):
                return len(nums)

            val = nums[ind]
            if val==0:
                return len(nums)

            return min([1+jump(ind+i) for i in range(1, val+1)])

        return jump(0)

s = Solution()
num_inputs = [
    [2,3,1,1,4],
    [2,3,6,1,4,7,9],
    [2,3,0,1,4]
]

for nums in num_inputs:
    print(s.jump(nums))