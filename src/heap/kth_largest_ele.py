from typing import List
import heapq

class Solution:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.



    Example 1:

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    Example 2:

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time complexity : O(Nlogk), Space complexity: O(k)
        # intialize heapq with size of K min heap
        # and first add k elements
        # now after that, check if the element is greater than min_ele , then pop and push new
        # element
        heap = []
        i = 0
        while i<k:
            heapq.heappush(heap, nums[i])
            i+=1

        while i < len(nums):
            if nums[i]>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
            i+=1

        return heap[0]


s = Solution()
inputs = [
    ([3,2,1,5,6,4], 2),
    ([3,2,3,1,2,4,5,5,6],4)
]

for arr, k in inputs:
    print(s.findKthLargest(arr,k))