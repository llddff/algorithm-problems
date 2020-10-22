class Solution:
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums.sort()
        if n == 0:
            return []
        for k in range(n):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            target = -nums[k]
            i, j = k + 1, n - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i + 1] == nums[i]: i += 1
                    while i < j and nums[j - 1] == nums[j]: j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return res
