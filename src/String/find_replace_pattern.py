from typing import List
"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matche
"""
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        O(M.K) : m is number of words, k is len of each word
        """
        result = []
        for string in words:
            mapper = {}
            reverse_mapper = {}
            if len(string)!=len(pattern):
                continue
            matched = True
            for i in range(len(string)):
                if pattern[i] not in reverse_mapper:
                    reverse_mapper[pattern[i]] = string[i]
                if string[i] not in mapper:
                    mapper[string[i]] = pattern[i]
                if (mapper[string[i]], reverse_mapper[pattern[i]]) != (pattern[i],string[i]):
                    matched = False
                    break
            if matched:
                result.append(string)


        return result
                        
                           
s = Solution()
inputs = [(["abc","deq","mee","aqq","dkd","ccc"], "abb"),
          (["a","b","c"], "a")
]

for words, pattern in inputs:
    print(s.findAndReplacePattern(words, pattern))