class Solution:
    """
    Let's go back to the interview context. For x \ge 2x≥2 the square root is always smaller than x / 2x/2 and larger than 0 : 0 < a < x / 20<a<x/2.
    Since aa is an integer, the problem goes down to the iteration over the sorted set of integer numbers. Here the binary search enters the scene

    Algorithm

    If x < 2, return x.

    Set the left boundary to 2, and the right boundary to x / 2.

    While left <= right:

    Take num = (left + right) / 2 as a guess. Compute num * num and compare it with x:

    If num * num > x, move the right boundary right = pivot -1

    Else, if num * num < x, move the left boundary left = pivot + 1

    Otherwise num * num == x, the integer square root is here, let's return it

    Return right
    """
    def mySqrt(self, x: int) -> int:
        """
        Time complexity : O(log N)
        """
        if x<2:
            return x

        left, right = 2, x//2

        while left<=right:
            pivot = left + (right-left)//2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right

s= Solution()
print(s.mySqrt(10))