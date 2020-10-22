class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        if not root:
            return '#!'
        result = str(root.val) + '!'
        left = self.Serialize(root.left)
        right = self.Serialize(root.right)
        return result + left + right

    def Deserialize(self, s):
        if s:
            i = iter(s.split('!'))

        def span_tree():
            data = next(i)
            if data == '#':
                return
            node = TreeNode(int(data))
            node.left = span_tree()
            node.right = span_tree()
            return node

        return span_tree()


a = Solution().Deserialize('1!2!4!#!#!5!#!#!3!6!#!#!7!#!#!')
b = Solution().Serialize(a)
b
