from collections import deque

"""
Design a hit counter which counts the number of hits received in the past 5 minutes 
(i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that 
calls are being made to the system in chronological order (i.e., timestamp is monotonically 
increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen
at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp
(i.e., the past 300 seconds).
"""

class HitCounter:
    """
    O(N) both space and time
    """

    def __init__(self):
        self.queue = deque()


    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        # pop elements
        if len(self.queue)==0:
            return 0

        while(timestamp-self.queue[0])>=300:
            self.queue.popleft()
            if len(self.queue)==0:
                return 0

        return len(self.queue)


        # Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))
obj.hit(300)
obj.hit(301)
print(obj.getHits(302))