class Solution:
    def searchRange(self, nums, target):
        result=[-1,-1]
        if not nums:
            return result
        n=len(nums)
        start=0
        end=n
        while start<end:
            mid=start+((end-start)>>1)
            if nums[mid]>=target:
                end=mid
            else:
                start=mid+1
        if start<n and nums[start]==target:
            result[0]=start
        start=0
        end=n
        while start<end:
            mid=start+((end-start)>>1)
            if nums[mid]<=target:
                start=mid+1
            else:
                end=mid
        if nums[start-1]==target:
            result[1]=start-1
        return result

a=Solution()
b=a.searchRange([2,2],3)
print(b)