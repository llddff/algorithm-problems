class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)>>1
            if nums[mid]==target:
                return True
            if nums[mid]==nums[l]:
                l+=1
                continue
            if nums[mid]>=nums[l]:
                if nums[mid]>target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False