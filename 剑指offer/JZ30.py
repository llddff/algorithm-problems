class Solution:
    def FindGreatestSumOfSubArray(self, array):
        n = len(array)
        dp = [0] * (n + 1)
        result = array[0]
        for i in range(1, n + 1):
            dp[i] = max(array[i - 1], dp[i - 1] + array[i - 1])
            result = max(result, dp[i])
        return result