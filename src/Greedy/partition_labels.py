from typing import List


class Solution:
    """
    You are given a string s. We want to partition the string into as many parts as possible so that
     each letter appears in at most one part.

    Return a list of integers representing the size of these parts.


    Example 1:

    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

    """

    def partitionLabels(self, s: str) -> List[int]:
        """
        Time complexity : O(N)
        """
        result = []
        N = len(s)

        i = 0

        last_dict = {}

        while(i<N):
            last_dict[s[i]] = i
            i+=1

        i = 0
        prev = 0
        while i < N:
            last = last_dict[s[i]]

            while i <=last:
                last = max(last, last_dict[s[i]])
                i+=1
            result.append(last-prev+1)
            prev = last+1

        return result

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))