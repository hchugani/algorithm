from collections import defaultdict
from typing import List
from functools import lru_cache
"""
472. Concatenated Words
Hard


Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
"""

class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.eow = ""


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        O(m*n)
        :param words:
        :return:
        """

        trie = TrieNode()
        result = []

        for word in words:
            node = trie
            for s in word:
                node = node.children[s]
            node.eow = word

        @lru_cache(maxsize=None)
        def dfs(word):
            if word=="":
                return True
            res = False
            node = trie
            for i,s in enumerate(word):
                if s not in node.children:
                    break
                node = node.children[s]
                if node.eow!="":
                    res = res or dfs(word[i+1:])
                    if res:
                        break

            return res




        for word in words:
            node = trie
            for i,s in enumerate(word):
                node = node.children[s]
                if node.eow!="":
                    if i!=len(word)-1 and dfs(word[i+1:]):
                        result.append(word)
                        break

        return result
        """
        
        wordset = set(words)
        res = set()
        
        @lru_cache(maxsize=None)
        def dfs(word):
            result = 1
            for i in range(1, len(word)):
                if word[:i] in wordset:
                    result = max(result,1+dfs(word[i:]))
            return 0 if result==1 and word not in wordset else result
        
        for word in words:
            if  word not in res and dfs(word)>1:
                res.add(word)
        
        return list(res)
        """

s = Solution()
inputs = [
    ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
]
for words in inputs:
    print(s.findAllConcatenatedWordsInADict(words))