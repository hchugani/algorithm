from typing import Optional
from Tree.level_order_traversal import Solution as LevelOrder
from Tree.insert_level_order import InsertLevelOrder
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
     Binary Tree Upside Down


     Given the root of a binary tree, turn the tree upside down and return the new root.

    You can turn a binary tree upside down with the following steps:

    The original left child becomes the new root.
    The original root becomes the new right child.
    The original right child becomes the new left child.

    The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.



    Example 1:


    Input: root = [1,2,3,4,5]
    Output: [4,5,2,null,null,3,1]

    """
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time complexity : O(N)
        Space complexity : O(logN) height of tree
        """
        self.new_root = None

        def dfs(node, prev):
            if node is None:
                return

            if node.left is None and node.right is None:
                self.new_root = node

            # first turn the left child
            dfs(node.left, node)

            # turn left and right child based on previous if it exists
            if prev:
                node.right = prev
                node.left = prev.right
            else:
                node.right = node.left = None

        dfs(root, None)
        return self.new_root


s = Solution()
root = InsertLevelOrder.insert([1,2,3,4,5])
new_root = s.upsideDownBinaryTree(root)
lo = LevelOrder()
print(lo.levelOrder(new_root))




