import sys

class BucketNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.data_set = set()

class AllOne:
    """
    inc, dec - need Dictionary/Map for O(1)
    getMaxKey, getMinKey - use linkedlist

    """
    def __init__(self):
        self.head = BucketNode(-sys.maxsize)
        self.tail = BucketNode(sys.maxsize)
        self.key_value_map = {}
        self.value_to_bucket_map = {}
        self.head.next , self.tail.prev = self.tail, self.head


    def insertAFterNode(self,node, new_bucket):
        next_node = node.next
        node.next, new_bucket.prev = new_bucket, node
        next_node.prev, new_bucket.next = new_bucket, next_node
        return new_bucket


    def inc(self, key: str) -> None:
        if key in self.key_value_map:
            self.changeVal(key, 1)
        else:
            if self.head.next.val != 1:
                new_bucket = self.insertAFterNode(self.head, BucketNode(1))

            self.head.next.data_set.add(key)
            self.key_value_map[key] = 1
            self.value_to_bucket_map[1] = self.head.next

    def removeKeyFromBucketDatalist(self, bucket, key):
        bucket.data_set.remove(key)
        if len(bucket.data_set)==0:
            bucket.prev.next, bucket.next.prev = bucket.next, bucket.prev
            bucket.next, bucket.prev = None, None
            del self.value_to_bucket_map[bucket.val]

    def changeVal(self, key, offset):
        cur_val = self.key_value_map[key]
        curBucket = self.value_to_bucket_map[cur_val]

        if (cur_val+offset) not in self.value_to_bucket_map:
            new_bucket = BucketNode(cur_val+offset)
            self.insertAFterNode(curBucket, new_bucket)
            self.value_to_bucket_map[cur_val+offset] = new_bucket
        else:
            new_bucket = self.value_to_bucket_map[cur_val+offset]

        new_bucket.data_set.add(key)

        self.key_value_map[key] = cur_val+offset
        # remove
        self.removeKeyFromBucketDatalist(curBucket, key)



    def dec(self, key: str) -> None:
        if key not in self.key_value_map:
            return
        if self.key_value_map[key]==1:
            del self.key_value_map[key]
            curBucket = self.value_to_bucket_map[1]
            self.removeKeyFromBucketDatalist(curBucket, key)
        else:
            self.changeVal(key, -1)


    def getMaxKey(self)-> str:
        if self.tail.prev == self.head:
            return ""
        bucket_node = self.tail.prev
        ret = bucket_node.data_set.pop()
        bucket_node.data_set.add(ret)
        return ret

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        bucket_node = self.head.next
        ret = bucket_node.data_set.pop()
        bucket_node.data_set.add(ret)
        return ret



# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.dec("hello")
obj.inc("hello")
obj.inc("hello")
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc("test")
print(obj.getMaxKey())
print(obj.getMinKey())