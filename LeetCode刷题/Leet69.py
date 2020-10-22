class Solution:
    def mySqrt(self, x):
        l,r,ans=0,x,0
        while l<=r:
            mid=(l+r)>>1
            if mid*mid<x:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans

    def niudun(self, x):
        if x==0:
            return 0
        C,x0=x,x
        while True:
            xi=(x0+C/x0)/2
            if abs(xi-x0)<1e-5:
                break
            x0=xi
        return int(xi)