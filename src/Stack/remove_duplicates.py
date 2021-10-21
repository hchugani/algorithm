"""
1209. Remove All Adjacent Duplicates in String II
Medium

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and
 equal letters from s and removing them, causing the left and the right side of the deleted substring to
 concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer
is unique.

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        O(n) both space and time
        """
        stack = []

        for c in s:
            if stack and stack[-1][0]==c:
                count = stack.pop()[1]
                stack.append((c, count+1))
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append((c, 1))

        ret = ""
        for c,freq in stack:
            ret += c*freq

        return ret

s = Solution()
print(s.removeDuplicates("deeedbbcccbdaa",3))