class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        ans=0
        while l<r and r<len(prices):
            ans = max(ans, prices[r]-prices[l])
            if prices[r]<prices[l]:
                l=r
            
            r+=1
        return ans