# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        result=dp[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1],0)+nums[i]
            result=max(dp[i],result)
        return result