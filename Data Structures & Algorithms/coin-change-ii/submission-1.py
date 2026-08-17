class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[j] 代表組成amount j的不同方式有dp[j]種
        #dp[i][j] 代表coins[0..i]組成 amount j 的方式有dp[i][j]種
        #dp[i][j] = dp[i - 1][j] + dp[i][j-coins[i]]
        #dp[j] = dp[j - coins[i]] + 1
        dp = [0] * (amount + 1)

        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[i] = 1
        
        for i in range(1,len(coins)):
            # print(dp)
            for j in range(coins[i],amount + 1):
                dp[j] += dp[j - coins[i]]
        print(dp)
        return dp[amount]