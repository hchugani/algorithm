from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity : O(P(N,k))
        Space complexity :  O(N)
        """
        result = []
        N = len(nums)
        counter ={}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] +=1

        def findPermute(comb=[]):
            if len(comb)==N:
                result.append(list(comb))
                return

            for i in counter.keys():
                if counter[i]>0:
                    counter[i]-=1
                    comb.append(i)
                    findPermute(comb)
                    comb.pop()
                    counter[i]+=1


        findPermute()
        return result


if __name__ == "__main__":
    sol = Solution()
    inputs = [
        [1, 1, 2],
        [1, 2, 3]
    ]
    for input in inputs:
        print(sol.permuteUnique(input))