from typing import List

"""
503. Next Greater Element II
Medium

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the
 array, which means you could search circularly to find its next greater number. If it doesn't exist, 
 return -1 for this number.

"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        O(N) both
        """
        result = [-1] * len(nums)

        stack = []

        for i in range(2*len(nums)):
            i = i % len(nums)
            while stack and nums[i]>nums[stack[-1]]:
                ind = stack.pop()
                result[ind] = nums[i]
            stack.append(i)
        return result


s = Solution()
inputs = [
    [1,2,3,4,3],
    [1,2,1]
]
for inp in inputs:
    print(s.nextGreaterElements(inp))