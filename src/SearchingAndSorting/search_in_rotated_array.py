from typing import List

class Solution:
    """
    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is rotated at an unknown pivot index k
    (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
     nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7]
    might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
    Given the array nums after the rotation and an integer target, return the index of target
    if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    """
    def search2(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            pivot = l + (r-l)//2
            if nums[pivot]==target:
                return pivot
            elif nums[pivot]>=nums[l]:
                if target>=nums[l] and target <nums[pivot]:
                    r = pivot-1
                else:
                    l = pivot+1
            else:
                if target >nums[pivot] and target<=nums[r]:
                    l = pivot+1
                else:
                    r = pivot-1

    def search(self, nums: List[int], target: int) -> int:
        """
        Time complexity : 2* O(log N)
        Space complexity : O(1)
        :param nums:
        :param target:
        :return:
        """
        low_ind = self.findLowestIndex(nums, 0, len(nums)-1)
        if low_ind ==0:
            return self.binarySearch(nums, 0, len(nums), target)
        if target == nums[low_ind]:
            return low_ind
        elif target >= nums[0]:
            return self.binarySearch(nums, 0, low_ind, target)
        else:
            return self.binarySearch(nums,low_ind, len(nums), target)

    def binarySearch(self, nums, l, r, target)->int:

        while l<=r:
            pivot = l + (r-l)//2
            if nums[pivot] == target:
                return pivot
            elif target>nums[pivot]:
                l = pivot+1
            else:
                r = pivot-1
        return -1


    def findLowestIndex(self, nums, l, r):
        if nums[l]<nums[r]:
            return l
        while l <=r:
            pivot = int(int(l+r)/2)
            if nums[pivot]>nums[pivot+1]:
                return pivot+1
            else:
                if nums[pivot]<nums[l]:
                    r = pivot-1
                else:
                    l = pivot+1
        return l

s = Solution()
sol = Solution()
inputs = [
    ([8,9,2,3,4],9),
    ([4,5,6,7,0,1,2],0)
]
for arr, ele in inputs:
    print(sol.search2(arr, ele))




