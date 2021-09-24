from typing import List

class Solution:
    """
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.



    Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    """
    def getExtremeInd(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo<hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid]>target or (left and target==nums[mid]):
                hi = mid
            else:
                lo = mid+1
        return lo

    def searchRange(self, nums, target):
        """
        Time complexity : O(log N)
        :param nums:
        :param target:
        :return:
        """
        # search for extrme left
        left_ind = self.getExtremeInd(nums, target, True)

        if left_ind == len(nums) or nums[left_ind]!=target:
            return [-1,-1]

        return [left_ind, self.getExtremeInd(nums, target, False)-1]

s = Solution()
sol = Solution()
inputs = [
    ([4,5,5,7,8,9],5),
    ([1],1)
]
for arr, ele in inputs:
    print(sol.searchRange(arr, ele))