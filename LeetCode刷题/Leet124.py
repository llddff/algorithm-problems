class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def maxGain(node):
            if not node:
                return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            nodeprice = node.val + leftGain + rightGain
            self.maxSum = max(self.maxSum, nodeprice)
            return max(leftGain, rightGain) + node.val

        maxGain(root)
        return self.maxSum
