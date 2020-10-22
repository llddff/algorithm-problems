class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res
