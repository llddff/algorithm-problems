class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        key, count = None, 0
        for num in numbers:
            if not key:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1
            if count == 0:
                key = None
        count=0
        for num in numbers:
            if key==num:
                count+=1
        if count>len(numbers)>>1:
            return key
        return 0

a=Solution().MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3])
a