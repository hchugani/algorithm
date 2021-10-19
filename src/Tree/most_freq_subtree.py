# Definition for a binary tree node.
"""

508. Most Frequent Subtree Sum
Medium

Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all
 the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at
that node (including the node itself).

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import Optional, List

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        O(N) both

        :param root:
        :return:
        """

        result = defaultdict(int)

        def postOrder(node, result):
            if node is None:
                return 0

            sum_left = postOrder(node.left, result)
            sum_right = postOrder(node.right, result)
            result[node.val+sum_left+sum_right]+=1

            return node.val+sum_left+sum_right


        postOrder(root, result)

        maxi = 1
        max_val = []
        for key in result.keys():
            if result[key]>1:
                if result[key]>maxi:
                    maxi = result[key]
                    max_val = []
                    max_val.append(key)
                elif result[key]==maxi:
                    max_val.append(key)


        return result.keys() if maxi==1 else max_val
