from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time complexity: O(H + k), where H is a tree height. This complexity is defined by the stack, which contains at least H + k elements, since before starting to pop out one has to go down to a leaf. This results in \mathcal{O}(\log N + k)O(logN+k) for the balanced tree and \mathcal{O}(N + k)O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
        Space complexity: O(H) to keep the stack, where HH is a tree height. That makes \mathcal{O}(N)O(N) in the worst case of the skewed tree, and \mathcal{O}(\log N)O(logN) in the average case of the balanced tree.
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            if not k:
                return root.val

            root = root.right


        