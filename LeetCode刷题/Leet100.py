class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not (p and q):
            return False
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right
