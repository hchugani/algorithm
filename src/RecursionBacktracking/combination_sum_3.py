from typing import List

class Solution:
    """
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Time complexity: O(9Pk . k)
        Space complexity : O(K) to backtrack
        Time Complexity: \mathcal{O}(\frac{9! \cdot K}{(9-K)!})O(
(9−K)!
9!⋅K
​
 )
        """
        result = []
        def combineSum(start, remain, combo):

            if remain==0 and len(combo) ==k:
                result.append(list(combo)) # Prepares list , K iterations
                return
            elif remain<0 or len(combo)==k:
                return



            for i in range(start, 10):
                combo.append(i) # backtracking
                combineSum(i+1, remain-i, combo)
                combo.pop()



        combineSum(1, n, combo=[])

        return result


if __name__ == "__main__":
    sol = Solution()
    inputs = [
        (3,7),
        (9,45)
    ]
    for k, n in inputs:
        print(sol.combinationSum3(k, n))