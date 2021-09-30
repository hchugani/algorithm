# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time complexity: O(N)
        Space complexity : O(1)
        :param root:
        :param p:
        :param q:
        :return:
        """

        p_val , q_val = p.val, q.val

        node = root

        while node:
            if p_val < node.val and q.val < node.val:
                node = node.left
            elif p.val>node.val and q.val > node.val:
                node = node.right
            else:
                return node
        return None

        # Recurvsive approach with O(N) time complexity
        # if p.val<root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val>root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root


#         def search(node, key, stack=[]):
#             l = r = None
#             if node:
#                 stack.append(node)
#                 l = search(node.left, key, stack)
#                 r = search(node.right, key, stack)
#                 if node.val== key.val:
#                     return list(stack)
#                 stack.pop() # backtrack
#             return l or r

#         stack1 = search(root,p, [])
#         stack2 = search(root, q, [])
#         LCA = None
#         for i in range( min(len(stack1), len(stack2))):
#             if stack1[i].val == stack2[i].val:
#                 LCA = stack1[i]

#         return LCA
