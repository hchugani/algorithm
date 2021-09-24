class Solution:
    """
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

    Example 1:

    Input: x = 2.00000, n = 10
    Output: 1024.00000
    Example 2:

    Input: x = 2.10000, n = 3
    Output: 9.26100
    Example 3:

    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

    """

    def fastPow(self, x: float, n:int)->float:
        n = int(n)
        if n==0:
            return 1

        half = self.fastPow(x, n/2)

        if (n%2==0):
            return half * half
        else:
            if n>0:
                return half * half * x
            else:
                return half * half/x


    def myPow(self, x: float, n: int) -> float:
        """
        if we have the result for x^n, to find x^(2*n)
        We dont have to multiply again n time simple x^n * X^n

        O(logn) : Time complexity
        O(logn) : Space complexity
        """
        return self.fastPow(x,n)


    def myPowN(self, x: float, n: int) -> float:
        """
        O(n) : Time complexity
        O(1) : Space complexity
        """
        res = 1
        if n<0:
            x = 1/x
            n = -n # can create overflow if n = -2 ^ 31
        while(n>0):
            res = res*x
            n = n-1

        return res

s = Solution()
print(s.myPow(2.0, 31))