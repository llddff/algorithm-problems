import functools


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        charlist = list(map(str, numbers))
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                sum1 = int(charlist[i] + charlist[j])
                sum2 = int(charlist[j] + charlist[i])
                if sum1 > sum2:
                    charlist[i], charlist[j] = charlist[j], charlist[i]
        return ''.join(charlist)

    def usekey(self, numbers):
        charlist = [str(i) for i in numbers]

        def cmp(a, b):
            return int(a + b) - int(b + a)

        charlist.sort(key=functools.cmp_to_key(cmp))
        return ''.join(charlist)


a = Solution().usekey([3, 32, 321])
a
