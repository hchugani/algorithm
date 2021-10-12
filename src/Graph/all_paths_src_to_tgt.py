from typing import List

class Solution:
    """
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

    """


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        ime Complexity: \mathcal{O}(2^N \cdot N)O(2
N
 ⋅N)

As we calculate shortly before, there could be at most 2^{N-1} - 12
N−1
 −1 possible paths in the graph.

For each path, there could be at most N-2N−2 intermediate nodes, i.e. it takes \mathcal{O}(N)O(N) time to build a path.

To sum up, a loose upper-bound on the time complexity of the algorithm would be (2^{N-1} - 1) \cdot \mathcal{O}(N) = \mathcal{O}(2^N \cdot N)(2
N−1
 −1)⋅O(N)=O(2
N
 ⋅N), where we consider it takes \mathcal{O}(N)O(N) efforts to build each path.

It is a loose uppper bound, since we could have overlapping among the paths, therefore the efforts to build certain paths could benefit others.

Space Complexity: \mathcal{O}(2^N \cdot N)O(2
N
 ⋅N)

Similarly, since at most we could have 2^{N-1}-12
N−1
 −1 paths as the results and each path can contain up to NN nodes, the space we need to store the results would be \mathcal{O}(2^N \cdot N)O(2
N
 ⋅N).

Since we also applied recursion in the algorithm, the recursion could incur additional memory consumption in the function call stack. The stack can grow up to NN consecutive calls. Meanwhile, along with the recursive call, we also keep the state of the current path, which could take another \mathcal{O}(N)O(N) space. Therefore, in total, the recursion would require additional \mathcal{O}(N)O(N) space.

To sum up, the space complexity of the algorithm is \mathcal{O}(2^N \cdot N) + \mathcal{O}(N) = \mathcal{O}(2^N \cdot N)O(2
N
 ⋅N)+O(N)=O(2
N
 ⋅N).
        """
        result = []
        N = len(graph)

        def dfs(i, tmp):
            if i==N-1:
                result.append(list(tmp))
                return

            for j in graph[i]:
                tmp.append(j)
                dfs(j, tmp)
                tmp.pop()

        path=[0]
        dfs(0, path)
        return result

s =Solution()
graph = [ [1,2],[3],[3],[]]
print(s.allPathsSourceTarget(graph))