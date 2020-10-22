class Solution:
    def reorderList(self, head):
        if not (head and head.next and head.next.next):
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        halfhead = slow.next
        slow.next = None
        halfhead = self.reverseList(halfhead)
        while halfhead:
            tmp = halfhead.next
            halfhead.next = head.next
            head.next = halfhead
            head = halfhead.next
            halfhead = tmp

    def reverseList(self, head):
        if not head:
            return
        tail = head
        head = head.next
        tail.next = None
        while head:
            tmp = head.next
            head.next = tail
            tail = head
            head = tmp
        return tail
