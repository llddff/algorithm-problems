class Solution:
    def fib(self, N):
        dp = [0, 1]
        for i in range(2, N + 1):
            tmp = sum(dp)
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[-1]
