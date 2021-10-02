# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    71. Second Minimum Node In a Binary Tree

        Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

    Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

    If no such second minimum value exists, output -1 instead.





    Example 1:


    Input: root = [2,2,5,null,null,5,7]
    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.

    """
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """
            Let \text{min1 = root.val}min1 = root.val. When traversing the tree at some node, \text{node}node, if \text{node.val > min1}node.val > min1, we know all values in the subtree at \text{node}node are at least \text{node.val}node.val, so there cannot be a better candidate for the second minimum in this subtree. Thus, we do not need to search this subtree.

    Also, as we only care about the second minimum \text{ans}ans, we do not need to record any values that are larger than our current candidate for the second minimum, so unlike Approach #1 we can skip maintaining a Set of values(uniques) entirely.
    Timecomplexity : O(N)(
    Space complexity : O(h) == O(N ) for call stack
        """

        self.ans = float("inf")
        min1 = root.val

        def preOrder(node):

            if node:
                if min1< node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    preOrder(node.left)
                    preOrder(node.right)

        preOrder(root)
        return -1 if self.ans==float("inf") else self.ans



