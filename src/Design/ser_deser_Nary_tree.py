"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        Serialization: O(N)O(N) where NN are the number of nodes in the tree. For every node, we add 2 different values
         to the final string and every node is processed exactly once. We add the value of the node itself and we also
         add the child switch sentinel. Also, for the nodes that end a particular level, we add the level end sentinel.
Deserialization: For deserialization, we process the entire string, one character at a time and also construct the tree
along the way. So, the overall time complexity for deserialization is 2N2N = O(N)O(N)
Space Complexity

Serialization: The space occupied by the serialization helper function is through the queue and the final string that is produced. We know the size of the final string to be 2N2N. So that is one part of the space complexity. The other part is the one occupied by the queue which is O(N)O(N). Overall, the space is O(N)O(N).
Deserialization: For deserialization, the space is mostly occupied by the two lists that we use. The space complexity there is O(N)O(N). Note that when we re-initialize a list, the memory that was allocated earlier is deallocated by the garbage collector and it's essentially equal to a single list of size O(N)O(N).

        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        string = []

        queue = deque([root])
        queue.append(None)

        while queue:
            node = queue.popleft()

            if node is None:
                string.append("#")
                # If this is an "endNode", we need to add another one
                # to mark the end of the current level unless this
                # was the last level.
                if queue:
                    queue.append(None)
            elif node == "C":
                # parent changed
                string.append("$")
            else:
                string.append(str(node.val))
                for child in node.children:
                    queue.append(child)

                if queue[0]!=None:
                    # add only if this is not the last in the current level
                    queue.append("C")

        return ",".join(string)





    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        # [1,"#",2,3,4,5,"#","$",6,7,"$",8,"$",9,10,"#","$",11,"$",12,"$",13,"$","#",14,"$","$","$","#","$","#"]
        if not data:
            return None
        data = data.split(",")

        root = Node(int(data[0]),[])
        prev_level = deque()
        cur_level = deque()
        cur_level.append(root)
        parent = root

        for i in range(1, len(data)):
            if data[i]=="#":
                # change cur_level to previous

                prev_level = cur_level
                cur_level = deque()

                parent = prev_level.popleft() if prev_level else None
            elif data[i] == "$":
                parent = prev_level.popleft() if prev_level else None
            else:
                child = Node(int(data[i]),[])
                cur_level.append(child)

                parent.children.append(child)

        return root











        # Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize(root))