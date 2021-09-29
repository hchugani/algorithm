from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Depth and height of a tree are equal
    for node , it is different
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time complexity : we visit each node exactly once, thus the time complexity is \mathcal{O}(N)O(N),
        #  where NN is the number of nodes.
        #
        # Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only
        # left child node, the recursion call would occur NN times (the height of the tree), therefore the
        # storage to keep the call stack would be \mathcal{O}(N)O(N). But in the best case (the tree is
        # completely balanced), the height of the tree would be \log(N)log(N). Therefore, the space complexity
        # in this case would be \mathcal{O}(\log(N))O(log(N)).
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


s = Solution()
# [3,9,20,null,null,15,7]
right = TreeNode(20, TreeNode(15), TreeNode(7))
root = TreeNode(3, TreeNode(9), right)
print(s.maxDepth(root))