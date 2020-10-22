class Solution:
    def calculate(self, s):
        stack = []
        n = operand = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                operand += int(ch) * 10 ** n
                n += 1
            elif ch != ' ':
                if n:
                    stack.append(operand)
                    n = operand = 0
                if ch == '(':
                    res = self.evaluate(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)
        if n:
            stack.append(operand)
        return self.evaluate(stack)

    def evaluate(self, stack):
        res = stack.pop() if stack else 0
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res
