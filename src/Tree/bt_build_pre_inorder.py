from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(inorder)

        def build(left, right):
            if left>right:
                return

            node = TreeNode(preorder[0])
            div = ind_map[preorder[0]]
            preorder.pop(0)
            node.left = build( left, div-1)
            node.right = build(div+1, right)

            return node


        ind_map = {}
        for i, val in enumerate(inorder):
            ind_map[val] = i

        return build(0, N-1)
