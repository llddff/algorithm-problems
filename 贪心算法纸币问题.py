# 小明手中有 1，5，10，50，100 五种面额的纸币，每种纸币对应张数分别为 5，2，2，3，5 张。若小明需要支付 456 元，则需要多少张纸币？
# 问题拆分为子问题: 小明选择纸币进行支付的过程，可以划分为n个子问题：即每个子问题对应为：在未超过456的前提下，在剩余的纸币中选择一张纸币
# 制定的贪心策略为：在允许的条件下选择面额最大的纸币
N = 5  # 5种面额
Count = [5, 2, 2, 3, 5]  # 纸币数量
Value = [1, 5, 10, 50, 100]


def solve(money):
    num = 0  # 目前用到的纸币张数
    for i in range(N - 1, -1, -1):  # 从最大面额开始选
        c = min(money // Value[i], Count[i])  # 当前用了几张
        money = money - c * Value[i]
        num += c
    if money != 0:
        num = -1  # 无解
    return num
