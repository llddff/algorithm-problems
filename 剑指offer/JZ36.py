class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        ta, tb = pHead1, pHead2
        while ta != tb:
            ta = ta.next if ta else pHead2
            tb = tb.next if tb else pHead1
        return ta
