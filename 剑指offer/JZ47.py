class Solution:
    def Sum_Solution(self, n):
        return n and (n+self.Sum_Solution(n-1))

a=Solution().Sum_Solution(100)
a