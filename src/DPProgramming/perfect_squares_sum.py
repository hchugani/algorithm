from functools import lru_cache
from math import sqrt

"""
279. Perfect Squares
Medium

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product
 of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

"""

class Solution:
    def numSquares(self, n: int) -> int:
        """
        O(n * sqrt(n)) : Time
        O(n): Space
        """

        squares = [i**2 for i in range(1, int(sqrt(n))+1)]

        @lru_cache(maxsize=None)
        def minSquare(num):
            if num==0:
                return 0

            if num<0:
                return float("inf")

            if num in squares:
                return 1
            return 1 + min([minSquare(num-k) for k in squares])

        return minSquare(n)

s = Solution()
for num in range(1, 100):
    print(s.numSquares(num))