from  functools import lru_cache
from  typing import List
"""
Recursion + Memoization
Dynamic Programming is always the appraoch you should consider whenever you see a hard problem asking the ways of paiting. Assume you're experienced leetcoder, you won't challenge hard problems otherwise, you can quickly come up with the dp array dp[i][j][k] that represents the minimum cost of paiting the houses[i] with color[j] at the neignborhoods[k].
So you immediately started to write the code. Then you were stuck at how to transit the dp array to next house especically when encountering the houses that have been painted before, because of the nature of 3 dimentional array.
I did the same thing, and spent half of one hour to be stuck at the dp implementation. However, I recalled the trick I always used to resolve hard dp problem that is using recursion + memoization instead. We can use the (i, j, k) as parameters as same as the dp array definition.
So let's come up with the base case

helper(i, j, k):
base case:
1. invalid, return float('inf')
    * i + 1 < k: the number of houses is smaller than neignborhoods
    * k < 1: no neignborhoods to paint houses
    * 0 < houses[i] != j: the houses is painted with a color different with j.
2. i == 0:
  return the cost[0][j] for the first house, or 0 if the house is already painted.
else:
try out each color by calling recusive `helper(i - 1, color, k)`, and pass different `k` as per whether `color == j`.
return the minimum + cost if house is not painted else minimum
Finally, memory the results using cache to improve the performance
"""

"""
1473. Paint House III
Hard

There is a row of m houses in a small city, each house must be painted with one of the n colors
 (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target
 neighborhoods. If it is not possible, return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
"""
class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        Time Complexity= O(MNK)
        Space Complexity= O(MNK)
        """
        @lru_cache(None)
        def helper(i, j, k)->int:
            # 0<houses[i]!=j : ignore cases where it is painted with undesired color
            if i + 1 < k or k <= 0 or 0 < houses[i] != j:
                return float('inf')

            if i==0:
                return 0 if houses[0]==j else cost[0][j-1]

            return min(helper(i-1, color, k if color==j else k-1 ) for color in range(1,n+1)) + (cost[i][j-1] if houses[i]==0 else 0)

        res = min(helper(m-1, color, target) for color in range(1, n+1))
        return res if res != float("inf") else -1

s = Solution()
print(s.minCost([0,2,1,2,0], cost= [[1,10],[10,1],[10,1],[1,10],[5,1]],m=5,n=2, target=3))

