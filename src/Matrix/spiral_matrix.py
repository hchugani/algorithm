"""

"""
from typing import List


class Solution:
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        result = []
        M = len(matrix)
        N = len(matrix[0])

        def add(i, j, dr):
            result.append(matrix[i][j])
            matrix[i][j] = -101
            dd = [dr]
            dd.extend([(0,1),(1,0),(0,-1),(-1,0)])

            for dx, dy in dd:
                new_i = i+dx
                new_j = j+dy
                if new_i<M and new_j<N and matrix[new_i][new_j]!=-101:
                    add(new_i, new_j, (dx,dy))
                    break


        for i in range(M):
            for j in range(N):
                if matrix[i][j]!=-101:
                    add(i, j, (0,1))

        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        O(m*n)
        """
        result = []
        M = len(matrix)
        N = len(matrix[0])

        x,y = 0,0
        dr = [(0,1),(1,0),(0,-1),(-1,0)]
        i = 0
        result.append(matrix[x][y])
        while len(result) != M * N:
            matrix[x][y] = -101
            dx, dy = dr[i]
            while x+dx>=M or y+dy>=N or (x+dx<M and y+dy<N and matrix[x+dx][y+dy]==-101):
                i+=1
                i%=4
                dx, dy = dr[i]
            x = x + dx
            y = y + dy
            result.append(matrix[x][y])

        return result
