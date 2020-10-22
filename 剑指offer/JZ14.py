class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if k == 0 or not head:
            return
        ahead = behind = head
        for i in range(k):
            if ahead.next:
                ahead = ahead.next
            else:
                return
        while ahead:
            ahead = ahead.next
            behind = behind.next
        return behind
