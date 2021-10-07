from collections import OrderedDict

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()


    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]


    def put(self, key: int, value: int) -> None:

        self.dict[key] = value
        self.dict.move_to_end(key)

        if len(self.dict)>self.capacity:
            self.dict.popitem(last=False) # remove from front

        def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()
    """

    def __init__(self, capacity: int):
        """
        Time complexity : O(1) both for put and get.

    Space complexity : O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.
        """
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next , self.tail.prev = self.tail, self.head
        self.cache = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # remove node
        self._remove_node(node)
        # move to front
        self._add_to_front(node)

        return node.val

    def _add_to_front(self, node):
        node.next ,node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node

    def _remove_node(self, node):
        #node.next.prev, node.prev.next = node.prev, node.next
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # remove node
            self._remove_node(node)
            # move to front
            self._add_to_front(node)

        else:
            # add new
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)
            self.size +=1
            if self.size>self.capacity:
                # delete LRU , last node
                node = self.tail.prev
                self._remove_node(node)
                node.next = node.prev = None
                del self.cache[node.key]
                self.size -= 1







                # Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
print(obj.get(1))
obj.put(1,0)
print(obj.get(1))
obj.put(4,2)
print(obj.get(1))
obj.put(3,2)
print(obj.get(1))
obj.put(5,2)