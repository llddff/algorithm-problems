class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)>>1
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[0]:
                if nums[mid]>target>=nums[0]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[-1]:
                    l=mid+1
                else:
                    r=mid-1
        return -1