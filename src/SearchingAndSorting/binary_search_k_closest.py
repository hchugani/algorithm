from typing import List
class Solution:

    def closestK(self, arr: List[int], target: int, k : int)->List[int]:

        def find_cross_over_point(arr, target):
            l = 0
            r = len(arr)-1

            while l <r:
                mid = l + (r-l)//2
                if arr[mid]==target:
                    return mid
                elif arr[mid]>target:
                    r = mid-1
                else:
                    if mid+1<=len(arr)-1 and target<arr[mid+1]:
                        return mid
                    l = mid+1
            return r

        l = find_cross_over_point(arr, target)
        r = l+1

        result = []
        if arr[l] == target:
            l-=1

        count = 0
        while (l>=0 and r<len(arr) and count<k):
            if(target-arr[l]<arr[r]-target):
                result.append(arr[l])
                l-=1
            else:
                result.append(arr[r])
                r+=1
            count+=1

        # assume no elements on left , then use right
        while(l<0 and r < len(arr) and count<k):
            result.append(arr[r])
            count+=1
            r+=1

        while(l>=0 and r == len(arr) and count<k):
            result.append(arr[l])
            count+=1
            l-=1


        return result
        # find the crossover point where elements are less or equal to target

s = Solution()
arr = [12, 16, 22, 30, 34, 39, 42, 45, 48, 50, 53, 55, 56]
print(s.closestK(arr=arr, target=43, k =4))