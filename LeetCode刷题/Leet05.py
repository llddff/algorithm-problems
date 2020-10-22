class Solution:
    def longestPalindrome(self, s):
        s_sharp='^#'+'#'.join(s)+'#$'
        n=len(s_sharp)
        p=[0]*n             # p[i]表示i作中心的最长回文子串的半径，初始化p[i]
        R = 0                    # 之前最长回文子串的右边界
        C = 0                    # 之前最长回文子串的中心位置
        for i in range(1,n-1):
            i_mirror=2*C-i
            if i<R:
                p[i] = min(R-i, p[i_mirror])
            else:
                p[i] = 0
            while s_sharp[i-p[i]-1] == s_sharp[i+p[i]+1]:
                p[i] += 1
            if (i+p[i]) > R:
                R, C = i+p[i], i
        maxLen=max(p)
        centerindex=p.index(maxLen)
        start=(centerindex-maxLen)//2
        return s[start:start+maxLen]
a=Solution()
b=a.longestPalindrome('babcdefedc')
print(b)