class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]