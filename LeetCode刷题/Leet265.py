def minCostII(costs):
    if len(costs)==0 or len(costs[0])==0:
        return 0
    n=len(costs)
    k=len(costs[0])
    dp=[[0 for i in range(k)] for i in range(n)]
    dp[0]=costs[0]
    for i in range(1,n):
        min1=2**30
        min2=2**30
        minIndex=0
        for l in range(k):   # 找出最小值与次小值
            if dp[i-1][l]<min1:
                min2=min1
                min1=dp[i-1][l]
                minIndex=l
            elif dp[i-1][l]<min2:
                min2=dp[i-1][l]
        for j in range(k):
            if j!=minIndex:
                dp[i][j]=min1+costs[i][j]
            else:
                dp[i][j]=min2+costs[i][j]
    return min(dp[-1])

a=minCostII([[1,5,3],[2,9,4]])
print(a)