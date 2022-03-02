"""
815. Bus Routes
Hard


You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 ->
5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target.
You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Our (breadth-first) search is on NN nodes, and each node could have NN edges, so it is O(N^2)
        bouth
        :param routes:
        :param source:
        :param target:
        :return:
        """
        if source==target:
            return 0

        self.graph = defaultdict(set)
        # buses as nodes
        routes = map(set, routes)
        routes = list(routes)

        for i, route in enumerate(routes):
            for j in range(i+1, len(routes)):
                routey = routes[j]
                for stop1 in route:
                    if stop1 in routey:
                        self.graph[i].add(j)
                        self.graph[j].add(i)

        seen , targets = set(), set()

        for i, route in enumerate(routes):
            if source in route:
                seen.add(i)
            if target in route:
                targets.add(i)

        queue = deque([(node,1) for node in seen])

        while queue:
            node, depth = queue.popleft()
            if node in targets:
                return depth
            for nei in self.graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

s = Solution()
print(s.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))