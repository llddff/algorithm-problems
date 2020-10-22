import collections


class Solution:
    def findAnagrams(self, s, p):
        res = []
        if len(p) > len(s):
            return res
        hashmap = collections.Counter(p)
        m, n, cnt = len(p), len(s), len(p)
        for i in range(m):
            if s[i] not in hashmap:
                continue
            elif hashmap[s[i]] > 0:
                cnt -= 1
            hashmap[s[i]] -= 1
        if cnt == 0: res.append(0)
        for i in range(n - m):
            if s[i] in hashmap:
                if hashmap[s[i]] >= 0:
                    cnt += 1
                hashmap[s[i]] += 1
            if s[i + m] in hashmap:
                if hashmap[s[i + m]] > 0:
                    cnt -= 1
                hashmap[s[i + m]] -= 1
            if cnt == 0: res.append(i + 1)
        return res
