# Definition for a binary tree node.

"""
863. All Nodes Distance K in Binary Tree
Medium

Given the root of a binary tree, the value of a target node target, and an integer k, return an
array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        O(N) both
        """
        parent = {}

        def dfs(node, par=None):
            if node is None:
                return

            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        queue = deque([(target, 0)])
        seen = set()
        seen.add(target)
        while queue:
            if queue[0][1]==k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for new_node in (node.left, node.right, parent[node]):
                if new_node and new_node not in seen:
                    seen.add(new_node)
                    queue.append((new_node,d+1))
        return []








