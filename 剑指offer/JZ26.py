class Solution:
    def __init__(self):
        self.pre = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.Convert(pRootOfTree.right)
        if self.pre:
            pRootOfTree.right = self.pre
            self.pre.left = pRootOfTree
        self.pre = pRootOfTree
        self.Convert(pRootOfTree.left)
        return self.pre
