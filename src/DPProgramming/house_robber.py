from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        O(N) Both 
        :param nums:
        :return:
        """

        @lru_cache(maxsize=None)
        def getMax(i=0):
            if i>=len(nums):
                return 0
            return max([nums[i] + getMax(i+2) for i in range(i, len(nums))])

        return getMax(0)

s = Solution()
inputs = [
    [1,2,3,1],
    [2,7,9,3,1],
    [1]
]

for nums in inputs:
    print(s.rob(nums))