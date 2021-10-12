import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        if num is None:
            return
        # we will have nearly balanced heaps, max_heap can be larger than min_heap
        # always first add element in max_heap
        heapq.heappush(self.max_heap, - num) # 1
        heapq.heappush(self.min_heap, -self.max_heap[0]) # 2
        heapq.heappop(self.max_heap) # 3

        # for first iteration
        if len(self.max_heap)<len(self.min_heap):
            heapq.heappush(self.max_heap, -self.min_heap[0]) # 4
            heapq.heappop(self.min_heap) # 5

    def findMedian(self) -> float:
        return -self.max_heap[0] if len(self.max_heap)>len(self.min_heap) \
                else (-self.max_heap[0]+self.min_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
nums = [-1,2,3,7,8,-9,-10]
for num in nums:
    obj.addNum(num)
    print(obj.findMedian())