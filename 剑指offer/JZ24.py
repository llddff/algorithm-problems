class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        if not root:
            return res
        self.sums = expectNumber
        self.DFS(root, res, [root.val])
        return res

    def DFS(self, root, result, path):
        if not root.left and not root.right and sum(path) == self.sums:
            result.append(path)
        if root.left:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right:
            self.DFS(root.right, result, path + [root.right.val])
