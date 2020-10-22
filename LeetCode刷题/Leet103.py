from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        level = deque()
        if not root:
            return []
        node_q = deque([root, None])
        order_left = True
        while node_q:
            cur_node = node_q.popleft()
            if cur_node:
                if order_left:
                    level.append(cur_node.val)
                else:
                    level.appendleft(cur_node.val)
                if cur_node.left:
                    node_q.append(cur_node.left)
                if cur_node.right:
                    node_q.append(cur_node.right)
            else:
                res.append(list(level))
                if node_q:
                    node_q.append(None)
                level = deque()
                order_left = not order_left
        return res
