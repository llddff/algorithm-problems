class Solution:
    def __init__(self):
        self.h = self.w = self.length = self.mat = 0

    def hasPath(self, matrix, rows, cols, path):
        self.mat = list(matrix)
        self.h, self.w = rows, cols
        self.length = len(path)
        for i in range(rows):
            for j in range(cols):
                if self.dfs(i, j, 0, path):
                    return True
        return False

    def dfs(self, i, j, pos, s):
        cor = [-1, 0, 1, 0, -1]
        if i < 0 or i >= self.h or j < 0 or j >= self.w:
            return False
        ch = self.mat[i * self.w + j]
        if ch == '#' or ch != s[pos]:
            return False
        if pos + 1 == self.length:
            return True
        self.mat[i * self.w + j] = '#'
        for k in range(4):
            if self.dfs(i + cor[k], j + cor[k + 1], pos + 1, s):
                return True
        self.mat[i * self.w + j] = ch
        return False
