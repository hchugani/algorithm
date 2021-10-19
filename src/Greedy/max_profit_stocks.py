from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        O(n) : time
        O(1) : space
        :param prices:
        :return:
        """

        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit+= prices[i]-prices[i-1]
        return profit

s = Solution()
inputs = [
    [7,1,5,3,6,4],
    [1,2,3,4,5],
    [7,6,4,3,1],
    [9]
]

for i in inputs:
    print(s.maxProfit(i))