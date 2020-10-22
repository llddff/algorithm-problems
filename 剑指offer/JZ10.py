class Solution:
    def rectCover(self, number):
        if number in (0, 1):
            return number
        a, b, c = 1, 1, 0
        for i in range(2, number + 1):
            c = a + b
            a, b = b, c
        return c