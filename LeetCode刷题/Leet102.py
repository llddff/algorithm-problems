import queue


class Solution:
    def levelOrder(self, root):
        res = []
        q = queue.SimpleQueue()
        if root:
            q.put(root)
        while not q.empty():
            level = []
            n = q.qsize()
            for i in range(n):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            res.append(level)
        return res
