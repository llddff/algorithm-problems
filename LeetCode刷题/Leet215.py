import heapq


class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        heapq.heapify(nums)
        for i in range(n - k):
            heapq.heappop(nums)
        return nums[0]
