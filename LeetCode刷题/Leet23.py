class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        if n == 0:
            return
        return self.mergeK(lists, 0, n - 1)

    def mergeK(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = (l + r) >> 1
        l1 = self.mergeK(lists, l, mid)
        l2 = self.mergeK(lists, mid + 1, r)
        return self.mergeTwo(l1, l2)

    def mergeTwo(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        l2.next = self.mergeTwo(l2.next, l1)
        return l2
