"""
1329. Sort the Matrix Diagonally
Medium

1482

173

Add to List

Share
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column
and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting
 from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.



Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

"""
from typing import List
import heapq


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        O(M*N*log(min(m,n)))
        O(min(n, m))
        """
        m = len(mat)
        n = len(mat[0])
        def sortDiagonal(row, col):

            diag = []
            diag_len = min(m-row, n-col)


            for i in range(diag_len):
                diag.append(mat[row+i][col+i])


            heapq.heapify(diag)

            for i in range(diag_len):
                mat[row+i][col+i] = heapq.heappop(diag)

        for i in range(m):
            sortDiagonal(i, 0)

        for col in range(1,n):
            sortDiagonal(0, col)

        return mat


s = Solution()
print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))



