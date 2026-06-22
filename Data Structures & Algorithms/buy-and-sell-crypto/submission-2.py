class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0
        fast = 1
        profit = 0
        if len(prices) == 1:
            return 0

        while fast < len(prices):
            if prices[slow] > prices[fast]:
                slow = fast
                fast += 1
            else:
                profit = max(profit,prices[fast] - prices[slow])
                fast += 1 
            
            # if fast >= len(prices):
            #     slow += 1
            #     fast = slow + 1
        return profit