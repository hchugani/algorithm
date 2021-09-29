from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        :param root:
        :return:
        """
        queue = []
        if root is not None:
            queue.append((root,0))
        height = self.getHeight(root)
        result = [[] for _ in range(height)]
        while queue:
            node,idx = queue.pop(0)
            result[idx].append(node.val)
            if node.left:
                queue.append((node.left, idx+1))
            if node.right:
                queue.append((node.right, idx+1))

        return result


    def getHeight(self, node: TreeNode)->int:
        if node is None:
            return 0

        return 1 + max(self.getHeight(node.right), self.getHeight(node.left))


s = Solution()
# [3,9,20,null,null,15,7]
right = TreeNode(20, TreeNode(15), TreeNode(7))
root = TreeNode(3, TreeNode(9), right)
print(s.levelOrder(root))