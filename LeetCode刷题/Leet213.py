class Solution:
    def rob(self, nums):
        def my_rob(nums):
            if not nums:
                return 0
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0 for i in range(n + 1)]
            dp[1] = nums[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
            return dp[-1]

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(my_rob(nums[:-1]), my_rob(nums[1:]))
