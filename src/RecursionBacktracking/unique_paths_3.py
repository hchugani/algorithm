from typing import List

"""
980. Unique Paths III
Hard


You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.

 
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        O(3^N) : Time
        O(N) : Space
        """
        M = len(grid)
        N = len(grid[0])

        result = []
        crossed = set()

        def backtrack(i, j, M, N):
            nonlocal valid_cell
            if grid[i][j]==2 and len(list(crossed))==valid_cell :
                result.append(list(crossed))
                return

            dir = [(0,1), (1,0), (-1,0),(0,-1)]
            for x, y in dir:
                new_x = i+x
                new_y = j+y
                if 0<=new_x<M and 0<=new_y<N and grid[new_x][new_y]!=-1 and (new_x, new_y) not in crossed:
                    crossed.add((new_x, new_y))
                    backtrack(new_x, new_y, M, N)
                    crossed.remove((new_x, new_y))

        start = None
        valid_cell = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] != -1:
                    valid_cell +=1

        x, y = start
        crossed.add((x, y))
        backtrack(x, y, M, N)


        return len(result)



s = Solution()

inputs = [
    [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],
    [[0,1],[2,0]]
]

for matrix in inputs:
    print(s.uniquePathsIII(matrix))
