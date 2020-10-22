from LeetCode刷题.Leet889 import TreeNode


class Solution:
    def buildTree(self, inorder, postorder):
        if not (inorder and postorder):
            return
        d = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def dfs(left, right):
            if left > right:
                return
            val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(val)
            index = d[val]
            root.right = dfs(index + 1, right)
            root.left = dfs(left, index - 1)
            return root

        return dfs(0, len(inorder) - 1)
