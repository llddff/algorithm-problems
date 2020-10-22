class Solution:
    def LastRemaining_Solution(self, n, m):
        if n <= 0:
            return -1
        result = 0
        for i in range(2, n + 1):
            result = (m + result) % i
        return result
