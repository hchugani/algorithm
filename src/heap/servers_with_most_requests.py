from collections import defaultdict
import heapq
from typing import List
"""
1606. Find Servers That Handled Most Number of Requests
Hard

You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. 
Each server has infinite computational capacity but cannot handle more than one request at a time. The r
equests are assigned to servers according to a specific algorithm:

The ith (0-indexed) request arrives.
If all servers are busy, the request is dropped (not handled at all).
If the (i % k)th server is available, assign the request to that server.
Otherwise, assign the request to the next available server (wrapping around the list of servers and 
starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the 
(i+1)th server, then the (i+2)th server, and so on.
You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the 
arrival time of the ith request, and another array load, where load[i] represents the load of the ith 
request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered
 busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

 

Example 1:


Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation:
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.

"""


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
        O(nlogk) time
        O(k) space

        """
        busy = []
        before = list(range(k))
        after = []
        result = [0]*k
        for i, (start, dur) in enumerate(zip(arrival, load)):
            ind = i % k
            if ind==0:
                after = before
                before = []

            while busy and busy[0][0]<=start:
                server = heapq.heappop(busy)[1]
                if server<ind:
                    heapq.heappush(before, server)
                else:
                    heapq.heappush(after, server)

            use_queue = after if after else before
            if use_queue:
                j = heapq.heappop(use_queue)
                heapq.heappush(busy, (start+dur, j))
                result[j] +=1

        a = max(result)
        return [i for i in range(len(result)) if result[i]==a]






    def busiestServers1(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = [0] * k
        counter = defaultdict(int)

        ind = 0
        for i in range(len(arrival)):
            ind = i % k

            cycle = False
            j = 0
            while not cycle and busy[ind]>arrival[i]:
                if j==k:
                    cycle = True
                    break
                ind+=1
                if ind==k:
                    ind = 0
                j+=1
            if not cycle:
                busy[ind] = arrival[i]+load[i]
                counter[ind]+=1

        maxi = 0
        result = []
        for key in counter.keys():
            if counter[key]==maxi:
                result.append(key)
            elif counter[key]>maxi:
                maxi = counter[key]
                result = []
                result.append(key)

        return result


s = Solution()
inputs = [
    (3,
    [1,2,3,4,5],
    [5,2,3,3,3]),
    (3,
    [1,2,3,4],
    [1,2,1,2]),
    (2,
    [2,3,4,8],
    [3,2,4,3])
]

for k, start, load in inputs:
    print(s.busiestServers(k, start, load))
