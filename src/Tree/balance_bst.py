class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        self.sort_arr = []

        def inOrder(node):
            if node is None:
                return

            if node.left:
                inOrder(node.left)

            self.sort_arr.append(node.val)

            if node.right:
                inOrder(node.right)

        def build(left, right):
            if left>right:
                return None

            mid = left+ (right-left)//2

            node = TreeNode(self.sort_arr[mid])

            node.left = build(left, mid-1)
            node.right = build(mid+1, right)

            return node

        inOrder(root)
        return build(0, len(self.sort_arr)-1)