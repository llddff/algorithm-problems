from LeetCode刷题.Leet889 import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        if not (preorder and inorder):
            return
        root = TreeNode(preorder[0])
        mid_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid_idx + 1], inorder[:mid_idx])
        root.right = self.buildTree(preorder[mid_idx + 1:], inorder[mid_idx + 1:])
        return root
