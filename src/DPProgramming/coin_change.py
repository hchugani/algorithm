from functools import lru_cache
from typing import List

"""
322. Coin Change
Medium


You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot 
be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Time complexity : O(S*n)O(S∗n). where S is the amount, n is denomination count. In the worst case the recursive tree of the algorithm has height of SS and the algorithm solves only SS subproblems because it caches precalculated solutions in a table. Each subproblem is computed with nn iterations, one by coin denomination. Therefore there is O(S*n)O(S∗n) time complexity.

Space complexity : O(S)O(S), where SS is the amount to change We use extra space for the memoization table.
        """

        @lru_cache(maxsize=None)
        def minChange(num):
            if num==0:
                return 0

            if num<0:
                return float("inf")

            if num in coins:
                return 1

            val =  1 + min([ minChange(num-k) for k in coins])
            return val

        val =  minChange(amount)
        return -1 if val==float("inf") else val

