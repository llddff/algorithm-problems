class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.does_tree1_have_tree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def does_tree1_have_tree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        return pRoot1.val == pRoot2.val and self.does_tree1_have_tree2(pRoot1.left,
                                                                       pRoot2.left) and self.does_tree1_have_tree2(
            pRoot1.right, pRoot2.right)
