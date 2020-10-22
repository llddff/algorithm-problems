import collections


class Solution:
    def __init__(self):
        self.cnt = collections.Counter()
        self.q = collections.deque()

    def FirstAppearingOnce(self):
        while self.q:
            c = self.q[0]
            if self.cnt[c] == 1:
                return c
            else:self.q.popleft()
        return '#'

    def Insert(self, char):
        if char not in self.cnt:
            self.q.append(char)
        self.cnt.update(char)
