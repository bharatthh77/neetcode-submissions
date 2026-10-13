class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target = len(cost)

        min_cost = [0] * (target+1)

        min_cost[0] = 0
        min_cost[1] = 0

        for i in range(2, target+1):
            min_cost[i] = min((min_cost[i-1] + cost[i-1]), (min_cost[i-2] + cost[i-2]))

        return min_cost[target]
