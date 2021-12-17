# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor1(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        """
        O(N) : time
        O(N) : space - due to recursion stack
        """
        self.previous = None
        self.target = None


        def inOrder(node):
            if node is None:
                return

            if node.left:
                inOrder(node.left)

            if self.previous ==p and self.target is None:
                self.target = node
                return

            self.previous = node

            if node.right:
                inOrder(node.right)

        if p.right:
            right = p.right
            while right.left:
                right = right.left
            self.target = right
        else:
            inOrder(root)

        return self.target

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        """
        O(H): time
        O(1) : Space
        """
        successor = None
        while root:
            if p.val>=root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor




