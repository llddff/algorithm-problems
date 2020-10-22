class Solution:
    # 返回 RandomListNode
    def __init__(self):
        self.visited = {}

    def getCloneNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        return

    def Clone(self, pHead):
        if not pHead:
            return
        newHead = RandomListNode(pHead.label)
        old = pHead
        self.visited[old] = newHead
        while old:
            newHead.random = self.getCloneNode(old.random)
            newHead.next = self.getCloneNode(old.next)
            old = old.next
            newHead = newHead.next
        return self.visited[pHead]
