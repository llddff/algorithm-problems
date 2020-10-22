class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array or not array[0]:
            return False
        m=len(array)
        n=len(array[0])
        row=m-1
        col=0
        while row>=0 and col<n:
            if array[row][col]<target:
                col+=1
            elif array[row][col]>target:
                row-=1
            else:
                return True
        return False