"""
123. Best Time to Buy and Sell Stock III
Hard


You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions
at the same time. You must sell before buying again.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        O(N) : Both
        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0

        N = len(prices)
        left_profit=[0]*N
        right_profit = [0]*(N+1)


        left_min = prices[0]
        right_max = prices[-1]

        for i in range(1, N):
            left_profit[i] = max(left_profit[i-1], prices[i]-left_min)
            left_min = min(left_min, prices[i])

            r = N-1-i
            right_profit[r] = max(right_profit[r+1], right_max-prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(N):
            max_profit = max(max_profit,left_profit[i]+right_profit[i+1])

        return max_profit

s = Solution()
inputs = [
    [3,3,5,0,0,3,1,4],
    [1,2,3,4,5]
]

for arr in inputs:
    print(s.maxProfit(arr))