class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        elif pNode.next:
            while pNode.next and pNode.next.right == pNode:
                pNode=pNode.next
            return pNode.next
        return