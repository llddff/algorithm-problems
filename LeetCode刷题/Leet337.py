class Solution:
    def rob(self, root):
        def robIn(root):
            if not root:
                return 0, 0
            left = robIn(root.left)
            right = robIn(root.right)
            r0 = max(left) + max(right)
            r1 = left[0] + right[0] + root.val
            return r0, r1

        return max(robIn(root))
