from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = len(costs[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[n-1] = costs[n-1]

        for i in range(n-2, -1, -1):
            for j in range(m):
                dp[i][j] = costs[i][j] + \
                    min([dp[i+1][k] for k in range(m) if j != k])
        
        return min(dp[0])
