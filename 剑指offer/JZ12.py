class Solution:
    def Power(self, base, exponent):
        if exponent < 0:
            base = 1 / base
            exponent = -exponent
        x = base
        ret = 1
        while exponent:
            if exponent & 1:
                ret *= x
            x *= x
            exponent >>= 1
        return ret


Solution().Power(2, 6)
