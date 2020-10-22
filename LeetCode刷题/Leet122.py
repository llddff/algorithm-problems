class Solution:
    def maxProfit(self, prices):
        profit=0
        n=len(prices)
        for i in range(1,n):
            tmp=prices[i]-prices[i-1]
            if tmp>0:
                profit+=tmp
        return profit