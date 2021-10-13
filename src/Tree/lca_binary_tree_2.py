
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Time complexity: O(H) height of the tree
        space complexity : O(H)
        """
        ancestors = set()

        node = p
        while node :
            ancestors.add(node)
            node = node.parent

        node = q
        while node not in ancestors:
            node = node.parent

        return node

s = Solution()
s.lowestCommonAncestor()