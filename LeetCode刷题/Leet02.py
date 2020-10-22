# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head=ListNode(0)
        p=l1
        q=l2
        curr=head
        carry=0
        while p or q:
            x=p.val if p else 0
            y=q.val if q else 0
            sum_=x+y+carry
            carry=sum_//10
            curr.next=ListNode(sum_%10)
            curr=curr.next
            if p:
                p=p.next
            if q:
                q=q.next
        if carry>0:
            curr.next=ListNode(carry)
        return head.next
