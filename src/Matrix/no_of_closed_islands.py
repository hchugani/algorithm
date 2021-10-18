from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """

        O(MN) both
        :param grid:
        :return:
        """
        count = 0
        M = len(grid)
        N = len(grid[0])
        self.visited = [[False for _ in range(N)] for _ in range(M)]

        def dfs(grid, x, y):

            self.visited[x][y] = True

            if y==0 or y==N-1:
                return False

            if x==0 or x==M-1:
                return False

            ret1 = ret2 = ret3 = ret4 = True
            if y-1>=0 and not self.visited[x][y-1] and grid[x][y-1]==0:
                ret1 = dfs(grid, x, y-1)
            if y+1 <N and not self.visited[x][y+1] and grid[x][y+1]==0:
                ret2 = dfs(grid, x, y+1)
            if x-1>=0 and not self.visited[x-1][y] and grid[x-1][y]==0:
                ret3 = dfs(grid, x-1, y)
            if x+1<M and not self.visited[x+1][y] and grid[x+1][y]==0:
                ret4 = dfs(grid, x+1, y )

            return ret1 and ret2 and ret3 and ret4


        for x in range(1,M-1):
            for y in range(1,N-1):
                if not self.visited[x][y] and grid[x][y]==0:
                    if dfs(grid, x, y):
                        count +=1

        return count

inputs = [
    [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]],
    [[1,1,1,1,1,1,1], [1,0,0,0,0,0,1], [1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],
     [1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
]
s = Solution()
for inp in inputs:
    print(s.closedIsland(inp))
