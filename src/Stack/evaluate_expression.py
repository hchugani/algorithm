from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time  and space: O(N)

        :param tokens:
        :return:
        """
        stack = []
        def add(a, b):
            return a + b

        def substract(a, b):
            return a-b

        def divide(a, b):
            return a/b

        def multiply(a, b):
            return a * b

        operators = {
            "+" : add,
            "-" : substract,
            "/" : divide,
            "*" : multiply
        }

        for token in tokens:
            if token in operators.keys():
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[token](int(operand1), int(operand2))
                stack.append(result)
            else:
                stack.append(token)

        return int(stack[0])

s  = Solution()

inputs = [
    ["2","1","+","3","*"],
    ["4","13","5","/","+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
]
for input in inputs:
    print(s.evalRPN(input))