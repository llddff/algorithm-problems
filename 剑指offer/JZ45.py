class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        aset = set()
        big, small = 0, 14
        for val in numbers:
            if val > 0:
                if val in aset:
                    return False
                aset.add(val)
                big = max(val, big)
                small = min(val, small)
        return big - small < 5

    def paixu(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        i, size = 0, len(numbers)
        for j in range(size):
            if numbers[j] == 0:
                i += 1
                continue
            if j + 1 < size and numbers[j] == numbers[j + 1]:
                return False
        return numbers[-1] - numbers[i] < 5
