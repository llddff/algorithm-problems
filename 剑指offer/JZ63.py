import heapq


class Solution:
    def __init__(self):
        self.minh = []
        self.maxh = []

    def Insert(self, num):
        if len(self.maxh) <= len(self.minh):
            heapq.heappush(self.maxh, -num)
        else:
            heapq.heappush(self.minh, num)
        if self.maxh and self.minh:
            if -self.maxh[0] > self.minh[0]:
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))

    def GetMedian(self):
        if len(self.maxh) > len(self.minh):
            median = -self.maxh[0]
        else:
            median = (-self.maxh[0] + self.minh[0]) / 2
        return median


a = Solution()
a.Insert(5)
a.GetMedian()
a.Insert(2)
a.GetMedian()
