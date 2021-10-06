"""
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.


Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

"""

import sys

class Node:

    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val

class MaxStack:
    """
    Time Complexity: O(N) for the popMax operation, and O(1) for the other      operations, where NN is the number of operations performed.

    Space Complexity: O(N), the maximum size of the stack
    """

    def __init__(self):
        self.stack = []


    def push(self, x: int) -> None:
        m = max(x, self.stack[-1][1] if self.stack else -sys.maxsize)
        self.stack.append((x, m))


    def pop(self) -> int:
        return self.stack.pop()[0]


    def top(self) -> int:
        return self.stack[-1][0]


    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        m = self.stack[-1][1]
        b = []
        while m!=self.stack[-1][0]:
            b.append(self.stack.pop()[0])

        self.stack.pop()# pop max
        while b:
            self.push(b.pop())
        return m
    """
    
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next , self.tail.pre = self.tail, self.head
        self.dict = defaultdict(list)

    def push(self, x: int) -> None:
        new = Node(x)
        new.next = self.tail
        new.prev = self.tail.prev
        self.tail.prev.next, self.tail.prev = new, new
        self.dict[x].append(new)
        

    def pop(self) -> int:
        node_to_remove = self.tail.prev
        node_to_remove.next.prev, node_to_remove.prev.next = node_to_remove.prev,node_to_remove.next
        node_to_remove.next, node_to_remove.prev = None, None
        self.dict[node_to_remove.val].pop()
        return node_to_remove.val

    def top(self) -> int:
        if self.tail :
            return self.tail.val

    def peekMax(self) -> int:
        max_key =  max(self.dict.keys())
        return self.dict[max_key][-1].val
    
    def removeNode(self,node):            
        node.next.pre, node.pre.next = node.pre, node.next
        node.next , node.prev = None

    def popMax(self) -> int:
        max_key =  max(self.dict.keys())
        node_to_remove = self.dict[max_key].pop()
        if len(self.dict[max_key])==0:
            del self.dict[max_key]
        self.removeNode(node_to_remove)
        return max_key
    """

    # Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(8)
obj.push(8)
obj.push(8)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.peekMax()
param_5 = obj.popMax()