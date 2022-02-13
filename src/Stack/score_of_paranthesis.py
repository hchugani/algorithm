"""
856. Score of Parentheses
Medium

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2

"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        O(N) :Time
        O(1) : Space
        """
        ans = bal = 0
        for i,c in enumerate(s):
            if c=="(":
                bal+=1
            else:
                bal-=1
                if s[i-1]=='(':
                    ans+=2**bal

        return ans


s = Solution()
print(s.scoreOfParentheses("(((())))"))