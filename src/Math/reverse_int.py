"""
7. Reverse Integer
Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        """

        O(logx) : Time stamp
        :param x:
        :return:
        """
        res = 0
        factor = 10
        sign = -1 if x < 0 else 1
        x = sign * x

        while x:
            rem = x % 10
            x = x // 10
            res = res * factor + rem

        res = sign * res
        if sign==1:
            if res > (pow(2,31)-1):
                return 0
        else:
            if res < -pow(2,31):
                return 0

        return res