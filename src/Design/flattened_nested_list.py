# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    """
    This creates new Data structure
    Time complexity : O(N+L) N total number of integers , L total number of lists
    O(N+D) space complexity: D is the depth and N is the number of interester
    """
    """
    def __init__(self, nestedList: [NestedInteger]):
        self._list = [] # 
        
        def flatten_list(nl):
            for n in nl:
                if n.isInteger():
                    self._list.append(n.getInteger())
                else:
                    flatten_list(n.getList())
                    
        flatten_list(nestedList)
        self._cur = -1
        
    
    def next(self) -> int:
        return self._list[self._cur]  # O(1)
        
    
    def hasNext(self) -> bool:
        self._cur +=1
        if self._cur<len(self._list): # O(1)
            return True
        return False
    """

    """
    Time complexity.

Constructor: O(N + L)O(N+L).

The worst-case occurs when the initial input nestedList consists entirely of integers and empty lists (everything is in the top-level). In this case, every item is reversed and stored, giving a total time complexity of O(N + L)O(N+L).

makeStackTopAnInteger(): O(\dfrac{L}{N})O( 
N
L
​
 ) or O(1)O(1).

If the top of the stack is an integer, then this function does nothing; taking O(1)O(1) time.

Otherwise, it needs to process the stack until an integer is on top. The best way of analyzing the time complexity is to look at the total cost across all calls to makeStackTopAnInteger() and then divide by the number of calls made. Once the iterator is exhausted makeStackTopAnInteger() must have seen every integer at least once, costing O(N)O(N) time. Additionally, it has seen every list (except the first) on the stack at least once also, so this costs O(L)O(L) time. Adding these together, we get O(N + L)O(N+L) time.

The amortized time of a single makeStackTopAnInteger is the total cost, O(N + L)O(N+L), divided by the number of times it's called. In order to get all integers, we need to have called it NN times. This gives us an amortized time complexity of \dfrac{O(N + L)}{N} = O(\dfrac{N}{N} + \dfrac{L}{N}) = O(\dfrac{L}{N}) 
N
O(N+L)
​
 =O( 
N
N
​
 + 
N
L
​
 )=O( 
N
L
​
 ).

next(): O(\dfrac{L}{N})O( 
N
L
​
 ) or O(1)O(1).

All of this method is O(1)O(1), except for possibly the call to makeStackTopAnInteger(), giving us a time complexity the same as makeStackTopAnInteger().

hasNext(): O(\dfrac{L}{N})O( 
N
L
​
 ) or O(1)O(1).

All of this method is O(1)O(1), except for possibly the call to makeStackTopAnInteger(), giving us a time complexity the same as makeStackTopAnInteger().

Space complexity : O(N + L)O(N+L).

In the worst case, where the top list contains NN integers, or LL empty lists, it will cost O(N + L)O(N+L) space. Other expensive cases occur when the nesting is very deep. However, it's useful to remember that D ≤ LD≤L (because each layer of nesting requires another list), and so we don't need to take this into account.
    
    """

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestList))

    def make_stack_top_an_integer(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))


    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.stack.pop().getInteger()


    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack)>0

##  https://leetcode.com/problems/flatten-nested-list-iterator/solution/ using generators
"""
class NestedIterator:

def __init__(self, nestedList: [NestedInteger]):
    # Get a generator object from the generator function, passing in
    # nestedList as the parameter.
    self._generator = self._int_generator(nestedList)
    # All values are placed here before being returned.
    self._peeked = None

# This is the generator function. It can be used to create generator
# objects.
def _int_generator(self, nested_list) -> "Generator[int]":
    # This code is the same as Approach 1. It's a recursive DFS.
    for nested in nested_list:
        if nested.isInteger():
            yield nested.getInteger()
        else:
            # We always use "yield from" on recursive generator calls.
            yield from self._int_generator(nested.getList())
    # Will automatically raise a StopIteration.

def next(self) -> int:
    # Check there are integers left, and if so, then this will
    # also put one into self._peeked.
    if not self.hasNext(): return None
    # Return the value of self._peeked, also clearing it.
    next_integer, self._peeked = self._peeked, None
    return next_integer
    
def hasNext(self) -> bool:
    if self._peeked is not None: return True
    try: # Get another integer out of the generator.
        self._peeked = next(self._generator)
        return True
    except: # The generator is finished so raised StopIteration.
        return False

"""

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())