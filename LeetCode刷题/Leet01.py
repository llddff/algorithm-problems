def twoSum(nums, target):
    m=len(nums)
    d={}
    enum=enumerate(nums)
    for i,v in enum:
        sub=target-v
        if sub in d:
            return d[sub],i
        d[v]=i
a=twoSum([2,7,11,15],13)
print(a)
# 使用了哈希表，就是'字典'来存储数组的下标和值，实现快速查找的目的