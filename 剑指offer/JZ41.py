class Solution:
    def FindContinuousSequence(self, tsum):
        result = []
        l, r = 1, 1
        tmp = 0
        while l <= tsum / 2:
            if tmp < tsum:
                tmp += r
                r += 1
            elif tmp > tsum:
                tmp -= l
                l += 1
            else:
                ans = [i for i in range(l, r)]
                result.append(ans)
                tmp -= l
                l += 1
        return result


a = Solution().FindContinuousSequence(100)
a
