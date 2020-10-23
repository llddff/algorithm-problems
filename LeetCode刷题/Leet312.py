class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        dp = [[0] * (n + 2) for a in range(n + 2)]
        val = [1] + nums + [1]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    score = val[i] * val[k] * val[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], score)
        return dp[0][n + 1]
