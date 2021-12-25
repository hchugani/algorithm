"""
1155. Number of Dice Rolls With Target Sum
Medium


You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice
 so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

"""
from functools import lru_cache

class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        O(NK): Both
        """

        @lru_cache(maxsize=None)
        def recur(n, t):
            if t <= 0 or t > n*k:
                return 0

            if n==1:
                if t <=k:
                    return 1
                else:
                    return 0
            count = 0
            for i in range(1, k+1):
                count+=recur(n-1, t-i)

            return count

        return recur(n,target) % ((10**9) + 7)


s = Solution()

inputs = [
    (30, 30, 500),
    (1, 6, 3)
]

for n, k, target in inputs:
    print(s.numRollsToTarget(n, k, target))