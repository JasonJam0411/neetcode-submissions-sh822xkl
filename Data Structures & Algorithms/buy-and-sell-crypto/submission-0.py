class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = prices[j]-prices[i]
                if profit>ans:
                    ans = profit
        return ans