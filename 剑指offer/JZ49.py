class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '+': '+', '-': '-'}
        he = 0
        label = 1
        for i in s:
            if i in d:
                if i == '+':
                    continue
                elif i == '-':
                    label = -1
                else:
                    he = he * 10 + d[i]
            else:
                return 0
        he = he * label
        if -0x80000000 <= he <= 0x7FFFFFFF:
            return he
        else:
            return 0
