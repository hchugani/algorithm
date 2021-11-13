from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        """
        Time complexity : O(log(min(m,n)))
        find pivot point in smaller array using binary search such that

            x1,x2,x3 | x4
            y1, y2,| y3, y4, y5, y6

        paritionx + paritiony = M+N+1//2

        median if total is even = avg(max(x3,y2), min(x4, y3))
                        if odd = max(x3, y2)

        binary search logic to find parition in x such that
             elements in left_partition_x <= elements in right_partition_y
             and  elements in right_partition_x <= elements in left_partition_y

             else if right most element in left_partiton_x > leftmost element in right_partion_y then move the pivot in x towards left

             else move towards right

        """
        m = len(nums1)
        n = len(nums2)


        def findMedian(a, b, n, m):
            l = 0
            r = n
            # n = 4, m = 6
            # a = [3]
            # b = [1, 2]


            while l<=r:
                i = (r+l)//2 #  i = 0
                j = (m+n+1)//2-i  # j = 1

                max_left_a =  float("-inf") if i==0 else a[i-1]
                min_right_a = float("inf") if i==n else a[i]

                max_left_b = float("-inf") if j==0 else b[j-1]
                min_right_b = float("inf") if j==m else b[j]

                if max_left_a<=min_right_b and max_left_b<=min_right_a:
                    # found values
                    if (m+n)%2==0:
                        return (max(max_left_a,max_left_b) + min(min_right_a, min_right_b ))/2
                    else:
                        return max(max_left_a,max_left_b)
                elif max_left_a>min_right_b:
                    r=i-1
                else:
                    l = i+1


            return 0


        if m <= n:
            median = findMedian(nums1, nums2, m, n)
        else:
            median = findMedian(nums2,nums1, n, m)

        return median



s = Solution()

nums = [
    ([1,3, 5, 8, 9,10],[2,4,6,8]),
    ([1,3],[2]),
    ([0,0],[0,0])
]

for num1, num2 in nums:
    print(s.findMedianSortedArrays(num1, num2))

