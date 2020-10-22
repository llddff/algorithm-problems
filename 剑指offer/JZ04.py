class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return
        root=TreeNode(pre[0])
        index=tin.index(pre[0])
        root.left=self.reConstructBinaryTree(pre[1:index+1],tin[:index])
        root.right=self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
        return root

a=Solution()
b=a.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
print(b)