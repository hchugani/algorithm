from typing import List
from collections import defaultdict
"""
212. Word Search II
Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

"""


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.eow = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        first iteration will have 4 iteration, from second atmost 3
        and it is repeated for each cell
        O(mn(4.3^(L-1))), L is max length of trien ndoe
        O(N): Space

        """
        trie = TrieNode()

        for word in words:
            node = trie
            for c in word:
                node = node.children[c]
            node.eow = word

        M = len(board)
        N = len(board[0])
        result = set()

        def backtrack(x, y, parent):
            node = parent.children[board[x][y]]
            letter = board[x][y]
            if node.eow:
                result.add(node.eow)
                node.eow = ""
            # mark it as visitied
            board[x][y]="#"

            dir = [(1,0),(-1,0),(0,1),(0,-1)]

            for dx, dy in dir:
                newx = x + dx
                newy = y + dy
                if 0<=newx<M and 0<=newy<N and board[newx][newy] in node.children.keys():
                    backtrack(newx, newy, node)
            # remove from visited
            board[x][y]=letter

            # pruning : if already matched found, and child are empty , delet it
            if len(node.children.keys())==0:
                del parent.children[letter]

        for i in range(M):
            for j in range(N):
                if board[i][j] in trie.children.keys():
                    backtrack(i, j, trie)

        return list(result)

s = Solution()
inputs = [
    ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
    ["oath","pea","eat","rain"])
]

for board, words in inputs:
    print(s.findWords(board, words))