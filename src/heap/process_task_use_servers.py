"""
1882. Process Tasks Using Servers
Medium

You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​
and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​
server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long
as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free
server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign
the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned
in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th
 task will be assigned to.

Return the array ans​​​​.

Example 1:

Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
"""
from typing import List
# class Server:
#     def __init__(self, ind, wt):
#         self.ind = ind
#         self.wt = wt

#     def __lt__(self, other):
#         if self.wt == other.wt:
#             return self.ind < other.ind
#         else:
#             return self.wt < other.wt

#     def __str__(self):
#         return f'ind: {self.ind}, wt: {self.wt}, busy: {self.busy_until}'
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        O(NlogN): Free
        O(N): Space
        """
        free = []
        ans = []
        busy = []

        for i, wt in enumerate(servers):
            heapq.heappush(free, (wt,i))

        for t, task in enumerate(tasks):
            f = t + task
            while busy and busy[0][0]<=t:
                _, wt, i = heapq.heappop(busy)
                heapq.heappush(free, (wt, i))
            if free:
                s_wt, s_i  = heapq.heappop(free)
                ans.append(s_i)
                heapq.heappush(busy, (f, s_wt, s_i))
            else:
                # if not free take , get the next server which will become free
                # and add the task time to it and insert back
                bt, s_wt, s_i  = heapq.heappop(busy)
                ans.append(s_i)
                heapq.heappush(busy, (bt+task, s_wt, s_i))

        return ans


s = Solution()
inputs = [
    ([3,2],[1,2,3,2,1,2]),
    ([5,1,4,3,2], [2,1,2,4,5,2,1])
]

for servers, tasks in inputs:
    print(s.assignTasks(servers, tasks))
