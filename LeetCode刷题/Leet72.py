class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            pre = dp[:]
            dp[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = pre[j - 1]
                else:
                    dp[j] = min(pre[j], dp[j - 1], pre[j - 1]) + 1
        return dp[n]
