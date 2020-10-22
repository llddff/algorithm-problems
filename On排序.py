# 计数排序的初步实现
def countSort(array):
    # 得到数列的最大值
    magnum = array[0]
    for i in range(1, len(array)):
        if array[i] > magnum:
            magnum = array[i]
    temp = [0] * (magnum + 1)
    for i in range(len(array)):
        temp[array[i]] += 1
    sortedarray = []
    for i in range(len(temp)):
        sortedarray += [i] * temp[i]
    return sortedarray


# 优化临时数组
def countSortv2(array):
    # 得到数列的最大值
    maxnum = array[0]
    minnum = array[0]
    for i in range(1, len(array)):
        if array[i] > maxnum:
            maxnum = array[i]
        if array[i] < minnum:
            minnum = array[i]
    temp = [0] * (maxnum - minnum + 1)
    for i in range(len(array)):
        temp[array[i] - minnum] += 1
    sortedarray = []
    for i in range(len(temp)):
        sortedarray += [i + minnum] * temp[i]
    return sortedarray


unsorted = [41, 62, 59, 14, 74, 76, 93, 90, 94, 33, 49, 35, 93, 60, 52, 22, 20, 66, 69, 57]
a = countSort(unsorted)
print(a)
b = countSortv2(unsorted)
print(b)
print(unsorted)

import antigravity
