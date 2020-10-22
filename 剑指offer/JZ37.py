class Solution:
    def GetNumberOfK(self, data, k):
        n = len(data)
        if not n:
            return 0
        start = 0
        end = n - 1
        first = self.get_first(data, k, start, end)
        if first == -1:
            return 0
        last = self.get_end(data, k, first, end)
        return last - first + 1

    def get_first(self, data, k, start, end):
        while start < end:
            mid = (start + end) >> 1
            if data[mid] < k:
                start = mid+1
            else:
                end = mid
        if data[start] == k:
            first = start
        else:
            first = -1
        return first

    def get_end(self, data, k, start, end):
        while start+1 < end:
            mid = (start + end) >> 1
            if data[mid] <= k:
                start = mid
            else:
                end = mid
        if data[end] == k:
            last = end
        elif data[start] == k:
            last = start
        else:
            last = -1
        return last
a=Solution().GetNumberOfK([3,3,3,3,4],3)
a