# Definition for a binary tree node.


"""
314. Binary Tree Vertical Order Traversal
Medium

Given the root of a binary tree, return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
from typing import List, Optional
from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        O(N) both
        """
        result = []
        if root is None:
            return result

        elements = defaultdict(list)

        queue = deque()
        queue.append((root,0))

        while queue:
            node, dist = queue.popleft()
            elements[dist].append(node.val)

            if node.left :
                queue.append((node.left, dist-1))
            if node.right:
                queue.append((node.right, dist+1))


        maxi = max(elements.keys())
        mini = min(elements.keys())

        for i in range(mini, maxi+1):
            result.append(elements[i])

        return result








