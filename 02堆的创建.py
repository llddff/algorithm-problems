def upAdjust(array):
    childIndex = len(array) - 1
    parentIndex = (childIndex - 1) >> 1
    temp = array[childIndex]
    while childIndex > 0 and temp < array[parentIndex]:
        array[childIndex] = array[parentIndex]
        childIndex = parentIndex
        parentIndex = (childIndex - 1) >> 1
    array[childIndex] = temp


def downAdjust(array, parentIndex, length):
    temp = array[parentIndex]
    childIndex = 2 * parentIndex + 1
    while childIndex < length:
        if childIndex + 1 < length and array[childIndex + 1] < array[childIndex]:
            childIndex += 1
        if temp <= array[childIndex]:
            break
        array[parentIndex] = array[childIndex]
        parentIndex = childIndex
        childIndex = 2 * parentIndex + 1
    array[parentIndex] = temp


def buildHeap(array):
    n = len(array)
    for i in range((n - 2) >> 1, -1, -1):
        downAdjust(array, i, n)
