from  typing import List

"""
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all 
the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(N) Time
        O(1) space
        """
        N = len(nums)
        left = [1] * N
        right = [1] * N

        result = [1] * N

        #         for i in range(1, N):
        #             left[i] = left[i-1]*nums[i-1]

        #         for i in range(N-2, -1, -1):
        #             right[i]=right [i+1]*nums[i+1]

        #         return[i*j  for i, j in zip(left, right)]

        for i in range(1, N):
            result[i] = result[i-1] * nums[i-1]

        R = 1
        for i in range(N-1, -1, -1):
            result[i] = result[i]*R
            R *=nums[i]


        return result

s  = Solution()
inputs = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]

for inp in inputs:
    print(s.productExceptSelf(inp))