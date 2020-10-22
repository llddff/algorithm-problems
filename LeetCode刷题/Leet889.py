class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre:
            return
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        left_len = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:left_len + 1], post[:left_len])
        root.right = self.constructFromPrePost(pre[left_len + 1:], post[left_len:-1])
        return root

a=Solution().constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])
a