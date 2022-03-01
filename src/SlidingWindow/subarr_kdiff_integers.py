"""
992. Subarrays with K Different Integers
Hard

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2],
 [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""
from typing import List


class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/1694376/Python-Sliding-Window

        O(N): time
        O(1): space
        """
        def atmost(nums, k):
            l = 0
            r = 0
            N = len(nums)
            counter = dict()
            ans = 0

            while r<N:
                counter[nums[r]] = counter.get(nums[r],0)+1

                while len(counter)>k:
                    counter[nums[l]]-=1
                    if counter[nums[l]]==0:
                        del counter[nums[l]]
                    l+=1

                ans+= r-l+1
                r+=1
            return ans

        return atmost(nums, k)-atmost(nums, k-1)

s = Solution()
print(s.subarraysWithKDistinct([1,2,1,2,3],2))