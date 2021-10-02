"""
244. Shortest Word Distance II
Medium

Share
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.


Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

"""

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        :param word1:
        :param word2:
        :return:
        """
        word_arr1 = []
        word_arr2 = []

        def two_pointers(word1, word2)->int:
            # word1 and word2 contains sorted indexes , use two pointers.
            M = len(word1)
            N = len(word2)

            i = j = 0
            mini = len(self.wordsDict)

            while i < M and j< N:
                mini = min(mini, abs(word1[i]-word2[j]))
                if word1[i]<word2[j]:
                    i+=1
                else:
                    j+=1

            while j<N :
                mini = min(mini, abs(word1[i-1]-word2[j]))
                j+=1

            while i < M:
                mini = min(mini, abs(word1[i]-word2[j-1]))
                i+=1
            return mini

        for i, word in enumerate(self.wordsDict):
            if word == word1:
                word_arr1.append(i)
            elif word==word2:
                word_arr2.append(i)

        return two_pointers(word_arr1, word_arr2)



        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(wordsDict)
        # param_1 = obj.shortest(word1,word2)