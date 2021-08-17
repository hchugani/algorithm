from typing import List

class Solution:

    def canPartitionKSubsetsDP(self, nums: List[int], k: int) -> bool:
        """
        DP with bit masking
        Time complexity : O(N * 2^N)
        Space complexity : O(2^N)
        """
        N = len(nums)

        if N<k:
            return False

        total = sum(nums)

        if total%k:
            return False

        target = total // k

        # [4,3,2,3,5,2,1] with 7
        # 1 << N gives 128 differnt combinations
        # dp will hold module %k

        dp = [-1 for i in range(1<<N)]

        dp[0] = 0 # empty set is always 0

        for mask in range((1<<N)):
            if dp[mask]==-1: # for elements > target , ignore adding
                continue

            for i in range(N):
                # Check if the current element
                # can be added to the current
                # subset/mask
                if((mask & (1<<i) == 0) and # ith bit is not set to avoid repetition of same number
                               dp[mask]+nums[i]<=target ):
                    # Transistion
                    dp[mask | 1<<i] = (dp[mask]+nums[i])%target

        if dp[(1<<N)-1]==0:
            return True
        else:
            return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        time complexity: NP hard , exponential
        space complexity : O(n)
        :param nums:
        :param k:
        :return:
        """
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
        print(sol.canPartitionKSubsetsDP(nums=nums, k=k))
