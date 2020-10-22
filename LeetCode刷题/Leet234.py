class Solution:
    def isPalindrome(self, head):
        if not head:
            return True
        formerend = self.findmid(head)
        laststart = self.reverselist(formerend.next)
        res = True
        first = head
        second = laststart
        while res and second:
            if first.val != second.val:
                res = False
            first = first.next
            second = second.next
        # formerend.next=self.reverselist(laststart)
        return res

    def reverselist(self, head):
        pre = None
        cur = head
        while cur:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
        return pre

    def findmid(self, head):
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
