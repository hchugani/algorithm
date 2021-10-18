from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        O(NKlogK) time
        O(NK)
        """
        """
        mapper = defaultdict(list)
        for s in strs:
            mapper[tuple(sorted(s))].append(s)
        
        return [ mapper[key] for key in mapper]
        """
        """
        O(NK): time
        O(NK) : space
        """
        ans = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1
            ans[tuple(count)].append(s)

        return ans.values()

inputs = [
    ["eat","tea","tan","ate","nat","bat"],
    [""]
]
s = Solution()
for inp in inputs:
    print(s.groupAnagrams(inp))