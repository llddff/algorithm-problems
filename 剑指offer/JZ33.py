class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        p2 = p3 = p5 = 0
        result = [1]
        for i in range(1, index):
            result.append(min(result[p2] * 2, result[p3] * 3, result[p5] * 5))
            if result[i] == result[p2] * 2:
                p2 += 1
            if result[i] == result[p3] * 3:
                p3 += 1
            if result[i] == result[p5] * 5:
                p5 += 1
        return result[index - 1]
