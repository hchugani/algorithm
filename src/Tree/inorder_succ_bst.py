
"""
510. Inorder Successor in BST II
Medium

Given a node in a binary search tree, return the in-order successor of that node in the BST.
 If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a
reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

"""

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        """
        O(H) - O(logN)
            If the node has a right child, and hence its successor is somewhere lower in the tree. Go to the right once and then as many times to the left as you could. Return the node you end up with.

    Node has no right child, and hence its successor is somewhere upper in the tree. Go up till the node that is left child of its parent. The answer is the parent
        """
        if node.right:
            left = node.right
            while left.left:
                left = left.left
            return left

        while node.parent is not None and node==node.parent.right:
            node = node.parent
        return node.parent


