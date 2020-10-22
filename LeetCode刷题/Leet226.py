class Solution:
    def invertTree(self, root):
        if not root:
            return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
