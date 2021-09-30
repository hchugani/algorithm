from typing import List

from drawtree import draw_level_order

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InsertLevelOrder:

    @staticmethod
    def insert(arr: List[int], i=0)->TreeNode:
        N = len(arr)
        root = None

        if i < N:
            temp = TreeNode(i)
            root = temp

            root.left = InsertLevelOrder.insert(arr, 2*i+1)
            root.right = InsertLevelOrder.insert(arr, 2*i+2)

        return root





