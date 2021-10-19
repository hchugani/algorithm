import sys
from typing import List

"""
121. Best Time to Buy and Sell Stock
Easy


You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different
 day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        O(n): time complexity
        o(1) : space
        :param prices:
        :return:
        """
        mini = sys.maxsize
        maxi = -sys.maxsize

        profit = 0

        for i in range(len(prices)):
            if maxi < prices[i]:
                maxi = prices[i]
            if mini > prices[i]:
                mini = prices[i]
                # reset maxi
                maxi = -sys.maxsize

            if maxi != -sys.maxsize:
                profit = max(profit, maxi-mini)

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