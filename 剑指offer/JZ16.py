class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        cur = dummy = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        cur.next = pHead1 if pHead1 else pHead2
        return dummy.next
