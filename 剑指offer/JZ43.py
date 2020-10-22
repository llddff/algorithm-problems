class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ''
        slen=len(s)
        n%=slen
        return s[n:]+s[:n]