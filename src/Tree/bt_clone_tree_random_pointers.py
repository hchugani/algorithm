# Definition for Node.
from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        """
        O(N): Both
        """
        if not root:
            return None

        copy = {}

        def dfs_copy(node):
            if node is None :
                return

            copy[node] = NodeCopy(node.val)

            dfs_copy(node.left)
            dfs_copy(node.right)


        def dfs_connect(node):
            if node is None:
                return

            if node.left:
                copy[node].left = copy[node.left]
            if node.right:
                copy[node].right = copy[node.right]
            if node.random:
                copy[node].random = copy[node.random]


            dfs_connect(node.left)
            dfs_connect(node.right)

        dfs_copy(root)
        dfs_connect(root)

        return copy[root]

