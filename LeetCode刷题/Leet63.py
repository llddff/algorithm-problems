class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0]==1:
            return 0
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[1 for k in range(m)] for i in range(n)]
        for i in range(1,n):
            dp[i][0]=0 if obstacleGrid[i][0]==1 else dp[i-1][0]
        for j in range(1,m):
            dp[0][j]=0 if obstacleGrid[0][j]==1 else dp[0][j-1]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1] if obstacleGrid[i][j] != 1 else 0
        return dp[-1][-1]
    def v2(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0]==1:
            return 0
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for i in range(1,n):
            obstacleGrid[i][0]=int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
        for j in range(1,m):
            obstacleGrid[0][j]=int(obstacleGrid[0][j]==0 and obstacleGrid[0][j-1]==1)
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return obstacleGrid[-1][-1]