class Solution:
    def convert(self, s, numRows):
        if numRows==1:
            return s
        n=len(s)
        T=2*numRows-2
        ret=''
        for i in range(numRows):
            for j in range(0,n-i,T):
                ret+=s[i+j]
                if i!=0 and i!=numRows-1 and j+T-i<n:
                    ret+=s[j+T-i]
        return ret
a=Solution()
b=a.convert("LEETCODEISHIRING",3)
print(b)