class Solution:
    def rotateRight(self, head, k):
        if not head:
            return
        if not head.next:
            return head
        old, n = head, 1
        while old.next:
            old = old.next
            n += 1
        old.next = head
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
