from LeetCode刷题.Leet02 import ListNode


class Solution:
    def sortList(self, head):
        h, length, merge = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        while merge < length:
            pre, h = res, res.next
            while h:
                h1, i = h, merge
                while i and h:
                    h, i = h.next, i - 1
                if i: break
                h2, i = h, merge
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = merge, merge - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            merge *= 2
        return res.next
a=ListNode(4)
a.next=ListNode(2)
a.next.next=ListNode(1)
a.next.next.next=ListNode(3)
b=Solution().sortList(a)
b