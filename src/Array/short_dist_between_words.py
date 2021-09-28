from typing import List


class Solution:
    """
    Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.



    Example 1:

    Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
    Output: 3

    """
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        O(N.M) - N passes , M for string comparison
        :param wordsDict:
        :param word1:
        :param word2:
        :return:
        """
        i1 = i2 = -1
        minDist = float("inf")
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i

            if i1 !=-1 and i2 !=-1:
                minDist = min(minDist, abs(i1-i2))

        return int(minDist)


sol = Solution()
inputs = [ (["practice", "makes", "perfect", "coding", "makes"],"coding", "practice")
           ]
for list,s1,s2 in inputs:
    print(sol.shortestDistance(list,s1,s2))