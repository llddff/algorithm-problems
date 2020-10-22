class Solution:
    def superEggDrop(self, K, N):
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    l, h = 1, n
                    while l + 1 < h:
                        mid = (l + h) >> 1
                        t1 = dp(k - 1, mid - 1)
                        t2 = dp(k, n - mid)
                        if t1 < t2:
                            l = mid
                        elif t1 > t2:
                            h = mid
                        else:
                            l = h = mid
                    ans = 1 + min(max(dp(k - 1, l - 1), dp(k, n - l)), max(dp(k - 1, h - 1), dp(k, n - h)))
                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)
