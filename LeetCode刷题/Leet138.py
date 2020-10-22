class Solution:
    def __init__(self):
        self.visited = {}

    def getCloneNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val)
                return self.visited[node]
        return

    def copyRandomList(self, head):
        if not head:
            return
        newHead = Node(head.val)
        old = head
        self.visited[old] = newHead
        while old:
            newHead.random = self.getCloneNode(old.random)
            newHead.next = self.getCloneNode(old.next)
            old = old.next
            newHead = newHead.next
        return self.visited[head]
