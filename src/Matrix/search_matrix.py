"""
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the
 following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        O(M+N): Time
        O(1) : Space
        """
        M = len(matrix)
        N = len(matrix[0])

        row = M-1
        col = 0

        vert = True
        while 0<=row<M and 0<=col<N:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                row-=1
            else:
                col+=1
        return False

s = Solution()
inputs = [
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
]

for matrix, n in inputs:
    print(s.searchMatrix(matrix, n))