import math


class Solution:
    def numSquares(self, n):
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        a = 0
        while a * a <= n:
            b = int(math.sqrt(n - a * a))
            if a * a + b * b == n:
                if a != 0 and b != 0:
                    return 2
                else:
                    return 1
            a += 1
        return 3

    def jiefa2(self, n):
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for remain in queue:
                for square_num in square_nums:
                    if remain == square_num:
                        return level
                    elif remain < square_num:
                        break
                    else:
                        next_queue.add(remain - square_num)
            queue = next_queue
        return level
