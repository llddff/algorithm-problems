class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0: return 0
        slow, fast = 0, 1
        while fast < n:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
