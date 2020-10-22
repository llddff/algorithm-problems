class Solution:
    def recoverTree(self, root):
        self.x = self.y = self.pre = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if not self.pre:
                self.pre = node
            else:
                if self.pre.val > node.val:
                    self.y = node
                    if not self.x:
                        self.x = self.pre

                self.pre = node
            dfs(node.right)

        dfs(root)
        if self.x and self.y:
            self.x.val, self.y.val = (self.y.val, self.x.val)

    def moris(self, root):
        x = y = pre = tmp = None
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = root
                    root = root.left
                else:
                    if pre and pre.val > root.val:
                        y = root
                        if not x:
                            x = pre
                    pre = root
                    tmp.right = None
                    root = root.right
            else:
                if pre and pre.val > root.val:
                    y = root
                    if not x:
                        x = pre
                pre = root
                root = root.right
        if x and y:
            x.val, y.val = y.val, x.val
a=TreeNode(3)
a.left=TreeNode(1)
a.right=TreeNode(4)
a.right.left=TreeNode(2)
b=Solution().recoverTree(a)
b