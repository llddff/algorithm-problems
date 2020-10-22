class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            cnt = 0
            for c in string:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0: return False
            return cnt == 0

        level = {s}
        while level:
            res = []
            for s in level:
                if isValid(s):
                    res.append(s)
            if res: return res
            next_level = set()
            for s in level:
                for i in range(len(s)):
                    if s[i] in '()':
                        next_level.add(s[:i] + s[i + 1:])
            level = next_level
