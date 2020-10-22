class Solution:
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        ans,i,j=0,0,0
        jihe=set()
        while i<n and j<n:
            if s[j] not in jihe:
                jihe.add(s[j])
                j+=1
                ans=max(ans,j-i)
            else:
                jihe.remove(s[i])
                i+=1
        return ans
        

class Solution:
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        ans,i=0,0
        d={}
        for j in range(n):
            if s[j] in d:
                i=max(d[s[j]],i)
            ans=max(ans,j-i+1)
            d[s[j]]=j+1
        return ans