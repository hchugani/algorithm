from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # First transpose the matrix

        def transpose(matrix):
            """
            Time complexity is O(M): M is number of cells N^2
            """
            N = len(matrix)
            for i in range(N):
                for j in range(i, N):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse
        def reverse(matrix):
            """
            Time complexity is O(M): M is number of cells N^2
            """
            N = len(matrix)
            for i in range(N):
                for j in range(N//2):
                    matrix[i][j] , matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]

        transpose(matrix)
        reverse(matrix)

inputs = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
]

s = Solution()
for inp in inputs:
    s.rotate(inp)
    print(inp)