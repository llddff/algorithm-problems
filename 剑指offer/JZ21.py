class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        i, j = 0, 0
        n = len(pushV)
        while i < n:
            if pushV[i] != popV[j]:
                stack.append(pushV[i])
                i += 1
            else:
                i += 1
                j += 1
                while stack and stack[-1] == popV[j]:
                    stack.pop()
                    j += 1
        return len(stack) == 0

Solution().IsPopOrder([1,2,3,4,5],[4,5,3,2,1])