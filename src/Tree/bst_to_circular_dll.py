from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        O(N) : both
        """
        if not root:
            return root

        first = None
        last = None

        def helper(node):
            nonlocal first, last
            if not node:
                return None

            helper(node.left)

            if not first:
                first = node

            if last:
                last.right = node
                node.left = last
            last = node
            helper(node.right)

        helper(root)
        last.right = first
        first.left = last

        return first

