from typing import List

class Solution:
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input

    """


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time complexity :
            Let NN be the number of candidates, TT be the target value, and MM be the minimal value among the candidates.

Time Complexity: \mathcal{O}(N^{\frac{T}{M}+1})O(N
M
T
​
 +1
 )

 Space complexity : O(T/M)
        """
        result = []

        def findCombo(start, new_target, combo):
            if new_target==0:
                result.append(list(combo)) # makes deep copy
                return
            elif new_target<0:
                return

            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                findCombo(i, new_target-candidates[i], combo)
                #findCombo(i+1, new_target-candidates[i], combo)
                combo.pop()

        findCombo(0, target, combo=[])

        return result


if __name__ == "__main__":
    sol = Solution()
    inputs = [
        ([2,3,6,7],  7),
        ([2],1)
    ]
    for k, n in inputs:
        print(sol.combinationSum(k, n))