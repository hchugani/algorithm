# Definition for a binary tree node.

"""
919. Complete Binary Tree Inserter
Medium

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete,
and returns the value of the parent of the inserted TreeNode.
TreeNode get_root() Returns the root node of the tree.

"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    """
    Time Complexity: The preprocessing is O(N), where NN is the number of nodes in the tree. Each insertion operation thereafter is O(1)O(1).

Space Complexity: O(N)
 .
    """

    def __init__(self, root: Optional[TreeNode]):
        self.deque = deque([])
        self.root = root
        q = deque([root])

        while q:
            node = q.popleft()

            # to maintain the insert order node
            if not node.left or not node.right:
                self.deque.append(node)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        node = self.deque[0]
        new = TreeNode(val)
        self.deque.append(new)

        if not node.left :
            node.left = new
        else:
            node.right = new
            self.deque.popleft()

        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()