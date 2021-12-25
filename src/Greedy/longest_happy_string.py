"""
1405. Longest Happy String
Medium

A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy
strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

"""

import heapq

class Node:
    def __init__(self, c, count):
        self.c = c
        self.count = count

    def __lt__(self, node):
        if self.count < node.count:
            return False
        else:
            return True

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            node_a = Node("a", a)
            heapq.heappush(heap, node_a)
        if b:
            node_b = Node("b", b)
            heapq.heappush(heap, node_b)
        if c:
            node_c = Node("c", c)
            heapq.heappush(heap, node_c)
        output = []

        first = second = None
        while heap:
            first = heapq.heappop(heap)
            if len(output)>=2:
                if output[-1]==first.c and output[-2]==first.c :
                    if heap:
                        second = heapq.heappop(heap)
                        heapq.heappush(heap, first)
                        output.append(second.c)
                        if second.count>1:
                            second.count -=1
                            heapq.heappush(heap, second)
                else:
                    output.append(first.c)
                    if first.count>1:
                        first.count -=1
                        heapq.heappush(heap, first)
            else:
                output.append(first.c)
                if first.count>1:
                    first.count -=1
                    heapq.heappush(heap, first)

        return "".join(output)


        return output

s = Solution()
inputs = [
    (1,1,7),
    (0,8,11)
]

for a, b, c in inputs:
    print(s.longestDiverseString(a,b,c))
