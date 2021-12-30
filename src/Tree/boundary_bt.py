# Definition for a binary tree node.
from typing import Optional, List
"""


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        O(N) : both
        """
        result = []

        def addLeaves(node):
            if node is None:
                return

            if isLeaf(node):
                result.append(node.val)
                return

            if node.left:
                addLeaves(node.left)

            if node.right:
                addLeaves(node.right)


        def isLeaf(node):
            if node.left is None and node.right is None:
                return True
            return False

        if not isLeaf(root):
            result.append(root.val)
        node = root.left
        while node:
            if not isLeaf(node):
                result.append(node.val)

            left = node.left
            if not left:
                node = node.right
            else:
                node = left

        addLeaves(root)

        stack = []
        node = root.right
        while node:
            if not isLeaf(node):
                stack.append(node.val)

            right = node.right
            if not right:
                node = node.left
            else:
                node = right

        while stack:
            result.append(stack.pop())

        return result
