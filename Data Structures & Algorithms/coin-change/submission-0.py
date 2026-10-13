class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0

        if amount == 0:
            return 0

        if amount < min(coins):
            return -1
        
        for e in coins:
            dp[e] = 1

        for i in range(1, amount+1):
            if i in dp:
                continue

            if i < min(coins):
                dp[i] = float('inf')

            for e in coins:
                if e > i:
                    break

                old = dp.get(i) if dp.get(i) else float('inf')

                new = (dp.get(i-e) + dp.get(e)) if dp.get(i-e) else float('inf')

                dp[i] = min(old, new)
            
            # print(dp)

        return -1 if dp[amount] == float('inf') else dp[amount]