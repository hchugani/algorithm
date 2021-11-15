from collections import defaultdict
from typing import List

"""
Time complexity is constant here since the board size is fixed and there is no N-parameter to measure. Though let's discuss the number of operations needed : (9!)^9(9!) 
9
 . Let's consider one row, i.e. not more than 99 cells to fill. There are not more than 99 possibilities for the first number to put, not more than 9 \times 89×8 for the second one, not more than 9 \times 8 \times 79×8×7 for the third one etc. In total that results in not more than 9!9! possibilities for a just one row, that means not more than (9!)^9(9!) 
9
  operations in total. Let's compare:

9^{81} = 1966270504755529136180759085269121162831034509442147669273154155379663911968099 
81
 =196627050475552913618075908526912116283103450944214766927315415537966391196809 for the brute force,

and (9!)^9 = 109110688415571316480344899355894085582848000000000(9!) 
9
 =109110688415571316480344899355894085582848000000000 for the standard backtracking, i.e. the number of operations is reduced in 10^{27}10 
27
  times !

Space complexity : the board size is fixed, and the space is used to store board, rows, columns and boxes structures, each contains 81 elements.

"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        row = [defaultdict(int) for _ in range(len(board))]
        col = [defaultdict(int) for _ in range(len(board))]
        subbox = [defaultdict(int) for _ in range(len(board))]
        box_idx = lambda i, j : (i//3)*3 + j//3

        def could_place(i, j, val):
            return row[i][val]==0 and col[j][val]==0 and subbox[box_idx(i, j)][val]==0

        def place_val(i, j, val):
            row[i][val]+=1
            col[j][val]+=1
            subbox[box_idx(i, j)][val]+=1
            board[i][j] = str(val)

        def remove_val(i, j, val):
            del row[i][val]
            del col[j][val]
            del subbox[box_idx(i, j)][val]
            board[i][j] = "."

        def place_next_val(i, j):
            if i==N-1 and j==N-1:
                return True
            else:
                if j < N-1:
                    j+=1
                elif j==N-1 and i<N-1:
                    i+=1
                    j=0
                return place(i, j)

        def place(i=0, j=0):
            if board[i][j] == ".":
                for val in range(1, 10):
                    if could_place(i,j, val):
                        place_val(i, j, val)
                        if place_next_val(i, j):
                            return True
                        remove_val(i, j, val)
            else:
                if place_next_val(i, j):
                    return True

        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    place_val(i, j, val)

        # backtrack
        place(0,0)


