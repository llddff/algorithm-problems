class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if k > n / 2:
            profit = 0
            for i in range(1, n):
                tmp = prices[i] - prices[i - 1]
                if tmp > 0:
                    profit += tmp
            return profit
        dp = [[[0, 0] for _k in range(k + 1)] for _n in range(n)]
        for _i in range(n):
            for _k in range(k, 0, -1):
                if _i == 0:
                    dp[-1][_k][0], dp[_i][0][0] = 0, 0
                    dp[-1][_k][1], dp[_i][0][1] = float('-inf'), float('-inf')
                dp[_i][_k][0] = max(dp[_i - 1][_k][0], dp[_i - 1][_k][1] + prices[_i])
                dp[_i][_k][1] = max(dp[_i - 1][_k][1], dp[_i - 1][_k - 1][0] - prices[_i])
        return dp[n - 1][k][0]
a=Solution().maxProfit(2,[2,1,2,0,1])
a