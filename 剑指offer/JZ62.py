class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return
        stack = []
        cur = pRoot
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur
                cur = cur.right
        return
