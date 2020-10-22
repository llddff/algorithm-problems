class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        slen, plen = len(s), len(pattern)
        f = [[False for j in range(plen + 1)] for i in range(slen + 1)]
        for i in range(slen + 1):
            for j in range(plen + 1):
                if j == 0:
                    f[i][j] = i == 0
                elif pattern[j - 1] != '*':
                    if i >= 1 and (s[i - 1] == pattern[j - 1] or pattern[j - 1] == '.'):
                        f[i][j] = f[i - 1][j - 1]
                else:
                    if j >= 2:
                        f[i][j] |= f[i][j - 2]
                    if i >= 1 and j >= 2 and (s[i - 1] == pattern[j - 2] or pattern[j - 2] == '.'):
                        f[i][j] |= f[i - 1][j]
        return f[slen][plen]
