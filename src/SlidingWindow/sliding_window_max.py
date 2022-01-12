from typing import List
"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left 
of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves
 right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        O(N): Time
        O(K): Space
        """
        result = []

        # queue will hold maximum elemnt
        deq = collections.deque([])

        def clean_deq(i):

            if deq and deq[0] == i-k:
                deq.popleft()

            while deq and nums[i]>nums[deq[-1]]:
                deq.pop()

        max_idx = 0
        for i in range(k):
            clean_deq(i)
            deq.append(i)
            if nums[i]>nums[max_idx]:
                max_idx = i

        result.append(nums[max_idx])

        j = k

        while j < len(nums):
            clean_deq(j)
            deq.append(j)
            result.append(nums[deq[0]])
            j+=1

        return result

s = Solution()
inputs  = [
    ([1,3,-1,-3,5,3,6,7] , 3)
]

for nums, k in inputs:
    print(s.maxSlidingWindow(nums,k))