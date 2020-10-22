class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre, cur, tmp = None, pHead, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
