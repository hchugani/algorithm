from typing import List


class Solution:
    """
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.



    Example 1:

    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Time complexity : O(N), Greedy
        """
        count = 0
        i = 0
        while i < len(flowerbed):
            if (flowerbed[i]==0 and
                    (i==0 or flowerbed[i-1]==0) and
                    (i==(len(flowerbed)-1) or flowerbed[i+1]==0)):
                flowerbed[i]=1
                count +=1
            i+=1

        return count>=n

s = Solution()
array = [1, 0, 0, 0,1]
print(s.canPlaceFlowers(array, 1))
print(s.canPlaceFlowers(array, 2))