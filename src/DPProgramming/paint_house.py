from typing import List

class PaintHouse:

    def minCostBottomUp(self, costs: List[List[int]])->int:
        """
        tiem complexity: O(n)
        space complexity : O(1)
        :param costs:
        :return:
        """
        if len(costs)==0:
            return 0
        for n in range(len(costs)-2, -1, -1):
            costs[n][0] += min(costs[n+1][1], costs[n+1][2])
            costs[n][1] += min(costs[n+1][0], costs[n+1][2])
            costs[n][2] += min(costs[n+1][0], costs[n+1][1])

        return min(costs[0])


    def minCost(self, costs: List[List[int]]) -> int:
        """
        time complexity: O(n)
        space complexity : O(n)
        :param costs:
        :return:
        """
        def paint_cost(n, color):
            if (n,color) in self.memo:
                return self.memo[(n,color)]
            total_cost = costs[n][color]
            # base case
            if n == len(costs)-1:
                pass
            elif color==0:
                total_cost += min(paint_cost(n+1, 1), paint_cost(n+1, 2))
            elif color==1:
                total_cost += min(paint_cost(n+1, 0), paint_cost(n+1, 2))
            elif color==2:
                total_cost += min(paint_cost(n+1, 0), paint_cost(n+1, 1))
            self.memo[(n, color)] = total_cost
            return total_cost

        if len(costs) == 0:
            return 0
        self.memo = {}
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))


if __name__ == "__main__":
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    p = PaintHouse()
    print(p.minCost(costs))
    print(p.minCostBottomUp(costs))
    costs = [[7,6,2]]
    print(p.minCost(costs))