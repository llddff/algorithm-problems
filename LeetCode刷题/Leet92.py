class Solution:
    def reverseBetween(self, head, m, n):
        if not head:
            return
        cur, pre = head, None
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        tail, con = cur, pre
        while n:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n -= 1
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
