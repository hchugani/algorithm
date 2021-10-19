from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(n)]

        layer = 0
        i = 1
        while layer < (n+1)//2:
            x = y = layer

            # left to right
            for y in range(layer, n-layer):
                matrix[x][y]=i
                i+=1

            # top to botton
            for x in range(layer+1, n - layer):
                matrix[x][y]=i
                i+=1

            for y in range(n-layer-2, layer-1, -1):
                matrix[x][y]=i
                i+=1

            for x in range(n-layer-2, layer, -1 ):
                matrix[x][y]=i
                i+=1

            layer+=1

        return matrix

s = Solution()
for i in range(1, 6):
    print(s.generateMatrix(i))