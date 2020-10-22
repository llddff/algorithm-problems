import queue


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        q = queue.SimpleQueue()
        q.put(pRoot)
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
            res.append(level)
        return res
