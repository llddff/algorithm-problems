class Solution:
    def Add(self, num1, num2):
        while num2:
            yu = (num1 & num2) << 1
            num1 ^= num2
            num2 = yu
        return num1


a = Solution().Add(-8, -6)
print(a)
