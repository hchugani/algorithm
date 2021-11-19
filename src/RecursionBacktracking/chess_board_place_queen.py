from  typing import List
"""
   The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
   
   Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

   Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


""" 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        O(N!) : Time
        O(N*N) : space
        """

        occupied = set()

        board = [ ["."]* n for _ in range(n)]

        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, col , diag, antidiag, state):
            if row == n:
                ans.append(create_board(state))
                return

            for c in range(n):
                cur_diag = row-c
                cur_anti_diag = row+c

                if (c in col or cur_diag in diag or cur_anti_diag in antidiag):
                    continue

                state[row][c] = "Q"
                col.add(c)
                diag.add(cur_diag)
                antidiag.add(cur_anti_diag)
                backtrack(row+1, col, diag, antidiag , state)
                col.remove(c)
                diag.remove(cur_diag)
                antidiag.remove(cur_anti_diag)
                state[row][c] = "."

        ans = []
        backtrack(0, set(), set(), set(), board)
        return ans


s = Solution()
for n in range(2,10):
    print(s.solveNQueens(n))