from typing import List

class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        leng = len(nums)
        if leng<k:
            return False

        total = sum(nums)
        if total%k:
            return False

        new_sum = total/k

        used = [False] * leng

        return self.partition(k, used, new_sum, 0, 0, nums)


    def partition(self, k : int, used: List[bool], sub_sum: int, cur_sum : int, start: int, nums: List[int])->bool:

        if k==1:
            return True

        if cur_sum==sub_sum:
            return self.partition(k-1, used, sub_sum, 0, 0, nums)

        for i in range(start, len(nums)):
            if not used[i] and nums[i]+cur_sum<=sub_sum:
                used[i]=True
                if self.partition(k, used, sub_sum, nums[i]+cur_sum, i+1, nums):
                    return True

                used[i] = False

        return False



if __name__ == "__main__":
    sol = Solution()
    inputs = [
        ([4,3,2,3,5,2,1],4),
        ([1,2,3,4],3)
    ]
    for nums, k in inputs:
        print(sol.canPartitionKSubsets(nums=nums, k=k))
