import sys

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mini = min(val, self.stack[-1][1] if self.stack else sys.maxsize)
        self.stack.append((val, mini))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]


    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]



            # Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
obj.pop()
obj.push(-2)
obj.push(-3)
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)