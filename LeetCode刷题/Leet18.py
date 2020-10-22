class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        if  n < 4:
            return []
        nums.sort()
        res = []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c, d = b + 1, n - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif sum < target:
                        c += 1
                    else:
                        d -= 1
        return res
