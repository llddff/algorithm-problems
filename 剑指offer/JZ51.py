class Solution:
    def multiply(self, A):
        n = len(A)
        B = [1] * n
        for i in range(1, n):
            B[i] = B[i - 1] * A[i - 1]
        tmp = 1
        for j in range(n - 2, -1, -1):
            tmp *= A[j + 1]
            B[j] *= tmp
        return B
