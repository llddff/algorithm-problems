class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        n = len(points)
        for i in range(n):
            record = {}
            for j in range(n):
                if j != i:
                    d = self.dis(points[i], points[j])
                    if d in record:
                        record[d] += 1
                    else:
                        record[d] = 1
            for it in record:
                res += record[it] * (record[it] - 1)
        return res

    def dis(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
