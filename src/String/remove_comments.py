"""
722. Remove Comments
Medium

526

1413

Add to List

Share
Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the
ith line of the source code. This represents the result of splitting the original source code string by the newline
character '\n'.

In C++, there are two types of comments, line comments, and block comments.

The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in
the same line should be ignored.
The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping)
 occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.)
 To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
The first effective comment takes precedence over others.

For example, if the string "//" occurs in a block comment, it is ignored.
Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer
list will be non-empty.

There will be no control characters, single quote, or double quote characters.

For example, source = "string s = "/* Not a comment. */";" will not be a test case.
Also, nothing else such as defines or macros will interfere with the comments.

It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment
 always starts a new comment.

"""

from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        """
        O(MN) : time
        """
        result = []

        inblock = False

        for line in source:
            if not inblock:
                result.append([])

            i = 0
            while i < len(line):
                if not inblock:
                    if line[i]=="/" and i+1<len(line) and line[i+1] in "/*":
                        if line[i+1]=="/":
                            break
                        inblock = True
                        i+=1
                    else:
                        result[-1].append(line[i])
                else:
                    if line[i]=="*" and i+1<len(line) and line[i+1] in "/":
                        inblock = False
                        i+=1
                i+=1

        return ["".join(line) for line in result if line]

s = Solution()
inputs = [
    ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
     "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
]

for lines in inputs:
    print(s.removeComments(lines))