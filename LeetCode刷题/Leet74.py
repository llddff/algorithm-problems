class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        startRow=0
        endRow=m-1
        while startRow<=endRow:
            mid=(startRow+endRow)>>1
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                startRow=mid+1
            else:
                endRow=mid-1
        selectRow=startRow-1
        if selectRow<0 :
            return False
        startCol=0
        endCol=n-1
        while startCol<=endCol:
            mid=(startCol+endCol)>>1
            if matrix[selectRow][mid]==target:
                return True
            elif matrix[selectRow][mid]<target:
                startCol=mid+1
            else:
                endCol=mid-1
        if endCol<0 or startCol>n:
            return False
        return False