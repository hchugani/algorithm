from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        O(N) : Time
        O(1): Space
        Do not return anything, modify nums in-place instead.
        """

        def reverse(a,lo, hi):
            while lo<hi:
                a[lo], a[hi] = a[hi], a[lo]
                lo+=1
                hi-=1

        N = len(nums)
        i = N-1
        x=-1
        while i>0:
            if nums[i-1]<nums[i]:
                x = i-1
                break
            i-=1

        if x == -1:
            reverse(nums, 0, N-1)
            return

        j = N-1
        while nums[j]<=nums[x]:
            j-=1

        # swap
        nums[x], nums[j] = nums[j], nums[x]

        reverse(nums, x+1, N-1)

s = Solution()
nums = [9,5,7,2,4,3,0]
s.nextPermutation(nums)
print(nums)
