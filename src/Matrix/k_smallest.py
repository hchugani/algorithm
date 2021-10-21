import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        if k > n*n:
            return

        for i in range(n):
            heapq.heappush(min_heap,(matrix[i][0], 0, i))

        i = k
        while min_heap:
            val, num, ind = heapq.heappop(min_heap)
            i-=1
            if i==0:
                return val
            if num+1<n:
                heapq.heappush(min_heap, (matrix[ind][num+1], num+1, ind))


s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))



