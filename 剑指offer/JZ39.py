class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.depth(pRoot) != -1

    def depth(self, node):
        if not node:
            return 0
        left = self.depth(node.left)
        if left == -1:
            return -1
        right = self.depth(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
