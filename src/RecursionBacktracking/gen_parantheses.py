from typing import List

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Back tracking
        Time complexity and space  = O(2^2n)
        """
        ans = []

        def generate(A = [], ind=[0]):
            if len(A) == 2*n:
                if ind[0]==0:
                    ans.append("".join(A))
            else:
                A.append('(')
                ind[0] +=1
                generate(A, ind)
                A.pop()
                ind[0] -=1
                ind[0] -=1
                if ind[0]<0:
                    ind[0] +=1
                    return
                A.append(')')
                generate(A, ind)
                A.pop()
                ind[0] +=1

        """
        def valid(s: List[str])->bool:
            # O(n)
            bal = 0
            for c in s:
                bal += 1 if c=="(" else -1
                if bal < 0 :
                    return False

            return True if bal==0 else False

        """
        generate()

        return ans

s = Solution()
print(s.generateParenthesis(8))