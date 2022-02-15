"""
430. Flatten a Multilevel Doubly Linked List
Medium


You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an
additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing
these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel
data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level,
doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and
before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.


"""


from typing import Optional, List
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.head = head

        def flat(node, parent):

            if parent:
                node.prev = parent

            prev = None
            cur = node
            while cur:
                next = cur.next
                if cur.child:
                    ret = flat(cur.child, cur)
                    cur.next = cur.child
                    ret.next  = next
                    cur.child = None
                    if next:
                        next.prev = ret
                prev = cur
                cur = cur.next

            return prev

        flat(head, None)
        return head