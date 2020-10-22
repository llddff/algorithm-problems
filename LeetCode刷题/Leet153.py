class Solution:
    def findMin(self, nums):
        if not nums:
            return 0
        start=0
        end=len(nums)-1
        while start<end:
            mid=(start+end)>>1
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        return nums[start]