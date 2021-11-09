from functools import lru_cache
"""
343. Integer Break
Medium


Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the 
product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        O(n*n)
        """

        @lru_cache(maxsize=None)
        def breakInt(n):
            if n==1:
                return 1

            maxi = 0
            for i in range(1,n):
                maxi = max(maxi, i * breakInt(n-i), i * (n-i))

            return maxi


        return breakInt(n)

s = Solution()
for n in range(2,59):
    print(s.integerBreak(n))