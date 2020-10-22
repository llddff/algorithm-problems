import heapq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k == 0 or k > len(tinput):
            return []
        return heapq.nsmallest(k, tinput)

    def kuaipai(self, tinput, k):
        def partition(alist, l, r):
            pivot = alist[r]
            i = l
            for j in range(l, r):
                if alist[j] < pivot:
                    alist[i], alist[j] = alist[j], alist[i]
                    i += 1
            alist[i], alist[r] = alist[r], alist[i]
            return i

        if k == 0 or k > len(tinput):
            return []
        l, r = 0, len(tinput) - 1
        while l <= r:
            p = partition(tinput, l, r)
            if p == k - 1:
                return tinput[:k]
            if p < k - 1:
                l = p + 1
            else:
                r = p-1
        return []
a=Solution().kuaipai([8,7,6,4,4,4,2,1],4)
a