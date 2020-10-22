class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        start, end = 1, n - 1
        while start < end:
            mid = (start + end) >> 1
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt > mid:
                end = mid
            else:
                start = mid + 1
        return start

    def lianbiao(self, nums):
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow
