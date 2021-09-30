from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time complexity : O(MN)
        Space complexity : O(MN)
        """
        M = len(grid)
        if M:
            N = len(grid[0])
        self.visited = [ [False for _ in range(N)] for i in range(M)]


        def dfs(grid, x , y):
            M  = len(grid)
            if M:
                N = len(grid[0])

            self.visited[x][y] = True

            if y-1>=0 and grid[x][y-1]=="1" and not self.visited[x][y-1]:
                dfs(grid, x, y-1)
            if y+1<N and grid[x][y+1]=="1" and not self.visited[x][y+1]:
                dfs(grid, x, y+1)
            if x+1<M and grid[x+1][y]=="1" and not self.visited[x+1][y]:
                dfs(grid, x+1, y)
            if x-1>=0 and grid[x-1][y]=="1"and not self.visited[x-1][y]:
                dfs(grid, x-1, y)

        count = 0
        for i in range(M):
            for j in range(N):
                if not self.visited[i][j] and grid[i][j]=="1":
                    count+=1
                    dfs(grid, i, j)

        return count

s = Solution()
input = [  ["1","1","0","0","0"],  ["1","1","0","0","0"],  ["0","0","1","0","0"],  ["0","0","0","1","1"]]
print(s.numIslands(input))

input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(input))



