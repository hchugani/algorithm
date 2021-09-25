from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i,num in enumerate(nums):
            if target-num in sum_dict:
                return [sum_dict[target-num], i]
            sum_dict[num] = i


