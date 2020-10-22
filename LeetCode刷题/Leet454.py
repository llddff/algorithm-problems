import collections


class Solution:
    def fourSumCount(self, A, B, C, D):
        AB = []
        for i in A:
            for j in B:
                AB.append(i + j)
        AB = collections.Counter(AB)
        res = 0
        for i in C:
            for j in D:
                if -i - j in AB:
                    res += AB[-i - j]
        return res
