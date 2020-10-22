class Solution:
    def reOrderArray(self, array):
        temp = []
        for i in array:
            if i & 1:
                temp.append(i)
        for i in array:
            if not i & 1:
                temp.append(i)
        return temp

    def v2(self, array):
        i = 0
        n = len(array)
        for j in range(n):
            if array[j] & 1:
                temp = array[j]
                for k in range(j - 1, i - 1, -1):
                    array[k + 1] = array[k]
                array[i] = temp
                i += 1
        return array
