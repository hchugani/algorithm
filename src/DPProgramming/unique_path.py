"""
62. Unique Paths
Medium


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

"""
class Solution:

    #     @lru_cache(maxsize=None)
    #     def uniquePaths(self, m: int, n: int) -> int:
    #         if m == 1 or n == 1:
    #             return 1

    #         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


    def uniquePaths(self, m: int, n: int) -> int:
        """
        O(MN) both
        """
        dist = [[1] * n for _ in range(m)] # base case

        for r in range(1, m):
            for c in range(1, n):
                dist[r][c] = dist[r-1][c] + dist[r][c-1] # either should come from up or left

        return dist[m-1][n-1]

s = Solution()
inputs = [
    (3,7),
    (23,12)
]

for m,n in inputs:
    print(s.uniquePaths(m,n))
