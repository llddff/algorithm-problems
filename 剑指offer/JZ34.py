import collections


class Solution:
    def FirstNotRepeatingChar(self, s):
        cnt = collections.Counter(s)
        n = len(s)
        for i in range(n):
            if cnt[s[i]] == 1:
                return i
        return -1
