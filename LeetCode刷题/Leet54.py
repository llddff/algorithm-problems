class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        lx = ly = 0
        rx = len(matrix) - 1
        ry = len(matrix[0]) - 1
        res = []
        while lx <= rx and ly <= ry:
            for j in range(ly, ry + 1):
                res.append(matrix[lx][j])
            for i in range(lx + 1, rx + 1):
                res.append(matrix[i][ry])
            if rx > lx and ry > ly:
                for rj in range(ry - 1, ly - 1, -1):
                    res.append(matrix[rx][rj])
                for ri in range(rx - 1, lx, -1):
                    res.append(matrix[ri][ly])
            lx, ly, rx, ry = lx + 1, ly + 1, rx - 1, ry - 1
        return res