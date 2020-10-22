class Solution:
    def uniquePaths(self, m, n):
        dp=[[1 for k in range(m)] for i in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
    def v2(self, m, n):
        dp=[1]*m
        for i in range(1,n):
            for j in range(1,m):
                dp[j]=dp[j]+dp[j-1]
        return dp[-1]
a=Solution()
b=a.v2(7,3)
print(b)