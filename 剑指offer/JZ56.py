class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return
        current_node = pHead
        pre_node = None
        while current_node:
            next_node = current_node.next
            if not next_node or next_node.val != current_node.val:
                pre_node = current_node
            else:
                while next_node and next_node.val == current_node.val:
                    next_node = next_node.next
                if pre_node is None:
                    pHead = next_node
                else:
                    pre_node.next = next_node
            current_node = next_node
        return pHead
