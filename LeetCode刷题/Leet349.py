class Solution:
    def intersection(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        res = set1 & set2
        return list(res)
