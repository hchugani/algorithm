"""
1110. Delete Nodes And Return Forest
Medium

Share
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.



Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        O(N): Both
        """

        result = []


        def dfs_delete(node, parent, to_delete,left=True):
            if not node:
                return

            dfs_delete(node.left, node, to_delete, True)
            dfs_delete(node.right, node, to_delete, False)

            l = node.left
            r = node.right
            if node.val in to_delete:
                if parent and left:
                    parent.left = None
                else:
                    if parent:
                        parent.right = None

                if l:
                    result.append(l)
                if r:
                    result.append(r)

        if root.val not in to_delete:
            result.append(root)
        dfs_delete(root, None, to_delete)
        return result



