"""
540. Single Element in a Sorted Array
Medium


You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
 element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

"""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """

        O(logN)


        Case 1: Mid’s partner is to the right, and the halves were originally even.

        The right side becomes odd-lengthed because we removed mid's partner from it. We need to set lo to mid + 2
        so that the remaining array is the part above mid's partner.

        Case 2: Mid’s partner is to the right, and the halves were originally odd.

        The left side remains odd-lengthed. We need to set hi to mid - 1 so that the remaining array is the part
        below mid.
        """

        def binarySearch(a)->int:
            N = len(a)
            lo = 0
            hi = N-1
            while lo<hi:
                mid = lo + (hi-lo)//2
                halfs_even = (hi-mid)%2==0
                if a[mid]==a[mid+1]:
                    if halfs_even:
                        lo = mid+2
                    else:
                        hi=mid-1
                elif a[mid]==a[mid-1]:
                    if halfs_even:
                        hi = mid-2
                    else:
                        lo = mid+1
                else:
                    return a[mid]
            return a[lo]

        return binarySearch(nums)

s = Solution()
print(s.singleNonDuplicate(
    [1,1,2,3,3,4,4,8,8]))