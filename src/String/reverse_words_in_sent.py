"""
151. Reverse Words in a String
Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string
should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        O(N) : both
        first trim, remove unncessary spaces
        reverse sentence
        reverse words
        """

        def trim_spaces(s):
            i, j = 0, len(s)-1

            while s[i]==" ":
                i+=1
            while s[j]==" ":
                j-=1

            output = []
            while i<=j:
                if s[i]==" " and i-1>=0 and s[i-1] == " ":
                    i+=1
                    continue
                output.append(s[i])
                i+=1

            return output

        def reverse_word(s, i , j):
            while i<=j:
                s[i],s[j] = s[j],s[i]
                j-=1
                i+=1

        def reverse_each_word(s):
            i, j = 0, len(s)
            start = end = 0
            while start<j:
                while end<j and s[end] != " ":
                    end+=1
                reverse_word(s, start, end-1)
                start = end+1
                end+=1


        l = [""]*len(s)

        for i in range(len(s)):
            l[i]=s[i]

        l = trim_spaces(l)
        reverse_word(l, 0, len(l)-1)
        reverse_each_word(l)
        return "".join(l)

s = Solution()
strings = [
    " the  sky  is blue  ",
    "a good   example",
    "hello world"
]
for st in strings:
    print(s.reverseWords(st))