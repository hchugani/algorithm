import heapq
from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # build up a heap containing time slots last longer than duration
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)

        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        return []

    def minAvailableDuration1(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """
        Time complexity : O(MlogM) + O(NlogN)
        space : O(M+N)
        """

        array = []
        for slot in slots1:
            array.append((slot[0], 1))
            array.append((slot[1], -1))

        for slot in slots2:
            array.append((slot[0], 2))
            array.append((slot[1], -2))


        array = sorted(array, key=lambda x: x[0])
        prev = None
        sum = 0
        for time in array:
            if prev is None:
                prev = time
                sum+=time[1]
                continue

            if sum==3:
                if duration<=(time[0]-prev[0]):
                    return [prev[0], prev[0]+duration]
            sum+=time[1]
            prev = time

        return []

s = Solution()
slot1, slot2 = [[10,50],[60,120],[140,210]], [[0,15]]

print(s.minAvailableDuration(slot1, slot2, 8))