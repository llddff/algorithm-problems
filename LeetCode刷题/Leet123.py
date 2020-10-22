class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        if n == 0:
            return 0
        fstBuy=-prices[0]
        fstSell=0
        secBuy=-prices[0]
        secSell=0
        for i in range(1,n):
            fstBuy=max(fstBuy,-prices[i])
            fstSell=max(fstSell,fstBuy+prices[i])
            secBuy=max(secBuy,fstSell-prices[i])
            secSell=max(secSell,secBuy+prices[i])
        return secSell