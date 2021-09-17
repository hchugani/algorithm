"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    """
    Time complexity : O(N)
    Space complexity : O(N)
    """
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        global maxi
        maxi = 0
        def max_depth(nestedList, depth=1)->int:
            global maxi
            maxi = max(maxi, depth)
            for nested in nestedList:
                if nested.getList():
                    max_depth(nested.getList(), depth+1)
        max_depth(nestedList)

        def dfs(nestedList, depth=1)->int:
            global maxi
            total = 0
            for nested in nestedList:
                if nested.getInteger():
                    total += nested.getInteger() * ( maxi-depth+1)
                else:
                    total+= dfs(nested.getList(), depth+1)
            return total

        return dfs(nestedList)





