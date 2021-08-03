
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        # Append at the end
        while last.next:
            last = last.next
        last.next = new_node

    def print_ll(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def reverse_k_groups(self, head: Node, k: int)-> Node:
        """
        time complexity: O(n)
        space complexity : O
        :param head:
        :param k:
        :return:
        """
        if head is None:
            return None
        cur = head
        # check if it has k nodes to reverse
        i = 0
        while cur is not None and i < k:
            cur = cur.next
            i+=1

        if i==k:
            prev = None
            cur = head
            next = None
            j = k
            while cur is not None and j>0:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                j-=1
            #next will k+1 which has to be reversed
            head.next = self.reverse_k_groups(next, k)
            return prev
        else:
             return head


if __name__== "__main__":
    ll = LinkedList()
    for i in range(1, 7):
        ll.append(i)
    #ll.print_ll()
    ll.head = ll.reverse_k_groups(ll.head,4)
    ll.print_ll()





