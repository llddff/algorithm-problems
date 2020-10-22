class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 1e30
        for c in [root.left, root.right]:
            if c:
                min_depth = min(min_depth, self.minDepth(c))
        return min_depth + 1
