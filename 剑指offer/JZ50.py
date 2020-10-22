class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        length=len(numbers)
        for i in range(length):
            while numbers[i] != i:
                if numbers[i]==numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                temp=numbers[i]
                numbers[i],numbers[temp]=numbers[temp],numbers[i]
        return False