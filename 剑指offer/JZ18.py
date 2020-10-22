class Solution:
    def Mirror(self, pRoot):
        def dfs(r):
            if not r:
                return
            left = dfs(r.left)
            right = dfs(r.right)
            r.left, r.right = right, left
            return r

        if not pRoot:
            return
        dfs(pRoot)
