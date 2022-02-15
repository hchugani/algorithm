from typing import List
from functools import lru_cache


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        O(L.L.N):
        O(N): Space
        """

        wordSet = set()
        for word in words:
            wordSet.add(word)

        @lru_cache(maxsize=None)
        def dfs(word)->int:

            max_len = 1
            for i, c in enumerate(word):
                s = word[0:i] + word[i+1:]
                if s in wordSet:
                    max_len = max(max_len,1+dfs(s))

            return max_len

        ans = 0
        for w in words:
            ans = max(ans,dfs(w))

        return ans

s = Solution()
print(s.longestStrChain(["bdca","bda","ca","dca","a"]))
