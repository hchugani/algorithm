# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    Serialization is the process of converting a data structure or object into a sequence of bits so that it
    can be stored in a file or memory buffer, or transmitted across a network connection link to be
    reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
    serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
    serialized to a string and this string can be deserialized to the original tree structure.

    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not
    necessarily need to follow this format, so please be creative and come up with different approaches
    yourself.

    """

    """
    This can be done by doing preorder traversal
    

    """

    def serialize(self, root):
        """Encodes a tree to a single string.
    We start from the root, node 1, the serialization string is 1,. Then we jump to its left subtree with
     the root node 2, and the serialization string becomes 1,2,. Now starting from node 2, we visit its left
      node 3 (1,2,3,None,None,) and right node 4 (1,2,3,None,None,4,None,None) sequentially.
      Note that None,None, appears for each leaf to mark the absence of left and right child node,
      this is how we save the tree structure during the serialization. And finally, we get back to the
      root node 1 and visit its right subtree which happens to be a leaf node 5. Finally, the serialization
      string is done as 1,2,3,None,None,4,None,None,5,None,None,.

        time complexity : O(N)
        space complexity = O(N) to store results

        :type root: TreeNode
        :rtype: str
        """
        def rserialize(node, string):

            if node is None:
                string += "None,"
            else:
                string += str(node.val) + ","
                string = rserialize(node.left, string)
                string = rserialize(node.right, string)

            return string

        return rserialize(root, "")



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        Now let's deserialize the serialization string constructed above
        1,2,3,None,None,4,None,None,5,None,None,. It goes along the string, initiate the node value and
         then calls itself to construct its left and right child nodes

         time complexity : O(N)
        space complexity = O(N) to store results

        :type data: str
        :rtype: TreeNode
        """

        if len(data)==0:
            return

        nodes = data.split(",")
        nodes.pop()

        def derserialize(nodes):

            if nodes[0] == "None":
                nodes.pop(0)
                return None

            l = nodes[0]
            root = TreeNode(l)
            nodes.pop(0)

            root.left = derserialize(nodes)
            root.right = derserialize(nodes)

            return root


        root = derserialize(nodes)
        return root






# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))