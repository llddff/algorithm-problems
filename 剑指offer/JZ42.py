class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        tmp = float('inf')
        result = []
        i, j = 0, len(array) - 1
        while i < j:
            if array[i] + array[j] == tsum:
                if array[i] * array[j] < tmp:
                    tmp = array[i] * array[j]
                    result = [array[i], array[j]]
                i += 1
                j -= 1
            elif array[i] + array[j] < tsum:
                i += 1
            else:
                j -= 1
        return result
