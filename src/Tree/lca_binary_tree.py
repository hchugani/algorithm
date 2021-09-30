# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # problem can be solved by using two arrays which keeps track of
        # the nodes, one for each search
        # preorder traversal

        # O(N) time complexity  with O(N) stack space
        def dfs_search(node, search_node, temp_stack):
            if node is None:
                return None

            if node:
                temp_stack.append(node)
                l = dfs_search(node.left, search_node, temp_stack)
                r = dfs_search(node.right, search_node, temp_stack)
                if node.val == search_node.val:
                    return list(temp_stack)
                temp_stack.pop() # backtrack

            return l or r

        stack1 = dfs_search(root, p, [])
        stack2 = dfs_search(root, q, [])

        lca = None
        for i in range(min(len(stack1), len(stack2))):
            if stack1[i].val==stack2[i].val:
                lca = stack1[i]

        return lca

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # problem can be solved by using two arrays which keeps track of
        # the nodes, one for each search
        # preorder traversal

        # O(N) time complexity  with O(N) stack space
        stack = [root]
        parent  = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parent[node.left] = node

            if node.right:
                stack.append(node.right)
                parent[node.right] = node

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q

        