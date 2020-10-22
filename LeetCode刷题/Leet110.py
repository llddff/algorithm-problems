class Solution:
    def isBalanced(self, root):
        return self.isBalancedHelper(root)[0]

    def isBalancedHelper(self, root):
        if not root:
            return True, -1
        leftBalanced, leftheight = self.isBalancedHelper(root.left)
        if not leftBalanced:
            return False, 0
        rightBalanced, rightheight = self.isBalancedHelper(root.right)
        if not rightBalanced:
            return False, 0
        return (abs(leftheight - rightheight) < 2), 1 + max(leftheight, rightheight)
