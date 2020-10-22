class Solution:
    def isSymmetrical(self, pRoot):
        def isSame(r1, r2):
            if not (r1 or r2):
                return True
            if not (r1 and r2):
                return False
            return r1.val == r2.val and isSame(r1.left, r2.right) and isSame(r1.right, r2.left)

        return not pRoot or isSame(pRoot.left, pRoot.right)
