"""
269. Alien Dictionary
Hard


There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted
lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the
 new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes
 before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is
 smaller if and only if s.length < t.length.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
"""
from typing import List
from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Time complexity : O(C)
        Space complexity : O(1) or O(U+min(U
2
 ,N)).

The adjacency list uses the most auxiliary memory. This list uses O(V + E)O(V+E) memory, where VV is the number of unique letters, and EE is the number of relations.
        Let C be the total length of all the words in the input list, added together.

        In the worst case, the first and second parts require checking every letter of every word (if the difference between two words was always in the last letter). This is O(C)O(C).

        """

        graph  = {}
        for word in words:
            for c in word:
                graph[c] = set()


        for first, second in zip(words, words[1:]):
            for c,d in zip(first, second):
                if c !=d:
                    graph[c].add(d)
                    break
            else:
                if len(second)<len(first):
                    return ""

        visited  = {}
        checked = {}
        for word in words:
            for c in word:
                visited[c] = False
                checked[c] = False

        output = deque([])

        def topological_dfs(node):
            if checked[node]:
                return True

            # cycle detection
            if visited[node]:
                return False

            visited[node] = True

            ret = True
            for i in graph[node]:
                ret = topological_dfs(i)
                if not ret:
                    break

            visited[node] = False
            checked[node] = True
            output.appendleft(node)
            return ret

        for key in graph.keys():
            if not topological_dfs(key):
                return ""

        return "".join(output)

s = Solution()
inputs = [
    ["wrt","wrf","er","ett","rftt"],
    ["z","x","z"],
    ["z","x"]
]

for words in inputs:
    print(s.alienOrder(words))

