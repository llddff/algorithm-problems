class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=0
        end=n
        while start<end:
            mid=start+((end-start)>>1)
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        if isBadVersion(start):
            return start