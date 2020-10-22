# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0 for i in range(n)] for i in range(n - 1)]
        dp.append(triangle[-1])
        for i in range(n - 2, -1, -1):
            # row=triangle[i]
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

    def v2(self, triangle):
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

    def v3(self, triangle):
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        return triangle[0][0]


a = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
b = Solution()
c = b.v3(a)
print(c)
