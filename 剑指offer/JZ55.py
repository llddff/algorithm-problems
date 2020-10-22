class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return
        slow = pHead.next
        fast = pHead.next.next
        while slow != fast:
            if not fast or not fast.next or not fast.next.next:
                return
            slow = slow.next
            fast = fast.next.next
        fast = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
