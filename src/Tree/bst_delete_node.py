# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        O(logN) both
        """
        if root is None:
            return None

        if key>root.val:
            root.right = self.deleteNode(root.right,key)
        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predec(root)
                root.left  = self.deleteNode(root.left, root.val)

        return root


    def successor(self,node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predec(self,node):
        node = node.left
        while node.right:
            node = node.right
        return node.val
