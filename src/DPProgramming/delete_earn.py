
from typing import List


"""
740. Delete and Earn
Medium

You are given an integer array nums. You want to maximize the number of points you get by performing
 the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to
 nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        I
        """
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num]=0
            counter[num] += 1

        prev = None
        first = second = 0
        for key in sorted(counter):
            if key-1 != prev:
                first, second = max(first,second)+key*counter[key],max(first,second)
            else:
                first, second = second+ +key*counter[key],max(first,second)
            prev = key

        return max(first,second)


s = Solution()
inputs = [
    [1,2,2,1],
    [2,7,9,3,1],
    [1]
]

for num in inputs:
    print(s.deleteAndEarn(num))



