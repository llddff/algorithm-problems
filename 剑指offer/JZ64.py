from collections import deque


class Solution:
    def maxInWindows(self, num, size):
        result = []
        if not num or len(num) < size or size<1:
            return result
        n = len(num)
        dq = deque()
        for i in range(n):
            while dq and num[dq[-1]] < num[i]:
                dq.pop()
            dq.append(i)
            if dq[0] + size <= i:
                dq.popleft()
            if i + 1 >= size:
                result.append(num[dq[0]])
        return result


a = Solution().maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)
a
