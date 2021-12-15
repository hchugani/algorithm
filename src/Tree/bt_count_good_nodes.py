# Definition for a binary tree node.
"""
1448. Count Good Nodes in Binary Tree
Medium


Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no
 nodes with a value greater than X.

Return the number of good nodes in the binary tree.



"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        O(N): both , O(H): Space
        """
        count = 0

        def dfs(node, maxi=float("-inf")):
            nonlocal count
            if node is None:
                return

            if node.val >=maxi:
                count +=1
                maxi = node.val

            if node.right:
                dfs(node.right, maxi)
            if node.left:
                dfs(node.left, maxi)

        dfs(root)
        return count

