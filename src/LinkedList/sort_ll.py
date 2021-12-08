# Definition for singly-linked list.
from typing import Optional
"""
Sort Linked List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time : O(NlogN)
        Space : O(logN) recursion stack top down approach
        """

        def getMid(node :ListNode)->ListNode:
            slow = node
            fast = node
            while fast and fast.next:
                prev_slow = slow
                slow = slow.next
                fast = fast.next.next

            prev_slow.next = None
            return slow


        def mergeSort(node : ListNode):
            if node is None or node.next is None:
                return node
            mid = getMid(node)
            left = mergeSort(node)
            right = mergeSort(mid)
            return merge(left, right)

        def merge(left:ListNode, right:ListNode):
            new_head = cur = None
            while left and right:
                if left.val<right.val:
                    if new_head is None:
                        new_head = cur = left
                    else:
                        cur.next = left
                        cur = left
                    left = left.next
                else:
                    if new_head is None:
                        new_head = cur = right
                    else:
                        cur.next = right
                        cur = right
                    right = right.next

            if left:
                if new_head is None:
                    new_head = cur = left
                else:
                    cur.next = left

            if right:
                if new_head is None:
                    new_head = cur = right
                else:
                    cur.next = right

            return new_head

        return mergeSort(head)


