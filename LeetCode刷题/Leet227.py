class Solution:
    def calculate(self, s):
        operand = 0
        stack = []
        sign = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(operand)
                if sign == '-':
                    stack.append(-operand)
                if sign == '*':
                    stack[-1] *= operand
                if sign == '/':
                    stack[-1] = int(stack[-1] / operand)
                sign = ch
                operand = 0
        return sum(stack)
