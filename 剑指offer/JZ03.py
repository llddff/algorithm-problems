class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode:
            return self.printListFromTailToHead(listNode.next) + [listNode.val]
        else:
            return []
