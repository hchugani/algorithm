class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:
    """
    Time Complexity: for each of the methods, the time complexity is \mathcal{O}(\frac{N}{K})O(
K
N
​
 ) where NN is the number of all possible keys and KK is the number of predefined buckets in the hashmap, which is 2069 in our case.

In the ideal case, the keys are evenly distributed in all buckets. As a result, on average, we could consider the size of the bucket is \frac{N}{K}
K
N
​
 .

Since in the worst case we need to iterate through a bucket to find the desire value, the time complexity of each method is \mathcal{O}(\frac{N}{K})O(
K
N
​
 ).

Space Complexity: \mathcal{O}(K+M)O(K+M) where KK is the number of predefined buckets in the hashmap and MM is the number of unique keys that have been inserted into the hashmap.
    """

    def hashkey(self, key)->int:
        return key%self.modulo

    def __init__(self):
        self.modulo = 10000
        self.hash = [[] for _ in range(self.modulo)]

    def put(self, key: int, value: int) -> None:
        address = self.hashkey(key)
        found_node = None
        for node in self.hash[address]:
            if node.key == key:
                found_node = node
        if found_node:
            found_node.val = value
        else:
            self.hash[address].append(Node(key, value))

    def get(self, key: int) -> int:
        address = self.hashkey(key)
        for node in self.hash[address]:
            if node.key == key:
                return node.val
        return -1

    def remove(self, key: int) -> None:
        address = self.hashkey(key)
        for index, node in enumerate(self.hash[address]):
            if node.key == key:
                del self.hash[address][index]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(3,4)
param_2 = obj.get(3)
print(param_2)
obj.remove(3)