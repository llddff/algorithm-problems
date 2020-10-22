class Solution:
    def Fibonacci(self, n):
        if n in (0, 1):
            return n
        a, b, c = 0, 1, 0
        for i in range(2, n + 1):
            c = a + b
            a, b = b, c
        return c
