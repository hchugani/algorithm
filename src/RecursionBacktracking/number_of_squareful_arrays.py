from typing import List
import math

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        result = []
        N = len(nums)
        counter ={}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] +=1

        def isPerfectSquare(x):
            if(x >= 0):
                sr = math.sqrt(x)
                # sqrt function returns floating value so we have to convert it into integer
                #return boolean T/F
                sr = int(sr)
                return (float(sr*sr) == float(x))
            return false

        def findPermute(combo=[]):
            if len(combo)==N:
                result.append(list(combo))
                return

            for key in counter.keys():
                if counter[key]>0:
                    if len(combo)!=0:
                        x = key + combo[-1]
                        if isPerfectSquare(x):
                            combo.append(key)
                            counter[key]-=1
                            findPermute(combo)
                            combo.pop()
                            counter[key]+=1
                    else:
                        combo.append(key)
                        counter[key]-=1
                        findPermute(combo)
                        combo.pop()
                        counter[key]+=1



        findPermute()
        return len(result)

if __name__ == "__main__":
    sol = Solution()
    inputs = [
        [1, 17, 8],
        [1, 2, 3]
    ]
    for input in inputs:
        print(sol.numSquarefulPerms(input))