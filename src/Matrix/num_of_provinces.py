from typing import List
"""
547. Number of Provinces
Medium

There are n cities. Some of them are connected, while some are not. If city a is connected directly 
with city b, and city b is connected directly with city c, then city a is connected indirectly with 
city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are
 directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        O(N^2) : Time
        O(N) : Space

        :param isConnected:
        :return:
        """
        count = 0
        N = len(isConnected)
        self.visited = [False for _ in range(N)]

        def dfs(grid, x):
            self.visited[x] = True

            for y in range(N):
                if not self.visited[y] and grid[x][y] == 1:
                    dfs(grid, y)


        for i in range(N):
            if not self.visited[i]:
                dfs(isConnected, i )
                count +=1

        return count

s = Solution()
inputs = [
    [[1,1,0],[1,1,0],[0,0,1]],
    [[1,0,0],[0,1,0],[0,0,1]]
]

for inp in inputs:
    print(s.findCircleNum(inp))