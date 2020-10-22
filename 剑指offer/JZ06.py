class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        start=0
        end=len(rotateArray)-1
        while start<end:
            mid=(start+end)>>1
            if rotateArray[mid]>rotateArray[end]:
                start=mid+1
            elif rotateArray[mid]==rotateArray[end]:
                end-=1
                continue
            else:
                end=mid
        return rotateArray[start]