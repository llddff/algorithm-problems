import queue


class Solution:
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        q = queue.SimpleQueue()
        q.put(('0000', 0))
        seen = {'0000'}
        while not q.empty():
            node, depth = q.get()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    q.put((nei, depth + 1))
        return -1
