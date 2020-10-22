class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n=len(nums)
        dp=[1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)
    def tanxin(self, nums):
        n=len(nums)
        if n<2:
            return n
        tail=[nums[0]]
        for i in range(1,n):
            if nums[i]>tail[-1]:
                tail.append(nums[i])
            # 如果新来的数比末尾的小，开始二分查找
            left=0
            right=len(tail)-1
            while left<right:
                mid=(left+right)>>1
                if tail[mid]<nums[i]:
                    left=mid+1
                else:
                    right=mid
            tail[left]=nums[i]
        return len(tail)
