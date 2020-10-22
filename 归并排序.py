def merge(array, start, end):
    # 左右2个有序序列依次比较，把最小元素放入临时空间，对应指针+1
    # 开辟额外大集合，设置指针
    mid=(start+end)//2
    p1=start
    p2=mid+1
    temp=[]
    while p1<=mid and p2<=end:
        if array[p1]<=array[p2]:
            temp.append(array[p1])
            p1+=1
        else:
            temp.append(array[p2])
            p2+=1
    # 左侧小集合还有剩余，依次放入大集合尾部
    if p1<=mid:
        temp+=array[p1:mid+1]
    if p2<=end:
        temp+=array[p2:]
    for i in range(len(temp)):
        array[start+i]=temp[i]
def mergeSort(array,start,end):
    if start<end:
        # 折半成两个小集合，分别进行递归,拆到最下面每个序列只有2个元素
        mid=(start+end)//2
        mergeSort(array,start,mid)
        mergeSort(array,mid+1,end)
        # 把两个有序小集合，归并成一个大集合
        merge(array, start, end)
unsorted=[41, 62, 59, 14, 74, 76, 93, 90, 94, 33, 49, 35, 93, 60, 52, 22, 20, 66, 69, 57]
mergeSort(unsorted,0,len(unsorted)-1)
print(unsorted)