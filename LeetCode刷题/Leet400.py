class Solution:
    def findNthDigit(self, n):
        base, digits = 9, 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        idx = n % digits
        number = 10 ** (digits - 1)
        if idx == 0:
            number += n // digits - 1
        else:
            number += n // digits
        if idx:
            for i in range(idx, digits):
                number //= 10
        return number % 10
