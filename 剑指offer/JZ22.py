import queue


# 注意python2包名不一样
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        result = []
        if not root:
            return result
        q = queue.SimpleQueue()
        q.put(root)
        while not q.empty():
            node = q.get()
            result.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return result
