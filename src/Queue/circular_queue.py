class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:
    """
    Time : O(1)
    Space : O(N)
    """

    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.tail = None
        self.count = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        if self.head is None:
            node.next = node
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.count +=1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.tail.next = self.head
        self.count -=1
        if self.count==0:
            self.head = self.tail = None
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.val


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val


    def isEmpty(self) -> bool:
        if self.count==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(6)
param_1 = obj.enQueue(8)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()