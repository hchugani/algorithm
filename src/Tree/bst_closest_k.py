# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq
from typing import Optional, List




class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
        O(NlogK) time complexity
        O(K) space complexity
        """
        self.min_heap = []


        def inOrder(node: TreeNode, target: int , k: int):
            if node:
                inOrder(node.left, target, k)
                diff = abs(target-node.val)
                if len(self.min_heap)>=k:
                    if -diff > self.min_heap[0][0]:
                        heapq.heappop(self.min_heap)
                        heapq.heappush(self.min_heap, (-diff, node.val))
                else:
                    heapq.heappush(self.min_heap, (-diff, node.val))
                inOrder(node.right, target, k)

        inOrder(root, target, k)
        return [val for dist,val in self.min_heap]


    def closestKValues1(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
        Using QuickSelect
        """
        self.arr = []
        def inOrder(node:TreeNode):
            if node:
                inOrder(node.left)
                self.arr.append(node.val)
                inOrder(node.right)

        def partition(l, r, pivot_ind):
            pivot = self.dist[pivot_ind]
            i =l
            j = r
            while i<j:

                while(i < len(self.dist) and self.dist[i]>=pivot ):
                    i+=1

                while(self.dist[j]<pivot):
                    j-=1

                if i<j:
                    # swap
                    self.dist[i], self.dist[j] = self.dist[j], self.dist[i]
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

            self.dist[j], self.dist[pivot_ind] = self.dist[pivot_ind], self.dist[j]
            self.arr[j], self.arr[pivot_ind] = self.arr[pivot_ind], self.arr[j]
            return j




        def quickSelct(left, right, kth_smallet):
            import random
            pivot = random.randint(left, right)
            ret_ind = partition(left, right, pivot)

            if ret_ind == kth_smallet:
                return
            elif kth_smallet < ret_ind:
                quickSelct(left, ret_ind-1, kth_smallet)
            else:
                quickSelct(ret_ind+1, right , kth_smallet)

        inOrder(root)
        self.dist = [ abs(x-target) for x in self.arr]
        quickSelct(0, len(self.dist)-1, len(self.dist)-k)

        return self.arr[len(self.dist)-k:]
