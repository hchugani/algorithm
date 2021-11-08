from typing import List

"""
36. Valid Sudoku
Medium


Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to 
the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        O(N*N) : Both
        """
        N = len(board)
        row = [set() for _ in range(N)]
        col = [set() for _ in range(N)]
        subbox =[set() for _ in range(N)]

        for i in range(len(board)):
            for  j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue

                if val in row[i]:
                    return False
                row[i].add(val)

                if val in col[j]:
                    return False
                col[j].add(val)

                # get box number
                idx = (i//3)*3 + j//3
                if val in subbox[idx]:
                    return False
                subbox[idx].add(val)

        return True


s = Solution()

input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(input))



