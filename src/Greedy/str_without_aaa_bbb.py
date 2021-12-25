"""
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.


Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"

"""

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        """
        O(a+b) : time
        O(1) : space
        """
        s = ""
        while (a+b) != 0:
            val = 0
            c = ""
            if a > b:
                val = a
                c = "a"
            else:
                val = b
                c = "b"

            if len(s)>=2:
                if s[-1]==c and s[-2]==c:
                    if c=="b":
                        if a>0:
                            s+="a"
                            a-=1
                    else:
                        if b>0:
                            s+="b"
                            b-=1
                else:
                    s+=c
                    if c=="a":
                        a-=1
                    else:
                        b-=1
            else:
                s+=c
                if c=="a":
                    a-=1
                else:
                    b-=1

        return s

s = Solution()
inputs = [
    (1,1),(4,1), (1,0)
]

for a, b in inputs:
    print(s.strWithout3a3b(a, b))