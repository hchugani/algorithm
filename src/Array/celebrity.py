# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Time complexity : O(N) + O(N) for iscelebrity
        if knows is called repeated we can use lru_cache around, with extra O(N) space

        from functools import lru_cache

        @lru_cache(maxsize=NOne)
        def cachedKnows(self, a , b):
            self.knows(a, b)
        """
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.isCelebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def isCelebrity(self, i):
        for j in range(self.n):
            if i==j :
                continue
            if knows(i, j) or not knows(j, i):
                return False

        return True

    """
    #Time complexity : O(N*N)
    
    def findCelebrity(self, n: int) -> int:
        self.n = n
        for i in range(n):
            if self.isCelebrity(i):
                return i
        return -1
    
    def isCelebrity(self, i):
        for j in range(self.n):
            if i==j :
                continue
            if knows(i, j) or not knows(j, i):
                return False
        
        return True
    """