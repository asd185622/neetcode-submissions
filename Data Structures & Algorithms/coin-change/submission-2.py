class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i][j]  使用前[0..i]硬幣可以組出amount j 的最小數量
        #dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]])
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n)]

        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = int(i / coins[0])
        
        for i in range(1,n):
            for j in range(amount + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1)
        print(dp)
        return -1 if dp[n - 1][amount] == float('inf') else dp[n - 1][amount]