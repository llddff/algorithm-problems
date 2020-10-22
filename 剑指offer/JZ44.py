class Solution:
    def ReverseSentence(self, s):
        slist=s.split()
        slist.reverse()
        return ' '.join(slist) if slist else ' '