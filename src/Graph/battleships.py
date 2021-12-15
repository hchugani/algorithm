from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        start = 0

        def dfs(x, y,dir=0):
            board[x][y] = start

            dirs = []
            if dir==1:
                # horizontal
                dirs.append((1,0))
            elif dir==-1:
                dirs.append((0,1))
            else:
                dirs.append((1,0))
                dirs.append((0,1))

            for dx,dy in dirs:
                new_x = x+dx
                new_y = y+dy
                if new_x<m and new_y<n and board[new_x][new_y]=="X":
                    if dx==1:
                        dir = 1
                    else:
                        dir = -1
                    dfs(new_x, new_y,dir)
                    break


        for i in range(m):
            for j in range(n):
                if board[i][j]=="X":
                    dfs(i,j)
                    start+=1

        return start
s = Solution()
inputs = [
    [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]],
    [["."]]
]

for board in inputs:
    print(s.countBattleships(board))