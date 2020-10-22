class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def dfs(left, right):
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

    def diedai(self, root):
        import queue
        if not root or not (root.left or root.right):
            return True
        q = queue.SimpleQueue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            left = q.get()
            right = q.get()
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)
        return True
