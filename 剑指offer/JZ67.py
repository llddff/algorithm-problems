class Solution:
    def cutRope(self, number):
        if number == 2:
            return 1
        elif number == 3:
            return 2
        f = [-1] * (number + 1)
        for i in range(1, 5):
            f[i] = i
        for i in range(5, number + 1):
            for j in range(1, i // 2 + 1):
                f[i] = max(f[i], j * f[i - j])
        return f[number]

    def tanxin(self, number):
        if number in (1, 2):
            return 1
        elif number == 3:
            return 2
        elif number <= 0:
            return 0
        m = number % 3
        if m == 0:
            return 3 ** (number / 3)
        elif m == 1:
            return 3 ** (number // 3 - 1) * 4
        elif m == 2:
            return 3 ** (number // 3) * 2
