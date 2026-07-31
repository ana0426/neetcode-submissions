class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0] 
        max_profit = 0

        for sell in range(len(prices)):
            min_buy = min(min_buy,prices[sell])
            curr = prices[sell] - min_buy
            max_profit = max(max_profit,curr)

        return max_profit
                

                 
