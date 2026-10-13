class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(am):
            if am == 0:
                return 0

            res = float('inf')

            if am in dp:
                return dp[am]

            for coin in coins:
                if am  >= coin:
                    res = min(res, 1 +  dfs(am - coin))

            dp[am] = res

            return res

        res = dfs(amount)

        return -1 if res == float('inf') else res


                

                    

