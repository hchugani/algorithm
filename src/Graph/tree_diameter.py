from typing import List
from collections import defaultdict


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.diameter = 0

        self.graph = defaultdict(list)
        for x, y in edges:
            self.graph[x].append(y)
            self.graph[y].append(x)

        visited = set()

        def dfs(cur, visited)->int:
            visited.add(cur)
            top_dist_1, top_dist_2 = 0, 0
            distance = 0

            for edge in self.graph[cur]:
                if edge not in visited:
                    distance = 1 + dfs(edge, visited)

                    if distance > top_dist_1:
                        top_dist_1, top_dist_2 = distance, top_dist_1
                    elif distance>top_dist_2:
                        top_dist_2 = distance

            distance = top_dist_1+top_dist_2
            self.diameter = max(self.diameter, distance)

            return top_dist_1

        dfs(0, visited)

        return self.diameter


s = Solution()
print(s.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))