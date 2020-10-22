class Solution:
    def jumpFloorII(self, number):
        if number == 0 or number == 1:
            return 1
        return 1 << (number - 1)
