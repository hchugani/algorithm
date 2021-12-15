# Definition for a binary tree node.
"""
979. Distribute Coins in Binary Tree
Medium


You are given the root of a binary tree with n nodes where each node in the tree has node.val coins.
There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be
from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        O(N): time
        O(H): space
        """
        self.ans = 0

        def dfs(node):
            if node is None:
                return 0

            L, R = dfs(node.left),dfs(node.right)
            self.ans += abs(L)+abs(R)
            return node.val+L+R-1

        dfs(root)
        return self.ans