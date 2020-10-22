class Solution:
    def findTargetSumWays(self, nums, S):
        n = len(nums)
        sumnum=sum(nums)
        if sumnum<S:
            return 0
        suma = S + sumnum
        if suma & 1:
            return 0
        suma >>= 1
        dp = [[0] * (suma + 1) for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(suma + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][suma]
