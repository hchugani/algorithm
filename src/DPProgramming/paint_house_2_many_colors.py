from typing import List

class PaintHouse2:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        O(n.k2)
        O(n.k) space
        :param costs:
        :return:
        """
        if len(costs)==0: return 0
        colors_count = len(costs[0])

        for n in range(len(costs)-2, -1, -1):
            for j in range(colors_count):
                best = float("inf")
                for k in range(colors_count):
                    if k != j:
                        best = min(best, costs[n+1][k] )
                costs[n][j] += best

        return min(costs[0])

    def minCostIIBetter(self, costs: List[List[int]]) -> int:
        """
        O(n.k)
        O(1)
        :param costs:
        :return:
        """
        if len(costs)==0: return 0
        colors_count = len(costs[0])

        for n in range(len(costs)-2, -1, -1):
            # find min_color and second_min_color in this loop
            min_color = second_min_color = None
            for j in range(colors_count):
                cost = costs[n+1][j]
                if min_color is None or cost<costs[n+1][min_color]:
                    second_min_color = min_color
                    min_color = j
                elif second_min_color is None or cost < costs[n+1][second_min_color]:
                    second_min_color = j

            for j in range(colors_count):
                if j == min_color:
                    # avoid adjacent run
                    costs[n][j] += costs[n+1][second_min_color]
                else:
                    costs[n][j] += costs[n+1][min_color]

if __name__ == "__main__":
    costs = [[17,2,17,4],[16,16,5,13],[14,3,19,15]]
    p = PaintHouse2()
    print(p.minCostII(costs))