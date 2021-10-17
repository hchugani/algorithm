from typing import List
"""
739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer
 such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
 If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        O(N) both

        Time complexity: O(N)O(N)

        At first glance, it may look like the time complexity of this algorithm should be O(N^2)O(N
        2
         ), because there is a nested while loop inside the for loop. However, each element can only be added to the stack once, which means the stack is limited to NN pops. Every iteration of the while loop uses 1 pop, which means the while loop will not iterate more than NN times in total, across all iterations of the for loop.

        An easier way to think about this is that in the worst case, every element will be pushed and popped once. This gives a time complexity of O(2 \cdot N) = O(N)O(2⋅N)=O(N).

        Space complexity: O(N)O(N)

        If the input was non-increasing, then no element would ever be popped from the stack, and the stack would grow to a size of N elements at the end.

        Note: answer does not count towards the space complexity because space used for the output format does not count.
        """
        result = [0] * len(temperatures)
        stack = [] # monotonically decreasing stack

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                ind = stack.pop()
                result[ind] = i-ind
            stack.append(i)

        return result

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))