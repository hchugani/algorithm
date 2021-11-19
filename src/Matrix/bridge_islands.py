from typing import List
"""
934. Shortest Bridge

In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally 
connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        O(N2) both
        """
        M = len(grid)
        N = len(grid[0])
        visited1 = set()
        visited2 = set()

        def dfs(i, j, visited):
            for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_x = i + x
                new_y = j + y
                if 0<=new_x<M and 0<=new_y<N and grid[new_x][new_y]==1 and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    dfs(new_x, new_y,visited)

        visited = visited1
        for i in range(M):
            for j in range(N):
                if (i, j) not in visited1 and (i, j) not in visited2 and grid[i][j]==1:
                    visited.add((i,j))
                    dfs(i, j,visited)
                    visited = visited2

        mini = float("inf")

        for (i, j) in visited1:
            for (x, y) in visited2:
                diff = abs(i-x)+abs(j-y)-1
                mini = min(mini, diff)
                if mini==1:
                    break

        return mini

s = Solution()

matrixes = [

    [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]],
    [[0,1],[1,0]]
]

for mat in matrixes:
    print(s.shortestBridge(mat))