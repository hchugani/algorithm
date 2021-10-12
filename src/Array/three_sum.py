from typing import List
"""
The result should not contain duplicates
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        O(n2) time complexity
        O(n or logn) depending on the sorting algorithm 
        :param nums:
        :return:
        """
        result = []
        nums.sort() # O(nlogn)
        N = len(nums)

        for i in range(N):
            if nums[i]>0:
                break

            if i==0 or nums[i]!=nums[i-1]:
                l = i+1
                r = N-1
                while(l<r):
                    cur_sum = nums[i] + nums[l]+nums[r]
                    if cur_sum ==0:
                        result.append([nums[i], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif cur_sum<0:
                        l+=1
                    else:
                        r-=1
        return result


s = Solution()
print(s.threeSum( [-1,0,1,2,-1,-4]))