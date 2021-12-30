"""
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.


Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time Complexity: \mathcal{O}(N \cdot 3 ^ L)O(N⋅3
L
 ) where NN is the number of cells in the board and LL is the length of the word to be matched.

For the backtracking function, initially we could have at most 4 directions to explore, but further the choices are reduced into 3 (since we won't go back to where we come from). As a result, the execution trace after the first step could be visualized as a 3-ary tree, each of the branches represent a potential exploration in the corresponding direction. Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary tree, which is about 3^L3
L
 .

We iterate through the board for backtracking, i.e. there could be NN times invocation for the backtracking function in the worst case.

As a result, overall the time complexity of the algorithm would be \mathcal{O}(N \cdot 3 ^ L)O(N⋅3
L
 ).

Space Complexity: \mathcal{O}(L)O(L) where LL is the length of the word to be matched
        """
        s1 = word[0]
        M = len(board)
        N = len(board[0])

        visited = set()

        def dfs(x,y,i):
            if i==len(word):
                return True


            dir = [(0,1),(1,0),(-1,0),(0,-1)]

            for dx,dy in dir:
                newx = x+dx
                newy = y+dy
                if 0<=newx<M and 0<=newy<N and (newx,newy) not in visited and board[newx][newy]==word[i]:
                    visited.add((newx,newy))
                    if dfs(newx,newy,i+1):
                        return True
                    visited.remove((newx,newy))

            return False

        for i in range(M):
            for j in range(N):
                if (i, j) not in visited and board[i][j]==word[0]:
                    visited.add((i,j))
                    if dfs(i,j,1):
                        return True
                    visited.remove((i,j))

        return False

s = Solution()
inputs = [
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
]

for board,word in inputs:
    print(s.exist(board,word))