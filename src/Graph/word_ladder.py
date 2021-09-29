from typing import List
from collections import defaultdict
import collections

class Solution:
    """
        A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



    Example 1:

    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time Complexity: O({M}^2 \times N)O(M
2
 ×N), where MM is the length of each word and NN is the total number of words in the input word list.

For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it. Since the length of each word is MM and we have NN words, the total number of iterations the algorithm takes to create all_combo_dict is M \times NM×N. Additionally, forming each of the intermediate word takes O(M)O(M) time because of the substring operation used to create the new string. This adds up to a complexity of O({M}^2 \times N)O(M
2
 ×N).

Breadth first search in the worst case might go to each of the NN words. For each word, we need to examine MM possible intermediate words/combinations. Notice, we have used the substring operation to find each of the combination. Thus, MM combinations take O({M} ^ 2)O(M
2
 ) time. As a result, the time complexity of BFS traversal would also be O({M}^2 \times N)O(M
2
 ×N).

Combining the above steps, the overall time complexity of this approach is O({M}^2 \times N)O(M
2
 ×N).

Space Complexity: O({M}^2 \times N)O(M
2
 ×N).

Each word in the word list would have MM intermediate combinations. To create the all_combo_dict dictionary we save an intermediate word as the key and its corresponding original words as the value. Note, for each of MM intermediate words we save the original word of length MM. This simply means, for every word we would need a space of {M}^2M
2
  to save all the transformations corresponding to it. Thus, all_combo_dict would need a total space of O({M}^2 \times N)O(M
2
 ×N).
Visited dictionary would need a space of O(M \times N)O(M×N) as each word is of length MM.
Queue for BFS in worst case would need a space for all O(N)O(N) words and this would also result in a space complexity of O(M \times N)O(M×N).
Combining the above steps, the overall space complexity is O({M}^2 \times N)O(M
2
 ×N) + O(M * N)O(M∗N) + O(M * N)O(M∗N) = O({M}^2 \times N)O(M
2
 ×N) space.
        """
        """
        Start from beginWord and search the endWord using BFS.

    Algorithm

    Do the pre-processing on the given wordList and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.

    Push a tuple containing the beginWord and 1 in a queue. The 1 represents the level number of a node. We have to return the level of the endNode as that would represent the shortest sequence/distance from the beginWord.

    To prevent cycles, use a visited dictionary.

    While the queue has elements, get the front element of the queue. Let's call this word as current_word.

    Find all the generic transformations of the current_word and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the all_combo_dict.

    The list of words we get from all_combo_dict are all the words which have a common intermediate state with the current_word. These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.

    Hence, for each word in this list of intermediate words, append (word, level + 1) into the queue where level is the level for the current_word.

    Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.
        """


        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*" + word[i+1:]].append(word)

        # BFS to find shortest path
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord : True}

        while queue: # N
            current_word, level = queue.popleft()
            for i in range(L): # M
                intermediate_word = current_word[:i]+"*" + current_word[i+1:]

                for word in all_combo_dict[intermediate_word]: #M
                    if word == endWord:
                        return level+1

                    # add it queue
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                all_combo_dict[intermediate_word] = []
        return 0



s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(s.ladderLength(beginWord, endWord, wordList))
