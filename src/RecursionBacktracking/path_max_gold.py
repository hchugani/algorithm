from typing import List
"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount
 of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        I think the time complexity should be O(MN * 3^MN). For the DFS, it would run at most O(3^MN),
        because at each recursion, we have 4 possible options and since we can't go back to where we come
        from. It's down to 3 choices. The deepest level we could go is MN. So the time complexity overall
        is O(MN * 3^MN).
        Space: O(MN)
        """
        M = len(grid)
        N = len(grid[0])

        self.visited = [ [False for _ in range(N)] for _ in range(M)]
        self.maxi = 0

        def dfs(grid, x, y, count = 0):
            self.visited[x][y] = True

            val1 = val2 = val3 = val4 = 0

            if y-1>=0 and grid[x][y-1] !=0 and not self.visited[x][y-1]:
                val1 = dfs(grid, x, y-1, count)

            if y+1<N and grid[x][y+1] !=0 and not self.visited[x][y+1]:
                val2 = dfs(grid, x, y+1, count)

            if x-1>=0 and grid[x-1][y] !=0 and not self.visited[x-1][y]:
                val3 = dfs(grid, x-1, y, count)

            if x+1<M and grid[x+1][y] !=0 and not self.visited[x+1][y]:
                val4 = dfs(grid, x+1, y, count)

            self.visited[x][y] = False
            return grid[x][y] + max(val1, val2, val3, val4)


        for i in range(M):
            for j in range(N):
                if grid[i][j] !=0:
                    self.maxi = max(dfs(grid,i, j), self.maxi)

        return self.maxi

s = Solution()
grids = [[0,6,0],[5,8,7],[0,9,0]]
print(s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))