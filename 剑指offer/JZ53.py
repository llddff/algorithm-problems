class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            float(s)
            return True
        except:
            return False
