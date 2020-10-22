unsorted=[41, 62, 59, 14, 74, 76, 93, 90, 94, 33, 49, 35, 93, 60, 52, 22, 20, 66, 69, 57]

def bubblesort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(0,n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


def selectionsort(arr):
    # 不断选出最小的数往前放
    n=len(arr)
    for i in range(n-1):
        minindex=i
        for j in range(i+1,n):
            if arr[j]<arr[minindex]:
                minindex=j
        if i!=minindex:
            arr[i],arr[minindex]=arr[minindex],arr[i]


def insertsort(arr):
    # 前面是已排序序列，后面是未排序序列，将未排序的依次抽出，插入已排序的合适位置
    # 把current位置暂存起来，依次与前面的比较，避免多次交换数据
    n=len(arr)
    for i in range(n):
        preindex = i-1
        current = arr[i]
        while preindex >=0 and arr[preindex] > current:
            arr[preindex+1] = arr[preindex]
            preindex -= 1
        arr[preindex+1] = current


def shellsort(arr):
    # 先选定一个gap，每隔一个gap的数放一组，每组进行选择排序，然后按规律减小gap，直到gap=1
    n=len(arr)
    k=1
    while 2**k-1 <= n/2:
        k+=1
    gap=2**k-1
    while gap>0:
        for i in range(gap,n):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j]>temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        k-=1
        gap=2**k-1


def partition(lie,startIndex,endIndex):
    # 选定枢轴后，比它小的放左边，比它大的放右边
    pivot=lie[startIndex]
    left=startIndex
    right=endIndex
    while left!=right:
        while left<right and lie[right]>pivot:
            right -= 1
        while left<right and lie[left]<=pivot:
            left += 1
        if left<right:
            lie[left],lie[right] = lie[right],lie[left]
    lie[left],lie[startIndex] = lie[startIndex],lie[left]
    return left

def quickSort(lie,startIndex,endIndex):
    if startIndex>=endIndex:
        return
    pivotIndex=partition(lie,startIndex,endIndex)
    quickSort(lie,startIndex,pivotIndex-1)
    quickSort(lie,pivotIndex+1,endIndex)


def radix(arr):
    # 基数排序,分别按个位、十位进行分桶,由低位到高位进行k次计数排序
    digit=0
    maxdigit=1
    maxvalue=max(arr)
    # 找出列表中最大的位数
    while 10**maxdigit < maxvalue:
        maxdigit+=1
    while digit < maxdigit:
        temp = [[] for i in range(10)]
        for i in arr:
            # 求出每一个元素的个、十、百位的值
            t = int((i/10**digit)%10)
            temp[t].append(i)
        coll=[]
        for bucket in temp:
            for i in bucket:
                coll.append(i)
        arr = coll
        digit+=1
    return arr


# bubblesort(unsorted)
# selectionsort(unsorted)
# insertsort(unsorted)
# shellsort(unsorted)
# quickSort(unsorted,0,len(unsorted)-1)
a=radix(unsorted)
print(unsorted)