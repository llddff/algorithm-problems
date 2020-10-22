class Solution:
    def isMatch(self, s, p):
        if s == p:
            return True
        m, n = len(s), len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 2] if p[i - 1] == '*' else False
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
        return dp[m][n]


a = Solution().isMatch('aaa', 'ab*a*c*a*')
a
