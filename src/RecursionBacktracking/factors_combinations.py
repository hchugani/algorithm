from typing import List


class Solution:
    """
    Numbers can be regarded as the product of their factors.

    For example, 8 = 2 x 2 x 2 = 2 x 4.
    Given an integer n, return all possible combinations of its factors. You may return the
    answer in any order.

    Note that the factors should be in the range [2, n - 1].



    Example 1:

    Input: n = 1
    Output: []
    Example 2:

    Input: n = 12
    Output: [[2,6],[3,4],[2,2,3]]

    """

    def getFactors(self, n: int) -> List[List[int]]:
        """

        Time Complexity : O(NlogN)
        Space complexity : O(T/2)
        :param n:
        :return:
        """
        result = []

        def findFactor(target, comb=[], start=2):
            if target==1:
                if len(comb)>1:
                    result.append(list(comb))
                return

            for i in range(start, target):
                if target%i==0:
                    comb.append(i)
                    findFactor(target//i, comb, start=i)
                    comb.pop()

        findFactor(n)
        return result
#         nums = [num for num in range(2, (n//2 +1)) if n%num == 0]
#         result = []
#         combinations = []

#         def backTrack(index, currProduct):

#             if currProduct == n:
#                 if combinations:
#                     result.append(combinations[:])
#                 return

#             if currProduct > n:
#                 return

if __name__ == "__main__":
    sol = Solution()
    inputs = [
        32, 12, 1
    ]
    for input in inputs:
        print(sol.getFactors(input))

#             for i in range(index, len(nums)):

#                 combinations.append(nums[i])
#                 backTrack(i, currProduct*nums[i])
#                 combinations.pop()

#         backTrack(0, 1)
#         return result

