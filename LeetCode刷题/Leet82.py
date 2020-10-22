class Solution:
    def deleteDuplicates(self, head):
        if not (head and head.next):
            return head
        dummy = ListNode(0)
        dummy.next = head
        a, b = dummy, dummy.next
        while b and b.next:
            if a.next.val != b.next.val:
                a, b = a.next, b.next
            else:
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
        return dummy.next
