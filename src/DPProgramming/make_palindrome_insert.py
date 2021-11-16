from functools import lru_cache

class Solution:
    def minInsertions(self, s: str) -> int:
        """
        O(n^2)
        """

        @lru_cache(maxsize=None)
        def getMin(l,r):
            if l>=r:
                return 0

            if s[l]==s[r]:
                return getMin(l+1,r-1)
            else:
                return 1 + min(getMin(l+1,r), getMin(l,r-1))

        return getMin(0, len(s)-1)


s = Solution()

inputs = [
    "zzazz", "mdabm","no","g"
]

for s1 in inputs:
    print(s.minInsertions(s1))