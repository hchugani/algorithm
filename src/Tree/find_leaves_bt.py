# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time complexity : O(HLogN)
        Space complexity : O(N) to hold the result
        """
        final_result = []

        def postOrder(node, result):
            if node:
                left_leaf_found = postOrder(node.left, result)
                right_leaf_found = postOrder(node.right, result)
                if not node.left and not node.right:
                    result.append(node.val)
                    return True
                if left_leaf_found: node.left = None
                if right_leaf_found: node.right = None
            return False


        while(True):
            result = []
            if postOrder(root, result):
                final_result.append(result)
                break

            final_result.append(result)


        return final_result


        # def getHeight(self,node)->int:
        #     if not node:
        #         return 0
        #     return 1  + max(self.getHeight(node.left), self.getHeight(node.right))


