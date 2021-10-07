from typing import List

class Solution:
    """
        n = 3
        self.board = [["" for _ in range(n)] for _ in range(n)]

        def checkCol(col, player_id):
            for i in range(n):
                if self.board[i][col] != player_id:
                    return False
            return True

        def checkRow(row, player_id):
            for i in range(n):
                if self.board[row][i] != player_id:
                    return False
            return True

        def checkDiag(player_id):
            for row in range(n):
                if self.board[row][row] != player_id:
                    return False
            return True

        def checkAntiDiag(player_id):
            for i in range(n):
                if self.board[i][n-1-i] != player_id:
                    return False
            return True

        player = "A"
        for move in moves:
            row = move[0]
            col = move[1]
            self.board[row][col] = player

            if checkRow(row, player) or checkCol(col, player) or checkDiag(player) or checkAntiDiag(player):
                return player
            if player=="A":
                player = "B"
            else:
                player = "A"

        return "Draw" if len(moves)==n*n else "Pending"
    """
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        Time complexity : O(m), m is number of moves

        space complexity : O(n) , n is grid size
        :param moves:
        :return:
        """
        N = 3
        rows = [0]*N
        cols = [0]*N
        diag = antidiag = 0
        player = 1
        win_name = ""

        def winner(sum_val):
            if sum_val==N:
                return "A"
            elif sum_val==-N:
                return "B"
            else:
                return ""

        for move in moves:
            row, col = move[0], move[1]
            rows[row] +=player
            cols[col] +=player
            if row == col:
                diag += player
            if (row == N-1-col) or (col==N-1-row):
                antidiag += player
            player = -1*player

        for r in rows:
            win_name = winner(r)
            if win_name:
                return win_name


        for c in cols:
            win_name = winner(c)
            if win_name:
                return win_name

        win_name = winner(diag)
        if win_name:
            return win_name

        win_name = winner(antidiag)
        if win_name:
            return win_name

        return "Draw" if len(moves)==N*N else "Pending"

s = Solution()
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(s.tictactoe(moves))
moves = [[0,0],[1,1]]
print(s.tictactoe(moves))
