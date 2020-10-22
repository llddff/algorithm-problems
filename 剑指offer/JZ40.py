class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        a = 0
        result = [0, 0]
        for k in array:
            a ^= k
        a &= -a
        for k in array:
            if k & a:
                result[0] ^= k
            else:
                result[1] ^= k
        return result


a = Solution().FindNumsAppearOnce([1, -7, 7, 7, 8, 8, 9, 9])
a
