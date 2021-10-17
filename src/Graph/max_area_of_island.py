"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

"""


from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        O(MN) both
        """
        M = len(grid)
        N = len(grid[0])
        self.visited = [[False for _  in range(N)] for _ in range(M)]
        self.maxi = 0

        def dfs(grid, x, y, count = [0]):
            self.visited[x][y] = True

            count[0]+=1

            if y-1>=0 and grid[x][y-1]==1 and not self.visited[x][y-1]:
                dfs(grid, x, y-1, count)
            if y+1<N and grid[x][y+1]==1 and not self.visited[x][y+1]:
                dfs(grid, x, y+1, count)
            if x-1>=0 and grid[x-1][y]==1 and not self.visited[x-1][y]:
                dfs(grid, x-1, y, count)
            if x+1<M and grid[x+1][y]==1 and not self.visited[x+1][y]:
                dfs(grid, x+1, y, count)

            self.maxi = max(self.maxi, count[0])


        for x in range(M):
            for y in range(N):
                if grid[x][y]==1 and not self.visited[x][y]:
                    dfs(grid, x, y, [0])

        return self.maxi


s = Solution()
input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(s.maxAreaOfIsland(input))