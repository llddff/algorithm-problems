class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        begin = 0
        end = len(ss)
        result = []

        def permu_core(str, begin, end):

            if begin >= end:
                result.append(str)
            else:
                for char in range(begin, end):
                    str_l = list(str)
                    str_l[char], str_l[begin] = str_l[begin], str_l[char]
                    str = ''.join(str_l)
                    permu_core(str, begin + 1, end)
            return result

        r = permu_core(ss, begin, end)
        return sorted(list(set(r)))


a = Solution().Permutation('abbb')
a
