from typing import List
"""
longest chain of pairs such that [a,b]  [c,d] c>b,
doesnt have to be continuos

"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        O(nlogn)
        with o(1) space

        :param pairs:
        :return:
        """

        pairs = sorted(pairs, key=lambda x : x[0])

        longest = 1
        prev = pairs[0]
        for i in range(1, len(pairs)):
            if pairs[i][0]>prev[1]:
                longest+=1
                prev = pairs[i]
            if pairs[i][0]<prev[1]:
                # replace the last one with this new pair and this fits
                # in the increasing pair
                prev = pairs[i]


        return longest

s = Solution()
inputs = [
    [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]],
    [[1,2],[7,8],[4,5]],
    [[1,2],[2,3],[3,4]],
]

for inp in inputs:
    print(s.findLongestChain(inp))