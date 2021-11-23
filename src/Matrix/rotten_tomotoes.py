from collections import deque
from typing import List
"""
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is
 impossible, return -1.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        O(MN) both
        """

        M = len(grid)
        N = len(grid[0])

        queue = deque()
        visited = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                    visited.add((i,j))

        maxi = 0

        while queue:
            x, y, dist = queue.popleft()
            maxi = max(maxi, dist)

            for dx, dy in [(1,0),(-1,0),(0,1), (0,-1)]:
                new_x = x + dx
                new_y = y + dy
                if 0<=new_x<M and 0<=new_y<N and (new_x, new_y) not in visited and grid[new_x][new_y]==1:
                    queue.append((new_x, new_y, dist+1))
                    visited.add((new_x, new_y))

        for i in range(M):
            for j in range(N):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxi = -1
                    break
        return maxi


s = Solution()
inputs = [
    [[2,1,1],[1,1,0],[0,1,1]],
    [[0,2]],
    [[2,1,1],[0,1,1],[1,0,1]],
    [[0]]
]

for matrix in inputs:
    print(s.orangesRotting(matrix))

