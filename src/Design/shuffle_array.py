from typing import List
import random
"""

"""

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.orig = list(nums) # deep copy

        """"
        def permute(inp, temp=[]):
            if len(temp) == len(nums):
                self.result.append(list(temp))
                return
            
            for k in range(len(inp)):
                temp.append(inp[k])
                permute(inp[0:k]+inp[k+1:], temp)
                temp.pop()
        permute(nums)
        """

    def reset(self) -> List[int]:
        """
        O(1)
        :return:
        """
        self.array = self.orig
        self.orig = list(self.orig)
        return self.array


    def shuffle(self) -> List[int]:
        """
        O(n) both

        :return:
        """
        aux = list(self.array)
        n = len(aux)-1
        for idx in range(len(self.array)):
            ind = random.randint(0, n)
            self.array[idx] = aux[ind]
            # swap current with last one - makes it O(n) instead of O(n2)
            aux[ind], aux[n] = aux[n], aux[ind]
            n-=1


        return self.array


nums = [1,2,3]
obj = Solution(nums)
print(obj.reset())
for _ in range(9):
    print(obj.shuffle())