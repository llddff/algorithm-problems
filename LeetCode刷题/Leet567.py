import collections


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        hashmap = collections.Counter(s1)
        m, n, cnt = len(s1), len(s2), len(s1)
        for i in range(m):
            if s2[i] not in hashmap:
                continue
            elif hashmap[s2[i]] > 0:
                cnt -= 1
            hashmap[s2[i]] -= 1
        if cnt == 0: return True
        for i in range(n - m):
            if s2[i] in hashmap:
                if hashmap[s2[i]] >= 0:
                    cnt += 1
                hashmap[s2[i]] += 1
            if s2[i + m] in hashmap:
                if hashmap[s2[i + m]] > 0:
                    cnt -= 1
                hashmap[s2[i + m]] -= 1
            if cnt == 0: return True
        return False
