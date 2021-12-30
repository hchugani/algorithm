"""
1386. Cinema Seat Allocation
Medium

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown
in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8]
 means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four
 adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent,
 but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a
 four-person group in the middle, which means to have two people on each side.
"""
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        O(N): both
        """
        res = 0
        mapper = {}

        for row, col in reservedSeats:
            if row not in mapper:
                mapper[row] = []
            mapper[row].append(col)

        for row in mapper.keys():
            cols = mapper[row]

            helper = [0]*10
            for col in cols:
                helper[col-1]=1
            occupied = False
            if helper[1:5]==[0,0,0,0]:
                res+=1
                occupied = True
            if helper[5:9]==[0,0,0,0]:
                res+=1
                occupied = True

            if not occupied:
                if helper[3:7]==[0,0,0,0]:
                    res+=1


        return res+(2*(n-len(mapper.keys())))


s = Solution()
inputs = [
    (3,[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])
]

for n, seats in inputs:
    print(s.maxNumberOfFamilies(n, seats))