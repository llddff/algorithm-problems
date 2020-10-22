import collections


class Solution:
    def minWindow(self, s, t):
        self.ori = collections.Counter(t)
        self.cnt = collections.Counter()
        l, r = 0, -1
        anslen = float('inf')
        ansL = ansR = -1
        sLen = len(s)
        while r < sLen:
            r += 1
            if r < sLen and s[r] in self.ori:
                self.cnt.update(s[r])
            while self.check() and l <= r:
                if r - l + 1 < anslen:
                    anslen = r - l + 1
                    ansL, ansR = l, l + anslen
                if s[l] in self.ori:
                    self.cnt.subtract(s[l])
                l += 1
        return '' if ansL == -1 else s[ansL:ansR]

    def check(self):
        for k, v in self.ori.items():
            if self.cnt.get(k, 0) < v:
                return False
        return True


a = Solution().minWindow("ADOBECODEBANC", 'ABCe')
a
