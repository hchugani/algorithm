from collections import deque
import heapq
from typing import List
"""
675. Cut Off Trees for Golf Event
Hard


You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n 
matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the 
tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

 

Example 1:


Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
"""


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        O(MNlogMN + 3^MN)
        O(MN)
        """
        M = len(forest)
        N = len(forest[0])
        pq = []
        for i in range(M):
            for j in range(N):
                if forest[i][j]>1:
                    heapq.heappush(pq, (forest[i][j], i, j))


        def bfs(x, y, nextx, nexty):
            seen = set()
            queue = deque([(x,y,0)])
            seen.add((x,y))

            while queue:
                newx, newy, step = queue.popleft()

                if newx==nextx and newy==nexty:
                    forest[x][y]=1
                    return step

                for dx, dy in [(-1,0),(1,0),(0,-1), (0,1)]:
                    if 0<=newx+dx<M and 0<=newy+dy<N and \
                                    forest[newx+dx][newy+dy]>=1 and (newx+dx,newy+dy) not in seen:
                        queue.append((newx+dx, newy+dy, step+1))
                        seen.add((newx+dx, newy+dy))

            return -1

        x, y = 0, 0
        steps = 0

        while pq:
            _,nextx, nexty = heapq.heappop(pq)
            shortest = bfs(x,y, nextx, nexty)
            if shortest == -1:
                return -1
            steps += shortest
            x, y = nextx, nexty

        return steps


s = Solution()
inputs = [
    [[1,2,3],[0,0,4],[7,6,5]],
    [[69438,55243,0,43779,5241,93591,73380],[847,49990,53242,21837,89404,63929,48214],[90332,49751,0,3088,16374,70121,25385],[14694,4338,87873,86281,5204,84169,5024],[31711,47313,1885,28332,11646,42583,31460],[59845,94855,29286,53221,9803,41305,60749],[95077,50343,27947,92852,0,0,19731],[86158,63553,56822,90251,0,23826,17478],[60387,23279,78048,78835,5310,99720,0],[74799,48845,60658,29773,96129,90443,14391],[65448,63358,78089,93914,7931,68804,72633],[93431,90868,55280,30860,59354,62083,47669],[81064,93220,22386,22341,95485,20696,13436],[50083,0,89399,43882,0,13593,27847],[0,12256,33652,69301,73395,93440,0],[42818,87197,81249,33936,7027,5744,64710],[35843,0,99746,52442,17494,49407,63016],[86042,44524,0,0,26787,97651,28572],[54183,83466,96754,89861,84143,13413,72921],[89405,52305,39907,27366,14603,0,14104],[70909,61104,70236,30365,0,30944,98378],[20124,87188,6515,98319,78146,99325,88919],[89669,0,64218,85795,2449,48939,12869],[93539,28909,90973,77642,0,72170,98359],[88628,16422,80512,0,38651,50854,55768],[13639,2889,74835,80416,26051,78859,25721],[90182,23154,16586,0,27459,3272,84893],[2480,33654,87321,93272,93079,0,38394],[34676,72427,95024,12240,72012,0,57763],[97957,56,83817,45472,0,24087,90245],[32056,0,92049,21380,4980,38458,3490],[21509,76628,0,90430,10113,76264,45840],[97192,58807,74165,65921,45726,47265,56084],[16276,27751,37985,47944,54895,80706,2372],[28438,53073,0,67255,38416,63354,69262],[23926,75497,91347,58436,73946,39565,10841],[34372,69647,44093,62680,32424,69858,68719],[24425,4014,94871,1031,99852,88692,31503],[24475,12295,33326,37771,37883,74568,25163],[0,18411,88185,60924,29028,69789,0],[34697,75631,7636,16190,60178,39082,7052],[24876,9570,53630,98605,22331,79320,88317],[27204,89103,15221,91346,35428,94251,62745],[26636,28759,12998,58412,38113,14678,0],[80871,79706,45325,3861,12504,0,4872],[79662,15626,995,80546,64775,0,68820],[25160,82123,81706,21494,92958,33594,5243]]
]

for tree in inputs:
    print(s.cutOffTree(tree))