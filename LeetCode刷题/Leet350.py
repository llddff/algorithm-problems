import collections


class Solution:
    def intersect(self, nums1, nums2):
        record = collections.Counter(nums1)
        # for i in nums1:
        #     if i in record:
        #         record[i] += 1
        #     else:record[i]=1
        res = []
        for i in nums2:
            if record.get(i, 0) > 0:
                res.append(i)
                record[i] -= 1
        return res
