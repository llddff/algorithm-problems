import queue


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        q = queue.SimpleQueue()
        q.put(pRoot)
        number = 0
        while not q.empty():
            levelsz = q.qsize()
            level = []
            while levelsz:
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                levelsz -= 1
            number += 1
            if not number & 1:
                level.reverse()
            res.append(level)
        return res
