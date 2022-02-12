"""
227. Basic Calculator II
Medium

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range
of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

"""

class Solution:
    def calculate(self, s: str) -> int:
        """
        O(n) : both

        22-5*3
        *, / high precidence, others low
        so when we encounter - or + , we hold the compuatation for later


        """
        operation = "+"
        cur_num = 0
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                cur_num = cur_num*10+int(c)
            if (not c.isdigit() and not c.isspace()) or i==len(s)-1:
                if operation == "+":
                    stack.append(cur_num)
                elif operation == "-":
                    stack.append(-cur_num)
                elif operation == '*':
                    stack.append(stack.pop()*cur_num)
                elif operation =="/":
                    stack.append(int(stack.pop()/cur_num))
                operation = c
                cur_num = 0

        res = 0
        while stack:
            res+=stack.pop()

        return res


s = Solution()
print(s.calculate("22-3*5"))
print(s.calculate(" 3/2 "))