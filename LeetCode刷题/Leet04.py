A = [1, 3, 5, 7, 9]
B = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def findMedian(x, y):
    lx = len(x)
    ly = len(y)
    leftk = (lx+ly+1)//2
    rightk = (lx+ly+2)//2           # 一个小技巧：将偶数和奇数的情况合并，如果是奇数，会求两次同样的 k

    def getKth(u, start1, end1, v, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return getKth(v, start2, end2, u, start1, end1, k)
        if len1 == 0:
            return v[start2 + k - 1]
        if k == 1:
            return min(u[start1], v[start2])
        i = start1+min(len1, k//2)-1
        j = start2+min(len2, k//2)-1
        if u[i] > v[j]:
            return getKth(u, start1, end1, v, j+1, end2, k-(j-start2+1))
        else:
            return getKth(u, i+1, end1, v, start2, end2, k-(i-start1+1))
    return (getKth(x, 0, lx-1, y, 0, ly-1, leftk)+getKth(x, 0, lx-1, y, 0, ly-1, rightk))/2


a = findMedian(A, B)
print(a)
