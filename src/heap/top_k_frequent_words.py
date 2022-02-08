
import heapq
from typing import List

class Word:

    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other)->bool:
        if self.count != other.count:
            return self.count<other.count
        else:
            return self.word>other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        O(n log(k)) time and O(n) extra space
        """
        counter = {}

        for word in words:
            if word not in counter:
                counter[word] = 0
            counter[word] +=1

        #return heapq.nlargest(k, sorted(counter.keys()), key=counter.get)

        min_heap = []

        for key in counter.keys():
            heapq.heappush(min_heap, Word(key, counter[key]))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        min_heap.sort()
        return reversed([word.word for word in min_heap])


s = Solution()
inputs = [
    (["i","love","leetcode","i","love","coding"],2),
    (["i","love","leetcode","i","love","coding"],3)
]

for words, k in inputs:
    print(s.topKFrequent(words,k))