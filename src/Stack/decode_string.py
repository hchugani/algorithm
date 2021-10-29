"""
394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are
well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are
 only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

"""

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Time Complexity: O(maxK⋅n), where \text{maxK}maxK is the maximum value of kk and nn is the length of a given string ss. We traverse a string of size nn and iterate kk times to decode each pattern of form \text{k[string]}k[string]. This gives us worst case time complexity as \mathcal{O}(\text{maxK} \cdot n)O(maxK⋅n).

Space Complexity: O(m+n), where mm is the number of letters(a-z) and nn is the number of digits(0-9) in string ss. In worst case, the maximum size of \text{stringStack}stringStack and \text{countStack}countStack could be mm and nn respectively.
        """
        def decode(s):
            count = 0
            stack = []
            for i in range(len(s)): # O(N)
                if s[i]=="]":
                    temp = []
                    while stack and stack[-1] != "[":
                        temp.append(stack.pop())
                    stack.pop()
                    num = []
                    while stack and stack[-1].isdigit():
                        num.append(stack.pop())
                    stack.append("".join((["".join(reversed(temp))] * int("".join(reversed(num)))))) # MaxK
                else:
                    stack.append(s[i])

            return "".join(stack)

        return decode(s)


s =Solution()
inputs = [
    "2[abc]3[cd]ef",
    "3[a2[c]]",
    "3[a]2[bc]",
    "abc3[cd]xyz",
]

for inp in inputs:
    print(s.decodeString(inp))