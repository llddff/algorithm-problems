class Solution:
    def findRepeatedDnaSequences(self, s):
        L, n = 10, len(s)
        seen, output = set(), set()
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp)
            seen.add(tmp)
        return list(output)
