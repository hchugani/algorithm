"""
2009. Minimum Number of Operations to Make Array Continuous
Hard

You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.



Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.
Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.
"""

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        O(NlogN) - sort
        https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/discuss/1483624/Sorting-%2B-Dedup-%2B-Binary-Search-with-Java
        """
        def binarySearch(arr, num):
            left, right = 0, len(arr)-1

            while left<=right:
                mid = left + (right-left)//2
                if arr[mid]==num:
                    return mid+1
                elif arr[mid]<num:
                    left = mid+1
                else:
                    right = mid-1
            return left


        n = len(nums)
        nums = sorted(list(set(nums)))

        ans = float("inf")
        for i, start in enumerate(nums):
            search_end = start+n-1

            # find unique elements within range [start, end]
            idx = binarySearch(nums, search_end)
            #unique elments for range [start, end]
            unique_ele = idx-i
            #possible changes
            changes = n-unique_ele
            ans = min(ans,changes)

        return ans

s = Solution()
print(s.minOperations([1,2,3,4,6]))
print(s.minOperations([4,2,5,3]))




