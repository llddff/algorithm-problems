class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 == 1: return False
        n = len(nums)
        s >>= 1
        dp = [False for j in range(s + 1)]
        dp[0] = True
        for i in range(n):
            for j in range(s, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[s]

    def huisu(self, nums):
        s = sum(nums)
        if s & 1: return False
        s >>= 1
        nums.sort(reverse=True)
        if nums[0] > s:
            return False
        return self.dfs(nums, s)

    def dfs(self, nums, total):
        if total == 0:
            return True
        if total < 0:
            return False
        for i in range(len(nums)):
            if self.dfs(nums[i + 1:], total - nums[i]):
                return True
        return False
