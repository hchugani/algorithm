class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            "}" : "{", "]" : "[", ")": "("
        }

        for i in range(len(s)):
            if s[i] in ["(", "{", "[" ]:
                stack.append(s[i])
            elif s[i] in ["}", ")", "]"]:
                if len(stack)==0:
                    return False
                if stack[-1] == mapper[s[i]]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True

s = Solution()
inputs = [
    "()",
    "()[]{}",
    "(]",
    "{[]}",
    "([)]",
    "]"
]
for input in inputs:
    print(s.isValid(input))