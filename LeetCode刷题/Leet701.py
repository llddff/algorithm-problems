from LeetCode刷题.Leet889 import TreeNode


class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
