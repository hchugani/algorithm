class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        O(MN) : Time
        O(M+N) : Space
        """
        if num1 == "0" or num2 == "0":
            return "0"

        N = len(num1)+len(num2)
        ans = [0]*N

        first = num1[::-1]
        second = num2[::-1]

        for place1, digit1 in enumerate(first):
            for place2, digit2 in enumerate(second):

                pos = place1+place2

                carry = ans[pos]
                val = carry + int(digit1) * int(digit2)
                ans[pos] = val % 10

                ans[pos+1] += val//10

        while ans[-1]==0:
            ans.pop()

        return ''.join(str(digit) for digit in reversed(ans))

s = Solution()
print(s.multiply("123","456"))